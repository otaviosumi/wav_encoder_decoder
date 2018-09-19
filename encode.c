#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv){

	int i;
	//options
	int d, c, h;
	char *filename, *filename_out, *command;
	d = c = h = 0;
	for(i = 1; i < argc; i++){
		if(argv[i][0] == '-'){
			if(argv[i][1] == 'd'){
				d = 1;
				printf("%s: utilização da codificação por diferenças\n", argv[i]);
			}else if(argv[i][1] == 'c'){
				c = 1;
				printf("%s: utilização da codificação por carreira\n", argv[i]);
			}else if(argv[i][1] == 'h'){
				h = 1;
				printf("%s: utilização da codificação Huffman\n", argv[i]);
			}else{
				printf("\nFlag não reconhecida, utilize: \n<-d> (codificação por diferenças)\n<-c> (codificação por carreira)\n<-h> (codificação Huffman)\n\n");
			}
		}
		if(i == argc-2){
			filename = argv[i];
			printf("%s\n", filename);
			command = "./wave_reader ";
			printf("%s\n", command);
		}
		if(i == argc-1){
			filename_out = argv[i];
			printf("%s\n", filename_out);
		}
	}
	char *f_command = malloc(strlen(command) + strlen(filename) + 1);
	strcpy(f_command, command);
	strcat(f_command, filename);
	if(EXIT_SUCCESS == system(f_command));
	
	
}