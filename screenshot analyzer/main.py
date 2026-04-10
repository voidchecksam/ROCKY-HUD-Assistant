import pynput
from PIL import ImageGrab
from plyer import notification
import json
import time
from google import genai

client = genai.Client(api_key="API_F**KING_KEY_HERE")

def get_answer(image):
    # redo tries for server hiccups
    for attempt in range(3):
        try:
            # bumpdown to 2.0-flash
            response = client.models.generate_content(
                model='gemini-2.0-flash',
                contents=["extract the answer to this question in json format", image]
            )
            return json.loads(response.text)
        except Exception as e:
            if "503" in str(e):
                time.sleep(2)
                continue
            return {"error": str(e)}

def main():
    print("starting desktop vision assistant on gemini 2.0...")

if __name__ == "__main__":
    main()