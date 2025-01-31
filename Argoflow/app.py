from fastapi import FastAPI, Request
from transformers import pipeline

app = FastAPI()

# Load the transformer model pipeline
generator = pipeline("text-generation", model="distilgpt2")

@app.post("/generate")
async def generate_text(request: Request):
    data = await request.json()
    prompt = data.get("prompt")
    if not prompt:
        return {"error": "No prompt provided"}
    
    # Generate text using the model
    result = generator(prompt, max_length=50, num_return_sequences=1)
    return {"generated_text": result[0]['generated_text']}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
