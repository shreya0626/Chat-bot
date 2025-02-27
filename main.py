from fastapi import FastAPI, Request
import json
import os
import google.generativeai as genai
from fastapi.middleware.cors import CORSMiddleware

# Initialize Google Gemini API
genai.configure(api_key="**gemini-api-key**")

app = FastAPI()

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load documentation data
data_folder = "data"
cdp_data = {}

for file in os.listdir(data_folder):
    if file.endswith(".json"):
        with open(os.path.join(data_folder, file), "r", encoding="utf-8") as f:
            cdp_name = file.replace(".json", "")
            cdp_data[cdp_name] = json.load(f)[cdp_name]

@app.post("/query/")
async def query(request: Request):
    """Handles user queries by searching documentation or generating a response."""
    user_input = await request.json()
    question = user_input.get("query", "")
    cdp = user_input.get("cdp", "").lower()

    if cdp not in cdp_data:
        return {"response": "I'm specialized in Segment, mParticle, Lytics, and Zeotap. Please specify one."}

    # Search for the answer
    doc_content = cdp_data[cdp]
    
    if question.lower() in doc_content:
        return {"response": doc_content[question.lower()]}

    # If no direct answer, use Google Gemini API to generate one
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Based on this documentation, answer: {question} \n\n {doc_content}")

    return {"response": response.text if response else "No relevant information found."}

