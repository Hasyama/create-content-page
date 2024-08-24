color 06
call ".venv\Scripts\activate.bat"
echo check what is going to be changed
python manage.py makemigrations --dry-run --verbosity 3
::preview for what is going to be changed
pause

python manage.py makemigrations
::will make a file to know what changed with previous file
pause

python manage.py migrate
::will actually apply the changes - update the database
pause