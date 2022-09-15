#!/bin/bash

set -e

exec python3 create_tables.py &
exec python3 forecasts.py