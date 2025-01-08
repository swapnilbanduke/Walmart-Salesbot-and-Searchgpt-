<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>WALMART-SALESBOT-AND-SEARCHGPT</h1> 
<h3>◦ SalesBot-SearchGPT: Innovating Sales Agent of Walmart, and Custom Search GPT bot!</h3>
<h5 align="center">Connect with me: <a href="https://www.linkedin.com/in/swapnil-banduke/">LinkedIn</a> 🚀</h5>
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
```

## 🚀 Getting Started

1. Clone the Walmart-SalesBot-and-SearchGPT repository:
```sh
   git clone https://github.com/swapnilbanduke/Walmart-Salesbot-and-Searchgpt.git
```

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

