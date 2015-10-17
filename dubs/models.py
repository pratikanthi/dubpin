from django.db import models


class Video(models.Model):
    org_url  = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __unicode__():
            return self.title


class Dubs(models.Model):
    dubbed_title = models.CharField(max_length=255)
    dub_of = models.ForeignKey(Video)
    dub_file = models.FileField()
    dubbed_language = models.CharField(max_length=255)

    def __unicode__():
            return self.dubbed_title
