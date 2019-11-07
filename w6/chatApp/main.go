package main

import (
	"log"
	"net/http"

	"github.com/gorilla/websocket"
)

// Message jsonで受け取る
type Message struct {
	Message string `json:"message"`
}

var clients = make(map[*websocket.Conn]bool)
var msg = make(chan Message)
var upgrader = websocket.Upgrader{}

func handleClients(w http.ResponseWriter, req *http.Request) {
	go broadcastMessage()

	// NOTE: websocketの状態を更新
	websocket, err := upgrader.Upgrade(w, req, nil)
	if err != nil {
		log.Fatal("handleClients, websocket upgrade: ", err)
	}
	// NOTE: websocketを閉じる
	defer websocket.Close()

	clients[websocket] = true

	for {
		var message Message

		if err := websocket.ReadJSON(&message); err != nil {
			log.Printf("handleClients, ReadJSON: %v", err)
			delete(clients, websocket)
			break
		}
		// NOTE: メッセージ送信
		msg <- message
	}
}

func broadcastMessage() {
	for {
		message := <-msg
		for client := range clients {
			if err := client.WriteJSON(message); err != nil {
				log.Printf("broadcastMessage, WriteJSON: %v", err)
				client.Close()
				delete(clients, client)
			}
		}
	}
}

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, req *http.Request) {
		http.ServeFile(w, req, "chat.html")
	})
	http.HandleFunc("/chat", handleClients)
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatal("main, ListenAndServe: ", err)
		return
	}
}
