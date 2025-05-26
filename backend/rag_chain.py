# from langchain_community.chat_models import ChatOpenAI
# from langchain.chains import ConversationalRetrievalChain
# from vectorstore import load_and_embed_documents
# from memory import get_memory

# retriever = load_and_embed_documents("docs/")
# memory = get_memory()
# llm = ChatOpenAI(temperature=0)

# qa_chain = ConversationalRetrievalChain.from_llm(
#     llm=llm,
#     retriever=retriever,
#     memory=memory
# )



# from langchain_community.chat_models import ChatOpenAI
# from langchain.chains import ConversationalRetrievalChain
# from vectorstore import load_and_embed_documents
# from dotenv import load_dotenv

# load_dotenv()

# # Load the single PDF document retriever
# retriever = load_and_embed_documents("docs/example.pdf")

# llm = ChatOpenAI(temperature=0)

# # Memory can be added here if you want
# qa_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever)


# from langchain_community.chat_models import ChatOpenAI
# from langchain.chains import ConversationalRetrievalChain
# from vectorstore import load_and_embed_documents
# from memory import get_memory
# from dotenv import load_dotenv

# load_dotenv()

# retriever = load_and_embed_documents("docs/example.pdf")
# llm = ChatOpenAI(temperature=0)

# memory = get_memory()

# qa_chain = ConversationalRetrievalChain.from_llm(
#     llm=llm,
#     retriever=retriever,
#     memory=memory
# )



# from langchain_community.chat_models import ChatOpenAI
# from langchain.chains import ConversationalRetrievalChain
# from vectorstore import load_and_embed_documents
# from memory import get_memory
# from dotenv import load_dotenv

# load_dotenv()

# retriever = load_and_embed_documents("docs/epl.pdf")
# llm = ChatOpenAI(temperature=0)
# memory = get_memory()

# qa_chain = ConversationalRetrievalChain.from_llm(
#     llm=llm,
#     retriever=retriever,
#     memory=memory,
#     return_source_documents=False,
# )



from langchain_community.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from vectorstore import load_and_embed_documents
from memory import get_memory
from dotenv import load_dotenv

load_dotenv()

retriever = load_and_embed_documents("docs/epl.pdf")
llm = ChatOpenAI(temperature=0)
memory = get_memory()

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory,
    return_source_documents=False,
)


def update_retriever(new_retriever):
    global retriever, qa_chain
    retriever = new_retriever
    qa_chain.retriever = retriever