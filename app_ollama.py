"""
Flask Web Server for AI Teaching Assistant (Ollama Version)
Provides REST API for the teaching assistant using local LLMs
"""
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from main_ollama import AITeachingAssistantOllama
from config_ollama import ConfigOllama
import os

app = Flask(__name__)
CORS(app)

# Initialize Teaching Assistant (Ollama)
ta = AITeachingAssistantOllama()

# Try to load existing knowledge base
if os.path.exists(ConfigOllama.VECTOR_STORE_PATH):
    ta.load_knowledge_base()
    ta.initialize_rag()


@app.route('/')
def home():
    """Home page"""
    return render_template('index.html')


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'knowledge_base_loaded': ta.vector_store_manager.vector_store is not None,
        'backend': 'ollama'
    })


@app.route('/api/ask', methods=['POST'])
def ask_question():
    """
    Ask a question to the teaching assistant
    """
    try:
        data = request.get_json()
        
        if not data or 'question' not in data:
            return jsonify({
                'error': 'Missing question in request body'
            }), 400
        
        question = data['question']
        
        print(f"Received question: {question}")
        
        if not ta.vector_store_manager.vector_store:
            return jsonify({
                'error': 'Knowledge base not loaded. Please upload course materials first.'
            }), 503
        
        print("Running RAG pipeline...")
        response = ta.ask(question, verbose=True)
        print("Response generated successfully")
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


@app.route('/api/upload', methods=['POST'])
def upload_materials():
    """
    Upload course materials
    """
    try:
        data = request.get_json()
        
        if not data or 'sources' not in data:
            return jsonify({
                'error': 'Missing sources in request body'
            }), 400
        
        sources = data['sources']
        
        # Load materials
        documents = ta.load_course_materials(sources)
        
        if not documents:
            return jsonify({
                'error': 'No documents loaded'
            }), 400
        
        # Process documents
        chunks = ta.process_documents(documents)
        
        # Save knowledge base
        ta.save_knowledge_base()
        
        # Initialize RAG
        ta.initialize_rag()
        
        return jsonify({
            'message': 'Course materials uploaded successfully',
            'documents_loaded': len(documents),
            'chunks_created': len(chunks)
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


@app.route('/api/search', methods=['POST'])
def similarity_search():
    """
    Perform similarity search
    """
    try:
        data = request.get_json()
        
        if not data or 'query' not in data:
            return jsonify({
                'error': 'Missing query in request body'
            }), 400
        
        query = data['query']
        k = data.get('k', ConfigOllama.TOP_K_RESULTS)
        
        if not ta.vector_store_manager.vector_store:
            return jsonify({
                'error': 'Knowledge base not loaded'
            }), 503
        
        results = ta.vector_store_manager.similarity_search_with_score(query, k)
        
        response = [
            {
                'content': doc.page_content,
                'metadata': doc.metadata,
                'score': float(score)
            }
            for doc, score in results
        ]
        
        return jsonify({
            'query': query,
            'results': response
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("Starting AI Teaching Assistant Server (Ollama)")
    print("=" * 60)
    print(f"Server running at: http://localhost:5000")
    print(f"API Endpoints:")
    print(f"  - GET  /api/health")
    print(f"  - POST /api/ask")
    print(f"  - POST /api/upload")
    print(f"  - POST /api/search")
    print("=" * 60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
