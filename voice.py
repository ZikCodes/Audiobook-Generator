import edge_tts

# Voice generating function
async def generate_voice(user_text, voice_choice):
    text = user_text
    
    communicate = edge_tts.Communicate(
        text,
        voice=voice_choice
    )
    audio = b""
    
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio += chunk["data"]
                      
    return audio
    
    
    