import os
import requests
from dotenv import load_dotenv


load_dotenv()
NAME = os.getenv("ASSISTANT_NAME", "EVA")

def save_memory(user_input, ai_response):
    """Saves the conversation to a text file."""
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        file.write(f"User: {user_input}\n")
        file.write(f"{NAME}: {ai_response}\n")
        file.write("-" * 20 + "\n")

def speak_to_eva(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "deepseek-r1:8b",
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        full_response = response.json().get("response", "")
        
        # Clean the Reasoning (R1) output
        if "</think>" in full_response:
            return full_response.split("</think>")[-1].strip()
        return full_response
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # This is MY custom startup sequence
    print(f"--- ⚡ EVA RESEARCH CORE v1.0 ⚡ ---")
    print(f"Owner: Mahesh | Status: Online")
    
    if os.path.exists("chat_history.txt"):
        print("\n--- Previous Conversation ---")
        with open("chat_history.txt", "a", encoding="utf-8") as f:
            print(f.read())
        print("--- End of History ---\n")

    while True:
        user_query = input(f"[Mahesh]: ")

        if user_query.lower() in ["exit", "quit", "bye"]:
            print(f"👋 {NAME}: Goodbye, Mahesh!")
            break
            
        print(f"\n[{NAME} is thinking...]")
        answer = speak_to_eva(user_query)
        
        print(f"\n[{NAME}]: {answer}")
        
        # ACTIVATE MEMORY
        save_memory(user_query, answer)