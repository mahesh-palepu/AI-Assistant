def assistant_brain(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input:
        return "Hello Researcher! System is active on Asus 16X."
    elif "math" in user_input:
        return "Linear Algebra is the heart of AI. Shall we study matrices?"
    else:
        return "I am still learning. Try saying 'hello' or 'math'."

# The interaction loop
print("--- JARVIS LITE STARTING ---")
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    response = assistant_brain(query)
    print(f"Assistant: {response}")