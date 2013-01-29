from django.db import models
from django.contrib import User


# Create your models here.
class NewsItem(models.model):
	title = models.CharField(max_length=50)
	date = models.DateField()
	content = models.TextField()
	author = models.ForeignKey(User, null=True, blank=True)
	publish = models.BooleanField(default=False)

	class Meta:
		ordering = ['-date']

	def __unicode__(self):
		return self.title

