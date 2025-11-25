"""
Demo script for AI Teaching Assistant
"""
import os
import sys

print("=" * 70)
print("AI TEACHING ASSISTANT - DEMO")
print("=" * 70)
print()

print("PROJECT STRUCTURE:")
print("-" * 70)
print("+ main.py              - Main application")
print("+ app.py               - Flask web server")
print("+ document_loader.py   - Load YouTube/PDF/Wikipedia")
print("+ text_splitter.py     - Intelligent text chunking")
print("+ vector_store.py      - FAISS vector database")
print("+ rag_chain.py         - RAG implementation")
print("+ examples.py          - Usage examples")
print("+ templates/index.html - Beautiful web UI")
print()

print("CAPABILITIES:")
print("-" * 70)
print("+ Load from YouTube videos (transcripts)")
print("+ Load from PDF documents")
print("+ Load from Wikipedia articles")
print("+ Load from text files")
print("+ Intelligent text chunking (1000 chars, 200 overlap)")
print("+ OpenAI embeddings (1536-dimensional vectors)")
print("+ FAISS vector store (fast similarity search)")
print("+ RAG pipeline (context-aware Q&A)")
print("+ Beautiful web interface")
print("+ REST API endpoints")
print("+ Interactive CLI mode")
print()

print("HOW TO RUN:")
print("-" * 70)
print()
print("STEP 1: Configure OpenAI API Key")
print("  - Get your API key from: https://platform.openai.com/api-keys")
print("  - Edit the .env file in this directory")
print("  - Replace 'your_openai_api_key_here' with your actual key")
print()
print("STEP 2: Run the application")
print()
print("  Option A: Web Interface (Recommended)")
print("    python app.py")
print("    Then open: http://localhost:5000")
print()
print("  Option B: Command Line")
print("    python main.py")
print()
print("  Option C: Examples")
print("    python examples.py")
print()

print("EXAMPLE USAGE:")
print("-" * 70)
print("""
from main import AITeachingAssistant

# Initialize
ta = AITeachingAssistant()

# Load Wikipedia article
sources = {
    'wikipedia': ['Artificial Intelligence']
}

# Process
docs = ta.load_course_materials(sources)
ta.process_documents(docs)
ta.save_knowledge_base()

# Ask questions
ta.ask("What is AI?")
ta.ask("What are applications of AI?")

# Interactive mode
ta.interactive_mode()
""")

print("=" * 70)
print()
print("DOCUMENTATION:")
print("   - README.md (complete documentation)")
print("   - QUICKSTART.md (5-minute setup)")
print("   - INDEX.md (start here guide)")
print("   - BUILD_SUMMARY.md (project overview)")
print()
print("=" * 70)
print()
print("NEXT STEPS:")
print("1. Add your OpenAI API key to .env file")
print("2. Run: python app.py")
print("3. Open: http://localhost:5000")
print()
print("=" * 70)
