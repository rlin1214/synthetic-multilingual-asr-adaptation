import pandas as pd
import soundfile as sf

# Load CSV with transcripts
#df = pd.read_csv(r"C:\Users\BOSSE\source\repos\W24D2\synthetic-multilingual-asr-adaptation\synthetic-multilingual-speech-asr\en\manifest.jsonl")
#C:\Users\BOSSE\source\repos\W24D2\synthetic-multilingual-asr-adaptation\synthetic-multilingual-speech-asr\en\manifest.jsonl
# need to read jsonl file.
df = pd.read_json(
    r"C:\Users\BOSSE\source\repos\W24D2\synthetic-multilingual-asr-adaptation\synthetic-multilingual-speech-asr\en\manifest.jsonl",
    lines=True
)


# Play a sample
file_path = r"C:\Users\BOSSE\source\repos\W24D2\synthetic-multilingual-asr-adaptation\synthetic-multilingual-speech-asr\en\en_0.wav"
#C:\Users\BOSSE\source\repos\W24D2\synthetic-multilingual-asr-adaptation\synthetic-multilingual-speech-asr\en\en_0.wav

data, samplerate = sf.read(file_path)
print("Audio data shape:", data.shape, "Sample rate:", samplerate)