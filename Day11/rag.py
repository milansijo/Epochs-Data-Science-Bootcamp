import os
import shutil

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# -----------------------------
# Configuration
# -----------------------------

DB_DIRECTORY = "chroma_db"

embedding_model = None
vector_db = None


# -----------------------------
# Lazy Load Embedding Model
# -----------------------------

def get_embedding_model():
    global embedding_model

    if embedding_model is None:
        embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    return embedding_model


# -----------------------------
# Create Vector Database
# -----------------------------

def create_vector_store(pdf_path):
    global vector_db

    # Delete previous database
    if os.path.exists(DB_DIRECTORY):
        shutil.rmtree(DB_DIRECTORY)

    # Load PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = splitter.split_documents(documents)

    # Create Vector Store
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=get_embedding_model(),
        persist_directory=DB_DIRECTORY
    )

    return vector_db


# -----------------------------
# Load Existing Vector Database
# -----------------------------

def load_vector_store():
    global vector_db

    # Already loaded
    if vector_db is not None:
        return vector_db

    # Database doesn't exist
    if not os.path.exists(DB_DIRECTORY):
        return None

    vector_db = Chroma(
        persist_directory=DB_DIRECTORY,
        embedding_function=get_embedding_model()
    )

    return vector_db


# -----------------------------
# Retrieve Context
# -----------------------------

def retrieve_context(question, k=4):

    db = load_vector_store()

    if db is None:
        return ""

    docs = db.similarity_search(
        query=question,
        k=k
    )

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    return context


# -----------------------------
# Clear Vector Database
# -----------------------------

def clear_vector_store():
    global vector_db
    global embedding_model

    vector_db = None
    embedding_model = None

    if os.path.exists(DB_DIRECTORY):
        shutil.rmtree(DB_DIRECTORY)