from rest_framework import serializers
from .models import Bible_Book


class BibleBookSerializer(serializers.ModelSerializer):
    chapter_list = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Bible_Book
        fields = ["title", "chapters", "verses", "chapter_list"]

    def get_chapter_list(self, obj):
        try:
            return obj.get_chapters_as_list
        except:
            return None
