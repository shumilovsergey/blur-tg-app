from django.urls import path
from .views import Main
from .views import StendupAuthorList
from .views import StendupFileList


app_name = 'api'
urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('stendup', StendupAuthorList.as_view(), name='stendup'),
    path('stendup/author', StendupFileList.as_view(), name='stendup_filelist')
]