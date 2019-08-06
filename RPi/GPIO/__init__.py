"""
Copyright (c) 2019 Harsha Alva

Based on original work "RPi.GPIO" by Ben Croston


Copyright (c) 2012-2018 Ben Croston

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import random
import time

VERSION = '0.6.5'


BOARD = 10
BCM = 11

PWM = 43

HIGH = 1
LOW = 0
OUT = 0
IN = 1

HARD_PWM = 9
SERIAL = 40
SPI = 41
I2C = 42
UNKNOWN = -1

PUD_OFF = 0
PUD_DOWN = 1
PUD_UP = 2

RISING = 1
FALLING = 2
BOTH = 3


def __randomBool():
    return random.uniform(0, 1) > 0.5


def cleanup(*args, **kwargs):
    pass


def setup(*args, **kwargs):
    pass


def output(*args):
    pass


def input(*args, **kwargs):
    if 'out' in kwargs:
        return kwargs.get("out")
    return HIGH if __randomBool() else LOW


def setmode(*args):
    pass


def getmode(**kwargs):
    if 'out' in kwargs:
        return kwargs.get("out")
    return BOARD if __randomBool() else BCM

def add_event_callback(*args, **kwargs):
    pass


def add_event_detect(*args, **kwargs):
    pass


def remove_event_detect(*args, **kwargs):
    pass


def event_detected(*args, **kwargs):
    if 'out' in kwargs:
        return kwargs.get("out")
    return True


def wait_for_edge(*args, **kwargs):
    wait = 1
    if 'out' in kwargs:
        wait = int(kwargs.get("out"))
    time.sleep(wait)


def gpio_function(*args):
    pass


def setwarnings(flag):
    pass
