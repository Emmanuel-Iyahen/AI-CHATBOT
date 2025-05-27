# from fastapi import FastAPI, Request
# from pydantic import BaseModel
# from rag_chain import qa_chain

# app = FastAPI()

# class ChatRequest(BaseModel):
#     message: str

# @app.post("/chat")
# async def chat(req: ChatRequest):
#     user_message = req.message
#     response = qa_chain.run(user_message)
#     return {"response": response}



# from fastapi import FastAPI, Request
# from fastapi.middleware.cors import CORSMiddleware
# from rag_chain import qa_chain
# from fastapi.responses import JSONResponse


# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Adjust this in production
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.post("/chat")
# async def chat(request: Request):
#     body = await request.json()
#     message = body.get("message")

#     try:
#         result = qa_chain.run({
#             "question": message,
#             "chat_history": []
#         })
#         return {"response": result}
#     except Exception as e:
#         print("❌ ERROR:", str(e))
#         return JSONResponse(status_code=500, content={"error": str(e)})





# from fastapi import FastAPI, Request
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import JSONResponse
# from rag_chain import qa_chain, retriever  # assuming retriever is imported here
# from langchain_community.chat_models import ChatOpenAI

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Change in production!
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# chat_history = []

# @app.post("/chat")
# async def chat(request: Request):
#     body = await request.json()
#     message = body.get("message")

#     try:
#         # Retrieve relevant docs from the PDF retriever
#         docs = retriever.get_relevant_documents(message)

#         # Check if retrieved docs have meaningful content
#         if docs and sum(len(doc.page_content) for doc in docs) > 20:
#             # Use ConversationalRetrievalChain with context from PDF
#             result = qa_chain.invoke({
#                 "question": message,
#                 "chat_history": chat_history
#             })
#             answer = result["answer"]
#         else:
#             # No relevant context found, fallback to direct OpenAI answer
#             llm = ChatOpenAI(temperature=0)
#             answer = llm.predict(message)

#         # Update chat history
#         chat_history.append((message, answer))

#         return {"response": answer}

#     except Exception as e:
#         print("❌ ERROR:", str(e))
#         return JSONResponse(status_code=500, content={"error": str(e)})





# from fastapi import FastAPI, Request, Depends
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import JSONResponse
# from rag_chain import qa_chain, retriever
# from langchain_community.chat_models import ChatOpenAI

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# llm = ChatOpenAI(temperature=0)

# # Simple per-request chat history (in real apps use DB/session store)
# def get_chat_history():
#     return []

# @app.post("/chat")
# async def chat(request: Request, chat_history = Depends(get_chat_history)):
#     body = await request.json()
#     message = body.get("message")

#     try:
#         docs = retriever.get_relevant_documents(message)
#         if docs and sum(len(doc.page_content) for doc in docs) > 20:
#             result = qa_chain.invoke({
#                 "question": message,
#                 "chat_history": chat_history
#             })
#             answer = result["answer"]
#         else:
#             answer = llm.predict(message)

#         chat_history.append((message, answer))

#         return {"response": answer}
#     except Exception as e:
#         print("❌ ERROR:", str(e))
#         return JSONResponse(status_code=500, content={"error": str(e)})


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

# @app.post("/chat")
# async def chat(request: Request):
#     body = await request.json()
#     message = body.get("message")

#     try:
#         # Fetch relevant documents for this query
#         docs = retriever.get_relevant_documents(message)

#         if docs and sum(len(doc.page_content) for doc in docs) > 20:
#             # Use QA chain with internal memory — NO manual chat_history passing
#             answer = qa_chain.run(message)
#         else:
#             # No relevant context found, fallback to pure LLM answer
#             answer = llm.predict(message)

#         return {"response": answer}

#     except Exception as e:
#         print("❌ ERROR:", str(e))
#         return JSONResponse(status_code=500, content={"error": str(e)})



# @app.post("/chat")
# async def chat(request: Request):
#     body = await request.json()
#     message = body.get("message")

#     try:
#         docs = retriever.get_relevant_documents(message)

#         if docs and sum(len(doc.page_content) for doc in docs) > 20:
#             answer = qa_chain.run(message)

