from django.db import models

class WordModel(models.Model):
    word=models.CharField(max_length=255)
    rank=models.IntegerField()

    def __str__(self):
        return self.word
