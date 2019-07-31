from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    index_html_page = loader.get_template('../ui/viewerdashboard.html')
    context = {}
    if "login_user" in request.session:
        context["login_user"] = request.session["login_user"]
    return HttpResponse(index_html_page.render(context, request))
