
import azure.cognitiveservices.speech as speechsdk
import decouple


speech_config = speechsdk.SpeechConfig(subscription=decouple.config('AZURE_SPEECH_KEY1'),
                                       region=decouple.config('AZURE_SPEECH_REGION'))

audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

speech_config.speech_synthesis_voice_name='en-US-DustinMultilingualNeural'

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

text = """
<speak xmlns="http://www.w3.org/2001/10/synthesis" version="1.0" xml:lang="en-US">
  <voice name="en-US-DustinMultilingualNeural"> 
     <prosody pitch="+20%" rate="fast" volume="+85%">Ha ha ha! hee hee heeheeheeheeeeeeee That’s hilarious!</prosody>
    <prosody pitch="+10%" rate="medium">Hee hee hee... Oh, stop it!</prosody>
  </voice>
</speak>
"""

# <prosody pitch="-15%" rate="55%" volume="+20%">Look how they massacred my boy!</prosody>

speech_synthesis_result = speech_synthesizer.speak_ssml_async(text).get()

if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized for text [{}]".format(text))
elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_synthesis_result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")