from datetime import datetime

from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from model.message import Message
from repo.message_repo import MessageRepo
from repo.schedule_repo import ScheduleRepo
from utils import timestamp


def index(request):
    index_html_page = loader.get_template('../ui/viewerdashboard.html')
    context = {}
    if "login_user" in request.session:
        context["login_user"] = request.session["login_user"]
        context["username"] = request.session["login_user"].split("@")[0]
        scheduleRepo = ScheduleRepo()
        context["row"] = scheduleRepo.fetchSchedule(scheduleRepo.getId(context["login_user"]),(datetime.today().weekday()+2)%7)
    else:
        return redirect("/")
    return HttpResponse(index_html_page.render(context, request))


def chat(request):
    index_html_page = loader.get_template('../ui/viewerchat.html')
    context = {}
    if"login_user" in request.session:
        context["login_user"] = request.session["login_user"]
        context["username"] = request.session["login_user"].split("@")[0]
    else:
        return redirect("/")
    messageRepo = MessageRepo()
    context["messages"] = messageRepo.fetch_messages(context["login_user"])
    return HttpResponse(index_html_page.render(context, request))


def chat_submit(request):
    context = {}
    if "login_user" in request.session:
        context["login_user"] = request.session["login_user"]
        context["username"] = request.session["login_user"].split("@")[0]
    else:
        return redirect("/")
    if request.POST:
        message = Message()
        message.email = context["login_user"]
        message.content = request.POST["content"]
        message.sender = True
        created_at = datetime.now()
        message.created_at = created_at.strftime('%Y-%m-%d %H:%M:%S')
        # message.created_at = timestamp()
        messageRepo = MessageRepo()
        messageRepo.save(message)
        return redirect("/account/viewerdash/chat/")
