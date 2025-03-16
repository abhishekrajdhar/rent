# Import required libraries
from fastapi import FastAPI, Request
from pydantic import BaseModel
import google.generativeai as genai
import google.api_core.exceptions
import uvicorn


# Initialize API key for Gemini
genai.configure(api_key="AIzaSyCnCxtKRmRxp9DOQcDi0htWHtj19mCJjpY")

# FastAPI app instance
app = FastAPI(title="RentRite AI Chat API")

# Request model for input validation
class ChatRequest(BaseModel):
    message: str

# Response model (optional, for clarity)
class ChatResponse(BaseModel):
    response: str

# API endpoint for chat
@app.post("/chat", response_model=ChatResponse)
async def chat_with_ai(chat_request: ChatRequest):
    user_message = chat_request.message
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(user_message)
        bot_reply = response.text
    except google.api_core.exceptions.GoogleAPIError:
        bot_reply = "Sorry, I am having trouble processing your request. Please try again later."

    return {"response": bot_reply}

# Run the app (optional if running via command line)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
