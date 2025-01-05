from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import os
import logging

# Environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY') or 'OPENAI_API_KEY'

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize FastAPI app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request and response models
class ConversationRequest(BaseModel):
    messages: List[str]

class ConversationResponse(BaseModel):
    messages: List[str]

class ChatResponse(BaseModel):
    text: str

# Updated imports and initialization
try:
    from langchain_openai import ChatOpenAI  # Use the updated library
    from langchain.prompts import PromptTemplate

    # Initialize LLM
    llm = ChatOpenAI(api_key=OPENAI_API_KEY)

    # Define a simple prompt for the LLM
    prompt_template = PromptTemplate(template="The user said: {input}. Please respond appropriately.")

    # Placeholder for knowledge base
    knowledge_base = {"sources_list": []}  # Update with actual implementation

except ImportError as e:
    logging.error(f"Error importing required modules: {e}")
    llm = None
    knowledge_base = None


@app.post("/walmartbot")
def handle_conversation(request: ConversationRequest):
    """
    Walmart Sales Bot Endpoint:
    Handles customer queries by interacting with the LLM.
    """
    try:
        if llm is None or knowledge_base is None:
            raise HTTPException(status_code=500, detail="LLM or knowledge base is not initialized.")

        # Process the input messages
        user_messages = " ".join(request.messages) if request.messages else ""
        logging.info(f"User messages: {user_messages}")

        # Use LLM to generate a response
        ai_message = llm.generate([prompt_template.format(input=user_messages)])
        logging.info(f"LLM Response: {ai_message.generations[0].text.strip()}")

        sources = knowledge_base.get("sources_list", [])
        response = {
            "messages": [ai_message.generations[0].text.strip()],
            "sources": sources,
        }
        knowledge_base["sources_list"] = []  # Reset sources
        return response

    except Exception as e:
        logging.error(f"Error in /walmartbot: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.post("/searchgpt")
def handle_chat(request: ChatResponse):
    """
    SearchGPT Endpoint:
    Provides real-time information using external sources.
    """
    try:
        if not request.text:
            return {"message": "Please enter input in the text field"}

        input_text = request.text
        logging.info(f"User input: {input_text}")
        # Replace with actual implementation of your search function
        response = f"Mock response for input: {input_text}"  # Replace with actual search function
        return {"response": response}

    except Exception as e:
        logging.error(f"Error in /searchgpt: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)
