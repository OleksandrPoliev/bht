from rest_framework import serializers

from booksmain.models import BooksModel


class bookserializer (serializers.ModelSerializer):
    class Meta:
        model = BooksModel
        fields = '__all__'
