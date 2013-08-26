from django.http import HttpResponse

def homepage_view(request):
    return HttpResponse("Please submit a session proposal below")
