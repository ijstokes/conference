#!/bin/bash
/usr/local/bin/gunicorn_django --bind=0.0.0.0:8008 &
