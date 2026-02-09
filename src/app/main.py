#src/app/main.py

from .retriever import retriever 
from .llm_client import llm_client 
from .orchestrator import orchestrator

#Asks user which mode to use, defaults to study if answer is not given
def choose_mode() -> str: 
    mode = input("Mode (study/assessment) [study]: ).strip().lower()

if mode = "":
    return "study"

if mode in ("study", "assessment")
    return mode 

print ("Invalid mode entered. Defaulting to Study Mode.")
    return "study"

#Prints model answer and sources from retrieved chunks
def display_response(response) -> None: 
    print("\n Answer")
    print(response.answer)
    print("\n sources used")
        if not response.chunks:
            print("No Chunks recieved.")
            return

for i chunk in enumerate(response.chunks, start = 1):
    print(f"[{i}]" {chunk.source} (score ={chunk.score}))
    print(f" {chunk.text}")

#main CLI loop for testing application flow
    def run() -> None 
    print("BIFS 614 Custom LLM Application Flow Demo")
    print("Type 'quit' to exit.\n")

    #choose mode at the beginning
    mode = choose_mode()

#create pipeline components
retriever = Retriever()
llm = llm_client(model_name = "stub-llm") 
orchestrator = orchestrator(retriever,llm)

#loop to ask user questions until they quit
while true:
    question = input("\n Please enter your question: ").strip() 

    if question.lower() in ("quit", "exit"):
        print("Goodbye!")
        break

    #send question through the system
    response = orchestrator.answer(question, mode= mode, k =4)     

    #display the results
    display_response(response)

    if __name__ == "__main__": 
        run()
