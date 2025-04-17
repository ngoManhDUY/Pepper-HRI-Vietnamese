import sys
import qi
from naoqi import ALProxy
import threading
ip = "192.168.0.132"
    
def move():
    animation_player = ALProxy("ALAnimationPlayer", ip, 9559)
    animation_player.run("animations/Stand/Gestures/Explain_1")

def speak_and_move(text):
    tts    = ALProxy("ALTextToSpeech", ip, 9559)
    thread = threading.Thread(target=move)

    thread.start()
    tts.say(text)

# The script will take the first argument from sys.argv
if __name__ == "__main__":
    text = sys.argv[1]  # The first argument passed to the script
    print(speak_and_move(text))
