import json, datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

import settings
from models import Artifact

@login_required
def index(request):
    return render(request, 'app/index.html', {})

@login_required
def artifacts(request):
    return render(request, 'app/artifacts.html', {})

@login_required
def data(request):
    response = {}
    url = request.GET.get('url')
    nonce = request.GET.get('nonce')
    if nonce:
        response['nonce'] = nonce
    query = request.META.get('QUERY_STRING')
    if query and not nonce:
        if query.startswith('url='):
            url = query[4:]
    if url:
        response['data'] = Artifact.get_by_url(url)
    return HttpResponse(json.dumps(response), content_type="application/json")

@login_required
def data_artifact(request):
    response = {}
    _key = request.GET.get('key')
    _format = request.GET.get('format', 'json')
    response = Artifact.get_by_key(_key)
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

