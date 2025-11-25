# AI Teaching Assistant - Ollama Setup Guide

## Using Local LLMs with Ollama (FREE!)

This guide shows how to run the AI Teaching Assistant completely FREE using Ollama.

---

## Step 1: Install Ollama

### Windows
1. Download from: https://ollama.ai/download
2. Run the installer
3. Ollama will start automatically

### Verify Installation
```bash
ollama --version
```

---

## Step 2: Download Models

### Download LLM (for responses)
```bash
ollama pull llama2
# or for better quality:
ollama pull mistral
```

### Download Embedding Model (for vector search)
```bash
ollama pull nomic-embed-text
```

---

## Step 3: Install Required Packages

```bash
pip install langchain-community sentence-transformers chromadb
```

---

## Step 4: Use the Ollama Version

Run the Ollama-compatible version:
```bash
python main_ollama.py
```

---

## Available Models

### LLMs (for Q&A):
- `llama2` (7B) - Good balance, ~4GB
- `mistral` (7B) - Better quality, ~4GB  
- `llama2:13b` - Higher quality, ~8GB
- `codellama` - For code questions

### Embeddings:
- `nomic-embed-text` - Best for RAG, ~274MB
- `all-minilm` - Faster, smaller

---

## Advantages of Ollama

✅ **Completely FREE** - No API costs
✅ **Privacy** - Data stays on your machine
✅ **Offline** - Works without internet
✅ **No rate limits** - Use as much as you want
✅ **Fast** - Local processing

---

## System Requirements

- **RAM**: 8GB minimum (16GB recommended)
- **Storage**: 5-10GB for models
- **GPU**: Optional (CPU works fine)

---

## Quick Start

```bash
# 1. Install Ollama
# Download from https://ollama.ai

# 2. Pull models
ollama pull mistral
ollama pull nomic-embed-text

# 3. Run the project
python main_ollama.py
```

---

## Troubleshooting

### "Ollama not found"
- Restart your terminal
- Check if Ollama service is running

### "Model not found"
- Run `ollama pull <model-name>` first

### Slow responses
- Use smaller models (llama2 instead of llama2:13b)
- Close other applications

---

**Now you can run the AI Teaching Assistant completely FREE!** 🎉
