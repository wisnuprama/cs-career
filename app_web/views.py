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

    '''
    TODO
    
    buatlah sebuah fungsi untuk membawa data apa saja
    yang akan dipasang di html dengan mengedit response.
    
    Fungsi tersebut bisa dibuat di views masing2 app yang nanti
    di import kesini dan dipanggil di index_dashboard
    
    misal status:
    buat fungsi di views.py app_status
    def fungsi(request, response)
        response['nama'] = 'hehe'
        
    setelah fungsi dibuat, buka views di app_web.
    import method tsb yng tadi dibuat.
    panggil fungsi tsb di index_dashboard dibawah variable response
    
    edit html di index.html di app_web/templates/web/index.html
    isi sesuai tab masing2.
    
    jika memang page yang kamu buat adalah page berbeda dari dashboard,
    boleh buat sendiri seperti views biasa yang dikerjakan di lab karena page
    berbeda.
    '''


    return render(request, html, response)
