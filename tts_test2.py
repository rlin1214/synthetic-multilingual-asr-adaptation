from TTS.api import TTS

# List available pretrained models
print(TTS.list_models())

# Initialize a pretrained model (English, fast TTS)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=True, gpu=False)

# Convert text to speech
text = "Hello! This is a test of TTS on Windows 10."
tts.tts_to_file(text=text, file_path="output.wav")