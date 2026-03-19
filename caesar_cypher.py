print("Welcome to the caesar cipher program, please enter your messsage so we can cypher it:")
message = input()
shift = 4
result = ""

for char in message:
    if char.isalpha():


        char_code = ord(char)

        new_char_code = char_code + shift

        new_char = chr(new_char_code)

        result = result + new_char


print(f"Your entered message was {message}")
print(f"Your encripted message is {result}")



