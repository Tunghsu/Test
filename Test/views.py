# -*-coding:utf-8 -*-
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render_to_response
import datetime

def home(request):
    name= '啊啊'
    now= datetime.datetime.now()
    return render_to_response('main.html',locals())

def hello(request):
    template = '<html><body>It\'s the first Line'
    template2 = '</br> Haha {{name}} </body></html>'
    template = template + template2
    T = Template(template)
    return HttpResponse(T.render(Context({'name':'Dorian'})))
def current_datetime(request):
    now = datetime.datetime.now()
        
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)