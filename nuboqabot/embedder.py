from decouple import config
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss


model = SentenceTransformer(config('SENTENCE_TRANSFORMER', cast=str))
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, 
    chunk_overlap=50
)

def embed_text(text: str):
    chunks = splitter.split_text(text)
    embeddings = model.encode(chunks, batch_size=16, show_progress_bar=False, normalize_embeddings=True)
    
    return chunks, np.array(embeddings)

def create_or_update_index(index, new_embeddings):
    if index is None:
        dim = new_embeddings.shape[1]
        index = faiss.IndexFlatL2(dim)
    index.add(new_embeddings)

    return index