git checkout .
git pull
.\dv3admin\python.exe manage.py makemigrations
.\dv3admin\python.exe manage.py migrate
.\dv3admin\Scripts\pip.exe install -r .\project\req_new.txt
.\project\vite-project.exe
