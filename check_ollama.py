
import requests
import json
import time

print("Checking Ollama Server...")

try:
    # Check version
    print("1. Checking version...")
    response = requests.get('http://localhost:11434/api/version', timeout=5)
    print(f"   Version: {response.json()['version']}")
    
    # Check loaded models
    print("\n2. Checking tags...")
    response = requests.get('http://localhost:11434/api/tags', timeout=5)
    models = [m['name'] for m in response.json()['models']]
    print(f"   Available models: {models}")
    
    # Simple generation test
    print("\n3. Testing simple generation (hello world)...")
    start_time = time.time()
    response = requests.post('http://localhost:11434/api/generate', 
                           json={
                               "model": "mistral",
                               "prompt": "Say hello!",
                               "stream": False
                           },
                           timeout=120) # 2 minute timeout
    duration = time.time() - start_time
    print(f"   Response: {response.json()['response']}")
    print(f"   Time taken: {duration:.2f} seconds")
    
except Exception as e:
    print(f"\nERROR: {e}")
