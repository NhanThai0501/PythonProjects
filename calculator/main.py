from replit import clear
from art import logo

def add(x1, x2):
  return x1 + x2

def subtract(x1, x2):
  return x1 - x2

def multiply(x1, x2):
  return x1 * x2

def divide(x1, x2):
  return x1 / x2

def square(x1):
  return x1 ** 2

def square_root(x1):
  return x1 ** 0.5

def exponent(x1, x2):
  return x1 ** x2

def logarithm(x1, x2):
  return x1 ** (1 / x2)

# def logarithm_base_10(x1):
#   return x1 ** (1 / 10)

# def logarithm_base_e(x1):
#   return x1 ** (1 / 2.718281828459045)

# def cube_root(x1):
#   return x1 ** (1 / 3)

# def cube(x1):
#   return x1 ** 3

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "^": exponent,
  "log": logarithm,
  # "log10": logarithm_base_10,
  # "loge": logarithm_base_e,
  # "sqrt": square_root,
  # "cbrt": cube_root,
  # "sqr": square,
  # "cube": cube

}

#input: array of valid symbols
#output: return the input after check everthin
def symbols_validation(valid_symbols):
  string_symbols = ""

  # This line will push the valid symbols into a string, and between them are space to seperate them.
  string_symbols = ", ".join(valid_symbols)

  while True:
    user_input = input(
        f"Please enter one of the following symbols {string_symbols}: ")

    if user_input in valid_symbols:
      break
    else:
      print("Invalid symbol. Please try again.")

  # At this point, user_input contains a valid symbol.
  return user_input


def calculator():
  print(logo)

  valid_symbols = []
  for symbol in operations:
    valid_symbols.append(symbol)

  num1 = float(input("What's the first number?: "))
  should_continue = True

  while should_continue:
    # operation_symbol = input("Pick an operation: ")
    operation_symbol = symbols_validation(valid_symbols)
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      print("End the program!")
      # calculator()

calculator()


