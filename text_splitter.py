"""
Text Splitter Module
Handles splitting documents into smaller chunks with overlap
"""
from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from config import Config


class TextChunker:
    """Split documents into smaller chunks for efficient retrieval"""
    
    def __init__(self, chunk_size: int = None, chunk_overlap: int = None):
        """
        Initialize text splitter
        
        Args:
            chunk_size: Size of each chunk (default from config)
            chunk_overlap: Overlap between chunks (default from config)
        """
        self.chunk_size = chunk_size or Config.CHUNK_SIZE
        self.chunk_overlap = chunk_overlap or Config.CHUNK_OVERLAP
        
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
    
    def split_documents(self, documents: List[Document]) -> List[Document]:
        """
        Split documents into chunks
        
        Args:
            documents: List of Document objects
            
        Returns:
            List of chunked Document objects
        """
        try:
            chunks = self.text_splitter.split_documents(documents)
            print(f"+ Split {len(documents)} documents into {len(chunks)} chunks")
            print(f"  Chunk size: {self.chunk_size}, Overlap: {self.chunk_overlap}")
            return chunks
        except Exception as e:
            print(f"X Error splitting documents: {e}")
            return []
    
    def split_text(self, text: str) -> List[str]:
        """
        Split raw text into chunks
        
        Args:
            text: Raw text string
            
        Returns:
            List of text chunks
        """
        try:
            chunks = self.text_splitter.split_text(text)
            print(f"+ Split text into {len(chunks)} chunks")
            return chunks
        except Exception as e:
            print(f"X Error splitting text: {e}")
            return []
