import os #This brings in Python's built-in os module
import requests #Brings in requests library.Used to send HTTP requests to APIs or webservices
from dotenv import load_dotenv # Loads hidden settings from a .env file


load_dotenv() # Loads variables from .env file into the program
NAME = os.getenv("ASSISTANT_NAME", "EVA")  # Gets assistant name from .env or defaults to EVA

def save_memory(user_input, ai_response): # Function to store user and AI conversation
    """Saves the conversation to a text file."""
    with open("chat_history.txt", "a", encoding="utf-8") as file: # Opens file in append mode to store chat history safely
        file.write(f"User: {user_input}\n") # Writes user input into file with a new line
        file.write(f"{NAME}: {ai_response}\n")  # Writes assistant response into file
        file.write("-" * 20 + "\n") # Adds a separator line for readability

def speak_to_eva(prompt):
    url = "http://localhost:11434/api/generate" # Local AI server endpoint
    payload = { # Data package sent to the AI server
        "model": "deepseek-r1:8b",
        "prompt": prompt,
        "stream": False
    }
    try:
        # Try to do the risky thing (calling the server)
        response = requests.post(url, json=payload) # Sends request to AI server with input data
        full_response = response.json().get("response", "")  # Extracts AI reply safely from JSON
        
        # Clean the Reasoning (R1) output
        if "</think>" in full_response:
            return full_response.split("</think>")[-1].strip() # Removes reasoning and returns clean answer
        return full_response # Return response directly if no reasoning tag found
    except Exception as e: # Catch any error that occurs in try block
        return f"Error: {e}"  # Returns error message instead of crashing

if __name__ == "__main__":
    # This is MY custom startup sequence
    print(f"--- ⚡ EVA RESEARCH CORE v1.0 ⚡ ---")
    print(f"Owner: Mahesh | Status: Online")
    
    if os.path.exists("chat_history.txt"): # Check if history file exists
        print("\n--- Previous Conversation ---")
        with open("chat_history.txt", "r", encoding="utf-8") as f:  # Opens file to read chat history
            print(f.read()) # Reads and displays stored chat history
        print("--- End of History ---\n")

    while True:  # Keeps the assistant running continuously
        user_query = input(f"[Mahesh]: ") # Takes input from user

        if user_query.lower() in ["exit", "quit", "bye"]: # Checks if user wants to exit
            print(f"👋 {NAME}: Goodbye, Mahesh!")
            break  # Stops the loop and exits program
            
        print(f"\n[{NAME} is thinking...]") # Shows that assistant is processing
        answer = speak_to_eva(user_query)  # Sends input to AI and gets response
        
        print(f"\n[{NAME}]: {answer}") # Prints AI response to user
        
        # ACTIVATE MEMORY
        save_memory(user_query, answer)