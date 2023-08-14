from django.db import models
from ckeditor.fields import RichTextField


class SurveyLink(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='survey_images/')
    link = models.URLField()

    def __str__(self):
        return self.title

class Survey(models.Model):
    hero_title = models.CharField(max_length=255)
    hero_description = RichTextField()
    survey_links = models.ManyToManyField(SurveyLink)

    def __str__(self):
        return self.hero_title


