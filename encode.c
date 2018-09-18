#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv){

	int i;
	char *filename;

	for(i = 1; i < argc; i++){
		if(argv[i][0] == '-'){
			if(argv[i][1] == 'd'){
				printf("%s: utilização da codificação por diferenças\n", argv[i]);
			}else if(argv[i][1] == 'c'){
				printf("%s: utilização da codificação por carreira\n", argv[i]);
			}else if(argv[i][1] == 'h'){
				printf("%s: utilização da codificação Huffman\n", argv[i]);
			}else{
				printf("\nFlag não reconhecida, utilize: \n<-d> (codificação por diferenças)\n<-c> (codificação por carreira)\n<-h> (codificação Huffman)\n\n");
			}
		}
		if(i == argc-1){
			filename = argv[i];
			printf("%s\n", filename);
		}
	}

	//int status = system("./wave_reader Engine-Noise.wav");
	
}