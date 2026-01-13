import sys
import time
import threading
import itertools
from langchain_ollama import OllamaLLM

thinking = False

def spinner():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if not thinking:
            break
        sys.stdout.write(f'\rBot is thinking... {c}')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * 30 + '\r')

def main():
    print("Chatbot 🤖 Started... [Type: exit to quit]\n")

    llm = OllamaLLM(model="llama3")
    conversation = ""

    while True:
        user_input = input("You: ")

        if user_input.lower() in ['exit', 'quit']:
            print("\nChatbot 🤖 stopped!")
            break

        conversation += f"User: {user_input}\nBot: "

        global thinking
        thinking = True

        spin_thread = threading.Thread(target=spinner)
        spin_thread.start()

        response = llm.invoke(conversation)

        thinking = False
        spin_thread.join()

        print("Bot:", response.strip(), "\n")
        conversation += f"{response}\n"

if __name__ == "__main__":
    main()
