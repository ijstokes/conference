#!/bin/bash
pkill -f gunicorn
/usr/local/bin/gunicorn_django -w 3 &
