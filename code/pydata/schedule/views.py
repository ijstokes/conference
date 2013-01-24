from schedule.models import Track, TimeSlot, SectionDay, Section
from django.shortcuts import render_to_response
from utilities.utilities import get_base_out_vars
# Create your views here.


def show_schedule_sectionDay(request, **kwargs):
    sectionDay = kwargs['sectionday']
    output = get_base_out_vars(request, **kwargs)
    output['debug'] = sectionDay
    output['sectionDay'] = SectionDay.objects.get(pk=sectionDay)
    output['tracks'] = set(Track.objects.filter(scheduleditem__timeSlot__sectionDay__exact=sectionDay))
    output['slots'] = TimeSlot.objects.filter(sectionDay__exact=sectionDay)
    return render_to_response('sv2013/templates/schedule/schedule.html', output)


def show_schedule_all(request, **kwargs):
    output = get_base_out_vars(request, **kwargs)
    output['sections'] = Section.objects.all()
    return render_to_response('sv2013/templates/schedule/full_schedule.html', output)
