"""
Vector Store Module
Handles embedding generation and FAISS vector store operations
"""
from typing import List, Optional
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from config import Config
import os


class VectorStoreManager:
    """Manage FAISS vector store for document embeddings"""
    
    def __init__(self, api_key: str = None):
        """
        Initialize vector store manager
        
        Args:
            api_key: OpenAI API key (default from config)
        """
        self.api_key = api_key or Config.OPENAI_API_KEY
        self.embeddings = OpenAIEmbeddings(
            openai_api_key=self.api_key,
            model=Config.EMBEDDING_MODEL
        )
        self.vector_store = None
    
    def create_vector_store(self, documents: List[Document]) -> FAISS:
        """
        Create FAISS vector store from documents
        
        Args:
            documents: List of Document objects
            
        Returns:
            FAISS vector store
        """
        try:
            print(f"Creating embeddings for {len(documents)} documents...")
            self.vector_store = FAISS.from_documents(
                documents=documents,
                embedding=self.embeddings
            )
            print(f"+ Vector store created successfully")
            return self.vector_store
        except Exception as e:
            print(f"X Error creating vector store: {e}")
            return None
    
    def add_documents(self, documents: List[Document]):
        """
        Add documents to existing vector store
        
        Args:
            documents: List of Document objects to add
        """
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
        """
        Save vector store to disk
        
        Args:
            path: Path to save vector store (default from config)
        """
        try:
            if self.vector_store is None:
                print("X No vector store to save")
                return
            
            save_path = path or Config.VECTOR_STORE_PATH
            os.makedirs(save_path, exist_ok=True)
            
            self.vector_store.save_local(save_path)
            print(f"+ Vector store saved to: {save_path}")
        except Exception as e:
            print(f"X Error saving vector store: {e}")
    
    def load_vector_store(self, path: str = None) -> Optional[FAISS]:
        """
        Load vector store from disk
        
        Args:
            path: Path to load vector store from (default from config)
            
        Returns:
            FAISS vector store or None
        """
        try:
            load_path = path or Config.VECTOR_STORE_PATH
            
            if not os.path.exists(load_path):
                print(f"X Vector store not found at: {load_path}")
                return None
            
            self.vector_store = FAISS.load_local(
                load_path,
                self.embeddings,
                allow_dangerous_deserialization=True
            )
            print(f"+ Vector store loaded from: {load_path}")
            return self.vector_store
        except Exception as e:
            print(f"X Error loading vector store: {e}")
            return None
    
    def similarity_search(self, query: str, k: int = None) -> List[Document]:
        """
        Search for similar documents using cosine similarity
        
        Args:
            query: Search query
            k: Number of results to return (default from config)
            
        Returns:
            List of similar Document objects
        """
        try:
            if self.vector_store is None:
                print("X No vector store available")
                return []
            
            k = k or Config.TOP_K_RESULTS
            results = self.vector_store.similarity_search(query, k=k)
            print(f"+ Found {len(results)} similar documents")
            return results
        except Exception as e:
            print(f"X Error in similarity search: {e}")
            return []
    
    def similarity_search_with_score(self, query: str, k: int = None) -> List[tuple]:
        """
        Search for similar documents with similarity scores
        
        Args:
            query: Search query
            k: Number of results to return
            
        Returns:
            List of (Document, score) tuples
        """
        try:
            if self.vector_store is None:
                print("X No vector store available")
                return []
            
            k = k or Config.TOP_K_RESULTS
            results = self.vector_store.similarity_search_with_score(query, k=k)
            print(f"+ Found {len(results)} similar documents with scores")
            return results
        except Exception as e:
            print(f"X Error in similarity search: {e}")
            return []
