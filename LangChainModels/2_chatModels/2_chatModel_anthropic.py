from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()
model = ChatAnthropic(model="claude-3-5-sonnet-20241022", temperature=1)

# Start conversation loop
inputstr = ""  # Initialize variable before using it
while True:
    inputstr = input("enter prompt: ")

    if inputstr.lower() in {"exit", "bye"}:
        print("Goodbye!")
        break

    # Invoke the model
    result = model.invoke(inputstr)

    # Print results
    print(f"\nResult: {result}")
    print(f"Content: {result.content}")
    print(f"Content length: {len(result.content)}\n")
