import logging
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from ip_app.models import IpLogModel
from ip_app.serializers import IpLogSerializer

logger = logging.getLogger(__name__)


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def ip_list(request):
    """
    List all log records, or create a new one.
    """
    if request.method == 'GET':
        records = IpLogModel.objects.all()
        serializer = IpLogSerializer(records, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        ip = request.META['HTTP_X_REAL_IP']
        logger.debug('ip: %s', ip)
        serializer = IpLogSerializer(data={'ip': ip})
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
