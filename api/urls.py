from django.urls import path
from .views import Main
from .views import StendupAuthorList
from .views import StendupFileList
from .views import StendupFile
#
from .views import PodcastAuthorList
from .views import PodcastFileList
from .views import PodcastFile
#
from .views import BookAuthorList
from .views import BookBookList
from .views import BookFileList
from .views import BookFile

app_name = 'api'
urlpatterns = [
    path('', Main.as_view(), name='main'),
    #stendups
    path('stendup', StendupAuthorList.as_view(), name='stendup'),
    path('stendup/author/<int:id>', StendupFileList.as_view(), name='stendup_filelist'),
    path('stendup/file/', StendupFile.as_view(), name='stendup_file'),
    #podcasts
    path('podcast', PodcastAuthorList.as_view(), name='podcast'),
    path('podcast/author/<int:id>', PodcastFileList.as_view(), name='podcast_filelist'),
    path('podcast/file/', PodcastFile.as_view(), name='podcast_file'),
    #books
    path('book', BookAuthorList.as_view(), name='book'),
    path('book/author/<int:id>', BookBookList.as_view(), name='book_booklist'),
    path('book/book/<int:id>', BookFileList.as_view(), name='book_filelist'),
    path('book/file/', BookFile.as_view(), name='book_file'),
]