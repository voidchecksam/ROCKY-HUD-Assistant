import pynput
from PIL import ImageGrab
from plyer import notification
import json
import base64
from io import BytesIO
from groq import Groq
import time

client = Groq(api_key="API_F**KING_KEY_HERE")

def get_answer_from_groq(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    base64_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    # added the retry loop back in just in case groq hangs too
    for attempt in range(3):
        try:
            # groq literally just decommissioned 3.2 vision right as i tested it. wtf. upgrading to llama 4
            completion = client.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct", 
                messages=[{"role": "user", "content": [{"type": "text", "text": "solve this and return ONLY valid json"}, {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}]}]
            )
            return completion.choices[0].message.content
        except Exception as e:
            if "429" in str(e) or "503" in str(e):
                time.sleep(2)
                continue
            return str(e)

def main():
    print("running llama 4 scout...")

if __name__ == "__main__":
    main()