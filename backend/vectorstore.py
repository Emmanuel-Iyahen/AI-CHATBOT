# from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import FAISS
# from langchain.document_loaders import PyMuPDFLoader

# def load_and_embed_documents(doc_path: str = "docs/"):
#     loader = PyMuPDFLoader(doc_path)
#     documents = loader.load()
#     embeddings = OpenAIEmbeddings()
#     db = FAISS.from_documents(documents, embeddings)
#     return db.as_retriever()



# import os
# from langchain_community.document_loaders import PyMuPDFLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import FAISS
# from langchain_openai import OpenAIEmbeddings

# def load_and_embed_documents(folder_path):
#     all_docs = []

#     for filename in os.listdir(folder_path):
#         if filename.endswith(".pdf"):
#             file_path = os.path.join(folder_path, filename)
#             loader = PyMuPDFLoader(file_path)
#             docs = loader.load()
#             all_docs.extend(docs)

#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
#     split_docs = text_splitter.split_documents(all_docs)

#     embeddings = OpenAIEmbeddings()
#     vectorstore = FAISS.from_documents(split_docs, embeddings)
#     return vectorstore.as_retriever()




# import os
# from langchain_community.document_loaders import PyMuPDFLoader
# from langchain_community.embeddings import OpenAIEmbeddings
# from langchain_community.vectorstores import FAISS
# from dotenv import load_dotenv

# load_dotenv()

# def load_and_embed_documents(pdf_path: str):
#     if not os.path.isfile(pdf_path):
#         raise ValueError(f"File path {pdf_path} is not a valid file")

#     loader = PyMuPDFLoader(pdf_path)
#     documents = loader.load()
#     embeddings = OpenAIEmbeddings()
#     vectorstore = FAISS.from_documents(documents, embeddings)
#     return vectorstore.as_retriever()




import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

def load_and_embed_documents(pdf_path: str):
    if not os.path.isfile(pdf_path):
        raise ValueError(f"File path {pdf_path} is not a valid file")

    loader = PyMuPDFLoader(pdf_path)
    documents = loader.load()

    # ✅ Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        separators=["\n\n", "\n", ".", " "]
    )
    split_docs = splitter.split_documents(documents)

    # ✅ Embed chunks
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(split_docs, embeddings)
    return vectorstore.as_retriever()
