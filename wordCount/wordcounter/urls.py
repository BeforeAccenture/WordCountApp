from django.contrib import admin
from django.urls import path,include
from wordcounter import views

app_name="wordcounter"
urlpatterns = [
    path("",views.index,name="index"),
]
