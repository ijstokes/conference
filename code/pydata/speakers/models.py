from django.db import models


class Speaker(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    organization = models.CharField(max_length=100, blank=True, null=True)
    image = models.FileField(upload_to='speakers', blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def name_org(self):
        if self.organization:
            return "{0} ({1})".format(self.name, self.organization)
        else:
            return self.name


class Presentation(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    speaker = models.ManyToManyField(Speaker)
    active = models.BooleanField(default=True)
    additional_info = models.TextField(blank=True)

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title

    def get_speakers(self):
        to_output = []
        for item in self.speaker.values('name'):
            to_output.append(item['name'])
        return to_output
