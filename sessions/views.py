from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from sessions.forms import SubmitSessionForm
from sessions.models import Session

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
    if form.is_valid():
        form_data = form.cleaned_data
        title = form_data['title']

        defined_title = get_title(title)
        session = Session.objects.create(
          title = defined_title
    )
    #No validation, returning original form etc for now
    return HttpResponseRedirect('/session/thanks/')

def session_thanks(request):
    return HttpResponse("Thanks")

def get_title(title):
    if (title == "Anna"):
      return "Anna"
    return "Shipman"
