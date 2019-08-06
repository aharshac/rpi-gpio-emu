This package provides placeholders to emulate the RPi.GPIO package functions on other devices.

The expected output from the functions "input", "getmode", "event_detected", and the delay time in seconds for "wait_for_edge" can be set using the "out" keyword argument.
The output for these functions is random otherwise, except for "wait_for_edge" which is 1 second.

The remaining functions "add_event_callback", "add_event_detect", "cleanup", "getmode", "gpio_function", "output", "remove_event_detect", "setmode", "setup", and "setwarnings" do nothing.

For examples and documentation of RPi.GPIO, visit http://sourceforge.net/p/raspberry-gpio-python/wiki/Home/

Project page: https://github.com/aharshac/rpi-gpio-emu

