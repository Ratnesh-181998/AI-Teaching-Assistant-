"""
RAG Chain Module
Implements Retrieval-Augmented Generation using LangChain
"""
from typing import List, Dict
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from vector_store import VectorStoreManager
from config import Config


class RAGChain:
    """RAG (Retrieval-Augmented Generation) implementation"""
    
    def __init__(self, vector_store_manager: VectorStoreManager, api_key: str = None):
        """
        Initialize RAG chain
        
        Args:
            vector_store_manager: VectorStoreManager instance
            api_key: OpenAI API key (default from config)
        """
        self.vector_store_manager = vector_store_manager
        self.api_key = api_key or Config.OPENAI_API_KEY
        
        # Initialize ChatGPT
        self.llm = ChatOpenAI(
            openai_api_key=self.api_key,
            model_name=Config.LLM_MODEL,
            temperature=Config.TEMPERATURE
        )
        
        # Custom prompt template
        self.prompt_template = """You are an AI Teaching Assistant designed to help students understand course materials.

Use the following context from lecture materials to answer the student's question. 
If you don't know the answer based on the context, say so - don't make up information.
Provide detailed, educational responses that help students learn.

Context from lectures:
{context}

Student Question: {question}

Teaching Assistant Response:"""
        
        self.prompt = PromptTemplate(
            template=self.prompt_template,
            input_variables=["context", "question"]
        )
    
    def create_qa_chain(self) -> RetrievalQA:
        """
        Create RetrievalQA chain
        
        Returns:
            RetrievalQA chain
        """
        try:
            if self.vector_store_manager.vector_store is None:
                print("X No vector store available")
                return None
            
            qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                chain_type="stuff",
                retriever=self.vector_store_manager.vector_store.as_retriever(
                    search_kwargs={"k": Config.TOP_K_RESULTS}
                ),
                return_source_documents=True,
                chain_type_kwargs={"prompt": self.prompt}
            )
            
            print("+ RAG chain created successfully")
            return qa_chain
        except Exception as e:
            print(f"X Error creating QA chain: {e}")
            return None
    
    def ask_question(self, question: str, return_sources: bool = True) -> Dict:
        """
        Ask a question using RAG
        
        Args:
            question: Student's question
            return_sources: Whether to return source documents
            
        Returns:
            Dictionary with answer and optional source documents
        """
        try:
            qa_chain = self.create_qa_chain()
            if qa_chain is None:
                return {
                    "answer": "Error: Unable to create QA chain",
                    "sources": []
                }
            
            result = qa_chain({"query": question})
            
            response = {
                "question": question,
                "answer": result["result"],
                "sources": []
            }
            
            if return_sources and "source_documents" in result:
                response["sources"] = [
                    {
                        "content": doc.page_content[:200] + "...",
                        "metadata": doc.metadata
                    }
                    for doc in result["source_documents"]
                ]
            
            return response
        except Exception as e:
            print(f"X Error answering question: {e}")
            return {
                "question": question,
                "answer": f"Error: {str(e)}",
                "sources": []
            }
    
    def ask_with_context(self, question: str) -> str:
        """
        Ask question and get answer with retrieved context
        
        Args:
            question: Student's question
            
        Returns:
            Answer string
        """
        try:
            # Retrieve relevant documents
            docs = self.vector_store_manager.similarity_search(question)
            
            if not docs:
                return "I couldn't find relevant information in the course materials to answer this question."
            
            # Combine context
            context = "\n\n".join([doc.page_content for doc in docs])
            
            # Create prompt
            prompt = self.prompt.format(context=context, question=question)
            
            # Get response from LLM
            response = self.llm.predict(prompt)
            
            return response
        except Exception as e:
            print(f"X Error: {e}")
            return f"Error generating response: {str(e)}"
