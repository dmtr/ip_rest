import logging

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

from ip_app.models import IpLogModel
from ip_app.serializers import IpLogSerializer

logger = logging.getLogger(__name__)


class IpList(generics.ListCreateAPIView):
    queryset = IpLogModel.objects.all()
    serializer_class = IpLogSerializer
    pagination_class = LimitOffsetPagination

    def post(self, request):
        ip = request.META.get('HTTP_X_REAL_IP')
        logger.debug('ip: %s', ip)
        serializer = IpLogSerializer(data={'ip': ip})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error('Real ip not found in headers')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
