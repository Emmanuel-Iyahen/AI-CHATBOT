
from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from rag_chain import qa_chain, retriever, llm  # import llm as well for fallback


import os
from vectorstore import load_and_embed_documents
from rag_chain import qa_chain, update_retriever

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this for production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



import os
from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from rag_chain import qa_chain, llm, update_retriever
from vectorstore import load_and_embed_documents
from memory import get_memory

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# CORS setup for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload_pdf/")
async def upload_pdf(title: str = Form(...), file: UploadFile = File(...)):
    try:


        # Save the file in chunks (1 MB at a time)
        file_location = os.path.join(UPLOAD_DIR, f"{title}.pdf")
        with open(file_location, "wb") as f:
            while True:
                chunk = await file.read(1024 * 1024)  # 1MB
                if not chunk:
                    break
                f.write(chunk)



        # Save uploaded PDF file
        # file_location = os.path.join(UPLOAD_DIR, f"{title}.pdf")
        # with open(file_location, "wb") as f:
        #     content = await file.read()
        #     f.write(content)

        # Load and embed the new PDF document
        retriever = load_and_embed_documents(file_location)

        # Update the retriever in the global qa_chain instance
        update_retriever(retriever)

        return {"message": f"PDF for '{title}' uploaded and retriever updated."}
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})




import re

def get_keywords(text):
    return set(re.findall(r"\b\w{3,}\b", text.lower()))



@app.post("/chat")
async def chat(request: Request):
    try:
        body = await request.json()
        message = body.get("message")

        if not message:
            return JSONResponse(status_code=400, content={"error": "Message is required"})

        # Retrieve relevant documents
        docs = qa_chain.retriever.get_relevant_documents(message)

        if docs:
            total_content = " ".join(doc.page_content.lower() for doc in docs)

            query_keywords = get_keywords(message)
            doc_keywords = get_keywords(total_content)

            has_overlap = bool(query_keywords & doc_keywords)

            if not has_overlap:
                # Use OpenAI fallback
                answer = llm.predict(message)
            else:
                # Use QA Chain
                result = qa_chain.invoke({
                    "question": message,
                    # "chat_history": []
                })
                answer = result["answer"]
        else:
            # No relevant docs found
            answer = llm.predict(message)

        return {"response": answer}

    except Exception as e:
        print("❌ ERROR:", str(e))
        return JSONResponse(status_code=500, content={"error": str(e)})






@app.post("/chat")
async def chat(request: Request):
    try:
        body = await request.json()
        message = body.get("message")

        if not message:
            return JSONResponse(status_code=400, content={"error": "Message is required"})

        # Retrieve relevant documents
        docs = qa_chain.retriever.get_relevant_documents(message)

        if docs:
            # Just use the RAG pipeline directly
            result = qa_chain.invoke({
                "question": message,
                "chat_history": []
            })
            answer = result["answer"]
        else:
            # Fallback: no docs found at all
            answer = llm.predict(message)

        return {"response": answer}

    except Exception as e:
        print("❌ ERROR:", str(e))
        return JSONResponse(status_code=500, content={"error": str(e)})




