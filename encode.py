import numpy as np #instalado
import struct
import sys
import wave 
import pickle
import operator

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

def build_huffman_tree(input_channels, chans):
	wav_dict = [
	{0:0},
	{0:0}
	]
	for ch in range(chans):
		for i in input_channels[ch]:
			if (i in wav_dict[ch]):
				wav_dict[ch][i] += 1
			else:
				wav_dict[ch][i] = 1

	for ch in range(chans):
		wav_dict[ch] = sorted(wav_dict[ch].items(), key=operator.itemgetter(1))
	return wav_dict

def main(argv):
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

	print diff_channels[0]
	diff_channels_out = get_diffs(diff_channels, samps, chans)
	print diff_channels_out[0]

	my_dict = build_huffman_tree(diff_channels_out, chans)
	print my_dict[0]

if __name__ == "__main__":
	main(sys.argv)



