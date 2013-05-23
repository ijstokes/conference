#!/bin/bash
/usr/local/bin/gunicorn_django -w 3 --bind 0.0.0.0:8013 &
