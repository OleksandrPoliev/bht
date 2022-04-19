from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
import requests
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from booksmain.forms import AddPostForm
from booksmain.models import BooksModel
from booksmain.serializers import bookserializer


class Main_View(ListView):
    model = BooksModel
    template_name = 'main.html'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            ser = request.POST['ser']
            search_logic=Q(title=ser,author=ser,book_language=ser,_connector=Q.OR)
            qs = BooksModel.objects.filter(search_logic)
            if len(qs)==0:
                success_message = 'Success! We dont fount  book'
                messages.success(request, success_message)
                return redirect('/')
            return render(request, 'main.html', {"ser": ser, 'qs': qs})
        else:
            return render(request, 'main.html')


class Add_Book(CreateView):
    model = BooksModel
    template_name = 'crud_books.html'
    form_class = AddPostForm

    def form_valid(self, form):
        form.save()
        success_message = 'Success! We just add new book'
        messages.success(self.request,success_message)
        return redirect('/')

class AuthorUpdateView(UpdateView):
    model = BooksModel
    template_name = 'updata_form.html'
    form_class = AddPostForm


    def form_valid(self, form):
        form.save()
        success_message = 'Success! We just Update book'
        messages.success(self.request, success_message)
        return redirect('/')

    def get_success_message(self):
        return self.success_message

class DeleteBookView(DeleteView):
    model = BooksModel
    success_url = "/"
    def get (self,*args,**kwargs):
        success_message = 'Success! We just delete book'
        messages.success(self.request, success_message)
        return self.delete(*args,**kwargs)
class GoogleBooks(ListView):

    template_name = 'import_book.html'
    model = BooksModel

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            googleapikey = ""
            google = request.POST['gooogle']
            params = {"q": google, 'key': googleapikey}
            r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=params)
            rq_to_google = r.json()
            data = rq_to_google['items'][1]['volumeInfo']
            BooksModel.objects.create(
                        title=data['title'],
                        author=data['authors'][0],
                        publish_date=str(data['publishedDate']),
                        ISBN=data['industryIdentifiers'][1]['identifier'],
                        num_pages=data['pageCount'],
                        book_img=data['imageLinks']['smallThumbnail'],
                        book_language=data['language'],
                    )
            return render(request, 'main.html')

class googleapi(APIView):
    def get(self,request):
        return Response({'title':'data'})



class BooksAPIView(viewsets.ModelViewSet):
    queryset = BooksModel.objects.all()
    serializer_class = bookserializer

    def retrieve(self, request, *args, **kwargs):
        params=kwargs
        search_logic = Q(title=params['pk'], author=params['pk'], book_language=params['pk'], _connector=Q.OR)
        qs = BooksModel.objects.filter(search_logic)
        serializer = bookserializer(qs, many=True)
        return Response(serializer.data)
