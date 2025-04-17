import openai
from openai import OpenAI
import subprocess

# Initialize OpenAI client with your API key
my_api_key = 'open-ai-key'  # Replace with your OpenAI API key
file_path = r'/home/ngonanhduy/Documents/pepper_gpt_viet/say_something.py'

client = OpenAI(
    api_key=my_api_key,
)

def get_text_input():
    """Get input from keyboard instead of microphone"""
    print("Type your question (or 'quit' to exit):")
    text = input("> ")
    
    if text.lower() in ['quit', 'exit']:
        return None
    
    print(f"You typed: {text}")
    return text

def get_openai_output(text):
    # Check if text is empty
    if not text:
        return "I couldn't understand what you typed."
    
    try:
        response = client.responses.create(
            model="gpt-4o",
            instructions="You are an assistant that talks like a teacher.",
            input=text,
        )
        
        print(f"Assistant: {response.output_text}")
        return response.output_text
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return "Sorry, I'm having trouble processing your request."

def speak_by_pepper(text):
    """Have Pepper speak the provided text"""
    try:
        result = subprocess.run(
            ['/home/ngonanhduy/anaconda3/envs/py27/bin/python2', file_path, text],
            text=True,
            check=True,
            capture_output=True
        )
        print("Pepper is speaking...")
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error when making Pepper speak: {e}")
        print(f"Error output: {e.stderr}")
        return None

def main():
    """Main function that handles the conversation loop"""
    print("=== Pepper Text Chat Interface ===")
    print("You can type questions and Pepper will respond.")
    
    while True:
        # Get text input from user
        text = get_text_input()
        
        # Check if user wants to quit
        if text is None:
            print("Goodbye!")
            break
            
        # Get response from OpenAI
        ans = get_openai_output(text)
        
        # Have Pepper speak the response
        speak_by_pepper(ans)
        print("-" * 50)

if __name__ == "__main__":
    main()