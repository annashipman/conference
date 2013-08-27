from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from sessions.forms import SubmitSessionForm


def homepage_view(request):
    return HttpResponse("Please submit a session proposal below")

def propose_session(request):
    t = get_template('propose_session.html')
    c = Context()
    html = t.render(c)
    return HttpResponse(html)

def submit_session(request):
    if request.method == 'POST':
        form = SubmitSessionForm(request.POST)
    else:
        form = SubmitSessionForm()
    #No validation, returning original form etc for now
    return HttpResponseRedirect('/session/thanks/')

def session_thanks(request):
    return HttpResponse("Thanks")
