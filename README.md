<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>WALMART-SALESBOT-AND-SEARCHGPT</h1> 
<h3>◦ SalesBot-SearchGPT: Innovating Sales Agent of Walmart, and Custom Search GPT bot!</h3>
<h5 align="center">Connect with me: <a href="https://www.linkedin.com/in/swapnil-banduke/">LinkedIn</a> 🚀</h5>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=flat-square&logo=tqdm&logoColor=black" alt="tqdm" />
<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=flat-square&logo=Jupyter&logoColor=white" alt="Jupyter" />
<img src="https://img.shields.io/badge/arXiv-B31B1B.svg?style=flat-square&logo=arXiv&logoColor=white" alt="arXiv" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat-square&logo=OpenAI&logoColor=white" alt="OpenAI" />

<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat-square&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat-square&logo=Pytest&logoColor=white" alt="Pytest" />
<img src="https://img.shields.io/badge/Wikipedia-000000.svg?style=flat-square&logo=Wikipedia&logoColor=white" alt="Wikipedia" />
</div>


## 📍 Overview

The Walmart SalesBot and SearchGPT repository provides a AI solution to improve customer service and search capabilities. The tool includes an AI chatbot, enabling users to interact with either the'WalmartBot' or'SearchGPT' bot in real-time. It utilizes a robust conversational AI agent that can fetch webpage content, gather weather details, conduct searches, and retrieve news. It provides a sales assistance system for Walmart, implementing stages of sales conversations and managing customer interactions. Additionally, the repository includes an API server for product search and information retrieval.This project draws inspiration from SalesGPT and various other open-source initiatives. It is important to note that no direct copying or borrowing of ideas has occurred, and sincere gratitude is extended to all open source projects. 

### Walmart Bot
The Streamlit interface offers users two distinct options: Walmart Bot and SearchGPT.

#### Walmart Bot Functionality
The Walmart Bot functionality allows users to seamlessly search for products on Walmart. Additionally, it provides responses to specific product-related queries such as pricing inquiries and feature comparisons (e.g., "What is the price of iPhone 12?" or "Compare features of products"). Each response is accompanied by a source link or product link, offering users a comprehensive answer.

#### Technical Implementation
- Language Models: OpenAI models are employed in the project, with the flexibility to utilize any open-source model from Hugging Face.
- Langchain: The system leverages Langchain to enhance its functionality. Techniques such as Prompt Engineering, RetrievalQA, and Vector Database utilization contribute to the robustness of the system.
- Vector Database: Pinecone serves as the vector database, providing efficient storage and retrieval capabilities. The system is adaptable, allowing the use of alternative vector databases or traditional databases via llamaindex.
- Embeddings: OpenAI embeddings are utilized in the current implementation, though open-source embeddings can be seamlessly integrated for further customization.
#### API and Framework Choices
- API Framework: FastAPI is chosen to develop the API, providing a high-performance and user-friendly interface. However, the system is designed to be flexible, allowing the use of alternative frameworks like Flask or others.
- User Interface Framework: Streamlit is employed to construct the interface, offering a visually appealing and interactive platform. Users have the freedom to choose alternative frameworks based on their preferences.

### SearchGPT Functionality
In addition to Walmart Bot, the interface also facilitates the use of SearchGPT, enabling users to search for any question and obtain answers from the internet.

#### Technical Implementation
Language Models: Large language models are utilized in combination with LangChain and various tools to power the SearchGPT system.

---

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The system is a conversational agent combining REST APIs, Search and Recommendation systems built with Python. It utilizes Python scripts, Jupyter Notebook, and Docker for deployment.|
| 📄 | **Documentation**  | The repository lacks a comprehensive README.md file, providing a detailed explanation of the system. Absence of inline comments make it hard to understand the modules' purpose.|
| 🔗 | **Dependencies**   | The system extensively relies on external libraries such as Pydantic, FAISS, OpenAI, Pinecone, DuckDuckGo, and much more for operating its functionalities.|
| 🧩 | **Modularity**     | The system is loosely coupled and separated into several scripts, each responsible for handling a certain aspect, making it adaptable, understandable, and maintainable.|
| 🧪 | **Testing**        | The system uses pytest as a testing framework but lacks any presence of dedicated test cases to validate its functionality.   |
| ⚡️ | **Performance**    | The system's performance heavily relies on the  efficiency of GPT AI model & Pinecone search engine, hence can be inferred to be performant. But it lacks performance testing or benchmarking.|
| 🔐 | **Security**       | There aren't any explicit security measures found. The system being API based, needs to ensure critical information is sanitized before processing. |
| 🔀 | **Version Control**| The repository lacks specific version control strategy as there's absence of branches, tags or even comprehensive commit messages. |
| 🔌 | **Integrations**   | The system integrates with various Python libraries, APIs, GPT AI model, and Walmart's product data, supporting the bot functionalities.|
| 📶 | **Scalability**    | The system is scalable due to its loosely coupled design that would support future enhancements, provided there is efficient error handling and architectural improvements. |


---


## 📂 Repository Structure

```sh
└── Walmart-SalesBot-and-SearchGPT/
    ├── Data/
    ├── Dockerfile
    ├── Images/
    ├── csv_to_vectore_database(pinecone).ipynb
    ├── requirements.txt
    ├── run_api.py
    ├── search_capabilities.py
    ├── streamlit_interface.py
    └── walmart_functions.py
</details>
---
## 🚀 Getting Started

### 📋 Prerequisites

Ensure you have the required dependencies installed on your system. You can find them in the [requirements.txt] file.

### 🔧 Installation

1. Clone the Walmart-SalesBot-and-SearchGPT repository:
```sh
   git clone https://github.com/swapnilbanduke/Walmart-Salesbot-and-Searchgpt.git
```sh

2. Change to the project directory:
```sh
cd Walmart-SalesBot-and-SearchGPT
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Running Walmart-SalesBot-and-SearchGPT

```sh
python run_api.py
```
### 🕹️ Running using Docker
```
docker build -t bot .
docker run -p 5000:5000 bot
```

### ✨ Interface
```sh
streamlit run streamlit_interface.py
```


#### *Contributing Guidelines*

<details closed>
<summary>Click to expand</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone <your-forked-repo-url>
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.


---
