<h1 align="center">

    CRIPTOGRAFIA DE PONTA A PONTA
</h1>

>Esta interface python-only demonstra uma das técnicas mais sofisticadas para proteger dados utilizando um truque matemático incrível

<p align="center">
  <a href="#introdução">Introdução</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#como-funciona-a-criptografia">Como funciona</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#demonstração-matemática">Matemática</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#teoria-e-aplicações-do-rsa">História</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#contato">Contato</a>
</p>


## Introdução

> A criptografia de ponta a ponta é um sistema de algoritmos matemáticos chamado RSA que embaralham seus dados de tal forma que ninguém sem acesso a senha poderá compreender o conteúdo.

Esse mini artigo vai demonstrar com riqueza de detalhes e uma linguagem acessível como mensageiros online fazem para proteger suas mensagens de texto. Para isso, foi criada uma programa utilizando: 
- Python 3.8
- Qt Designer 5.14.1

> Todos os códigos estão disponíveis acima com comentários

Uma versão portátil para Windows está disponível para download na pasta [windeploy](https://github.com/EduFreit4s/end-to-end-encryption/tree/master/windeploy)

## Como funciona a criptografia

Agora que você sabe que os dados são embaralhados, vamos aprofundar esse processo.

> A criptografia funciona como uma transformada cuja função inversa é muito difícil de calcular. Ficou estranho né? Eu explico! Imagine o seno(x) = m. Na matemática, se quisermos encontrar o seno(x) cuja resposta é m, basta aplicar a função inversa arcoseno(m) que encontraremos x.
>
> *Exemplo: seno(90) = 1, logo, arcoseno(1) é igual a 90.* *Fácil né?* 

Assim como o seno, algoritmo que estamos estudando é uma função com dado de entrada e saída:

<p align="center">
	<b>m^e mod n = m'</b>
</p>

E o inverso da nossa metáfora:

<p align="center">
	<b>m'^d mod n = m</b>
</p>

*Onde **m** e **'m** significa texto puro e o criptografado respectivamente.*
>A equação com **e** é utilizada para codificar o texto puro
>
>A equação com **d** é usada para decodificar  

Chamamos **e** e **n** de chave pública e **d** de chave privada  
    
 <h2 align="center">
    Chave pública e Chave privada
</h2>

>Nossa senha na verdade são três números (**e**, **d** e **n**), as "chaves". Para encontrá-las são necessários uma sequência de passos:

- Definir dois números primos.

	*Quanto maior esses números primos, mais seguro é a criptografia*
 
 >Chamamos esses números primos de **p** e **q**. **n** é obtido a partir produto de p e q. 

- Calcular função totiente φ(**n**) que é dado por (**p**-1)*(**q**-1). 

> A matemática garante que existe um **e** tal que 1 < **e** < φ(**n**)  e o máximo divisor comum entre **e** e φ(**n**) é igual a 1.

- Achar **d**, o inverso modular de **e**

> A **chave privada** ou **d**, pode ser encontrada rapidamente quando **d*****e** mod φ(**n**) for igual a um. 

## Demonstração matemática


<h4 align="center">
	
	p = 13, q = 17 | n -> p*q -> 13*17 = 221
	
	φ(n) -> φ(221) = (p-1)*(q-1) -> (13-1)*(17-1) -> 12*16 = 192
	e = MMC(φ(n),e) = 1 -> MMC(192,e) = 1 -> MMC(192,11) = 1 -> e = 11
	d = d*e mod φ(n) = 1 -> d*11 mod 192 = 1 -> 35*11 mod 192 = 1 -> d = 35
	
	Chave pública[e] = 11  |  Chave privada[d] = 35  |  Módulo[n] = 221
	
</h4>


>Para embaralhar o texto, cada letra será convertida em um número <b>com 6 caracteres</b>, essa relação valor-letra pode ser chamada de cifra. Neste programa foi utilizado o padrão ASCII que enumera as letras e símbolos mais utilizados.

Vamos criptografar a palavra "<b>IFPB</b>"<br>

*Para simplificar os cálculos utilizaremos a tabela abaixo ao invés do padrão ASCII*

| LETRA | VALOR |
| ----- | ----- |
|   I 	|   6 	|
|   F 	|   1	|
|   P 	|   4 	|
|   B 	|   7	|

> Utilizando a cifra e a função <b>m</b>^<b>e</b> mod <b>n</b>  para criptografar temos:
<p align="center">
I ---> <b>6</b>^<b>11</b> mod <b>221</b> = 000141<br>
F ---> <b>1</b>^<b>11</b> mod <b>221</b> = 000001<br> 
P ---> <b>4</b>^<b>11</b> mod <b>221</b> = 000166<br>
B ---> <b>7</b>^<b>11</b> mod <b>221</b> = 000184<br> 
</p>
 
> Nossa palavra "<b>IFPB</b>" codificada é: "<b>000141</b>000001<b>000166</b>000184"

#### Agora vamos reverter o processo seguindo os passos:

- Quebrar a informação em bloco <b>com 6 caracteres</b>
<p align="center">
	<b>000141</b>000001<b>000166</b>000184
</p>

>Utilizando a função <b>m'</b>^<b>d</b> mod <b>n</b>  para decodificar temos:
 
<p align="center">
<b>000141</b>^<b>35</b> mod <b>221</b> = 6<br>
000001^<b>35</b> mod <b>221</b> = 1<br> 
<b>000166</b>^<b>35</b> mod <b>221</b> = 4<br>
000184^<b>35</b> mod <b>221</b> = 7<br> 
</p>

- Utilizar a cifra 

| VALOR | LETRA |
| ----- | ----- |
|   6 	|   I 	|
|   1 	|   F	|
|   4 	|   P 	|
|   7 	|   B	|

> Nossa cifra“<b>6</b>1<b>4</b>7" convertida é: "<b>IFPB</b>" 

*obs.: utilize a calculadora do Windows ou esse [site](https://www.wolframalpha.com/) se quiser calcular esses números grandes!*


## Teoria e aplicações do RSA

RSA é um acrônimo para (Rivest-Shamir-Adleman). Cientistas criadores do algoritmo apresentado pela primeira vez em 1978 para uso militar e estratégico. 
A RSA Data Security Inc. (empresa que padroniza o algoritmo) recomenda gerar números primos  <em>p e q</em> com 2048 bits de tamanho, ou seja, 617 dígitos. Isso garante proteção até 2030.  

A teoria dos números é a base da criptografia assimétrica e sua força vem do problema da fatoração de inteiros. Problema esse tão difícil quanto o problema do [caixeiro viajante](https://pt.wikipedia.org/wiki/Problema_do_caixeiro-viajante) ou [logaritmo discreto](https://pt.wikipedia.org/wiki/Logaritmo_discreto) <br/>

Sabendo que <b>n</b> é um produto de <em>p e q</em> e <b>n</b> trafega em rede insegura, podemos roubar essa informação e utilizar todos computadores do planeta para encontrar via força bruta, os dois fatores <em>p * q</em> que deram origem a <b>n</b>. 

> Basicamente, fatorar um semi primo (produto de dois números primos) <em>p e q</em> pode levar o tempo do universo se  <em>p e q</em> forem grandes o suficiente!

<p align="center">
  <img width="400" height="200" src="https://github.com/EduFreit4s/end-to-end-encryption/blob/master/images/404.jpg">
</p>

A criptografia mudou o mundo para sempre. Essa técnica protege todo tipo de dado na internet. Desenvolvedores podem blindar seu software com chaves que garantem autenticidade. RSA também é utilizado em programas de vpn que torna impossível rastrear uma remetente web.  

> Sem criptografia a internet como conhecemos hoje não existiria 

## Contato 

- E-mail:  [freitas.eduardo@academico.ifpb.edu.br](mailto:freitas.eduardo@academico.ifpb.edu.br)
                                          
                                                
                                                 Copyright (c) 2020 EduFreit4s



