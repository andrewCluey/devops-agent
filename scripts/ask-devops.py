import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

with open("changes.txt", "r") as f:
    content = f.read()  # call the method

load_dotenv()

project_client = AIProjectClient(
    endpoint=os.environ["PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)

agent_name = "devops"
openai_client = project_client.get_openai_client()

# Optional Step: Create a conversation to use with the agent
conversation = openai_client.conversations.create()
print(f"Created conversation (id: {conversation.id})")

# Chat with the agent to answer questions
response = openai_client.responses.create(
    conversation=conversation.id,  # Optional conversation context for multi-turn
    extra_body={"agent": {"name": agent_name, "type": "agent_reference"}},
    input=f"{content}",
)
# print the output to the console
print(f"Response output: {response.output_text}")

# save the output to a markdown file
with open("output.md", "w", encoding="utf-8") as f:
    f.write(response.output_text)
