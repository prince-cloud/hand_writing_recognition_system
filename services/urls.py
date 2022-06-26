from django.urls import path
from .import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'services'

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),

    path('scantext/', views.scan_text, name="scan_text"),
    path('api/scantext/', views.scan_text_api, name="scan_text_api"),
    path('translate/', views.translateText, name="translateText"),
    path('api/translate/', views.translateText_api, name="translateText_api"),
]