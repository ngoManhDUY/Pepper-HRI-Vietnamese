import paramiko
import sys
import os
import time
from naoqi import ALProxy

# Set your robot's IP
PEPPER_IP = "192.168.0.132"
PEPPER_PORT = 9559
SSH_USERNAME = "nao"  # Default username for Pepper
SSH_PASSWORD = "nao"  # Default password for Pepper

def copy_to_pepper(local_file):
    """Copy local file to Pepper"""
    remote_file = "/home/nao/audio_file.mp3"
    
    try:
        # Set up SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(PEPPER_IP, username=SSH_USERNAME, password=SSH_PASSWORD)
        
        # Copy file
        sftp = ssh.open_sftp()
        sftp.put(local_file, remote_file)
        sftp.close()
        ssh.close()
        
        print("File copied to Pepper: {}".format(remote_file))
        return remote_file
        
    except Exception as e:
        print("Error copying file: {}".format(e))
        return None

def play_audio_on_pepper(audio_file):
    try:
        # Connect to Pepper's audio player
        audio_player = ALProxy("ALAudioPlayer", PEPPER_IP, PEPPER_PORT)
        
        # Play the file on Pepper
        print("Playing audio on Pepper...")
        audio_id = audio_player.playFile(audio_file)
        print("Audio playing with ID: {}".format(audio_id))
        
        # Wait for audio to finish
        time.sleep(3)
        
    except Exception as e:
        print("Error: {}".format(e))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        local_file = sys.argv[1]
    else:
        local_file = "/home/ngonanhduy/Documents/pepper_gpt_viet/vietnamese_speech.mp3"
    
    if os.path.exists(local_file):
        # Copy to Pepper
        remote_file = copy_to_pepper(local_file)
        
        if remote_file:
            # Play the file
            play_audio_on_pepper(remote_file)
    else:
        print("Error: File '{}' doesn't exist".format(local_file))