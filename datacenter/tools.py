def get_duration(visit):
    entered_at = visit.entered_at
    leaved_at = visit.leaved_at

    if leaved_at is None:
        return
    
    duration = leaved_at - entered_at

    return duration


def formatted_time(duration):
    total_seconds_of_visit = duration.total_seconds()

    hours_of_visit = int(total_seconds_of_visit // 3600)
    minutes_of_visit = int((total_seconds_of_visit % 3600) // 60)
    seconds_of_visit = int(total_seconds_of_visit % 60)
    format_time = '{}:{}:{}'.format(hours_of_visit, minutes_of_visit, seconds_of_visit)

    return format_time


def is_visit_long(duration, minutes=60):
    total_minutes_of_visit = duration.total_seconds() // 60
    return total_minutes_of_visit > minutes