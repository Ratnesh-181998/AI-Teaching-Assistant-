
import sys
import os
from main_ollama import AITeachingAssistantOllama
from config_ollama import ConfigOllama

print("Testing Ollama RAG Pipeline...")

# Initialize
try:
    ta = AITeachingAssistantOllama()
except Exception as e:
    print(f"Error initializing: {e}")
    sys.exit(1)

# Check Vector Store
if os.path.exists(ConfigOllama.VECTOR_STORE_PATH):
    print("Loading knowledge base...")
    ta.load_knowledge_base()
else:
    print("No knowledge base found. Please run main_ollama.py first to create it.")
    sys.exit(1)

# Initialize RAG
print("Initializing RAG chain...")
ta.initialize_rag()

# Ask Question
question = "What is Artificial Intelligence?"
print(f"\nAsking: {question}")
try:
    response = ta.ask(question, verbose=True)
    print("\nResponse received!")
    print(f"Answer length: {len(response['answer'])}")
except Exception as e:
    print(f"\nError asking question: {e}")
