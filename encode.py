import numpy as np #instalado
import struct
import sys
import wave 

def is_valid(input):
	if input == '-d':
		return True
	elif input == '-c':
		return True
	elif input == '-h':
		return True
	return False


diff_bool = run_bool = huff_bool = False

#tratando os argumentos de entrada
wave_file = wave.open(sys.argv[-2], 'r')
# wave_raw_data = open(sys.argv[-2], 'r')
argc = len(sys.argv)


if argc <= 3:
	print 'Poucos argumentos\nFormato:\npython encode.py -d -h -c <audio.wav> <saida.bin>'
	exit() # se estiver errado interrompe o codigo
compressions = argc - 3

#verifica metodos
for i in range(1, 1+compressions):
	if is_valid(sys.argv[i]) == False:
		print 'Entrada incorreta\nFormato:\npython encode.py -d -h -c <audio.wav> <saida.bin>'
		exit()

#lendo os arquivos
chans = wave_file.getnchannels()
samps = wave_file.getnframes()

s = wave_file.readframes(samps)
wave_file.close()

unpstr = '<{0}h'.format(samps*chans)
x = list(struct.unpack(unpstr, s))

left_channel = x[0::chans]
right_channel = x[1::chans]