#             # If answer contains "no mention" or "I don't have information" phrases, fallback
#             no_info_phrases = [
#                 "no mention",
#                 "don't have information",
#                 "don't have enough information",
#                 "no relevant",
#                 "cannot provide",
#                 "sorry"
#             ]

#             if any(phrase.lower() in answer.lower() for phrase in no_info_phrases):
#                 answer = llm.predict(message)

#         else:
#             answer = llm.predict(message)

#         return {"response": answer}

#     except Exception as e:
#         print("❌ ERROR:", str(e))
#         return JSONResponse(status_code=500, content={"error": str(e)})



# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# @app.post("/upload_pdf/")
# async def upload_pdf(title: str = Form(...), file: UploadFile = File(...)):
#     # Save uploaded PDF file
#     file_location = os.path.join(UPLOAD_DIR, f"{title}.pdf")
#     with open(file_location, "wb") as f:
#         content = await file.read()
#         f.write(content)

#     # Load and embed the new PDF document
#     retriever = load_and_embed_documents(file_location)

#     # Update the retriever in the global qa_chain instance
#     update_retriever(retriever)

#     return {"message": f"PDF for '{title}' uploaded and retriever updated."}


# @app.post("/chat")
# async def chat(request: Request):
#     body = await request.json()
#     message = body.get("message")

#     try:
#         docs = retriever.get_relevant_documents(message)
#         total_content = " ".join(doc.page_content.lower() for doc in docs)

#         if docs and sum(len(doc.page_content) for doc in docs) > 20:
#             # If the retrieved docs do not mention the keyword exactly, fallback
#             if message not in total_content:
#                 answer = llm.predict(message)
#             else:
#                 result = qa_chain.invoke({
#                     "question": message,
#                     "chat_history": []
#                 })
#                 answer = result["answer"]
#         else:
#             answer = llm.predict(message)

#         return {"response": answer}

#     except Exception as e:
#         print("❌ ERROR:", str(e))
#         return JSONResponse(status_code=500, content={"error": str(e)})




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
        # Save uploaded PDF file
        file_location = os.path.join(UPLOAD_DIR, f"{title}.pdf")
        with open(file_location, "wb") as f:
            content = await file.read()
            f.write(content)

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





#works partially

# @app.post("/chat")
# async def chat(request: Request):
#     try:
#         body = await request.json()
#         message = body.get("message")

#         if not message:
#             return JSONResponse(status_code=400, content={"error": "Message is required"})

#         # Retrieve relevant documents
#         docs = qa_chain.retriever.get_relevant_documents(message)

#         if docs:
#             total_content = " ".join(doc.page_content.lower() for doc in docs)

#             # Fallback if question not semantically represented in retrieved docs
#             if message.lower() not in total_content:
#                 answer = llm.predict(message)
#             else:
#                 result = qa_chain.invoke({
#                     "question": message,
#                     "chat_history": []
#                 })
#                 answer = result["answer"]
#         else:
#             # Fallback: no docs found
#             answer = llm.predict(message)

#         return {"response": answer}

#     except Exception as e:
#         print("❌ ERROR:", str(e))
#         return JSONResponse(status_code=500, content={"error": str(e)})



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




# @app.post("/chat")
# async def chat(request: Request):
#     try:
#         body = await request.json()
#         message = body.get("message")

#         if not message:
#             return JSONResponse(status_code=400, content={"error": "Message is required"})

#         # Run RAG chain
#         result = qa_chain.invoke({
#             "question": message,
#             "chat_history": []
#         })

#         answer = result["answer"]
#         source_docs = result.get("source_documents", [])

#         # Check if retrieved sources are empty or clearly off-topic
#         content_combined = " ".join(doc.page_content.lower() for doc in source_docs)
#         if not source_docs or (message.lower() not in content_combined and len(content_combined) < 20):
#             print("📉 Fallback to LLM without context")
#             answer = llm.predict(message)

#         # Debug log for development
#         print("📥 User:", message)
#         print("🤖 Answer:", answer)
#         print("📚 Retrieved Chunks:", [doc.page_content[:150] for doc in source_docs])

#         return {"response": answer}

#     except Exception as e:
#         print("❌ ERROR:", str(e))
#         return JSONResponse(status_code=500, content={"error": str(e)})
