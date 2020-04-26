# end-to-end-encryption

> The interface of user is equal to a joke. If you have than explain, she the not so good

<p align="center">
  <a href="#-intro">Introdução</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-works">Como funciona</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-Demonstração">Matemática</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-História do RSA, teoria e aplicações">Sobre</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-technologies">Technologies</a>
</p>


## Introdução
Este programa escrito em python demonstra uma técnica de criptação utilizada no mundo todo 

<p align="center">
  <img width="460" height="400" src="https://github.com/EduFreit4s/end-to-end-encryption/blob/master/images/home.PNG">
</p>

## Como funciona criptografia assimétrica?

A criptografia é baseada em uma transformada cuja função inversa é muito difícil de calcular. Ficou estranho né? Eu explico! Imagine o seno (*x*) = *m*. Se quisermos encontrar o valor de **x** da função seno cuja resposta é **m**, basta aplicar a função inversa arco seno (*m*) = *x*. *Exemplo: seno (90) = 1 logo, arco seno (1) é igual a 90.* *Até agora fácil né?*

A função *assimétrica RSA* depende de 3 números importantes que chamamos de chave pública, módulo e chave privada. Funciona assim:
Com a minha chave pública e módulo, qualquer pessoa no mundo pode achar **m**, mas apenas quem tiver a chave privada e o módulo podem achar **x**!

A função assimétrica de criptografia é dada por (*x*^*chave pública*) mod *módulo* = **m** e a função inversa é dada por (**m**^*chave privada*) mod *módulo* = **x**. Na nossa analogia, **x** representa o texto puro, enquanto o **m** é o mesmo texto codificado.  

*Observe que apenas a chave privada é capaz de desfazer a criptografia. A segurança do sistema depende de ninguém a conhecer ou quão difícil é tentar descobri-la*

### *Chave pública, privada e módulo*

São necessários dois números primos bem grandes. Chamaremos esses números de **p** e **q**. O nosso primeiro número mágico **módulo** é o produto de *p e q*. Vamos chamar esse produto de **n**.
Depois é necessário calcular Phi (**n**) que é dado por (**p**-1) * (**q**-1).

Vamos chamar a nossa **chave pública** de *e*. A matemática garante que existe um 1 < *e* < Phi (**n**) cujo o máximo divisor comum entre **e** e Phi (**n**) é igual a um.

Por último, a **chave privada** ou **d**, é um fator do produto **d** * **e** cujo o resto da divisão por Phi (**n**) tem valor igual a um. <br/> *Exemplo: e * d mod Phi (n) = 1*

### *Demonstração*

*p = 13, q = 17* <br/>
*n = 13 * 17 = 221* <br/>
*Phi (n) = Phi (221) = (p-1) * (q-1) = (13-1) * (17-1) = 12 * 16 = 192* <br/>
*MMC (Phi (n), e) = 1, MMC (192, e) = 1, MMC (192, 11) = 1, e = 11* <br/>
*d = d * e mod Phi (n) = 1, d * 11 mod 192 = 1, 35 * 11 mod 192 = 1, d = 35.* <br/>

Chave pública = 11 <br/>
Chave privada = 35 <br/>
Módulo = 221 <br/>

Na criptografia cada letra é convertida em um número, essa relação valor-letra pode ser chamada de cifra. Neste programa foi utilizado o padrão ASCII que enumera as letras e símbolos mais utilizados.

*Exemplo: E = 4, u = 2*

Codificando: **42**^*11 (717.368.321.110.468.608) mod 221 = **87** <br/>
Descodificando: **87**^35 (76.414.159.693.594.362.648.493.473.462.227.115.569.994.383.111.779.411.134.326.272.099.143) mod 221 = **42** <br/>

*42 = Eu*

*obs.: utilize a calculadora do Windows ou esse [site](https://www.wolframalpha.com/) se quiser calcular esses números grandes! *

## 🚀 Technologies

### História do RSA, teoria e aplicações

RSA é um acrônimo para (Rivest-Shamir-Adleman). Cientistas criadores do algoritmo apresentado pela primeira vez em 1978 para uso militar e estratégico. 
A RSA Data Security Inc. (empresa que padroniza o algoritmo) recomenda gerar números primos p e q com 2048 bits de tamanho, ou seja, 617 dígitos. Isso garante proteção até 2030.  

A teoria dos números é a base do rsa e sua força vem do problema da fatoração de inteiros em tempo polinomial. Problema esse tão difícil quanto o problema do [caixeiro viajante](https://pt.wikipedia.org/wiki/Problema_do_caixeiro-viajante) ou [logaritmo discreto](https://pt.wikipedia.org/wiki/Logaritmo_discreto) <br/><br/>
*Quantas combinações de p e q são capazes de gerar um n?* Essa resposta só depende do tamanho de p e q. <br/>
<p align="center">
  <img width="400" height="200" src="https://github.com/EduFreit4s/end-to-end-encryption/blob/master/images/404.jpg">
</p>
Se eles forem tão grandes quanto possível, mesmo com todo poder computacional da terra, levaria mais tempo do que a idade do universo para quebrar o sistema.<br/><br/>

A criptografia mudou o mundo para sempre. Essa técnica protege todo tipo de dado na internet. Desenvolvedores podem blindar seu software com chaves que garantem autenticidade. RSA também é utilizado em programas de vpn que torna impossível rastrear uma remetente web. 


- Email:  [freitas.eduardo@academico.ifpb.edu.br](mailto:freitas.eduardo@academico.ifpb.edu.br)
                                          
                                                
                                                 Copyright (c) 2020 EduFreit4s





