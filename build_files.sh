echo
pip install -r requirements.txt
echo

echo
python3.9 manage.py collectstatic --noinput --clear
echo


echo
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput
echo