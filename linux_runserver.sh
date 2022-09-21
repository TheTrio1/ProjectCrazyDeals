#! /usr/bin/bash 

my_app_path=$( dirname $(readlink -f "$0"))
source "$my_app_path/Backend/pyenv/bin/activate"

cd "$my_app_path/Backend/ShoppingCart"
python manage.py runserver 8590 
