
from django.urls import path

from denis.my_cv.views import MainPage

urlpatterns = [
    path('',MainPage.as_view())
]