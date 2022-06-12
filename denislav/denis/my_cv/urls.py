
from django.urls import path

from denis.my_cv.views import MainPage, en_mode, de_mode

urlpatterns = [
    path('',MainPage.as_view(),name='index'),
    path('en/',en_mode,name='en'),
    path('de/',de_mode,name='de')
]