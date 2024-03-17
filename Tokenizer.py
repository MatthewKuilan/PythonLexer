class Token:
  def __init__(self, type_, value):
      self.type = type_
      self.value = value

  def get_value(self):
      return self.value

  def get_type(self):
      return self.type


class Lexer:
  def __init__(self, filename):
      self.token_array = []
      u_input = open(filename, "r")
      self.buffer = ""
      self.lex(u_input.read())

  def print_tokens(self):
      print("-- Output --")
      for token in self.token_array:
          print(f"[{token.get_type()}: {token.get_value()}]")

  def isOP(self, op):
      match op:
          case "+":
              return True
          case "~":
              return True
          case "X":
              return True
          case "/":
              return True
          case "=":
              return True
          case "is":
              return True
      return False

  def get_word(self, u_input, curr_pos):
      curr_type = "NUM" if ord('1') <= ord(u_input[curr_pos]) <= ord('9') else "KEY"
      buffer = ""
      word = ""
      while curr_pos < len(u_input) and u_input[curr_pos] != " " and u_input[curr_pos] != "\n" and u_input[curr_pos] != "\t" and not self.isOP(u_input[curr_pos]):
          buffer += u_input[curr_pos]
          curr_pos += 1
      match buffer:
          case "if":
              word = "if"
          case "then":
              word = "then"
          case "else":
              word = "else"
          case "is":
              word = "is"
              curr_type = "OP"
          case "print":
              word = "print"
          case _:
              word = buffer
              curr_type = "NUM" if word.isnumeric() else "ID"
      curr_pos -= 1
      return word, curr_type, curr_pos


  def lex(self, u_input):
      curr_pos = 0
      #for char in u_input:
      while curr_pos < len(u_input):
          char = u_input[curr_pos]
          match char:
              case "+":
                  self.token_array.append(Token("OP", "+"))
              case "~":
                  self.token_array.append(Token("OP", "~"))
              case "X":
                  self.token_array.append(Token("OP", "X"))
              case "=":
                  self.token_array.append(Token("OP", "="))
              case "/":
                  self.token_array.append(Token("OP", "/"))
              case " ":
                  ...
              case "\n":
                  ...
              case "\t":
                  ...
              case _:
                  word, word_type, new_pos = self.get_word(u_input, curr_pos)
                  self.token_array.append(Token(word_type, word))
                  curr_pos = new_pos
          self.buffer = ""
          curr_pos += 1




newLex = Lexer("user_input.txt")
newLex.print_tokens()
