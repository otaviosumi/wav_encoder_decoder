# wav_encoder_decoder
Trabalho de Multimidia &amp; Hipermidia

## Objetivo

O objetivo principal do projeto é colocar em prática alguns conceitos teóricos abordados em sala
de aula relacionados a técnicas de compressão. Para isso, os grupos deverão implementar algumas
técnicas de compressão/descompressão – a saber – aplicadas a áudio digital. Serão empregadas as
técnicas de codificação por diferenças, codificação por carreira (run-length) e codificação por
Huffman. As três técnicas deverão ser aplicadas, de modo combinado ou isolado, a um arquivo de áudio
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

### Onde:
|Item      |Função    |
|----------|----------|
|decode |nome do decodificador|
|<entrada.bin> |arquivo binário comprimido|
|<saida.wav> |arquivo WAV sem compressão|
