from django.db import models
from django.db.models import Q

class WordModel(models.Model):
    word=models.CharField(max_length=255)
    frequency=models.IntegerField()

    def __str__(self):
        return self.word

class WordManager(models.Manager):
    def get_queryset(self):
        return WordQuerySet(self.model,using=self._db)

    def search(self,query):
        return self.get_queryset().all().search(query)

class WordQuerySet(models.query.QuerySet):
    def search(self,query):
        lookups=(Q(word__icontains=query))
        return self.filter(lookups).distinct()
