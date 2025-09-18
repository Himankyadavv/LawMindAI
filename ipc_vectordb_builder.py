from langchain_community.docstore.document import Document 
from langchain_chroma import Chroma 
from langchain_huggingface import HuggingFaceEmbeddings 

def load_ipc_data(file_path : str) -> list[dict]:
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
    

    
