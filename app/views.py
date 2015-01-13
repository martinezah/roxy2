import json, datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

import settings
from models import Artifact

def index(request):
    return redirect('artifacts')

@login_required
def artifacts(request):
    return render(request, 'app/artifacts.html', {})

@login_required
def data_artifact(request):
    response = {}
    _key = request.GET.get('key')
    _format = request.GET.get('format', 'json')
    response = Artifact.get(_key)
    if _format == 'html':
        timestamp = response.get('timestamp')
        if timestamp:
            response['timestamp'] = datetime.datetime.fromtimestamp(timestamp/1000.0)
        imported = response.get('imported')
        if imported:
            response['imported'] = datetime.datetime.fromtimestamp(imported/1000.0)
        return render(request, 'app/artifact.html', response)
    else:
        return HttpResponse(json.dumps(response), content_type="application/json")

