from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
#packages
import os, io
from google.cloud import vision
from google.cloud.vision_v1 import types
from google.cloud import vision_v1
from translate import Translator


from services.forms import ScanTextForm, TranslateTextForm
# Create your views here.




def index(request):
    return render(request, 'index.html', {
        "ScanTextForm": ScanTextForm()
    })

def scan_text(request: HttpRequest):
    docText = ""
    print(request.headers)
    if request.method == "POST":
        form = ScanTextForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            scan_form = form.save(commit=False)
            image_file = data['image']
            client = vision_v1.ImageAnnotatorClient()
            content = image_file.read()
            image = vision_v1.types.Image(content=content)
            response = client.document_text_detection(image=image)
            docText = response.full_text_annotation.text
            print(docText)
            scan_form.save()
        else:
            messages.error(request, 'form invalid')
    else:
        form = ScanTextForm()
    
    return render(request, 'pages/scan_text.html', 
        {
            "form": form, 
            "docText": docText,
            "translate_form": TranslateTextForm(),
        })


def translateText(request):
    translation = ""
    translate_to = ""
    if request.method == "POST":
        form = TranslateTextForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            translateForm = form.save(commit=False)
            text = data['text']
            translate_to = data['translate_to']

            translator = Translator(to_lang=f"{translate_to}")
            translation = translator.translate(f"{text}")

            print (translation)
            translateForm.save()
        else:
            messages.error(request, "invalid data entry")
    else:
        form = TranslateTextForm()

    return render(request, "pages/translate_text.html", 
        {
            "form": form, 
            "translation": translation,
            "translate_to": translate_to
        })
    

@csrf_exempt
def scan_text_api(request: HttpRequest):
    docText = ""
    if request.method == "POST":
        form = ScanTextForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            scan_form = form.save(commit=False)
            image_file = data['image']
            client = vision_v1.ImageAnnotatorClient()
            content = image_file.read()
            image = vision_v1.types.Image(content=content)
            response = client.document_text_detection(image=image)
            docText = response.full_text_annotation.text
            print(docText)
            scan_form.save()

            
        else:
            return JsonResponse({
                "docText": docText,
                "success": False,
                "message": "Translation faild. Please try again later."
            })
    else:
        return JsonResponse({
                "docText": docText,
                "success": False,
                "message": "Translation faild. Please try again later."
            })
    return JsonResponse({
        "docText": docText,
        "success": True,
        "message": "Translated successfully"
    })

@csrf_exempt
def translateText_api(request: HttpRequest):
    translation = ""
    translate_to = ""
    if request.method == "POST":
        form = TranslateTextForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            translateForm = form.save(commit=False)
            text = data['text']
            translate_to = data['translate_to']

            translator = Translator(to_lang=f"{translate_to}")
            translation = translator.translate(f"{text}")

            print (translation)
            translateForm.save()
        else:
            return JsonResponse({
                "translation": translation,
                "translated_to": translate_to,
                "success": False,
                "message": "Translation faild. Please try again later."
            })

    else:
        return JsonResponse({
            "translation": translation,
            "translated_to": translate_to,
            "success": False,
            "message": "form failed"
        })

    return JsonResponse({
                "translation": translation,
                "translated_to": translate_to,
                "success": True,
                "message": "translation success"
            })
    
    