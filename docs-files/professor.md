# Teacher User Guide

You can check here as a teacher what you can do on this application

## Adding new users

- You can add a user using the file _users.csv_ opening in a Sheets application such as Excel or as text using csv formmat, defining username, password and user type.
##### You can choose any of the following User Types

| User Type     | Description   |
| ------------- |:-------------:|
| admin         | User that can do anything such as teachers |
| aluno         | user that have the permission to summit files to challenges     |


```log
bruno,admin,admin
ciclano,pa,aluno
fulano,pe,aluno
```

- For the changes to be applied you need to run  _adduser.py_ python file with

    **``python3 adduser.py``**

> The output should look like this

```console
$ python3 adduser.py
fulano
ciclano

```

## Adding new challenges

You can add a new challenge to the application you can use sqlite3 or creating a .sql file with the content

#### Using sqlite3

**``sqlite3 quiz.db``**

```mysql
Insert into QUIZ(numb, release, expire, problem, tests, results, diagnosis) values ([ 'numero' ], ['start-date'],['due-date'],['problem example'],['input sample'],['expected output'],['diagnostic']);
```




