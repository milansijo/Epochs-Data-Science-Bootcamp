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

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------
# Create Vector Database
# -----------------------------

def create_vector_store(pdf_path):
    """
    Loads the uploaded PDF, splits it into chunks,
    generates embeddings and stores them in ChromaDB.
    """

    # Delete previous database
    if os.path.exists(DB_DIRECTORY):
        shutil.rmtree(DB_DIRECTORY)

    # Load PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = splitter.split_documents(documents)

    # Create Vector Store
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=DB_DIRECTORY
    )

    vector_db.persist()

    return vector_db


# -----------------------------
# Load Existing Vector Database
# -----------------------------

def load_vector_store():

    if not os.path.exists(DB_DIRECTORY):
        return None

    vector_db = Chroma(
        persist_directory=DB_DIRECTORY,
        embedding_function=embedding_model
    )

    return vector_db


# -----------------------------
# Retrieve Context
# -----------------------------

def retrieve_context(question, k=4):
    """
    Retrieves the most relevant chunks from ChromaDB.
    """

    db = load_vector_store()

    if db is None:
        return ""

    docs = db.similarity_search(
        query=question,
        k=k
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return context


# -----------------------------
# Delete Database
# -----------------------------

def clear_vector_store():

    if os.path.exists(DB_DIRECTORY):
        shutil.rmtree(DB_DIRECTORY)