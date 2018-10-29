# Wav encoder decoder
Trabalho de Multimidia &amp; Hipermidia

## Introdução

Este trabalho visa em exercitar a prática para a matéria de Multimídia & Hipermídia por meio de codificação de algoritmos de compressão/descompressão de um arquivo de áudio no formato WAV (este guarda a informação à respeito das ondas sonoras).
Para atingir este objetivo iremos utilizar a linguagem [python](https://www.tutorialspoint.com/python/python_command_line_arguments.htm) em conjunto com módulos para interpretar o arquivo [WAV](https://github.com/python/cpython/blob/2.7/Lib/wave.py).

## Objetivo

O objetivo principal do projeto é colocar em prática alguns conceitos teóricos abordados em sala
de aula relacionados a técnicas de compressão. Para isso, os grupos deverão implementar algumas
técnicas de compressão/descompressão – a saber – aplicadas a áudio digital. Serão empregadas as
técnicas de **codificação por diferenças, codificação por carreira ([Run-length](https://www.fileformat.info/mirror/egff/ch09_03.htm)) e codificação por
[Huffman](https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/)**. As três técnicas deverão ser aplicadas, de modo combinado ou isolado, a um arquivo de áudio
em formato WAV sem compressão. Os dados resultantes da compressão devem ser armazenados em um
arquivo binário. 

## Método:
#### Para entrada:
  - [x] Leitura dos dados no cabeçalho do arquivo WAV
  - [x] Separação do cabeçalho e do corpo do arquivo
  - [x] Criação da função para Run-length
  - [ ] Criação da função para Huffman
  - [x] Criação da função para Diferenças
  - [x] Leitura dos inputs (tipos de compressão)
  - [x] Escrita em arquivo (bin)
#### Para saída:
  - [x] Leitura do arquivo de entrada
  - [ ] Criação da função para Run-length
  - [ ] Criação da função para Huffman
  - [x] Criação da função para Diferenças 
  - [x] Leitura dos inputs (tipos de descompressão)
  - [x] Escrita em arquito (wav)
  

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

## Ferramentas utilizadas:
|Módulo     |Versão       |
|-----------|-------------|
|Python     | 2.7.12      |
|numpy      |1.15.2       |
|anytree    |2.4.3        |

