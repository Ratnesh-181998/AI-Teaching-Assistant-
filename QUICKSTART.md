# Quick Start Guide - AI Teaching Assistant

## 🚀 Get Started in 5 Minutes

### Step 1: Install Dependencies
```bash
cd AI_Teaching_Assistant
pip install -r requirements.txt
```

### Step 2: Configure API Key
Create a `.env` file:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### Step 3: Run the Application

#### Option A: Web Interface (Recommended)
```bash
python app.py
```
Open browser: `http://localhost:5000`

#### Option B: Command Line
```bash
python main.py
```

#### Option C: Try Examples
```bash
python examples.py
```

---

## 📖 Simple Example

```python
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
ta.ask("What are the applications of AI?")

# Interactive mode
ta.interactive_mode()
```

---

## 🎯 Common Use Cases

### 1. Load YouTube Lecture
```python
sources = {
    'youtube': ['https://www.youtube.com/watch?v=VIDEO_ID']
}
```

### 2. Load PDF Textbook
```python
sources = {
    'pdf': ['textbook.pdf', 'slides.pdf']
}
```

### 3. Load Multiple Sources
```python
sources = {
    'youtube': ['VIDEO_URL'],
    'pdf': ['lecture.pdf'],
    'wikipedia': ['Topic Name']
}
```

---

## 🔧 Troubleshooting

**Problem**: "OpenAI API key not found"
- **Solution**: Create `.env` file with your API key

**Problem**: "No knowledge base loaded"
- **Solution**: Run the app once to create vector store

**Problem**: "Module not found"
- **Solution**: `pip install -r requirements.txt`

---

## 📊 What Happens Behind the Scenes?

1. **Documents loaded** from your sources
2. **Text split** into chunks (1000 chars with 200 overlap)
3. **Embeddings created** using OpenAI (1536-dimensional vectors)
4. **Stored in FAISS** for fast similarity search
5. **Questions answered** using RAG:
   - Query → Embedding
   - Similarity search → Retrieve context
   - Context + Query → ChatGPT → Answer

---

## 💡 Tips

- **First run takes time**: Creating embeddings for large documents
- **Costs money**: OpenAI API charges for embeddings + ChatGPT
- **Save vector store**: Reuse without recreating embeddings
- **Quality matters**: Better source materials = better answers

---

## 🌐 Web Interface

The web UI provides:
- ✅ Beautiful gradient design
- ✅ Real-time Q&A
- ✅ Chat history
- ✅ Source citations
- ✅ Mobile responsive

---

## 📞 Need Help?

1. Check `README.md` for detailed documentation
2. Run `examples.py` for demonstrations
3. Review code comments in each module

---

**Ready to build your AI Teaching Assistant? Let's go! 🚀**
