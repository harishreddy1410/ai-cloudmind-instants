from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from openai import OpenAI
from google import genai
import os 

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise Exception("GEMINI_API_KEY is missing")

app = FastAPI()

@app.get("/", response_class=HTMLResponse)


#def instant():
#    client = OpenAI()
#    message = """
#        You are on a website that has just been deployed to production for the first time!
#        Please reply with an enthusiastic announcement to welcome visitors to the site, explaining that it is live on production for the first time!
#        """
#    messages = [{"role": "user", "content": message}]
#    response = client.chat.completions.create(model="gpt-5-nano", messages=messages)
#    reply = response.choices[0].message.content.replace("\n", "<br/>")
#    html = f"<html><head><title>Live in an Instant!</title></head><body><p>{reply}</p></body></html>"
#    return html

def instant():
    client = genai.Client()    
    chat = client.chats.create(
    model="gemini-3.8-flash"
    )    
    response = chat.send_message("""
    You are on a website that has just been deployed to production for the first time!
    Please reply with an enthusiastic announcement to welcome visitors to the site, explaining that it is live on production for the first time!
    """)
    
    reply = response.text.replace("\n", "<br/>")
    
    return f"""
    <html>
    <head><title>Live in an Instant!</title></head>
    <body><p>{reply}</p></body>
    </html>
    """