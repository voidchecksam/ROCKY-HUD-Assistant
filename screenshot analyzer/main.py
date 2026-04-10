import pynput
from PIL import ImageGrab
from plyer import notification
import json
import base64
from io import BytesIO
from groq import Groq
import time

# ofc google locked the free tier (429 quota 0) because i don't have a card attached.
# openai or claude out of the question (I AM BROKE) 
# of course if anyone has a paid sub to any api they can replace the import instead of groq
# groq give llama 3.2 vision free tier, lpu speed is insane 
client = Groq(api_key="API_F**KING_KEY_HERE")

def get_answer_from_groq(image):
    # groq aint gon work w ur jpeg dawg BASE64 TIMEE should also lessen token usage i think
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    base64_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.2-11b-vision-preview",
            messages=[{"role": "user", "content": [{"type": "text", "text": "solve this"}, {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}]}]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return str(e)

def main():
    print("starting vision assistant...")

if __name__ == "__main__":
    main()