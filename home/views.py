import traceback

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.template import loader, RequestContext

# Create your views here.
from django.template.context_processors import csrf

from model.teacher import Teacher
from repo.user_repo import UserRepo
from service.account_service import AccountService
from service.forum_service import ForumService
from utils import password_hash


def index(request):
    index_html_page = loader.get_template('../ui/index.html')
    context = {"title": "Welcome to NCCS forum site!"}
    if "login_user" in request.session:
        context["login_user"] = request.session["login_user"]
    return HttpResponse(index_html_page.render(context, request))

def newuser(request):
    index_html_page = loader.get_template('../ui/newuser.html')
    context = {}
    return HttpResponse(index_html_page.render(context,request))

def signin(request):
    signup_html_page = loader.get_template('../ui/index.html')
    context = {}
    if request.method == 'POST':
        email = request.POST["txtEmail"]
        password = request.POST["txtPassword"]
        if email == "project@kys.com" and password == "12345678":
            request.session["login_user"] = email
            context["success_msg"] = "Login successful."
            return redirect("/account/admindash/index/")
        if not email:
            context["error_msg"] = "Invalid email or password."
        else:
            # ph = password_hash(password)
            account_service = AccountService()
            user = account_service.signin(email, password)
            if user is None:
                context["error_msg"] = "Invalid email or password."
            else:
                request.session["login_user"] = user
                context["success_msg"] = "Login successful."
                return redirect("/account/viewerdash/index/")
    return HttpResponse(signup_html_page.render(context, request))


def register(request):
    signup_html_page = loader.get_template('../ui/newuser.html')
    context = {}
    if request.method == 'POST':
        email = request.POST["email"]
        confirmation = request.POST["confirmation"]
        password =  request.POST["password"]
        cpassword = request.POST["cpassword"]
        print(confirmation)
        user = Teacher()
        user.email = email
        if not email:
            context["error_msg"] = "Invalid email."
        elif not password or len(str(password).strip(' ')) <= 7:
            context["error_msg"] = "Password must be 8 character long."
        elif not cpassword or cpassword != password:
            context["error_msg"] = "Password don't match."
        else:
            try:
                use_repo = UserRepo()
                if use_repo.register(email, confirmation, password_hash(password)):
                    request.session["login_user"] = user
                    context["success_msg"] = "Your account is verified"
                    return redirect("/")
                else:
                    context["error_msg"] = "Confirmation code didnt matched"
            except Exception:
                traceback.print_exc()
                context["error_msg"] = "Something went wrong"
    return HttpResponse(signup_html_page.render(context,request))


def about(request):
    return HttpResponse("This is about page.")


