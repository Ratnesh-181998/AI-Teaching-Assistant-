"""
Installation verification script for AI Teaching Assistant
"""
import sys


def test_imports():
    """Test if all required packages are installed"""
    print("Testing imports...")
    print("-" * 60)
    
    required_packages = [
        ('langchain', 'LangChain'),
        ('langchain_community', 'LangChain Community'),
        ('langchain_openai', 'LangChain OpenAI'),
        ('openai', 'OpenAI'),
        ('faiss', 'FAISS'),
        ('flask', 'Flask'),
        ('flask_cors', 'Flask-CORS'),
        ('dotenv', 'Python-dotenv'),
        ('PyPDF2', 'PyPDF2'),
    ]
    
    failed = []
    
    for package, name in required_packages:
        try:
            __import__(package)
            print(f"+ {name}")
        except ImportError:
            print(f"X {name} - NOT INSTALLED")
            failed.append(name)
    
    print("-" * 60)
    
    if failed:
        print(f"\n❌ Missing packages: {', '.join(failed)}")
        print("\nInstall with: pip install -r requirements.txt")
        return False
    else:
        print("\n✅ All packages installed successfully!")
        return True


def test_config():
    """Test configuration"""
    print("\nTesting configuration...")
    print("-" * 60)
    
    try:
        from config import Config
        
        if Config.OPENAI_API_KEY and Config.OPENAI_API_KEY != 'your_openai_api_key_here':
            print("+ OpenAI API key configured")
        else:
            print("⚠ OpenAI API key not configured")
            print("  Create .env file with: OPENAI_API_KEY=your_key")
        
        print(f"+ Chunk size: {Config.CHUNK_SIZE}")
        print(f"+ Chunk overlap: {Config.CHUNK_OVERLAP}")
        print(f"+ LLM model: {Config.LLM_MODEL}")
        print(f"+ Embedding model: {Config.EMBEDDING_MODEL}")
        
        print("-" * 60)
        print("\n✅ Configuration loaded successfully!")
        return True
        
    except Exception as e:
        print(f"X Configuration error: {e}")
        print("-" * 60)
        return False


def test_modules():
    """Test if all custom modules can be imported"""
    print("\nTesting custom modules...")
    print("-" * 60)
    
    modules = [
        'config',
        'document_loader',
        'text_splitter',
        'vector_store',
        'rag_chain',
        'main'
    ]
    
    failed = []
    
    for module in modules:
        try:
            __import__(module)
            print(f"+ {module}.py")
        except Exception as e:
            print(f"X {module}.py - ERROR: {e}")
            failed.append(module)
    
    print("-" * 60)
    
    if failed:
        print(f"\n❌ Failed modules: {', '.join(failed)}")
        return False
    else:
        print("\n✅ All modules loaded successfully!")
        return True


def test_simple_workflow():
    """Test a simple workflow"""
    print("\nTesting simple workflow...")
    print("-" * 60)
    
    try:
        from document_loader import DocumentLoader
        from text_splitter import TextChunker
        
        # Test text splitting
        chunker = TextChunker(chunk_size=100, chunk_overlap=20)
        text = "This is a test. " * 50
        chunks = chunker.split_text(text)
        
        print(f"+ Text splitting works ({len(chunks)} chunks created)")
        
        # Test document loader
        loader = DocumentLoader()
        print("+ Document loader initialized")
        
        print("-" * 60)
        print("\n✅ Basic workflow test passed!")
        return True
        
    except Exception as e:
        print(f"X Workflow test failed: {e}")
        print("-" * 60)
        return False


def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("AI Teaching Assistant - Installation Test")
    print("=" * 60 + "\n")
    
    results = []
    
    # Run tests
    results.append(("Package Installation", test_imports()))
    results.append(("Configuration", test_config()))
    results.append(("Custom Modules", test_modules()))
    results.append(("Simple Workflow", test_simple_workflow()))
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print("=" * 60)
    
    if all(result[1] for result in results):
        print("\n🎉 All tests passed! Your installation is ready.")
        print("\nNext steps:")
        print("1. Configure your OpenAI API key in .env")
        print("2. Run: python main.py")
        print("   OR: python app.py (for web interface)")
        print("   OR: python examples.py (for demonstrations)")
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above.")
        print("\nCommon fixes:")
        print("- Install packages: pip install -r requirements.txt")
        print("- Create .env file with your OpenAI API key")
    
    print()


if __name__ == "__main__":
    main()
