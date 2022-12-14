from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render,get_object_or_404


def index(request):

    #return HttpResponse(template.render(context, request))
    return render(request,'strax_site/index.html')
