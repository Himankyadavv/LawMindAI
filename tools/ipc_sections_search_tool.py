# ipc_sections_search_tool.py
# import libraries

import os
from dotenv import load_dotenv
from crewai.tools import tool
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


@tool("IPC Sections Search Tool")
def search_ipc_sections(query: str) -> list[dict]:
    """
    Search IPC vector database for sections relevant to the input query.

    Args:
        query (str): User query in natural language.

    Returns:
        list[dict]: List of matching IPC sections with metadata and content.
    """

    load_dotenv()
    persist_dir = os.getenv("PERSIST_DIRECTORY_PATH", "./chromvector_db")
    collection_name = os.getenv("IPC_COLLECTION_NAME", "ipc_sections")

    if not persist_dir:
        raise EnvironmentError("Persist directory path not found")

    embedding = HuggingFaceEmbeddings()

    # Load Vector Store
    vectordb = Chroma(
        collection_name=collection_name,
        embedding_function=embedding,
        persist_directory=persist_dir
    )

    top_k = 3

    # similarity search — k must be passed as keyword argument
    docs = vectordb.similarity_search(query, k=top_k)

    # Format Result
    return [
        {
            "section": doc.metadata.get("section"),
            "section_title": doc.metadata.get("section_title"),
            "chapter": doc.metadata.get("chapter"),
            "chapter_title": doc.metadata.get("chapter_title"),
            "content": doc.page_content
        }
        for doc in docs
    ]
