#!/bin/sh

# we selectively only update tables for non-Django-generated tables
# i.e., each of our features is itself a Django app, so we separately
# update the db for those. this prevents us from wiping out the users
# table on each run, for example. 

apps=(login companion blog webstore frontend);

python2 manage.py sqlclear "${apps[@]}" | python2 manage.py dbshell;
python2 manage.py sqlall "${apps[@]}" | python2 manage.py dbshell
