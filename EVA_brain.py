import os
import requests
from dotenv import load_dotenv

# 1. Initialize the Vault
load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")
NAME = os.getenv("ASSISTANT_NAME", "EVA")

def speak_to_eva(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "deepseek-r1:8b",  # UPDATED TO YOUR DOWNLOADED BRAIN
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        full_response = response.json().get("response", "")
        
        # R1 models include their "thoughts" in the output. 
        # This part removes the internal 'thinking' so you just see the answer.
        if "</think>" in full_response:
            return full_response.split("</think>")[-1].strip()
        return full_response
    except Exception as e:
        return f"Error connecting to EVA's brain: {e}"

if __name__ == "__main__":
    print(f"🚀 {NAME} (Reasoning Mode) Online.")
    
    if not TOKEN:
        print("⚠️ Warning: GITHUB_TOKEN not found in .env vault.")
    
    user_query = input(f"\n[Mahesh]: ")
    print(f"\n[{NAME} is reasoning...]")
    
    answer = speak_to_eva(user_query)
    print(f"\n[{NAME}]: {answer}")