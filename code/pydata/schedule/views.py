from schedule.models import Track, TimeSlot, SectionDay, Section
from django.shortcuts import render_to_response
from utilities.utilities import get_base_out_vars
# Create your views here.


def show_schedule_sectionDay(request, **kwargs):
    conference              = kwargs['conference']
    sectionDay              = SectionDay.objects.get(day=kwargs['sectionday'], conference__name=conference)
    output                  = get_base_out_vars(request, **kwargs)
    output['sectionDay']    = sectionDay
    output['tracks']        = set(Track.objects.filter(scheduleditem__timeSlot__sectionDay__exact=sectionDay.id))
    output['slots']         = TimeSlot.objects.filter(sectionDay__exact=sectionDay.id)
    return render_to_response('%s/templates/schedule/schedule.html' % conference, output)


def show_schedule_all(request, **kwargs):
    conference              = kwargs['conference']
    output                  = get_base_out_vars(request, **kwargs)
    output['sections']      = set(Section.objects.filter(sectionday__timeslot__scheduleditem__presentation__conference__name=conference))
    return render_to_response('%s/templates/schedule/full_schedule.html' % conference, output)
