# devops-agent

This repo provides steps and scripts to create a new agent in Azure Foundry, that can be used to provide summaries of submitted code.

Here, the example is to include this as part of a CI/CD pipeline, to summarise changes between branches in a Git repo. For example when submitting a Pull request to merge a feature branch into a Main branch.

## examples

The examples are not intended to be production grade code or infrastrucutre. For the most part, they have been cloned from open source repos to provide workable code examples for the agwent to analyse. Do not treat them as ready for production. They serve a purpose to give a wide array of different projects for the agent to review.

## Create a new agent

Create an agent in Azure foundry, using your choice of model, but maybe if just for a poc or testing use one of the small (SLM) models like "gpt-4o-mini".

Once created, save the agent name, endpoint and model name using the environment vars that are defined below. You can use the `devops-agent.py` script if you wish as this will create an agent in the foundry. 

Currently, the 'ask-devops' script reads the diff from a file named changes.txt, this requires a `git diff` to be saved to this file, then you can go right ahead and run `ask-devops.py`, this will submit the content of the changes.txt file to the agent. The agent has the instructions of what to do. If using the devops-agent.py script, then it will provide a summary and advice based on this content.

## pre-requisites

An Azure Foundry project
Python 3.11 or greater

## steps

login to https://ai.azure.com/ and select your project, or create a new one.
make a note of the project endpoint, the API key is not required if you are using entra authentication
Save the endpoint url in an environment variable
run az login
Create an agent by clicking `start building --> create agent` or by running the devops-agent.py script

With the agent created, you can now submit code to it to provide a summary.

If you use the pythion script `ask-devops.py` then this will read the content of a file called `changes.txt` , that should be populated from a `git diff` command. (specifically `git diff > ./changes.txt`), this will result in the devops agent providing a summmary of the changes that Git can see. Exactly which source and target branch these changes are from depends on the git diff command used. For example:

## environment vars

export PROJECT_ENDPOINT="https://andrew-8114-resource.services.ai.azure.com/api/projects/andrew-8114"
export AGENT_NAME="devops"
export MODEL_DEPLOYMENT_NAME="gpt-4o-mini"

## dependencies

pip install azure-ai-projects --pre
pip install openai azure-identity python-dotenv

## Next Steps

