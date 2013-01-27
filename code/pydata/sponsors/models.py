from django.db import models
from events.models import Conference


# Create your models here.
class SponsorLevel(models.Model):
    name = models.CharField(max_length=50)
    min_amount = models.IntegerField()
    description = models.TextField()
    conference = models.ForeignKey(Conference)
    small_logo_height = models.IntegerField()

    def __unicode__(self):
        return "{0} - {1}".format(self.name, self.conference)


class Sponsor(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    level = models.ForeignKey(SponsorLevel, related_name='sponsors')
    logo = models.FileField(upload_to='sponsor_logos')
    description = models.TextField()
    priority = models.IntegerField()

    def __unicode__(self):
        return self.name

    def id_tag(self):
        return "sponsor_{0}".format(self.id)
