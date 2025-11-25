"""
Example script demonstrating how to use the AI Teaching Assistant
"""
from main import AITeachingAssistant
from config import Config
import os


def example_youtube_demo():
    """Example: Load from YouTube and ask questions"""
    print("\n" + "="*60)
    print("EXAMPLE 1: YouTube Video Demo")
    print("="*60)
    
    ta = AITeachingAssistant()
    
    # Example YouTube video about Machine Learning
    sources = {
        'youtube': [
            'https://www.youtube.com/watch?v=ukzFI9rgwfU',  # ML Crash Course
        ]
    }
    
    # Load and process
    documents = ta.load_course_materials(sources)
    if documents:
        ta.process_documents(documents)
        ta.save_knowledge_base('./demo_vector_store')
        
        # Ask questions
        ta.ask("What is machine learning?")
        ta.ask("What are the types of machine learning?")


def example_pdf_demo():
    """Example: Load from PDF and ask questions"""
    print("\n" + "="*60)
    print("EXAMPLE 2: PDF Demo")
    print("="*60)
    
    ta = AITeachingAssistant()
    
    # Add your PDF path here
    sources = {
        'pdf': [
            '../System_Design_on_AI_Teaching_Assistant.pdf'
        ]
    }
    
    documents = ta.load_course_materials(sources)
    if documents:
        ta.process_documents(documents)
        ta.save_knowledge_base('./pdf_vector_store')
        
        ta.ask("What is RAG?")
        ta.ask("How does the teaching assistant work?")


def example_wikipedia_demo():
    """Example: Load from Wikipedia and ask questions"""
    print("\n" + "="*60)
    print("EXAMPLE 3: Wikipedia Demo")
    print("="*60)
    
    ta = AITeachingAssistant()
    
    sources = {
        'wikipedia': [
            'Artificial Intelligence',
            'Machine Learning'
        ]
    }
    
    documents = ta.load_course_materials(sources)
    if documents:
        ta.process_documents(documents)
        ta.save_knowledge_base('./wiki_vector_store')
        
        ta.ask("What is artificial intelligence?")
        ta.ask("What is the difference between AI and ML?")


def example_mixed_sources():
    """Example: Load from multiple sources"""
    print("\n" + "="*60)
    print("EXAMPLE 4: Mixed Sources Demo")
    print("="*60)
    
    ta = AITeachingAssistant()
    
    sources = {
        'youtube': [
            # Add YouTube URLs
        ],
        'pdf': [
            # Add PDF paths
        ],
        'wikipedia': [
            'Natural Language Processing',
            'BERT (language model)'
        ],
        'text': [
            # Add text file paths
        ]
    }
    
    documents = ta.load_course_materials(sources)
    if documents:
        ta.process_documents(documents)
        ta.save_knowledge_base()
        
        # Interactive mode
        ta.interactive_mode()


def example_load_existing():
    """Example: Load existing vector store"""
    print("\n" + "="*60)
    print("EXAMPLE 5: Load Existing Knowledge Base")
    print("="*60)
    
    ta = AITeachingAssistant()
    
    # Load existing vector store
    ta.load_knowledge_base()
    
    if ta.vector_store_manager.vector_store:
        # Ask questions
        ta.ask("Explain the concept covered in the materials")
        
        # Or start interactive mode
        # ta.interactive_mode()
    else:
        print("No existing knowledge base found!")


def example_custom_questions():
    """Example: Custom question-answering workflow"""
    print("\n" + "="*60)
    print("EXAMPLE 6: Custom Q&A Workflow")
    print("="*60)
    
    ta = AITeachingAssistant()
    
    # Load existing or create new
    if os.path.exists(Config.VECTOR_STORE_PATH):
        ta.load_knowledge_base()
    else:
        sources = {
            'wikipedia': ['Python (programming language)']
        }
        documents = ta.load_course_materials(sources)
        ta.process_documents(documents)
        ta.save_knowledge_base()
    
    # List of questions
    questions = [
        "What is Python?",
        "What are the main features of Python?",
        "Who created Python?",
        "What is Python used for?"
    ]
    
    # Ask all questions
    for q in questions:
        response = ta.ask(q, verbose=True)
        print("\n" + "-"*60 + "\n")


if __name__ == "__main__":
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║        AI Teaching Assistant - Example Demonstrations      ║
    ╚════════════════════════════════════════════════════════════╝
    
    Available examples:
    1. YouTube Video Demo
    2. PDF Demo
    3. Wikipedia Demo
    4. Mixed Sources Demo
    5. Load Existing Knowledge Base
    6. Custom Q&A Workflow
    
    """)
    
    choice = input("Select example (1-6) or 'q' to quit: ").strip()
    
    examples = {
        '1': example_youtube_demo,
        '2': example_pdf_demo,
        '3': example_wikipedia_demo,
        '4': example_mixed_sources,
        '5': example_load_existing,
        '6': example_custom_questions
    }
    
    if choice in examples:
        examples[choice]()
    elif choice.lower() == 'q':
        print("Goodbye!")
    else:
        print("Invalid choice!")
