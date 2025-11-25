"""
Configuration for Ollama (Local LLM)
"""
import os
from dotenv import load_dotenv

load_dotenv()

class ConfigOllama:
    # Ollama Settings
    OLLAMA_BASE_URL = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')
    
    # Model Settings
    LLM_MODEL = os.getenv('OLLAMA_LLM_MODEL', 'mistral')  # or 'llama2'
    EMBEDDING_MODEL = os.getenv('OLLAMA_EMBEDDING_MODEL', 'nomic-embed-text')
    
    # Text Splitting Settings
    CHUNK_SIZE = int(os.getenv('CHUNK_SIZE', 1000))
    CHUNK_OVERLAP = int(os.getenv('CHUNK_OVERLAP', 200))
    
    # Vector Store Settings
    VECTOR_STORE_PATH = os.getenv('VECTOR_STORE_PATH', './vector_store_ollama')
    VECTOR_STORE_TYPE = 'chroma'  # Using Chroma instead of FAISS for Ollama
    
    # Retrieval Settings
    TOP_K_RESULTS = int(os.getenv('TOP_K_RESULTS', 4))
    
    # Temperature for LLM
    TEMPERATURE = float(os.getenv('TEMPERATURE', 0.7))
    
    # No API key needed!
    OPENAI_API_KEY = None
