from datetime import datetime

def assistant_brain(user_input):
    user_input=user_input.lower()
    ct=datetime.now()

    if "hello" in user_input or "hey" in user_input:
        return"Voice assistance activated.\nWelcome sir."
    elif "time" in user_input or "date" in user_input or "day" in user_input:
        return str(ct)
    elif "math" in user_input:
        return "Which chapter would you like to learn sir?"
    else:
        return "I am still learning,Try saying hello or math or ask date or time"
    
print("AI--Assistant--Lite")

while True:
    user_responce = input("you: ")
    if user_responce.lower() == "exit" :
        break
    AI_responce = assistant_brain(user_responce)
    print(f"Assistant : {AI_responce}")