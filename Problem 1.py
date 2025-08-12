dataBase = {    # This is a dictionary thet stores known questions and answers can be expanded to include more
    'hello':'Hi there! How can I help you today?',
    'who are you':'My name is Fawzy, your AI assistant.',
    'what is your purpose':'I am here to assist you with your tasks.',
    'default':'I did\'t understand that. Can you please rephrase?'
}
userData={} # This is a dictionary to store user data
print("Welcome to Fawzy, your AI assistant!")
name = input('Enter Your Name: ')
userData['name'] = name
print(f'Hello, {name}!')
while True:
    userInput = input('You: ').lower() # Takes user input and converts it to lowercase for easier matching
    if userInput in dataBase:
        print(f'Fawzy: {dataBase[userInput]}')
    
    elif userInput == "exit": # Exits the program
        print(f'Fawzy: Goodbye, {name}! It was nice talking to you')
        break
    
    elif userInput == "add": # Adds two numbers
        n1 = float(input("Enter the First Number: "))
        n2 = float(input("Enter the Second Number: "))
        result = n1 + n2
        print(f'Fawzy: The result of adding {n1} and {n2} is {result}.')
    elif userInput == "subtract": # Subtracts two numbers
        n1 = float(input("Enter the First Number: "))
        n2 = float(input("Enter the Second Number: "))
        result = n1 - n2
        print(f'Fawzy: The result of subtracting {n1} from {n2} is {result}.')
    else:
        print(f'Fawzy: {dataBase["default"]}') # Default response if input is not recognized