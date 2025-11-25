"""
Document Loader Module
Handles loading documents from various sources: YouTube, PDF, Wikipedia
"""
from typing import List
from langchain.schema import Document
from langchain_community.document_loaders import (
    YoutubeLoader,
    PyPDFLoader,
    WikipediaLoader
)
import os


class DocumentLoader:
    """Load documents from multiple sources"""
    
    @staticmethod
    def load_from_youtube(video_url: str) -> List[Document]:
        """
        Load transcript from YouTube video
        
        Args:
            video_url: YouTube video URL
            
        Returns:
            List of Document objects
        """
        try:
            loader = YoutubeLoader.from_youtube_url(
                video_url,
                add_video_info=True
            )
            documents = loader.load()
            print(f"+ Loaded YouTube video: {video_url}")
            return documents
        except Exception as e:
            print(f"X Error loading YouTube video: {e}")
            return []
    
    @staticmethod
    def load_from_pdf(pdf_path: str) -> List[Document]:
        """
        Load content from PDF file
        
        Args:
            pdf_path: Path to PDF file
            
        Returns:
            List of Document objects
        """
        try:
            if not os.path.exists(pdf_path):
                raise FileNotFoundError(f"PDF file not found: {pdf_path}")
            
            loader = PyPDFLoader(pdf_path)
            documents = loader.load()
            print(f"+ Loaded PDF: {pdf_path} ({len(documents)} pages)")
            return documents
        except Exception as e:
            print(f"X Error loading PDF: {e}")
            return []
    
    @staticmethod
    def load_from_wikipedia(query: str, max_docs: int = 2) -> List[Document]:
        """
        Load content from Wikipedia
        
        Args:
            query: Search query for Wikipedia
            max_docs: Maximum number of documents to load
            
        Returns:
            List of Document objects
        """
        try:
            loader = WikipediaLoader(query=query, load_max_docs=max_docs)
            documents = loader.load()
            print(f"+ Loaded Wikipedia articles for: {query}")
            return documents
        except Exception as e:
            print(f"X Error loading Wikipedia: {e}")
            return []
    
    @staticmethod
    def load_from_text(text_path: str) -> List[Document]:
        """
        Load content from text file
        
        Args:
            text_path: Path to text file
            
        Returns:
            List of Document objects
        """
        try:
            if not os.path.exists(text_path):
                raise FileNotFoundError(f"Text file not found: {text_path}")
            
            with open(text_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            doc = Document(
                page_content=content,
                metadata={"source": text_path}
            )
            print(f"+ Loaded text file: {text_path}")
            return [doc]
        except Exception as e:
            print(f"X Error loading text file: {e}")
            return []
