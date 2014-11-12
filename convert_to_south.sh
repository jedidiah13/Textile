#!/bin/sh

# grab the userdb.sqlite3 file from the last commit before it was removed
git checkout 5c4e0375b18fb9ac82fc231546f291c10fed24fc userdb.sqlite3
# remove the database from the git index (we don't want to commit it again)
git rm --cached userdb.sqlite3
# sync the db to create the migration table
python2 manage.py syncdb --noinput
# 'migrate' all of the apps using South
for i in login companion blog webstore frontend ; do
    # the reason this migration is fake is because we want South
    # to record the first migration in its table (so that the next
    # migrations don't fail), but if it actually runs the migration,
    # it will attempt to recreate the table, which will fail
    python2 manage.py migrate "$i" 0001 --fake
    # Now we actually take that DB and migrate it up to the latest version
    # (the above takes the db *with data* from an old commit and then tells
    #  South to record the initial migration fakely --- but any migrations
    #  made since that point would not have been applied to that old commit,
    #  so this applies all the 'real' migrations to THAT copy of the database)
    python2 manage.py migrate "$i"
done
