from langchain_ollama import OllamaLLM

def main():
    print("Chatbot🤖 Started...[Type:exit to quit]\n")
    
    llm=OllamaLLM(model="llama3")
    conversation=""
    
    while True:
        user_input=input("You:")
        
        if user_input.lower() in ['exit','quit']:
            response=llm.invoke("exit\n")
            print(response)
            print()
            print("chatbot🤖 stopped!")
            break
        
        conversation+=f"User:{user_input}\nBot:"
        
        response=llm.invoke(conversation)
        print("Bot:",response.strip()) 
        print()  
        conversation+=f"{response}\n"
    
    
    
if __name__=="__main__":
    main()    
            
    