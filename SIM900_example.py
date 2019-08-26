from SIM900 import *

sim = initialize()

print ping()

#### TEST OF FUNCTIONS

## MULTIPLEXER
# SETTING CHANNELS
set_channel(3)
print("CHANNEL: %s"%get_channel())
sleep(0.5)
set_channel(0)
print("CHANNEL: %s"%get_channel())
sleep(1)

# SETTING BYPASS
set_bypass(True)
print("bypass: %s"%get_bypass())
sleep(0.5)
set_bypass(False)
print("bypass: %s"%get_bypass())
sleep(1)

# SETTING BUFFER
set_buffer(True)
print("buffer: %s"%get_buffer())
sleep(0.5)
set_buffer(False)
print("buffer: %s"%get_buffer())
sleep(1)


## PREAMP
# SETTING GAIN
set_gain(2)
print("gain: %s"%get_gain())
sleep(0.5)
set_gain(1)
print("gain: %s"%get_gain())
sleep(1)

set_AC_coupling(True)
sleep(0.5)
set_AC_coupling(False)
sleep(1)

set_dif_input(True)
sleep(0.8)
set_dif_input(False)
sleep(1)

set_float_shield(False)
sleep(0.5)
set_float_shield(True)
sleep(1)


## VOLTMETER
print("Voltage on channel 4: %s"%get_voltage(4))
sleep(1)
print("All voltages: %s"%get_multivoltage())
sleep(2)
