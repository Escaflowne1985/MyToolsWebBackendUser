.\dv3admin\Scripts\pip.exe install -r req_new.txt
.\dv3admin\python.exe manage.py makemigrations
.\dv3admin\python.exe manage.py migrate
.\dv3admin\python.exe manage.py runserver 0.0.0.0:9000
pause