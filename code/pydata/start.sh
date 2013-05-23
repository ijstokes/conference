#!/bin/bash

set -e
LOGFILE=error.log
NUM_WORKERS=3
BIND=127.0.0.1:8013
# user/group to run as
exec gunicorn_django -w $NUM_WORKERS \
	--bind=127.0.0.1:8013 \
    --log-level=debug \
	--log-file=error.log 2>> error.log &
