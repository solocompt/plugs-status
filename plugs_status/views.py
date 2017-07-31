from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions

from plugs_status import utils

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def api_status(request):
    """
    API is running
    """
    if utils.check_connection():
        return Response(data={'status': 'running'})
    else:
        return Response(data={'status': 'not running'})
