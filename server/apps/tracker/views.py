# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def register(request, template='register.html'):
    return render_to_response(template, RequestContext(request, {}))
