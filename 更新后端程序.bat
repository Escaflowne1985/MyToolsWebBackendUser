git checkout .
git pull
.\dv3admin\Scripts\pip.exe install -r req_new.txt
.\dv3admin\python.exe manage.py makemigrations
.\dv3admin\python.exe manage.py migrate
pause