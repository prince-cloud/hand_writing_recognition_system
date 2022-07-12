from django.urls import path
from .import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'services'

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),

    ## web
    path('scantext/', views.scan_text, name="scan_text"),
    path('translate/', views.translateText, name="translateText"),
    path('texttospeech/', views.texttospeech, name="texttospeech"),

    ## apis
    path('api/texttospeech/', views.text_to_speech_api, name="texttospeech_api"),

    path('api/scantext/', views.scan_text_api, name="scan_text_api"),
    path('api/translate/', views.translateText_api, name="translateText_api"),
]