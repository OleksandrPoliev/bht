

from booksmain.models import BooksModel



from django import template

register = template.Library()

@register.simple_tag()
def getallbook():
    return BooksModel.objects.all()