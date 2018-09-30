# wav_encoder_decoder
Trabalho de Multimidia &amp; Hipermidia

## Ideias:

Utilizar [python](https://docs.python.org/2/library/wave.html)

## Objetivo

O objetivo principal do projeto é colocar em prática alguns conceitos teóricos abordados em sala
de aula relacionados a técnicas de compressão. Para isso, os grupos deverão implementar algumas
técnicas de compressão/descompressão – a saber – aplicadas a áudio digital. Serão empregadas as
técnicas de **codificação por diferenças, codificação por carreira ([Run-length](https://www.fileformat.info/mirror/egff/ch09_03.htm)) e codificação por
[Huffman](https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/)**. As três técnicas deverão ser aplicadas, de modo combinado ou isolado, a um arquivo de áudio
em formato WAV sem compressão. Os dados resultantes da compressão devem ser armazenados em um
arquivo binário. 

## Codificação

```encode -d -c -h <entrada.wav> <saida.bin>```


### Onde:
|Item      |Função    |
|----------|----------|
|encode |nome do codificador|
|-d |utilização da codificação por diferenças|
|-c |utilização da codificação por carreira|
|-h |utilização da codificação Huffman|
|<entrada.wav> |arquivo original sem compressão|
|<saida.bin> |arquivo binário comprimido|

## Decodificação

```decode <entrada.bin> <saida.wav>```

## Antes de usar:

Compilar os dois arquivos .c (a ferramenta e o código de codificação):
```
gcc encode.c -o encode
gcc wave_reader.c -o wave_reader
```

### Onde:
|Item      |Função    |
|----------|----------|
|decode |nome do decodificador|
|<entrada.bin> |arquivo binário comprimido|
|<saida.wav> |arquivo WAV sem compressão|
