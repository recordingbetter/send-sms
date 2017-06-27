from django.db import models


class SendSMS(models.Model):
    TYPE = (
        ('sms', 'SMS'),
        ('lsm', 'LMS'),
        )
    sender = models.CharField(max_length=15)
    receiver = models.CharField(max_length=15)
    type = models.CharField(max_length=10, choices=TYPE)
    text = models.TextField()
    result = models.CharField(max_length=50, null=True, blank=True)
