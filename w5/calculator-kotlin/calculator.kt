fun main(args: Array<String>) {
//    print("数式を入力してください: ")
//    val expression = readLine()

  println(Parser("12+34+56").expression())
  println(Parser("1-2-3").expression())
  println(Parser("1-2+3").expression())
  println(Parser("2*3+4").expression())
  println(Parser("2+3*4").expression())
  println(Parser("100/10/2").expression())
  println(Parser("(2+3)*4").expression())
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

  // NOTE: expression = term, {("+", term) | ("-", term)}
  // NOTE: e.g. 5, 1+2, 4-1
  fun expression(): Int {
    var num = term()
    loop@ do {
      if (lastPosition() < 0) break
      when (str[lastPosition()]) {
        '+' -> {
          nextPosition()
          num += term()
          continue@loop
        }
        '-' -> {
          nextPosition()
          num -= term()
          continue@loop
        }
      }
      break@loop
    } while (true)
    return num
  }

  // NOTE: term = factor, {("*", factor) | ("/", factor)}
  // NOTE:  e.g. 4, 2*3, 6/2
  fun term(): Int {
    var num = factor()
    loop@ do {
      if (lastPosition() < 0) break
      when (str[lastPosition()]) {
        '*' -> {
          nextPosition()
          num *= factor()
          continue@loop
        }
        '/' -> {
          nextPosition()
          num /= factor()
          continue@loop
        }
      }
      break@loop
    } while (true)
    return num
  }

  // NOTE: factor = {"(", expression, ")"} | number
  // NOTE: e.g. (2*3+3), 3
  fun factor(): Int {
    var bracket: Int
    if (str[lastPosition()] == '(') {
      nextPosition()
      bracket = expression()
      if (str[lastPosition()] == ')') {
        nextPosition()
      }
      return bracket
    }
    return readNumber()
  }
}
