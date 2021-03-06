from django.db import models
from django.contrib.auth.models import User

from pydata.settings import CURRENT_CONF_ID
from events.models import Conference

# Create your models here.
class NewsItem(models.Model):
    title       = models.CharField(max_length=75)
    date        = models.DateTimeField()
    content     = models.TextField()
    author      = models.ForeignKey(User, null=True, blank=True)
    publish     = models.BooleanField(default=False)
    conference  = models.ForeignKey(Conference, default=CURRENT_CONF_ID)

    class Meta:
        ordering = ['-date']

    def __unicode__(self):
        return self.title
