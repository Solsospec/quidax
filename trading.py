import threading
from time import time, sleep
import requests
import datetime
import pytz
import math




# Shared stop event
stop_event = threading.Event()


# This thread will listen for "stop" input
def listen_for_stop():
    while not stop_event.is_set():
        user_input = input("Type 'stop' to quit:\n")
        if user_input.lower() == 'stop':
            stop_event.set()


# Simulations
def app1():
    print("App 1 starting...")
    while not stop_event.is_set():
        print("App 1 working...")
        sleep(1)
        break  # Break after one iteration
    print("App 1 done.")


def app2():
    print("App 2 starting...")
    while not stop_event.is_set():
        print("App 2 working...")
        sleep(1)
        break
    print("App 2 done.")


def app3():
    print("App 3 starting...")
    while not stop_event.is_set():
        print("App 3 working...")
        sleep(1)
        break
    print("App 3 done.")


def app4():
    print("App 4 starting...")
    while not stop_event.is_set():
        print("App 4 working...")
        sleep(1)
        break
    print("App 4 done.")


# Main controller
def main_loop():
    while not stop_event.is_set():
        app1()
        if stop_event.is_set(): break
        app2()
        if stop_event.is_set(): break
        app3()
        if stop_event.is_set(): break
        app4()
        if stop_event.is_set(): break
        print("Loop cycle complete. Restarting...\n")
        sleep(1)


if __name__ == "__main__":
    # Start the stop-listener thread
    stop_thread = threading.Thread(target=listen_for_stop, daemon=True)
    stop_thread.start()

    # Run the main app loop
    main_loop()

    print("Shutdown complete.")