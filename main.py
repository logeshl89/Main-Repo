from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key="AIzaSyCcbkTa-vHbMZZ3B0CRdP1lVca2RXqt4Zs")  # Replace with your actual API key
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048
}
model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
)

# Create FastAPI instance
app = FastAPI()

# Pydantic model for request payload
class Prompt(BaseModel):
    prompt: str

# Define API route
@app.post("/generate_text/")
def generate_text(prompt: Prompt):
    try:
        response = model.generate_content(prompt.prompt)
        return {"generated_text": response.text}
    except Exception as e:
        return {"error": str(e)}
