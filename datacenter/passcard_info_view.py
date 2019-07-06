from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.tools import get_duration, formatted_time, is_visit_long


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)[0]
    all_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit in all_visits:
        date = visit.entered_at
        duration_without_format = get_duration(visit)
        if duration_without_format is None:
            is_strange, duration = 'Находится в помещении', duration_without_format
        else:
            is_strange, duration = is_visit_long(duration_without_format), formatted_time(duration_without_format)

        visit_info = {
            "entered_at": date,
            "duration": duration,
            "is_strange": is_strange
        }
        this_passcard_visits.append(visit_info)

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
