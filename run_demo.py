"""
Complete Demo - AI Teaching Assistant
This script demonstrates the full RAG pipeline
"""
import sys
import os

print("=" * 70)
print("AI TEACHING ASSISTANT - COMPLETE DEMONSTRATION")
print("=" * 70)
print()

# Import the teaching assistant
from main import AITeachingAssistant
from config import Config

# Check API key
if not Config.OPENAI_API_KEY or Config.OPENAI_API_KEY == 'your_openai_api_key_here':
    print("ERROR: OpenAI API key not configured!")
    print("Please edit .env file and add your API key.")
    sys.exit(1)

print("Step 1: Initializing AI Teaching Assistant...")
print("-" * 70)
ta = AITeachingAssistant()
print()

# Check if knowledge base exists
if os.path.exists(Config.VECTOR_STORE_PATH):
    print("Step 2: Loading existing knowledge base...")
    print("-" * 70)
    ta.load_knowledge_base()
    print()
else:
    print("Step 2: Creating knowledge base from Wikipedia...")
    print("-" * 70)
    print("Loading article: 'Retrieval-Augmented Generation'")
    print()
    
    sources = {
        'wikipedia': ['Retrieval-Augmented Generation', 'FAISS']
    }
    
    # Load documents
    documents = ta.load_course_materials(sources)
    
    if not documents:
        print("ERROR: Failed to load documents!")
        print("Check your internet connection and try again.")
        sys.exit(1)
    
    print()
    print("Step 3: Processing documents (chunking + embedding)...")
    print("-" * 70)
    ta.process_documents(documents)
    
    print()
    print("Step 4: Saving knowledge base...")
    print("-" * 70)
    ta.save_knowledge_base()
    print()

print("Step 5: Initializing RAG chain...")
print("-" * 70)
ta.initialize_rag()
print()

print("=" * 70)
print("KNOWLEDGE BASE READY!")
print("=" * 70)
print()

# Ask sample questions
print("DEMONSTRATION: Asking Questions")
print("=" * 70)
print()

questions = [
    "What is RAG (Retrieval-Augmented Generation)?",
    "How does FAISS work?",
    "What are the benefits of using RAG?"
]

for i, question in enumerate(questions, 1):
    print(f"\nQuestion {i}: {question}")
    print("-" * 70)
    
    response = ta.ask(question, verbose=False)
    
    print(f"\nAnswer:")
    print(response['answer'])
    
    if response.get('sources'):
        print(f"\nSources: {len(response['sources'])} documents retrieved")
    
    print()
    print("=" * 70)

print()
print("DEMONSTRATION COMPLETE!")
print()
print("Next steps:")
print("1. Run 'python app.py' to start the web interface")
print("2. Run 'python main.py' for interactive Q&A mode")
print("3. Check README.md for more information")
print()
print("=" * 70)
