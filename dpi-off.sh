#!/bin/bash

cleanup() {
    if kill -0 $PID1 2>/dev/null; then
        kill $PID1
    fi
    if kill -0 $PID2 2>/dev/null; then
        kill $PID2
    fi
    exit
}

trap cleanup SIGINT SIGTERM

# Enter the command to start the first process.
# Example of running spoofdpi:
./spoofdpi &
PID1=$!

# Enter command to start two process:
./Telegram &
PID2=$!

wait -n $PID1 $PID2

cleanup
