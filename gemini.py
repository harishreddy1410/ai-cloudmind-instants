import os
from google import genai

def instant():
    client = genai.Client(api_key="my google api key")    
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

print(instant())