import visa
from time import sleep
def initialize():
	'''
	Main initialization of device. Please return this function to variable "sim"
	'''
	global sim
	rm = visa.ResourceManager()
	sim = rm.open_resource('ASRLCOM3::INSTR')
	sim.read_termination = "\r\n"
	sim.write_termination = "\r\n"
	sim.write("FLSH")
	return sim


def write(msg):
	sim.write(msg)

def read():
	data = sim.read()
	if data == "":
		print("/empty read/"),
		data = read()
	return data

def query(msg):
	write(msg)
	return read()

def ping(restart=0):
	'''
	Check whether device responds
	'''
	if restart:
		write("quit")
		write("SRST")
	try:
		data = query("ECHO? 'LOL'")
		if data == 'LOL':
			return "echo test successful."

		else:
			if not restart:
				print("echo test failed.Attempting Restart.")
				return ping(restart=1)
			else:
				raise IOError("Confusing device communication.")
	except:
		if not restart:
			print("echo test failed. Error. Attempting Restart.")
			return ping(restart=1)
		else:
			raise IOError("echo test failed. Error.")


def set_channel(channel):
	'''
	Select channel on multiplexer (1-8), 0 = not connected
	'''
	write("SNDT 8,'CHAN {}'".format(int(channel)))

def get_channel():
	'''
	Get selected channel.
	'''
	write("CONN 8,'quit'")
	val = query("CHAN?")
	write('quit')
	return int(val)

def set_bypass(value):
	'''
	Set bypass value of multiplexer (True/False) (1/0).
	'''
	write("CONN 8,'quit'")
	write("BPAS {}".format(int(value)))
	write('quit')

def get_bypass():
	'''
	Get bypass value of multiplexer.
	'''
	write("CONN 8,'quit'")
	val = query("BPAS?")
	write('quit')
	return bool(int(val))

def set_buffer(value):
	'''
	Set buffer value of multiplexer (True/False) (1/0).
	'''
	write("CONN 8,'quit'")
	write("BUFR {}".format(int(value)))
	write('quit')

def get_buffer():
	'''
	Get buffer value of multiplexer.
	'''
	write("CONN 8,'quit'")
	val = query("BUFR?")
	write('quit')
	return bool(int(val))

def set_gain(value): #SET GAIN AT PREAMP
	'''
	Set gain value of preamp.
	'''
	write("CONN 6,'quit'")
	values=[1,2,5,10,20,50,100]
	try:
		values.index(value)
		write("GAIN {}".format(int(value)))
	except ValueError:
		print("BAD GAIN SET, IGNORING")
	write("quit")
def get_gain():
	'''
	Get gain value of preamp.
	'''	
	write("CONN 6,'quit'")
	values=[1,2,5,10,20,50,100]
	valind = int(query("GAIN?"))
	write("quit")
	return values[valind-1]
def set_AC_coupling(value):
	'''
	Set AC coupling, if False, then DC coupling
	'''
	if value==True:
		write("SNDT 6,'COUP 1'")
	else:
		write("SNDT 6,'COUP 2'")
def set_dif_input(value): #SELECT A-B input, else absolute A input
	'''
	SELECT A-B input, else absolute A input
	'''
	if value==True:
		write("SNDT 6,'INPT 2'")
	else:
		write("SNDT 6,'INPT 1'")
def set_float_shield(value):
	'''
	Set floating shield voltage, else ground it
	'''
	if value==True:
		write("SNDT 6,'SHLD 1'")
	else:
		write("SNDT 6,'SHLD 2'")
# def set_autoscale(value):
# 	write("CONN 4,'quit'")
# 	if value==True:
		
# 	write("quit")
def get_voltage(channel):
	write("CONN 4,'quit'")
	try:
		return float(query("VOLT? {}".format(int(channel))))
	except:
		print("error getting voltage")
	finally:
		write("quit")
def flush_output():
	write("FLSH")
def reset():
	write("*RST")
def get_multivoltage():
	write("CONN 4,'quit'")
	data = []
	try:
		for channel in range(1,5):
			data.append(float(query("VOLT? {}".format(int(channel)))))
	except:
		print("error getting voltage.")
	finally:
		write("quit")
		return data
def get_queue_status():
	sleep(0.05)
	print("ReadQ @ port 4: %s"%query("NOUT? 4"))
	print("WriteQ @ port 4: %s"%query("NINP? 4"))


