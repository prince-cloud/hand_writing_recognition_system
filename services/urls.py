from django.urls import path
from .import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'services'

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),

    #path('scanned-text/', views.scan_text, name="scan_text"),
    path('scantext/', views.scan_text, name="scan_text"),
    path('translate/', views.translateText, name="translateText"),
]