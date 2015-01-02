import json

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

import settings

@api_view(['GET'])
def index(request):
    response = {"version":settings.ROXY_VERSION}
    return Response(response)
