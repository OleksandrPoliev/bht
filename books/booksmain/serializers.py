from rest_framework import serializers

from .models import BooksModel


class bookserializer (serializers.ModelSerializer):
    class Meta:
        model = BooksModel
        fields = '__all__'
