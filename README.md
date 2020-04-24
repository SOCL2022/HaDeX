# ChatGPT + Enterprise data with Azure OpenAI and Cognitive Search

This sample demonstrates a few approaches for creating ChatGPT-like experiences over your own data using the Retrieval Augmented Generation pattern. It uses Azure OpenAI Service to access the ChatGPT model (gpt-35-turbo), and Azure Cognitive Search for data indexing and retrieval.

The repo includes sample data so it's ready to try end to end. In this sample application we use a fictitious company called Contoso Electronics, and the experience allows its employees to ask questions about the benefits, internal policies, as well as job descriptions and roles.

![RAG Architecture](docs/appcomponents.png)

## Features

* Chat and Q&A interfaces
* Explores various options to help users evaluate the trustworthiness of responses with citations, tracking of source content, etc.
* Shows possible approaches for data preparation, prompt construction, and orchestration of interaction between model (ChatGPT) and retriever (Cognitive Search)
* Settings directly in the UX to tweak the behavior and experiment with options

![Chat screen](docs/chatscreen.png)

## Getting Started

> **IMPORTANT:** In order to deploy and run this example, you'll need an **Azure subscription with access enabled for the Azure OpenAI service**. You can request access [here](https://aka.ms/oaiapply).

### Prerequisites

- Azure Developer CLI (install from [here](https://aka.ms/azure-dev/install))
- Python (install from [here](https://www.python.org/downloads/))
    - **Imporant**: Python and the pip package manager must be in the path in Windows for the setup scripts to work.
- Node.js (install from [here](https://nodejs.org/en/download/))
- Git (install from [here](https://git-scm.com/downloads))
- Powershell (pwsh) (install from [here](https://github.com/powershell/powershell))
   - **Imporant**: Ensure you can run pwsh.exe from a PowerShell command. If this fails, you likely need to upgrade PowerShell.

### Installation

Starting from scratch:
1. Create a new folder and switch to it in the terminal
2. Run "azd up -t azure-search-openai-demo"
    * For the target location, the regions that currently support the models used in