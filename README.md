# 🧠 AI-Powered Document-Aware Conversational Chatbot

This project is a conversational chatbot built with FastAPI. It combines OpenAI’s language model with a PDF document retriever to answer user queries based on the document content and also general knowledge. It supports conversational memory to maintain context across chat interactions. The frontend serves a simple web chat UI.
it understands and answers questions based on uploaded PDF documents using **LangChain**, **OpenAI GPT-4**, and **FAISS** for semantic search. if question asked is not in document context, it falls back to OpenAI's GPT to respond intelligently even without document context.

![Chatbot Demo](https://d2vrvpw63099lz.cloudfront.net/chatbots-pillar-post/chatbot-pillar.png)

## ✨ Features

### ✅ Document Processing

- Upload and parse PDFs of any length
- Automatic text chunking and embedding
- FAISS vector store for efficient similarity search

### ✅ Conversation Capabilities

- Context-aware responses with `ConversationBufferMemory`
- Multi-turn dialogue retention
- Follow-up question handling

### ✅ Hybrid Intelligence

- Retrieval-Augmented Generation (RAG) for document answers
- GPT-4 fallback for general knowledge
- Confidence-based response selection

### ✅ User Experience

- Clean responsive interface
- Real-time processing indicators
- Keyboard-friendly controls

#

# 📁 **Project Structure**

```plaintext
chatbot/
├── backend/
│   ├── main.py              # FastAPI server (8000)
│   ├── rag_chain.py         # Core RAG pipeline
│   ├── vectorstore.py       # FAISS operations
│   ├── memory.py            # Session memory
│   ├── requirements.txt     # Python deps
│   └── docs/                # PDF storage
├── frontend/
│   ├── index.html           # Chat interface
│   ├── style.css            # Tailwind-like CSS
│   └── app.js               # API handlers
├
├── .env                     # Env
├
└── README.md
```

#

# 🚀 Installation & Setup

### Prerequisites

- Python 3.8+ (python --version)

- OpenAI API key

## 1. Clone & Prepare

```
git clone https://github.com/yourusername/ai-pdf-chatbot.git
cd ai-pdf-chatbot
```

## 2. 📦 Step 2: Set Up the Backend (FastAPI)

Navigate to the backend/ directory and create a virtual environment:

```
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the required dependencies:

```
pip install -r requirements.txt
```

## 🔐 Step 3: Add Your API Key (openapi)

```
OPENAI_API_KEY=your_openai_key_here
```

## ▶️ Step 4: Run the Backend Server

Start the FastAPI server with:

```
uvicorn main:app --reload
```

Your backend is now running at http://localhost:8000.

#

# 🐳 Run the Project with Docker Compose

You can easily spin up the chatbot with both the frontend and backend using Docker Compose.

## 📁 Project Structure

```
chatbot/
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   ├── rag_chain.py
│   ├── vectorstore.py
│   ├── memory.py
│   ├── requirements.txt
│   └── docs/
├── frontend/
│   ├── Dockerfile
│   ├── index.html
│   ├── style.css
│   └── app.js
├── docker-compose.yml
└── README.md
```

#

### 🛠️ Prerequisites

- Docker: Install Docker

- Docker Compose: Already included with Docker Desktop

# 🚀 Steps to Run the App

## Step 1 – Clone the Repository

```

git clone https://github.com/your-username/chatbot.git
cd chatbot
```

## Step 2 – Add Your OpenAI API Key

Create a .env file in the backend/ directory and place your openapi key:

```
OPENAI_API_KEY=your-openai-api-key
```

## Step 3 – Build and Run with Docker Compose

```
docker-compose up --build
```

This command:

- Builds both backend and frontend Docker images

- Launches both containers and connects them together

## Step 4 – Access the App

🌐 Visit: http://localhost:9000 (as specified in docker-compose file or you can change port to your convenience)

The frontend UI will load, and you can upload a pdf containing context and start chatting with the AI assistant.

## 🧼 Stopping and Cleaning Up

```
docker-compose down
```

## 🎥 Demo

![Chatbot Demo](./chatdemo.gif)

### 🗂 Upload a PDF

### 💬 Ask a Document-Specific Question

✅ The chatbot fetches the answer from the document using RAG.

## OR

### 💬 Ask a General Question

```
Hello
Tell me a joke
What's the weather?
```

✅ The chatbot falls back to OpenAI's GPT to respond intelligently even without document context.

## 🚀 Live Demo

[![Live Demo](https://img.shields.io/badge/Demo-Live-green?style=for-the-badge)](https://my-chatbot-app.azurecontainerapps.io/)

## 💡 Future Improvements

- Multi-document support

- Docker-based deployment

- Cloud hosting (AWS/GCP)

- Streamed GPT responses

- Persistent conversation logs

#

## 🙌 Acknowledgements

Huge thanks to the open-source community and the LangChain team!

![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-blueviolet)
