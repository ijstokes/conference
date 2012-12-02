import datetime
from django.db import models

# Create your models here
class Conference(models.Model):
    class Meta:
        verbose_name = _('Conference')
        verbose_name_plural = _('Conferences')

    name = models.CharField(max_length = 15)
    title = models.CharField(max_length = 200)
    location = models.CharField(max_length = 100)
    begin_date = models.DateTimeField('Start Date')
    end_date = models.DateTimeField('End Date')

    def __unicode__(self):
        return self.name

   
