from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
import app_auth.forms as auth_form


# Create your views here.

def index(request):
    if 'user_login' in request.session:
        return HttpResponseRedirect(reverse('web:dashboard'))

    html = 'web/auth/login.html'
    response = {
        'login_form': auth_form.LoginForm,
    }

    return render(request, html, response)


def index_dashboard(request):
    if 'user_login' not in request.session:
        return HttpResponseRedirect(reverse('web:index'))

    html = 'web/index.html'
    response = {
        'user_login': request.session['user_login']
    }
    return render(request, html, response)
