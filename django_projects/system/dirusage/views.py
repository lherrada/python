from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
import duroot

# Create your views here.

def dirinfo(request,dirpath):

    template = loader.get_template('dirusage/dirinfo.html')
    result=duroot.results(dirpath)
    context = RequestContext(request, {
        'result': result,
        'dirpath': dirpath,
    })
    return HttpResponse(template.render(context))

# Create your views here.
