import numpy as np #instalado
import struct
import sys
import wave 
import pickle
import operator
import cPickle as pickle

diff_bool = False
run_bool = False
huff_bool = False


def is_valid(input):
	global diff_bool
	global run_bool
	global huff_bool
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


def get_run_length(input_channels, ch):
	wav_run = [] #temp
	for i in range(len(input_channels[ch])):
		if i > 0:
			if input_channels[ch][i] != input_channels[ch][i-1]:
				wav_run.append(1)
				wav_run.append(input_channels[ch][i])
			else:
				wav_run[-2] += 1
		else:
			wav_run.append(1)
			wav_run.append(input_channels[ch][i])
	return wav_run


def build_run_length(input_channels, chans):
	wav_run = []
	for i in range(chans):
		wav_run.append(get_run_length(input_channels, i))
	return wav_run


def main(argv):
	argc = len(sys.argv)
	if argc <= 2:
		print 'Poucos argumentos\nFormato:\npython decode.py <entrada.bin> <saida.wav>'
		exit()
	wave_file = wave.open(sys.argv[-1], 'w')
	input_file = sys.argv[-2]

	diff_channels = 0

	with open(input_file, 'rb') as input_data:
		diff_channels = pickle.load(input_data)
	with open('header_' + input_file, 'rb') as input_data:
		diff_bool = pickle.load(input_data)
		run_bool = pickle.load(input_data)
		huff_bool = pickle.load(input_data)
		params = pickle.load(input_data)
		chans = pickle.load(input_data)
		samps = pickle.load(input_data)






if __name__ == "__main__":
	main(sys.argv)



