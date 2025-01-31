from fastapi import FastAPI, Request
from transformers import pipeline
import json
import os

app = FastAPI()

# Load the transformer model pipeline
generator = pipeline("text-generation", model="distilgpt2")

# Path to the file where prompts will be stored
PROMPT_FILE_PATH = "/app/data/prompts.json"

# Ensure the prompts file exists
if not os.path.exists(PROMPT_FILE_PATH):
    with open(PROMPT_FILE_PATH, 'w') as f:
        json.dump([], f)

@app.post("/generate")
async def generate_text(request: Request):
    data = await request.json()
    prompt = data.get("prompt")
    if not prompt:
        return {"error": "No prompt provided"}
    
    # Save the prompt to the file
    try:
        with open(PROMPT_FILE_PATH, 'r+') as f:
            prompts = json.load(f)
            prompts.append(prompt)
            f.seek(0)
            json.dump(prompts, f)
        print(f"Saved prompt: {prompt}")
    except Exception as e:
        print(f"Error saving prompt: {e}")
    
    # Generate text using the model
    result = generator(prompt, max_length=50, num_return_sequences=1)
    return {"generated_text": result[0]['generated_text']}

@app.get("/prompts")
async def get_prompts():
    # Retrieve the stored prompts
    try:
        with open(PROMPT_FILE_PATH, 'r') as f:
            prompts = json.load(f)
        return {"prompts": prompts}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
