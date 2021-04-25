@ECHO OFF
start cmd.exe /C "python manage.py runserver && cd C:\User\ChikU\Documents\skp"
start C:\"Program Files"\Google\Chrome\Application\chrome.exe "http://127.0.0.1:8000/"