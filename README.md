# 🧠 AI-Powered PDF Chatbot

An intelligent chatbot that understands and answers questions based on uploaded PDF documents using **LangChain**, **OpenAI GPT-4**, and **FAISS** for semantic search.

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
├── tests/                   # pytest files
├── .env.example             # Env template
├── LICENSE
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

## 🧪 Demo Example

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
