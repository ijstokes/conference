#!/bin/bash

set -e
LOGFILE=error.log
NUM_WORKERS=3
BIND=50.56.188.141.1:8000
# user/group to run as
exec gunicorn_django -w $NUM_WORKERS \
	--bind=50.56.188.141:8000 \
    --log-level=debug \
	--log-file=error.log 2>> error.log &
