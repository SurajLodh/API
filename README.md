Microsoft Windows [Version 10.0.19042.870]
(c) 2020 Microsoft Corporation. All rights reserved.

C:\Users\suraj\Downloads\practice\Project_final>django-admin startproject API

C:\Users\suraj\Downloads\practice\Project_final>cd API

C:\Users\suraj\Downloads\practice\Project_final\API>python -m venv venv

C:\Users\suraj\Downloads\practice\Project_final\API>venv\scripts\activate.bat


(venv) C:\Users\suraj\Downloads\practice\Project_final\API>pip install django
Collecting django
  Using cached Django-3.1.7-py3-none-any.whl (7.8 MB)
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.1-py3-none-any.whl (42 kB)
Collecting asgiref<4,>=3.2.10
  Using cached asgiref-3.3.1-py3-none-any.whl (19 kB)
Collecting pytz
  Using cached pytz-2021.1-py2.py3-none-any.whl (510 kB)
Installing collected packages: sqlparse, asgiref, pytz, django
Successfully installed asgiref-3.3.1 django-3.1.7 pytz-2021.1 sqlparse-0.4.1
WARNING: You are using pip version 20.1.1; however, version 21.0.1 is available.
You should consider upgrading via the 'c:\users\suraj\downloads\practice\project_final\api\venv\scripts\python.exe -m pip install --upgrade pip' command.


(venv) C:\Users\suraj\Downloads\practice\Project_final\API>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
April 03, 2021 - 08:45:56
Django version 3.1.7, using settings 'API.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[03/Apr/2021 08:46:12] "GET / HTTP/1.1" 200 16351
[03/Apr/2021 08:46:12] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[03/Apr/2021 08:46:12] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
[03/Apr/2021 08:46:12] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
[03/Apr/2021 08:46:12] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
Not Found: /favicon.ico
[03/Apr/2021 08:46:13] "GET /favicon.ico HTTP/1.1" 404 1969



-------------------------------Creating app1 which is based on Rest API-------------------------------------

(venv) C:\Users\suraj\Downloads\practice\Project_final\API>pip install djangorestframework
Collecting djangorestframework
  Using cached djangorestframework-3.12.4-py3-none-any.whl (957 kB)
Requirement already satisfied: django>=2.2 in c:\users\suraj\downloads\practice\project_final\api\venv\lib\site-packages (from djangorestframework) (3.1.7)
Requirement already satisfied: pytz in c:\users\suraj\downloads\practice\project_final\api\venv\lib\site-packages (from django>=2.2->djangorestframework) (2021.1)
Requirement already satisfied: sqlparse>=0.2.2 in c:\users\suraj\downloads\practice\project_final\api\venv\lib\site-packages (from django>=2.2->djangorestframework) (0.4.1)
Requirement already satisfied: asgiref<4,>=3.2.10 in c:\users\suraj\downloads\practice\project_final\api\venv\lib\site-packages (from django>=2.2->djangorestframework) (3.3.1)
Installing collected packages: djangorestframework
Successfully installed djangorestframework-3.12.4
WARNING: You are using pip version 20.1.1; however, version 21.0.1 is available.
You should consider upgrading via the 'c:\users\suraj\downloads\practice\project_final\api\venv\scripts\python.exe -m pip install --upgrade pip' command.

(venv) C:\Users\suraj\Downloads\practice\Project_final\API>pip install django-rest-knox
Collecting django-rest-knox
  Using cached django_rest_knox-4.1.0-py3-none-any.whl (13 kB)
Requirement already satisfied: djangorestframework in c:\users\suraj\downloads\practice\project_final\api\venv\lib\site-packages (from django-rest-knox) (3.12.4)
Collecting cryptography
  Using cached cryptography-3.4.7-cp36-abi3-win_amd64.whl (1.6 MB)
Requirement already satisfied: django in c:\users\suraj\downloads\practice\project_final\api\venv\lib\site-packages (from django-rest-knox) (3.1.7)
Collecting cffi>=1.12
  Using cached cffi-1.14.5-cp37-cp37m-win_amd64.whl (178 kB)
Requirement already satisfied: pytz in c:\users\suraj\downloads\practice\project_final\api\venv\lib\site-packages (from django->django-rest-knox) (2021.1)
Requirement already satisfied: asgiref<4,>=3.2.10 in c:\users\suraj\downloads\practice\project_final\api\venv\lib\site-packages (from django->django-rest-knox) (3.3.1)
Requirement already satisfied: sqlparse>=0.2.2 in c:\users\suraj\downloads\practice\project_final\api\venv\lib\site-packages (from django->django-rest-knox) (0.4.1)
Collecting pycparser
  Using cached pycparser-2.20-py2.py3-none-any.whl (112 kB)
Installing collected packages: pycparser, cffi, cryptography, django-rest-knox
Successfully installed cffi-1.14.5 cryptography-3.4.7 django-rest-knox-4.1.0 pycparser-2.20
WARNING: You are using pip version 20.1.1; however, version 21.0.1 is available.
You should consider upgrading via the 'c:\users\suraj\downloads\practice\project_final\api\venv\scripts\python.exe -m pip install --upgrade pip' command.

(venv) C:\Users\suraj\Downloads\practice\Project_final\API>pip install django-filter
Collecting django-filter
  Using cached django_filter-2.4.0-py3-none-any.whl (73 kB)
Requirement already satisfied: Django>=2.2 in c:\users\suraj\downloads\practice\project_final\api\venv\lib\site-packages (from django-filter) (3.1.7)
Requirement already satisfied: pytz in c:\users\suraj\downloads\practice\project_final\api\venv\lib\site-packages (from Django>=2.2->django-filter) (2021.1)
Requirement already satisfied: asgiref<4,>=3.2.10 in c:\users\suraj\downloads\practice\project_final\api\venv\lib\site-packages (from Django>=2.2->django-filter) (3.3.1)
Requirement already satisfied: sqlparse>=0.2.2 in c:\users\suraj\downloads\practice\project_final\api\venv\lib\site-packages (from Django>=2.2->django-filter) (0.4.1)
Installing collected packages: django-filter
Successfully installed django-filter-2.4.0
WARNING: You are using pip version 20.1.1; however, version 21.0.1 is available.
You should consider upgrading via the 'c:\users\suraj\downloads\practice\project_final\api\venv\scripts\python.exe -m pip install --upgrade pip' command.

make changes into >> API >> settings 
add into INSTALLED_APPS = [
    '...................',
    'rest_framework',
    'django_filters'
]
and 

STATIC_URL = '/static/'

(venv) PS C:\Users\suraj\Downloads\practice\Project_final\API> python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
April 03, 2021 - 14:11:26
Django version 3.1.7, using settings 'API.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.













