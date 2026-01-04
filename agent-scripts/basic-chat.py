import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import (
    AIProjectClient,
)  # https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-projects

# load environemnt vars (see README.md)
load_dotenv()

# display details of model and Foundry project
print(f"Using PROJECT_ENDPOINT: {os.environ['PROJECT_ENDPOINT']}")
print(f"Using MODEL_DEPLOYMENT_NAME: {os.environ['MODEL_DEPLOYMENT_NAME']}")

project_client = AIProjectClient(
    endpoint=os.environ["PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)

openai_client = project_client.get_openai_client()

response = openai_client.responses.create(
    model=os.environ["MODEL_DEPLOYMENT_NAME"],
    input="What is the size of France in square miles?",
)
print(f"Response output: {response.output_text}")
