from django.db import models


# Create your models here.
class Bible_Book(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, unique=True)
    chapters = models.IntegerField(blank=False, null=False)
    verses = models.JSONField()

    @property
    def get_chapters_as_list(self):
        chapter_list = []

        for chapter in range(self.chapters):
            real_chapter = chapter + 1
            chapter_list.append(real_chapter)

        return chapter_list
