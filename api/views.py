from django.views import View
from django.shortcuts import render, redirect
from .models import StendupAuthors
from django.http import JsonResponse

class Main(View):
    def get(self, request):
        return render(request, 'main.html')
      
class StendupAuthorList(View):
    def get(self, request):
        stendup_authors = StendupAuthors.objects.all()
        return render(request, 'stendups/authors.html', {'stendup_authors':stendup_authors})
    
class StendupFileList(View):
    def get(self, request, id):
        # stendup_author_id = request['stendup_author_id']
        print(id)
        return render(request, 'stendups/files.html')