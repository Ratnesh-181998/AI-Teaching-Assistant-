"""
AI Teaching Assistant - Ollama Version (FREE!)
Complete RAG pipeline using local LLMs
"""
from document_loader import DocumentLoader
from text_splitter import TextChunker
from vector_store_ollama import VectorStoreManagerOllama
from rag_chain_ollama import RAGChainOllama
from config_ollama import ConfigOllama
import os


class AITeachingAssistantOllama:
    """Main AI Teaching Assistant class using Ollama"""
    
    def __init__(self):
        """Initialize the teaching assistant"""
        self.loader = DocumentLoader()
        self.chunker = TextChunker()
        self.vector_store_manager = VectorStoreManagerOllama()
        self.rag_chain = None
        
        print("=" * 60)
        print("AI Teaching Assistant Initialized (Ollama - FREE!)")
        print("=" * 60)
        print(f"LLM Model: {ConfigOllama.LLM_MODEL}")
        print(f"Embedding Model: {ConfigOllama.EMBEDDING_MODEL}")
        print("=" * 60)
    
    def load_course_materials(self, sources: dict):
        """Load course materials from multiple sources"""
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
        """Process documents: split into chunks and create embeddings"""
        print("\nSplitting Documents into Chunks...")
        print("-" * 60)
        chunks = self.chunker.split_documents(documents)
        
        print("\nCreating Vector Store with Ollama Embeddings...")
        print("-" * 60)
        print("(This may take a few minutes on first run)")
        self.vector_store_manager.create_vector_store(chunks)
        
        return chunks
    
    def save_knowledge_base(self, path: str = None):
        """Save the vector store to disk"""
        print("\nSaving Knowledge Base...")
        print("-" * 60)
        self.vector_store_manager.save_vector_store(path)
    
    def load_knowledge_base(self, path: str = None):
        """Load existing vector store from disk"""
        print("\nLoading Knowledge Base...")
        print("-" * 60)
        self.vector_store_manager.load_vector_store(path)
    
    def initialize_rag(self):
        """Initialize RAG chain for question answering"""
        print("\nInitializing RAG Chain with Ollama...")
        print("-" * 60)
        self.rag_chain = RAGChainOllama(self.vector_store_manager)
        print("+ RAG chain ready for questions")
    
    def ask(self, question: str, verbose: bool = True):
        """Ask a question to the teaching assistant"""
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
        print("Interactive Teaching Assistant Mode (Ollama)")
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
    
    print("\n" + "=" * 70)
    print("AI TEACHING ASSISTANT - OLLAMA VERSION (FREE!)")
    print("=" * 70)
    print("\nThis version uses Ollama - completely FREE, no API costs!")
    print("\nMake sure Ollama is installed and models are downloaded:")
    print("  ollama pull mistral")
    print("  ollama pull nomic-embed-text")
    print("=" * 70 + "\n")
    
    # Initialize Teaching Assistant
    ta = AITeachingAssistantOllama()
    
    # Check if vector store already exists
    if os.path.exists(ConfigOllama.VECTOR_STORE_PATH):
        print("\nFound existing knowledge base!")
        choice = input("Load existing knowledge base? (y/n): ").strip().lower()
        
        if choice == 'y':
            ta.load_knowledge_base()
        else:
            # Example: Load course materials
            print("\nLet's create a new knowledge base!")
            print("Loading Wikipedia article about 'Artificial Intelligence'...")
            
            sources = {
                'wikipedia': ['Artificial Intelligence']
            }
            
            documents = ta.load_course_materials(sources)
            if documents:
                ta.process_documents(documents)
                ta.save_knowledge_base()
    else:
        # Load example materials
        print("\nNo knowledge base found. Let's create one!")
        print("Loading Wikipedia article about 'Artificial Intelligence'...")
        
        sources = {
            'wikipedia': ['Artificial Intelligence']
        }
        
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
