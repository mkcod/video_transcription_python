# Video to Text Transcription (Private & Free)

This project extracts audio from a video file and transcribes the audio to text using Azure Cognitive Services.

## Requirements

- Python 3.6+
- `moviepy`
- `azure-cognitiveservices-speech`
- `pydub`
- `dotenv`

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mkcod/video_transcription_python.git
   cd video_transcription_python
   ```

2. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Azure Cognitive Services:**

   - Create an Azure account and set up the Speech service.
   - Obtain your subscription key and region.

4. **Create a `.env` file in the project directory and add your Azure Speech service credentials:**

   ```env
   AZURE_SPEECH_KEY=your_azure_speech_key
   AZURE_SPEECH_REGION=your_azure_speech_region
   ```

5. **Place your video file in the project directory and name it `video.mp4` or update the `video_path`.**

## Usage

1. **Run the script:**

   ```bash
   python main.py
   ```

2. **The script will:**

   - Extract audio from the video file.
   - Convert the audio to a format compatible with Azure Speech.
   - Transcribe the audio to text.
   - Save the transcription to `transcription.txt`.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
