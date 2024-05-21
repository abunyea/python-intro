message = input("Enter a message: ")

encodedMessage = message.replace('a', '*')
encodedMessage = encodedMessage.replace('e', '&')
encodedMessage = encodedMessage.replace('i', '^')
encodedMessage = encodedMessage.replace('o', '%')
encodedMessage = encodedMessage.replace('u', '#')

print(f"Encoded message: {encodedMessage}")
