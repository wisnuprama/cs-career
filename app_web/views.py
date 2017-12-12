from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from app_auth import forms as auth_form
from app_status import views as status_views
from app_friend import views as friend_views
from app_profile import views as profile_views
from core import strings


# Create your views here.

def index(request):
    if 'user_login' in request.session:
        return HttpResponseRedirect(reverse('web:dashboard'))

    html = 'auth/login.html'
    response = {
        'TITLE': strings.TITLE,
        'page_title': 'Welcome',
        'YEAR': strings.YEAR,
        'login_form': auth_form.LoginForm,
    }

    return render(request, html, response)


def index_dashboard(request):
    if 'user_login' not in request.session:
        return HttpResponseRedirect(reverse('web:index'))

    html = 'web/index.html'
    response = {
        'TITLE': strings.TITLE,
        'page_title': 'Dashboard',
        'YEAR': strings.YEAR,
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
    boleh buat sendiri seperti views biasa yang dikerjakan di lab. hal itu karena page
    berbeda dari dashboard.
    
    pembuatan fungsi seperti ini karena aktivitas user yang ditempatkan di
    satu page sehingga hal yang diperlukan di render bersamaan dan masing-masing
    aktifitas dipisahkan dalam tab-tab.
    
    contoh ada dibawah ini:
        - fungsi tidak mengembalikan apa2, dia hanya mengedit dictionary response
          masukan data ke dictionary tersebut
    '''
    status_views.index(request, response)
    friend_views.index(request, response)
    profile_views.index(request, response)

    print(request.session['user_login'])

    return render(request, html, response)
