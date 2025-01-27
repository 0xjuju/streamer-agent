import decouple
import pyaudio
import requests

headers = {
    "accept": "*/*",
    "content-type": "application/json",
    "Authorization": f"Bearer {decouple.config('SPEECHIFY_API_KEY')}"
}


def get_voices():
    url = "https://api.sws.speechify.com/v1/voices"
    voices = requests.get(url, headers=headers)
    return voices.text


def stream_speech(voice_id: str, text: str, language="en-US", model="simba-english"):

    url = "https://api.sws.speechify.com/v1/audio/stream"

    payload = {
        "input": text,
        "language": language,
        "model": model,
        "voice_id": voice_id
    }

    speech = requests.post(url, headers=headers, json=payload)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,  # Audio format
                    channels=1,  # Mono audio
                    rate=44100,  # Sampling rate (match the API's audio rate if known)
                    output=True)
    try:

        # Stream audio in real time
        for chunk in speech.iter_content(chunk_size=1024):
            if chunk:  # Only play non-empty chunks
                stream.write(chunk)
    except Exception as e:
        print(e)

    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()


def tts(voice_id: str, text: str, language="en-US", audio_format="wav", model="simba-english"):

    url = "https://api.sws.speechify.com/v1/audio/speech"

    payload = {
        "audio_format": audio_format,
        "input": text,
        "language": language,
        "model": model,
        "voice_id": voice_id
    }
    speech = requests.post(url, headers=headers, json=payload)
    return speech.json()










