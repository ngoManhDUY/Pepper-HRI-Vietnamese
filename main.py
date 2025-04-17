import openai
import speech_recognition as sr
from openai import OpenAI
import subprocess

# Initialize recognizer
recognizer = sr.Recognizer()
my_api_key = 'open-ai-key'  # Replace with your OpenAI API key
file_path = r'/home/ngonanhduy/Documents/pepper_gpt_viet/say_something.py' #change to the path of your script

client = OpenAI(
    # This is the default and can be omitted
    api_key=my_api_key,
)

def listen_2_input():
    # Use device index 4 (your built-in microphone)
    mic_index = 4  # HDA Intel PCH: ALC257 Analog
    
    with sr.Microphone(device_index=mic_index) as source:
        print("Please say something...")
        recognizer.adjust_for_ambient_noise(source)
        recognizer.dynamic_energy_threshold = True
        recognizer.energy_threshold = 4000  # You may need to adjust this value
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        return ""

def get_openai_output(text):
    # Check if text is empty
    if not text:
        return "I couldn't understand what you said."
    
    try:
        response = client.responses.create(
            model="gpt-4o",
            instructions="You are an Pepper Robot develop at Vietnam Academy and Institute and technology.",
            input=text,
            # You might need to explicitly set max_tokens parameter
        )
        
        print(response.output_text)
        return response.output_text
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return "Sorry, I'm having trouble processing your request."

def speak_by_pepper(text):
    result = subprocess.run(
        ['/home/ngonanhduy/anaconda3/envs/py27/bin/python2', file_path, text],  # change to the path of python27 interpreter in your pc
        text=True
    )

def main():
    print("=== Pepper Voice Assistant ===")
    print("Say 'goodbye' or 'exit' to end the conversation")
    
    while True:
        text = listen_2_input()
        
        # Check for exit commands
        if text.lower() in ["goodbye", "exit", "quit", "stop"]:
            print("Ending conversation. Goodbye!")
            break
            
        ans = get_openai_output(text)
        speak_by_pepper(ans)
        print("-" * 50)  # Separator between conversations

main()
