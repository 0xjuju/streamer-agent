
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from framework.agents import OpenAI
from text_to_speech.azure_speech_api import tts

app = FastAPI()
openai_api = OpenAI()


@app.post("/api/chat")
async def chat_endpoint(request: Request):

    data = await request.json()
    user_message = data.get("message")
    messages = openai_api.process_message(message=user_message, instructions="", thread_id="thread_ZhdVMfBTRXm7orSa9Rn0iSwd")
    reply = next((message.content[0].text for message in messages if message.role == "assistant"), None).value
    tts(reply)
    response_text = f"Tony: {reply}"
    return JSONResponse({"reply": response_text})



