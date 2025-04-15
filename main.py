import moviepy.editor as mp
import azure.cognitiveservices.speech as speechsdk
from pydub import AudioSegment
import os
from dotenv import load_dotenv
import time

# Load environment variables from .env file
load_dotenv()
key=os.getenv("AZURE_SPEECH_KEY")
region=os.getenv("AZURE_SPEECH_REGION")

# Path to your video file
video_path = "video.mp4"
audio_path = "extracted_audio.wav"

# Extract audio from video
video = mp.VideoFileClip(video_path)
video.audio.write_audiofile(audio_path)

# Convert audio to a format compatible with Azure Speech
audio = AudioSegment.from_wav(audio_path)
audio.export(audio_path, format="wav")

# Initialize speech config
speech_config = speechsdk.SpeechConfig(subscription=key, region=region)
speech_config.speech_recognition_language = "en-US"  # Set language as needed

# Create an audio configuration using the audio file
audio_config = speechsdk.audio.AudioConfig(filename=audio_path)

# Create a speech recognizer
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

# Initialize the transcription result
all_results = []

# Create a class to manage the transcription state
class TranscriptionCompletionWaiter:
    def __init__(self):
        self.done = False
        
    def set_done(self):
        self.done = True

# Instantiate the waiter
waiter = TranscriptionCompletionWaiter()

# Callback functions for events
def recognized_cb(evt):
    all_results.append(evt.result.text)
    print(f"RECOGNIZED: {evt.result.text}")

def stop_cb(evt):
    print('CLOSING on {}'.format(evt))
    waiter.set_done()

def canceled_cb(evt):
    print('CANCELED: {}'.format(evt))
    waiter.set_done()

# Connect callbacks to the events
speech_recognizer.recognized.connect(recognized_cb)
speech_recognizer.session_stopped.connect(stop_cb)
speech_recognizer.canceled.connect(canceled_cb)

# Start continuous recognition
print("Starting continuous speech recognition...")
speech_recognizer.start_continuous_recognition()

# Wait for completion (or timeout)
while not waiter.done:
    time.sleep(0.5)

# Stop recognition
speech_recognizer.stop_continuous_recognition()

# Combine all results
full_transcription = ' '.join(all_results)
print("\nComplete Transcription:")
print(full_transcription)

# Optionally save the transcription to a file
with open("transcription.txt", "w") as file:
    file.write(full_transcription)
    print("Transcription saved to transcription.txt")