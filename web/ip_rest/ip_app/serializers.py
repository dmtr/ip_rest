from rest_framework import serializers
from ip_app.models import IpLogModel


class IpLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpLogModel
        fields = ('ip', 'timestamp')
