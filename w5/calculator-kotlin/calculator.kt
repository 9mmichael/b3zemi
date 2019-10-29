fun main(args: Array<String>) {
//    print("数式を入力してください: ")
//    val expression = readLine()

  println(Parser("12+34+56").expression())
  println(Parser("1-2-3").expression())
  println(Parser("1-2+3").expression())
  println(Parser("2*3+4").expression())
  println(Parser("2+3*4").expression())
  println(Parser("100/10/2").expression())
}

class Parser(val str: String) {
  var position = 0

  fun lastPosition(): Int {
    if (position < str.length) {
      return position
    }
    return -1
  }

  fun nextPosition() {
    position++
  }

  fun readNumber(): Int {
    val sb = StringBuilder()
    var loopCount: Int
    do {
      loopCount = lastPosition()
      if (loopCount >= 0 && str.get(loopCount).isDigit()) {
        sb.append(str.get(loopCount))
        nextPosition()
      } else break
    } while (true)
    return sb.toString()
        .toInt()
  }

  fun expression(): Int {
    var num = readNumber()
    do {
      if (lastPosition() < 0) break
      when (str[lastPosition()]) {
        '+' -> {
          nextPosition()
          num += readNumber()
        }
        '-' -> {
          nextPosition()
          num -= readNumber()
        }
        '*' -> {
          nextPosition()
          num *= readNumber()
        }
        '/' -> {
          nextPosition()
          num /= readNumber()
        }
      }
    } while (true)
    return num
  }
}
