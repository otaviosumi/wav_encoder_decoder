import numpy as np #instalado
import struct
import sys
import wave 
import pickle

diff_bool = run_bool = huff_bool = False

def is_valid(input):
	if input == '-d':
		diff_bool = True
		return True
	elif input == '-c':
		run_bool = True
		return True
	elif input == '-h':
		huff_bool = True
		return True
	return False

def get_diffs(input_channels, samps, chans):
	diff_channels_out = np.empty((chans, samps), dtype=int)
	for i in range(chans):
		diff_channels_out[i][0] = input_channels[i][0]
		for ii in range(1, samps):
			diff_channels_out[i][ii] = input_channels[i][ii] - input_channels[i][ii - 1]
	return diff_channels_out

def get_de_diffs(input_channels, samps, chans):
	diff_channels_out = np.empty((chans, samps), dtype=int)
	for i in range(chans):
		diff_channels_out[i][0] = input_channels[i][0]
		for ii in range(1, samps):
			diff_channels_out[i][ii] = input_channels[i][ii] + diff_channels_out[i][ii - 1]
	return diff_channels_out


#tratando os argumentos de entrada
wave_file = wave.open(sys.argv[-2], 'r')
output_file = open(sys.argv[-1], 'w+b')
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

diff_channels = np.empty((chans, samps), dtype=int)

s = wave_file.readframes(samps)
wave_file.close()

unpstr = '<{0}h'.format(samps*chans)
x = list(struct.unpack(unpstr, s))

for i in range(chans):
	diff_channels[i] = np.array(x[i::chans]) 

left_channel = np.array(x[0::chans]) 
right_channel = np.array(x[1::chans])

print diff_channels[0]
diff_channels_out = get_diffs(diff_channels, samps, chans)
print diff_channels_out[0]
diff_channels_out = get_de_diffs(diff_channels_out, samps, chans)
print diff_channels_out[0]
