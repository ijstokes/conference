from django.db import models

from pydata.settings    import CURRENT_CONF_ID
from events.models import Conference

class Sponsor(models.Model):
    name                = models.CharField(max_length=50)
    url                 = models.URLField()
    logo                = models.FileField(upload_to='sponsor_logos')
    description         = models.TextField()
    priority            = models.IntegerField()

    def __unicode__(self):
        return self.name

    def id_tag(self):
        return "sponsor_{0}".format(self.id)

class SponsorLevel(models.Model):
    name                = models.CharField(max_length=50)
    min_amount          = models.IntegerField()
    description         = models.TextField()
    conference          = models.ForeignKey(Conference, default=CURRENT_CONF_ID)
    sponsors            = models.ManyToManyField(Sponsor)
    small_logo_height   = models.IntegerField()

    def __unicode__(self):
        return "{0} - {1}".format(self.name, self.conference)
