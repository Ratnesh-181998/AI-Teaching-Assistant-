"""
AI Teaching Assistant - Main Application
Complete RAG pipeline implementation
"""
from document_loader import DocumentLoader
from text_splitter import TextChunker
from vector_store import VectorStoreManager
from rag_chain import RAGChain
from config import Config
import os


class AITeachingAssistant:
    """Main AI Teaching Assistant class"""
    
    def __init__(self):
        """Initialize the teaching assistant"""
        self.loader = DocumentLoader()
        self.chunker = TextChunker()
        self.vector_store_manager = VectorStoreManager()
        self.rag_chain = None
        
        print("=" * 60)
        print("AI Teaching Assistant Initialized")
        print("=" * 60)
    
    def load_course_materials(self, sources: dict):
        """
        Load course materials from multiple sources
        
        Args:
            sources: Dictionary with source types and paths/URLs
                    {
                        'youtube': ['url1', 'url2'],
                        'pdf': ['path1', 'path2'],
                        'wikipedia': ['query1', 'query2'],
                        'text': ['path1', 'path2']
                    }
        """
        all_documents = []
        
        print("\nLoading Course Materials...")
        print("-" * 60)
        
        # Load YouTube videos
        if 'youtube' in sources:
            for url in sources['youtube']:
                docs = self.loader.load_from_youtube(url)
                all_documents.extend(docs)
        
        # Load PDFs
        if 'pdf' in sources:
            for path in sources['pdf']:
                docs = self.loader.load_from_pdf(path)
                all_documents.extend(docs)
        
        # Load Wikipedia articles
        if 'wikipedia' in sources:
            for query in sources['wikipedia']:
                docs = self.loader.load_from_wikipedia(query)
                all_documents.extend(docs)
        
        # Load text files
        if 'text' in sources:
            for path in sources['text']:
                docs = self.loader.load_from_text(path)
                all_documents.extend(docs)
        
        print(f"\nTotal documents loaded: {len(all_documents)}")
        return all_documents
    
    def process_documents(self, documents):
        """
        Process documents: split into chunks and create embeddings
        
        Args:
            documents: List of Document objects
        """
        print("\nSplitting Documents into Chunks...")
        print("-" * 60)
        chunks = self.chunker.split_documents(documents)
        
        print("\nCreating Vector Store (Embeddings)...")
        print("-" * 60)
        self.vector_store_manager.create_vector_store(chunks)
        
        return chunks
    
    def save_knowledge_base(self, path: str = None):
        """
        Save the vector store to disk
        
        Args:
            path: Path to save (default from config)
        """
        print("\nSaving Knowledge Base...")
        print("-" * 60)
        self.vector_store_manager.save_vector_store(path)
    
    def load_knowledge_base(self, path: str = None):
        """
        Load existing vector store from disk
        
        Args:
            path: Path to load from (default from config)
        """
        print("\nLoading Knowledge Base...")
        print("-" * 60)
        self.vector_store_manager.load_vector_store(path)
    
    def initialize_rag(self):
        """Initialize RAG chain for question answering"""
        print("\nInitializing RAG Chain...")
        print("-" * 60)
        self.rag_chain = RAGChain(self.vector_store_manager)
        print("+ RAG chain ready for questions")
    
    def ask(self, question: str, verbose: bool = True):
        """
        Ask a question to the teaching assistant
        
        Args:
            question: Student's question
            verbose: Whether to print detailed response
            
        Returns:
            Response dictionary
        """
        if self.rag_chain is None:
            self.initialize_rag()
        
        if verbose:
            print("\n" + "=" * 60)
            print(f"Question: {question}")
            print("=" * 60)
        
        response = self.rag_chain.ask_question(question)
        
        if verbose:
            print(f"\nAnswer:\n{response['answer']}")
            
            if response['sources']:
                print(f"\nSources ({len(response['sources'])}):")
                for i, source in enumerate(response['sources'], 1):
                    print(f"\n  [{i}] {source['content']}")
                    if 'source' in source['metadata']:
                        print(f"      Source: {source['metadata']['source']}")
        
        return response
    
    def interactive_mode(self):
        """Start interactive Q&A session"""
        print("\n" + "=" * 60)
        print("Interactive Teaching Assistant Mode")
        print("=" * 60)
        print("Type your questions below. Type 'exit' or 'quit' to stop.\n")
        
        if self.rag_chain is None:
            self.initialize_rag()
        
        while True:
            try:
                question = input("Student: ").strip()
                
                if question.lower() in ['exit', 'quit', 'q']:
                    print("\nGoodbye! Happy learning!")
                    break
                
                if not question:
                    continue
                
                self.ask(question, verbose=True)
                print("\n" + "-" * 60)
                
            except KeyboardInterrupt:
                print("\n\nGoodbye! Happy learning!")
                break
            except Exception as e:
                print(f"\nError: {e}")


def main():
    """Main function - Example usage"""
    
    # Initialize Teaching Assistant
    ta = AITeachingAssistant()
    
    # Example: Load course materials
    sources = {
        'youtube': [
            # Add your YouTube lecture URLs here
            # 'https://www.youtube.com/watch?v=...'
        ],
        'pdf': [
            # Add paths to your PDF files here
            # '../lecture_slides.pdf'
        ],
        'wikipedia': [
            # Add Wikipedia topics here
            # 'Machine Learning',
            # 'Natural Language Processing'
        ],
        'text': [
            # Add paths to text files here
        ]
    }
    
    # Check if vector store already exists
    if os.path.exists(Config.VECTOR_STORE_PATH):
        print("\nFound existing knowledge base!")
        choice = input("Load existing knowledge base? (y/n): ").strip().lower()
        
        if choice == 'y':
            ta.load_knowledge_base()
        else:
            # Load and process new materials
            documents = ta.load_course_materials(sources)
            if documents:
                ta.process_documents(documents)
                ta.save_knowledge_base()
    else:
        # Load and process materials
        documents = ta.load_course_materials(sources)
        if documents:
            ta.process_documents(documents)
            ta.save_knowledge_base()
    
    # Start interactive mode
    if ta.vector_store_manager.vector_store is not None:
        ta.interactive_mode()
    else:
        print("\nNo knowledge base available. Please add course materials first.")


if __name__ == "__main__":
    main()
