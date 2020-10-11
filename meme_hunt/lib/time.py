from datetime import datetime, time
from django.utils import timezone

class TimeConverter:

    @staticmethod
    def now():
        return timezone.now()

    @staticmethod
    def min(date):
        return timezone.make_aware(
                timezone.datetime.combine(date, time.min),
                timezone.get_current_timezone())

    @staticmethod
    def max(date):
        return timezone.make_aware(
                timezone.datetime.combine(date, time.max),
                timezone.get_current_timezone())
