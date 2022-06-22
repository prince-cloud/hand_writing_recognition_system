import os, io
from google.cloud import vision
from google.cloud.vision_v1 import types
from google.cloud import vision_v1
# Create your views here.


#def scanText():
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


