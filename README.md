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
Master:
1. Connect to the team with project B
2. Add Friend
3. Add/edit User expertise
Frontend
1. Login button
Backend
1. Backend: latest status is showing different user's status
      
## Credit
Our lecturer: Ibu Maya Retno Ayu Setyautami S.Kom., M.Kom.
& the teaching assistant team, especially Kak Hafiyyan & Kak Teguh.

User Interface beautifully designed by Adyanissa F. Kirana and well-tailored by PPW F 01 Team.
