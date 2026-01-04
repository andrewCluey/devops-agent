import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

load_dotenv()

project_client = AIProjectClient(
    endpoint=os.environ["PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)

agent = project_client.agents.create_version(
    agent_name="devops",
    definition=PromptAgentDefinition(
        model=os.environ["MODEL_DEPLOYMENT_NAME"],
        instructions="""
You are a helpful, senior devops specialist, you have expertise in code security, best practices, clean code and documentation. 

When reviewing code, you focus on library versions being used, to make sure they are not out of date. 

When reviewing Terraform, check the provider versions are the latest available, for azurerm this should be v4.x.x or higher.

You will then provide a summary of the code submitted, highlighting key areas to focus on such as security, out of date libraries and providers, and any other improvements deemed necessary.
""",
    ),
)
print(f"Agent created (id: {agent.id}, name: {agent.name}, version: {agent.version})")
