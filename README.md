# devops-agent

This repo provides steps and scripts to create a new agent in Azure Foundry, that can be used to provide summaries of submitted code.

Here, the example is to include this as part of a CI/CD pipeline, to summarise changes between branches in a Git repo. For example when submitting a Pull request to merge a feature branch into a Main branch.

## examples

The examples are not intended to be production grade code or infrastructure. For the most part, they have been cloned from open source repos to provide workable code examples for the agent to analyse. Do not treat them as ready for production. They serve a purpose to give a wide array of different projects for the agent to review.

## Create a new agent

Create an agent in Azure foundry, using your choice of model, but maybe if just for a poc or testing use one of the small (SLM) models like "gpt-4o-mini".

Once created, save the agent name, endpoint and model name using the environment vars that are defined below. You can use the `devops-agent.py` script if you wish as this will create an agent in the foundry. 

You can interact with the agent using a variety of methods, but for this use case we want to integrate the agent into a pipeline. So we have a Python script called 'ask-devops.py'. This script reads the content of a file named changes.txt (the intention is that this is the result of a `git diff`). Running the `ask-devops.py` script will submit the content of the changes.txt file to the agent. The agent has been instructed to review this file, and provide a sumamry. If the agent was created using the devops-agent.py script, then it will provide a summary and advice based on the git diff content.

## pre-requisites

- An Azure Foundry project
- Python 3.11 or greater
- Git

## steps to demo

login to https://ai.azure.com/ and select your project, or create a new one.
Make a note of the project endpoint, the API key is not required if you are using entra authentication.
- Save the endpoint url in an environment variable
- Run az login
- Create an agent by clicking `start building --> create agent` or by running the devops-agent.py script. The script includes an example instruction set.

With the agent created, you can now submit code to it to provide a summary.

The script `ask-devops.py`, reads the content from a file named `changes.txt`, with the intention being that this is the result of a `git diff` command (`git diff main $branchName > ./changes.txt`). This results in the devops agent providing a summmary of the changes submitted to the specified branch when compared to the main branch. Exactly which source and target branch these changes are from depends on the git diff command used. For example:

`git diff main feature/initial > changes.txt`

This will compare the commited changes in the `feature/initial` branch, to the main branch.

You can use one of the example projects in the `./examples` directory, with local git for this.

- With the foundry project and agent setup, you're good to jump straight in to the code
- Create a new local Git repo by creating a new directory on your system and run `git init`
- add some files, good starting places are a README.md, the `ask-devops.py` script (this is for runnign locally, not great for prod but fine for testing)
- run `git add .` and then `git commit -am "initial" to commit these to the main branch
- create a new branch, and switch to it. `git branch feature/code` and then `git switch feature/code`

Now that you are in the new branch, go ahead and copy one of the example code projects to your repo. 
Run a `git status` to show all the files that are now in the repo. Run `git add .` so that they are managed by Git. Run again to show all files are tracked by Git.

Run `git commit -am "added exmaple code"`. The branch is now simulating an initial commit of a brand new project, where a whole load of app and/or terraform code has been committed to a branch. You now need to get the git diff into a changes.txt file (this is what the `ask-devops.py` script reads to send to the agent).

run `git diff main feature/code > changes.txt`, this will populate the git diff into the chanegs.txt file.

Now simply run the ask-devops.py script, `python ask-devops.py`, this pamy be `python3 ask-devops.py` depending on your systems pythin visrtual environment setup. Also make sure that the pythion requirements are installed first, either with the requirements.txt or refer to the `dependencies` section below.

The agent will review the contents of the changes.txt file, as this is the a big merge (main contained none of this), the changes.txt will effectively have the whole repo. This means the agent will review all code. The script takes the repsosne and saves it to `output.md` for review.

## environment vars

export PROJECT_ENDPOINT="https://andrew-8114-resource.services.ai.azure.com/api/projects/andrew-8114"
export AGENT_NAME="devops"
export MODEL_DEPLOYMENT_NAME="gpt-4o-mini"

## dependencies

pip install azure-ai-projects --pre
pip install openai azure-identity python-dotenv

## Azure devops pipeline

The pipeline template can be used to integrate this into an Azure Devops pipeline.
This requires the build service account to have permissions to contribute to pull requests (PullRequestContribute).

The pipeline will take the AI Agents summary, and write this as a comment in the PR. It will also save the summary as a file named output.md.

The pipeline template incldues a bash script that sets up the DevOps agent to run the `ask-devops.py` script, by installing the libraries, runs the `git diff` and writes the diff changes to a ./changes.txt file.s

## Next Steps

Add context for the agent to use. This can be a knowledgbase, to include your own best practices for writing code. maybe minimum versions of libraries, or where to check for library versions, where documentation is etc. This will give the agent a live reference point to make sure that it alwasy uses YOUR standards, not what it thinks is correct. For production implementatins, this is an important step.
