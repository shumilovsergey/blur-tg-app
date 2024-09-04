from django.urls import path
from .views import Main
from .views import Out
from .views import StendupAuthorsList



app_name = 'api'
urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('stendup', StendupAuthorsList.as_view(), name='stendup')
]