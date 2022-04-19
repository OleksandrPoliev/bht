
from django.urls import path , include


from rest_framework import routers


from .views import Main_View, Add_Book, AuthorUpdateView, GoogleBooks, BooksAPIView, DeleteBookView

app_name = "mainapp"

router=routers.SimpleRouter()
router.register(r'books',BooksAPIView, basename='books')

urlpatterns = [
    path('', Main_View.as_view(),name='home'),
    path('add/',Add_Book.as_view(),name='add'),
    path('updata/<int:pk>',AuthorUpdateView.as_view(),name='updata'),
    path('google',GoogleBooks.as_view(),name='import'),
    path('api/books',include(router.urls)),
    path('delete/<int:pk>',DeleteBookView.as_view(),name='del')
]

