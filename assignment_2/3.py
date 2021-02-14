inputString = 'restarteR'
inputString = inputString[0] + inputString[1:].lower().replace(inputString[0], "$")
print(inputString)