from django.db import models


class IpLogModel(models.Model):

    ip = models.GenericIPAddressField('Ip address')

    timestamp = models.DateTimeField()

    def __str__(self):
        return 'ip: {o.ip}, timestamp: {o.timestamp}'.format(o=self)
