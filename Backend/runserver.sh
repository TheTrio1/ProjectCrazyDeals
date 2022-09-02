#! /usr/bin/bash 

my_app_path=$( dirname $(readlink -f "$0"))
source "$my_app_path/pyenv/Scripts/activate"

cd "$my_app_path/ShoppingCart"
python manage.py runserver 