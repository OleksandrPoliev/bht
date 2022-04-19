from django.contrib import admin

from booksmain.models import BooksModel
class Admin_BooksModel(admin.ModelAdmin) :
    list_display = ('id','title','author','publish_date','book_language')
    list_display_links = ('id','publish_date')
    search_fields=('title','author','publish_date','book_language')




admin.site.register(BooksModel,Admin_BooksModel)
# Register your models here.
