import os
from gtts import gTTS
import sys

def generate_vietnamese_audio(text=None):
    """Generate Vietnamese audio file from text"""
    # Default text or use provided text
    if text is None:
        text = "Xin chào, tôi là robot Pepper"
    else:
        # Use the text provided as command line argument
        text = text
    
    try:
        # Create audio file in the script's directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        audio_file = os.path.join(current_dir, "vietnamese_speech.mp3")
        
        # Generate Vietnamese speech
        tts = gTTS(text=text, lang='vi')
        tts.save(audio_file)
        
        print(f"Audio file saved to {audio_file}")
        print("Success!")
        
    except Exception as e:
        print(f"Error generating audio: {e}")

if __name__ == "__main__":
    # If text is provided as command line argument, use it
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
        generate_vietnamese_audio(text)
    else:
        generate_vietnamese_audio()