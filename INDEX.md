# 🎓 AI Teaching Assistant - Start Here!

Welcome to your **AI Teaching Assistant** built with RAG architecture!

---

## 🚀 Quick Start (3 Steps)

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Configure API Key
Create a `.env` file:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 3️⃣ Run the Application
```bash
python app.py
```
Then open: **http://localhost:5000**

---

## 📚 Documentation Guide

### 🆕 New User?
1. **START HERE** → `QUICKSTART.md` (5-minute setup)
2. **Run Examples** → `python examples.py`
3. **Verify Setup** → `python verify_setup.py`

### 📖 Want Full Details?
- **Complete Docs** → `README.md`
- **Project Overview** → `PROJECT_SUMMARY.md`
- **Build Summary** → `BUILD_SUMMARY.md`

### 💻 Ready to Code?
- **Main App** → `main.py`
- **Web Server** → `app.py`
- **Examples** → `examples.py`

---

## 🎯 What Can You Do?

### Option 1: Web Interface (Easiest)
```bash
python app.py
```
- Beautiful UI at `http://localhost:5000`
- Real-time Q&A
- Chat history
- Source citations

### Option 2: Command Line
```bash
python main.py
```
- Interactive terminal mode
- Type questions, get answers
- Full control

### Option 3: Run Examples
```bash
python examples.py
```
- 6 different scenarios
- YouTube, PDF, Wikipedia demos
- Learn by example

### Option 4: Use as Library
```python
from main import AITeachingAssistant

ta = AITeachingAssistant()
sources = {'wikipedia': ['Python (programming language)']}
docs = ta.load_course_materials(sources)
ta.process_documents(docs)
ta.ask("What is Python?")
```

---

## 📁 Project Files

### 🎯 Core Application
- `main.py` - Main application
- `app.py` - Flask web server
- `config.py` - Configuration
- `document_loader.py` - Load documents
- `text_splitter.py` - Chunk text
- `vector_store.py` - FAISS vector DB
- `rag_chain.py` - RAG implementation

### 📚 Documentation
- `README.md` - Complete documentation
- `QUICKSTART.md` - Quick start guide
- `PROJECT_SUMMARY.md` - Project overview
- `BUILD_SUMMARY.md` - Build details
- `INDEX.md` - This file

### 🧪 Examples & Tools
- `examples.py` - Usage examples
- `verify_setup.py` - Installation test

### 🌐 Web Interface
- `templates/index.html` - Web UI

### ⚙️ Configuration
- `requirements.txt` - Dependencies
- `.env.example` - Config template
- `.gitignore` - Git ignore

---

## 🏗️ Architecture

```
📥 INPUT SOURCES
   ├── YouTube Videos
   ├── PDF Documents
   ├── Wikipedia Articles
   └── Text Files
          ↓
📄 DOCUMENT LOADER
          ↓
✂️ TEXT SPLITTER (1000 chars, 200 overlap)
          ↓
🧠 EMBEDDING GENERATOR (OpenAI)
          ↓
💾 FAISS VECTOR STORE
          ↓
🔍 SIMILARITY SEARCH
          ↓
🤖 CHATGPT RESPONSE
          ↓
💬 ANSWER TO USER
```

---

## ✅ Features

- ✅ Multi-source document loading
- ✅ Intelligent text chunking
- ✅ Vector embeddings (OpenAI)
- ✅ Fast similarity search (FAISS)
- ✅ RAG pipeline
- ✅ Beautiful web UI
- ✅ REST API
- ✅ Interactive CLI
- ✅ Persistent storage
- ✅ Source citations

---

## 🎓 How It Works

1. **Load** course materials (YouTube/PDF/Wikipedia)
2. **Split** into chunks with overlap
3. **Embed** text into vectors (1536-D)
4. **Store** in FAISS for fast search
5. **Query** → Find similar chunks
6. **Retrieve** relevant context
7. **Generate** answer with ChatGPT
8. **Return** answer + sources

---

## 🛠️ Troubleshooting

### "Module not found"
```bash
pip install -r requirements.txt
```

### "OpenAI API key not found"
Create `.env` file with your API key

### "No knowledge base loaded"
Run the app once to create vector store

### Need help?
```bash
python verify_setup.py
```

---

## 📊 Quick Stats

- **Files**: 16
- **Python Modules**: 7
- **Lines of Code**: 1,500+
- **Documentation**: 30+ KB
- **Examples**: 6 scenarios
- **Interfaces**: 3 (Web, CLI, API)

---

## 🎯 Use Cases

- 📚 Educational platforms
- 🏢 Corporate training
- 📖 Documentation Q&A
- 🔬 Research assistants
- 💼 Customer support

---

## 🚀 Next Steps

1. ✅ Read `QUICKSTART.md`
2. ✅ Run `python verify_setup.py`
3. ✅ Try `python examples.py`
4. ✅ Start `python app.py`
5. ✅ Build your knowledge base!

---

## 💡 Tips

- **First run**: Takes time to create embeddings
- **Save vector store**: Reuse without recreating
- **Better sources**: Better answers
- **API costs**: OpenAI charges apply

---

## 📞 Support

- Check documentation files
- Run verification script
- Review code comments
- Try examples

---

## 🎉 You're Ready!

Your AI Teaching Assistant is ready to use. Start with:

```bash
python app.py
```

**Happy Teaching! 🎓✨**

---

**Built with ❤️ using LangChain, FAISS, and OpenAI**
