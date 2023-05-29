import nltk
from nltk.chat.util import Chat, reflections


pairs = [
    ["hi|hey|hello", ["Hello!", "Hi there!", "Hey!"]],
    ["what is your name?", ["My name is Chatbot. How can I assist you?", "I'm Chatbot. What can I do for you?"]],
    ["how are you?", ["I'm doing well, thank you.", "I'm fine. How about you?"]],
    ["what time is it?", ["Sorry, I don't have a watch."]],
    ["what is today's date?", ["Sorry, I don't have a calendar."]],
    ["bye|goodbye", ["Bye!", "Goodbye!", "Have a nice day!"]]
]

chatbot = Chat(pairs, reflections)


print("Hello! I'm a chatbot. Ask me anything!")
while True:
  
    user_input = input("You: ")

   
    if user_input.lower() == "exit":

        break

    
    response = chatbot.respond(user_input)

    
    print("Chatbot:", response)
