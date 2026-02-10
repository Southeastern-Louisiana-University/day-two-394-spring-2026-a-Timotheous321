@echo off

docker build -t lab1-watcher .

docker run --rm -it ^
  -v %cd%\logs:/app/logs ^
  lab1-watcher
