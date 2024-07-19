from rest_framework import throttling

import datetime


class EarlyMorningThrottle(throttling.BaseThrottle):
    """
    Restricts any requests between 4am and 6am.
    """
    def allow_request(self, request, view):
        now = datetime.datetime.now().hour
        if 4 <= now <= 6:
            return False
        return True
