from django.db import models
from speakers.models import Presentation
from datetime import timedelta


class Section(models.Model):
    name = models.CharField(max_length=30)
    start_day = models.DateField()
    end_day = models.DateField()

    def __unicode__(self):
        return self.name


class SectionDay(models.Model):
    section = models.ForeignKey(Section)
    day = models.IntegerField()

    def __unicode__(self):
        return self.get_name()

    def get_name(self):
        return "{0} - Day {1}".format(self.section.name, self.day)

    def get_date(self):
        day_diff = self.day - 1
        date = self.section.start_day + timedelta(days=day_diff)
        return date


class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    sectionDay = models.ForeignKey(SectionDay)

    def __unicode__(self):
        return self.name()

    def name(self):
        time_format = '%I:%M'
        day = self.sectionDay.get_name()
        start_time = self.start_time.strftime(time_format)
        end_time = self.end_time.strftime(time_format)
        return '{0} {1} - {2}'.format(day, start_time, end_time)


class RoomUseType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=50)
    useType = models.ForeignKey(RoomUseType)
    capacity = models.IntegerField(blank=True, null=True)
    map_image = models.FileField(upload_to='rooms', blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class ScheduledItemType(models.Model):
    name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name


class ScheduledItem(models.Model):
    itemType = models.ForeignKey(ScheduledItemType)
    timeSlot = models.ForeignKey(TimeSlot)
    num_slots = models.IntegerField(default=1)
    track = models.ForeignKey(Track, blank=True, null=True)
    room = models.ForeignKey(Room, blank=True, null=True)
    presentation = models.ForeignKey(Presentation, blank=True, null=True)

    def __unicode__(self):
        if not self.presentation:
            return self.itemType.name + " " + self.timeSlot.name()
        return self.presentation.title
