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
	#tratando os argumentos de entrada
	wave_file = wave.open(sys.argv[-2], 'r')
	output_file = sys.argv[-1]
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
	params = wave_file.getparams()

	diff_channels = np.empty((chans, samps), dtype=int)

	s = wave_file.readframes(samps)
	wave_file.close()

	unpstr = '<{0}h'.format(samps*chans)
	x = list(struct.unpack(unpstr, s))

	for i in range(chans):
		diff_channels[i] = np.array(x[i::chans]) 

	
	###########################################################
	#sempre aplica por DIFERENCA
	# print 'The original from first channel:'
	print diff_channels[0]
	if diff_bool:
		diff_channels = get_diffs(diff_channels, samps, chans)
	print diff_channels[0]
	###########################################################

	###########################################################
	#sempre acha o run length
	if run_bool:
		diff_channels = build_run_length(diff_channels, chans)
	#print diff_channels[0]
	###########################################################

	###########################################################
	#sempre constroi TABELA DE HUFFMAN
	if huff_bool:
		my_dict = build_huffman_tree(diff_channels, chans)
		print 'Erro: Huffman nao implementado...'
		# print my_dict[0]

	###########################################################


	with open(output_file, 'wb') as output:
		pickle.dump(diff_channels, output, pickle.HIGHEST_PROTOCOL)
	with open('header_' + output_file, 'wb') as output:
		pickle.dump(diff_bool, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(run_bool, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(huff_bool, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(params, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(chans, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(samps, output, pickle.HIGHEST_PROTOCOL)




if __name__ == "__main__":
	main(sys.argv)



