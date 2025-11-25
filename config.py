"""
Configuration settings for AI Teaching Assistant
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # OpenAI Settings
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    # AWS Settings (Optional)
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
    
    # Text Splitting Settings
    CHUNK_SIZE = int(os.getenv('CHUNK_SIZE', 1000))
    CHUNK_OVERLAP = int(os.getenv('CHUNK_OVERLAP', 200))
    
    # Vector Store Settings
    VECTOR_STORE_PATH = os.getenv('VECTOR_STORE_PATH', './vector_store')
    
    # Embedding Model
    EMBEDDING_MODEL = 'text-embedding-ada-002'
    
    # LLM Model
    LLM_MODEL = 'gpt-3.5-turbo'
    
    # Retrieval Settings
    TOP_K_RESULTS = 4
    
    # Temperature for LLM
    TEMPERATURE = 0.7
