from django.contrib import admin
from .models import StendupAuthors
from .models import StendupFiles
from .models import PodcastAuthors
from .models import PodcastFiles
from .models import BookAuthors
from .models import BookBooks
from .models import BookFiles


admin.site.register(StendupAuthors)
admin.site.register(StendupFiles)
admin.site.register(PodcastAuthors)
admin.site.register(PodcastFiles)
admin.site.register(BookAuthors)
admin.site.register(BookBooks)
admin.site.register(BookFiles)


