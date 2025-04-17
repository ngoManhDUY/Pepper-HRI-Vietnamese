import sys
from naoqi import ALProxy
ip = "192.168.0.132" #Change to pepper ip 

sys.path.append("/home/ngomanhduy/Downloads/pynaoqi-python2.7-2.5.7.1-linux64/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")

def speak(text):
    tts    = ALProxy("ALTextToSpeech", ip, 9559)
    tts.say(text)

# The script will take the first argument from sys.argv
if __name__ == "__main__":
    text = sys.argv[1]  # The first argument passed to the script
    print(speak(text))
