# TP2 - PPW F 01

visit us http://cs-career.herokuapp.com/

## About

### Status
[![pipeline status](https://gitlab.com/ppwf01/the-next-ling-in/badges/master/pipeline.svg)](https://gitlab.com/ppwf01/ling-in/commits/master)
[![coverage report](https://gitlab.com/ppwf01/the-next-ling-in/badges/master/coverage.svg)](https://gitlab.com/ppwf01/ling-in/commits/master)

### Anggota Kelompok
|   Nama                     | NPM        |
|----------------------------|------------|
| Adyanissa Farsya Kirana    | 1606918212 |
| Ario Seto                  | 1606917670 |
| Damar Wardoyo              | 1606918080 |
| Wisnu Pramadhitya Ramadhan | 1606918055 |

## Program

### Important
This program required python 3.6+ as it needs new python module _**secret**_ (for more information please 
read https://docs.python.org/3/library/secrets.html).

### Install
1. Clone the repository ```git clone https://gitlab.com/ppwf01/the-next-ling-in.git```
2. Check your python version, if you still have version below 3.6, please upgrade or install
new one on other environment, you can use pyenv (please read https://github.com/pyenv/pyenv). 
If you are a Windows user just install from python website.
3. Create python env with virtualenv or venv ```python3 -m venv env```
4. Activate the python env:
    - Linux/macOS ```source env/bin/activate```
    - Windows ```env\Script\activate.bat```
   To deactivate the env, run ```deactivate```
5. Install dependencies with pip ```pip3 install -r requirements.txt```
6. Setup the database: 
    
    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
    
   or you can run ```$ ./deplyoment.sh```
7. Run ```python3 manage.py collectstatic``` to collect static files (image, js, css, etc.)
8. Run server ```python3 manage.py runserver``` or you can run ```$ ./runserver.sh```
9. To run unittest and see the coverage report, run ```$ ./runtest.sh```
10. _**Note**_ that **Windows user** needs bash to run .sh script, please the .sh script for run manually

### TODO
1. Buka file app_web/templates/web/index.html, app_web/views.py, dan core/abstract/views.py
2. penjelasan file
    - web ini bersifat single page, yang beda page hanya edit profile
    - app_web adalah aplikasi yang menampilan website, selain itu, aplikasi bersifat api,
      hanya mengembalikan data, memodifikasi session atau httpredirect
    - file index.html adalah file yang ditampilkan di dashboard
    - file app_web/views.py adalah yang mengurus rendering
    - file core/abstract/views.py adalah file yang berisi fungsi response yang akan di wrap
      di fungsi yang mengembalikan data json atau tidak lain adalah fungsi sebagai api.
      Untuk menggunakan views ini baca docs string fungsi tsb atau liat contoh app_status.
    - untuk mengembalikan model ke jsonresponse, model perlu di serialize, yang intinya adalah
      metode merubah isi/fields model menjadi QueryDict/sederhananya Dict python. Karena json
      hanya bisa dikirim dalam bentuk dict, bukan mentahan model.
3. Lalu bagaimana menampilkan app kalian di single page web ini?
    1. pertama baca TODO di fungsi index_dashboard app_web/views.py.
    2. kita mulai dari membuat fungsi di views masing2 seperti yang dijelaskan di TODO
    3. pada intinya, membuat fungsi yang hanya mengedit isi dictionary yang akan di render.
       isi data dengan hal-hal yang akan ditampilkan di halaman dashboard.
       
        ```
        def function(request, data):
            data['query_friend'] = [1,2,3,4,5]
            ...
        ```
        
    4. untuk mempermudah, sebaiknya membuat fungsi-fungsi yang mengembalikan data-data yang
       diperlukan. Buatlah file di app masing, ```utils.py```. Untuk contoh, bisa dilihat di
       app_auth, app_status, app_web, app_friend.
       misal di ```utils.py``` app_friend
       
       ```
       def get_user_friends(user):
            return Friendship.objects.filter(user1=user)
       
       from app_auth import utils as auth_utils
       def insert_new_friend_to_database(user, user2npm):
            user2 = auth_utils.get_or_create_user(npm=user2npm)
            friendship = Friendship(user1=user, user2=user2)
            friendship.save()
            
            return friendship
       ```
       
       dan banyak lagi yang bisa dibuat untuk membantu views bekerja.
       Catatan: buatlah fungsi yang spesifik melakukan sesuatu.
    5. setelah membuat views di app masing2, buat kembali app_web/views.py bagian fungsi
       index_dashboard, dan panggilah fungsi tersebut, misal:
       
       ```
       from app_friend import views as friend_views 
       ...
       def index_dashboard(request):
           ...
           response = {
               ...
           }
           ...
           
           friend_views.fungsi_kalian(request, response)
           .
           .
           .
           return render()
           
       ```
       
    6. Backend Selesai jika tidak membuat api untuk ajax atau webservice
    7. Selanjutnya buka app_web/templates/web/index.html dan baca TODO dibawah,
       pada intinya buat file html di templates app masing2 dengan susunan directory
       templates/nama_app/file.html. Untuk contoh bisa di liat di app_status.
       jangan lupa include file html tersebut di index.html.
    8. Untuk css dan javascript bisa ditambahkan di file app_web/static/ base.js dan base.css
       atau buat di static app masing2 dan nanti bisa include di include di base.html. 
       tapi jika membuat di base, berilah comment. 
       untuk base.css sudah disiapkan masing2 tabnya dengan id #tab-namaapp.
    9. setiap app ditampilkan di tab masing2.
    10. SELESAI, buatlah unittest masing2, yang sepertinya unittestnya lebih mudah dan sangat
        pendek dari yang dilab karena ya ga ribet rendering2 dan check dia balikin apa,
        karena views nya hanya mengedit dictionary atau fungsi di utils yang
        mengembalikan query model. hehe ntaps kan.
      
## Credit
Our lecturer: Ibu Maya Retno Ayu Setyautami S.Kom., M.Kom.
& the teaching assistant team, especially Kak Hafiyyan & Kak Teguh.

User Interface beautifully designed by Adyanissa F. Kirana and well-tailored by PPW F 01 Team.
