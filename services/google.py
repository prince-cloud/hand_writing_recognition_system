import os, io
from google.cloud import vision
from google.cloud.vision_v1 import types
from google.cloud import vision_v1
from google.cloud import translate_v2 as translate
from google.cloud import texttospeech_v1

# Create your views here.


def scanText():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'./ServiceAccountToken.json'
    client = vision_v1.ImageAnnotatorClient()

    print(client)

    FOLDER_PATH = r'./media'
    IMAGE_FILE = '1.jpg'
    FILE_PATH = os.path.join(FOLDER_PATH, IMAGE_FILE)

    with io.open(FILE_PATH, 'rb') as image_file:
        content = image_file.read()

    image = vision_v1.types.Image(content=content)
    response = client.document_text_detection(image=image)
    docText = response.full_text_annotation.text
    print(docText)


def translateText():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'./ServiceAccountAPI.json'
    translate_client = translate.Client()

    text = "hello world, i love you all"
    target = "ha"
    output = translate_client.translate(
        text,
        target_language = target,
    )

    print("========= printing output ===========")
    print(output)


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'./ServiceAccountAPI.json'
client = texttospeech_v1.TextToSpeechClient()

text = '<speak> Hello, my name is Prince Achemapong and i am trying out to use google\n text to speech </speak>'

synthesis_input = texttospeech_v1.SynthesisInput(ssml=text)

voice = texttospeech_v1.VoiceSelectionParams(
    language_code = 'en-in',
    ssml_gender = texttospeech_v1.SsmlVoiceGender.MALE,
)

print(client.list_voices)
audio_config = texttospeech_v1.AudioConfig(
    audio_encoding = texttospeech_v1.AudioEncoding.MP3
)

response = client.synthesize_speech(
    input = synthesis_input,
    voice = voice,
    audio_config = audio_config,

)



with open(f'./media/audio/audio.mp3', 'wb') as output:
    output.write(response.audio_content)