# end-to-end-encryption

## Status: Incompleto!

Este programa escrito em python demonstra uma tecnica de criptação utilizada no mundo todo 

![RSA](https://github.com/EduFreit4s/end-to-end-encryption/blob/master/images/home.PNG)

## Como funciona criptografia assimétrica?

A criptografia é baseada em uma transformada cuja função inversa é muito díficil de calcular. Ficou estranho né? Eu explico! Imagine o sen(*x*) = *m*. Se quisermos encontrar o valor de **x** da função seno cuja resposta é **m**, basta aplicar a função inversa arcoseno(*m*) = *x*. *Exemplo: sen(90) = 1 logo, arcosen(1) é igual a 90.* Até agora fácil né?

A função *assimétrica RSA* depende de 3 números importantes que chamamos de chave pública, módulo e chave privada. Funciona assim:
Com a minha chave pública e módulo, qualquer pessoa no mundo pode achar **m**, mas apenas quem tiver a chave privada e o módulo podem achar **x**!

A função assimétrica de criptográfia é dada por (*x*^*chave pública*) mod *módulo* = **m** e a função inversa ou de descriptografia é dada por (**m**^*chave privada*) mod *módulo* = **x**.  

*Observe que apenas a chave privada é capaz de desfazer a criptográfia e a segurança do sistema depende de ninguém conhecê-la ou quão díficil é tentar descobrir*

### *chave pública, privada e módulo

O primeiro passo é escolher dois números primos bem grandes. Chamaremos esses números de *p* e *q*. Depois é necessário calcular a 
