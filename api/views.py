from django.views import View
import json
import requests
from django.shortcuts import render, redirect
from .models import StendupAuthors
from .models import StendupFiles
from .models import PodcastAuthors
from .models import PodcastFiles
from .models import BookAuthors
from .models import BookBooks
from .models import BookFiles


from django.http import JsonResponse
from rest_framework.response import Response

from server.const import TOKEN_TG

class Main(View):
    def get(self, request):
        return render(request, 'main.html')

class About(View):
    def get(self, request):
        return render(request, 'about.html')
      
# stendup
class StendupAuthorList(View):
    def get(self, request):
        stendup_authors = StendupAuthors.objects.all()
        return render(request, 'stendups/authors.html', {'stendup_authors':stendup_authors})
    
class StendupFileList(View):
    def get(self, request, id):
        if not StendupAuthors.objects.filter(id=id).exists():
            return redirect("/stendup")
        else:
            stendup_author = StendupAuthors.objects.get(id=id)
            file_list = StendupFiles.objects.filter(author_name=stendup_author)
            return render(request, 'stendups/files.html', {'stendup_author':stendup_author, 'file_list':file_list})
        
class StendupFile(View):
    def get(self, request):
        file_id = request.GET.get('file_id')
        chat_id = request.GET.get('chat_id')

        if StendupFiles.objects.filter(id=file_id).exists():
            stendup_file = StendupFiles.objects.get(id=file_id)
            tg_id = stendup_file.tg_id
            url = f"https://api.telegram.org/bot{TOKEN_TG}/sendDocument"

            response = requests.post(url, data={
                'chat_id': chat_id,
                'document': tg_id
            })

        return redirect("/")
    
#podcast
class PodcastAuthorList(View):
    def get(self, request):
        authors = PodcastAuthors.objects.all()
        return render(request, 'podcasts/authors.html', {'authors':authors})
    
class PodcastFileList(View):
    def get(self, request, id):
        if not PodcastAuthors.objects.filter(id=id).exists():
            return redirect("/podcast")
        else:
            author = PodcastAuthors.objects.get(id=id)
            file_list = PodcastFiles.objects.filter(author_name=author)
            return render(request, 'podcasts/files.html', {'author':author, 'file_list':file_list})
        
class PodcastFile(View):
    def get(self, request):
        file_id = request.GET.get('file_id')
        chat_id = request.GET.get('chat_id')

        if PodcastFiles.objects.filter(id=file_id).exists():
            podcast_file = PodcastFiles.objects.get(id=file_id)
            tg_id = podcast_file.tg_id
            url = f"https://api.telegram.org/bot{TOKEN_TG}/sendDocument"

            response = requests.post(url, data={
                'chat_id': chat_id,
                'document': tg_id
            })

        return redirect("/")
#books
class BookAuthorList(View):
    def get(self, request):
        authors = BookAuthors.objects.all()
        return render(request, 'books/authors.html', {'authors':authors})

class BookBookList(View):
    def get(self, request, id):
        if not BookAuthors.objects.filter(id=id).exists():
            return redirect("/book")
        else:
            author = BookAuthors.objects.get(id=id)
            book_list = BookBooks.objects.filter(author=author)
            return render(request, 'books/books.html', {'author':author, 'book_list':book_list})

class BookFileList(View):
    def get(self, request, id):
        if not BookBooks.objects.filter(id=id).exists():
            return redirect("/book")
        else:
            book = BookBooks.objects.get(id=id)
            file_list = BookFiles.objects.filter(book=book)

            if BookFiles.objects.filter(book=book).count() == 1:
                book_file = file_list[0]
                file_id = book_file.id
                return render(request, 'books/one_file_book.html', {'file_id':file_id})
            
            return render(request, 'books/files.html', {'book':book, 'file_list':file_list})
        
class BookFile(View):
    def get(self, request):
        file_id = request.GET.get('file_id')
        chat_id = request.GET.get('chat_id')

        if BookFiles.objects.filter(id=file_id).exists():
            book_file = BookFiles.objects.get(id=file_id)
            tg_id = book_file.tg_id
            url = f"https://api.telegram.org/bot{TOKEN_TG}/sendDocument"

            response = requests.post(url, data={
                'chat_id': chat_id,
                'document': tg_id
            })

        return redirect("/")