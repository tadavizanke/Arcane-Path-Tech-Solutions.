def chatbot(question):
    question = question.lower() 

    if "hello" in question or "hi" in question:
        return "Hello! How can I help you?"

    elif "how are you" in question:
        return "I'm fine. How are you?!"

    elif "what is your name" in question:
        return "My name is Rahul."
    
    elif "who are you" in question:
        return "I am your assistant."

    elif "bye" in question:
        return "Goodbye! Have a great day."

    else:
        return "I'm sorry, I don't understand that question."

if __name__ == "__main__":
    print("Chatbot: Hello! How can I help you?")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break

        reply = chatbot(user_input)
        print("Chatbot:", reply)
