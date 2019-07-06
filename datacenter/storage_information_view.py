# from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
from datacenter.tools import formatted_time, is_visit_long


def storage_information_view(request):
    unclosed_visits = Visit.objects.filter(leaved_at=None)
    time_now = timezone.now()
    non_closed_visits = []
    
    for visit in unclosed_visits:
        visit_time = time_now - visit.entered_at
        duration = formatted_time(visit_time)
        is_strange = is_visit_long(visit_time)

        visit_info = {
            "who_entered": visit.passcard,
            "entered_at": visit.entered_at,
            "duration": duration,
            "is_strange": is_strange 
        }
        non_closed_visits.append(visit_info)

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
