# Add after imports
import pyaudio
import wave

# Test audio function you can add to verify your microphone works
def test_microphone():
    p = pyaudio.PyAudio()
    print("Available audio devices:")
    for i in range(p.get_device_count()):
        dev_info = p.get_device_info_by_index(i)
        print(f"Device {i}: {dev_info['name']}")
        print(f"  Input channels: {dev_info['maxInputChannels']}")
        print(f"  Default sample rate: {dev_info['defaultSampleRate']}")
    p.terminate()

# Add this line to call the function when the script runs
if __name__ == "__main__":
    test_microphone()