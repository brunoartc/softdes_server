# Dev User Guide

## Dependencies
- sqlite3 system wide application
```console
$ sudo apt -y install sqlite3
```

- install python modules
```console
$ pip3 install -r requirments.txt
```


## Setting up database

```bash
sqlite3 quiz.db < quiz.sql
```

## Starting up server

```bash
python3 softdes.py
```

And open to http://0.0.0.0


