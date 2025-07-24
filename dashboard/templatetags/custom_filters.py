
from django import template
from datetime import datetime, timedelta

register = template.Library()

@register.filter
def add_hours(time_obj, hours):
    """Add hours to a time object"""
    if isinstance(time_obj, datetime.time):
        # Convert time to datetime for calculation
        today = datetime.today()
        dt = datetime.combine(today, time_obj)
        dt += timedelta(hours=int(hours))
        return dt.time()
    return time_obj

@register.filter
def mul(value, arg):
    """Multiply the value by the argument"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0