"""
Vector Store Manager for Ollama
Uses Chroma DB with local embeddings
"""
from typing import List, Optional
from langchain.schema import Document
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from config_ollama import ConfigOllama
import os


class VectorStoreManagerOllama:
    """Manage Chroma vector store with Ollama embeddings"""
    
    def __init__(self):
        """Initialize vector store manager with Ollama"""
        self.embeddings = OllamaEmbeddings(
            base_url=ConfigOllama.OLLAMA_BASE_URL,
            model=ConfigOllama.EMBEDDING_MODEL
        )
        self.vector_store = None
        print(f"Using Ollama embeddings: {ConfigOllama.EMBEDDING_MODEL}")
    
    def create_vector_store(self, documents: List[Document]) -> Chroma:
        """
        Create Chroma vector store from documents
        
        Args:
            documents: List of Document objects
            
        Returns:
            Chroma vector store
        """
        try:
            print(f"Creating embeddings for {len(documents)} documents...")
            self.vector_store = Chroma.from_documents(
                documents=documents,
                embedding=self.embeddings,
                persist_directory=ConfigOllama.VECTOR_STORE_PATH
            )
            print(f"+ Vector store created successfully")
            return self.vector_store
        except Exception as e:
            print(f"X Error creating vector store: {e}")
            return None
    
    def add_documents(self, documents: List[Document]):
        """Add documents to existing vector store"""
        try:
            if self.vector_store is None:
                print("No existing vector store. Creating new one...")
                self.create_vector_store(documents)
            else:
                self.vector_store.add_documents(documents)
                print(f"+ Added {len(documents)} documents to vector store")
        except Exception as e:
            print(f"X Error adding documents: {e}")
    
    def save_vector_store(self, path: str = None):
        """Save vector store to disk (Chroma auto-persists)"""
        try:
            if self.vector_store is None:
                print("X No vector store to save")
                return
            
            # Chroma auto-persists, just confirm
            print(f"+ Vector store saved to: {ConfigOllama.VECTOR_STORE_PATH}")
        except Exception as e:
            print(f"X Error saving vector store: {e}")
    
    def load_vector_store(self, path: str = None) -> Optional[Chroma]:
        """Load vector store from disk"""
        try:
            load_path = path or ConfigOllama.VECTOR_STORE_PATH
            
            if not os.path.exists(load_path):
                print(f"X Vector store not found at: {load_path}")
                return None
            
            self.vector_store = Chroma(
                persist_directory=load_path,
                embedding_function=self.embeddings
            )
            print(f"+ Vector store loaded from: {load_path}")
            return self.vector_store
        except Exception as e:
            print(f"X Error loading vector store: {e}")
            return None
    
    def similarity_search(self, query: str, k: int = None) -> List[Document]:
        """Search for similar documents"""
        try:
            if self.vector_store is None:
                print("X No vector store available")
                return []
            
            k = k or ConfigOllama.TOP_K_RESULTS
            results = self.vector_store.similarity_search(query, k=k)
            print(f"+ Found {len(results)} similar documents")
            return results
        except Exception as e:
            print(f"X Error in similarity search: {e}")
            return []
    
    def similarity_search_with_score(self, query: str, k: int = None) -> List[tuple]:
        """Search for similar documents with similarity scores"""
        try:
            if self.vector_store is None:
                print("X No vector store available")
                return []
            
            k = k or ConfigOllama.TOP_K_RESULTS
            results = self.vector_store.similarity_search_with_score(query, k=k)
            print(f"+ Found {len(results)} similar documents with scores")
            return results
        except Exception as e:
            print(f"X Error in similarity search: {e}")
            return []
