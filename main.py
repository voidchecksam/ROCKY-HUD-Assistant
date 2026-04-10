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
    
    for attempt in range(3):
        try:
            completion = client.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct", 
                messages=[{"role": "user", "content": [{"type": "text", "text": "solve this and return ONLY valid json"}, {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}]}]
            )
            
            # remove weird markdown block formatting
            clean_text = completion.choices[0].message.content.strip().replace('```json', '').replace('```', '')
            return json.loads(clean_text)
            
        except Exception as e:
            if "429" in str(e) or "503" in str(e):
                time.sleep(2)
                continue
            return {"error": str(e)}

def notify(message: str, title: str = "Test Assistant"):
    try:
        notification.notify(title=title, message=message, app_name="Test Assistant", timeout=7)
    except Exception as e:
        pass

def on_press(key):
    if key == pynput.keyboard.Key.f8:
        print("\ncapturing screen... ")
        notify("processing...")
        try:
            image = ImageGrab.grab()
            
            # BIG FIX: resizing image to save tokens
            image.thumbnail((1280, 1280)) 
            
            result = get_answer_from_groq(image)
            print(result)
            notify(f"Answer: {result.get('answer', 'Error')}")
            
        except Exception as e:
            print(f"error: {e}")
            notify("error occurred. check console.")

def main():
    print("listening for F8 hotkey...")
    with pynput.keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()