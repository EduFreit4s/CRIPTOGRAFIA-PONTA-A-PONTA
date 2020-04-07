# end-to-end-encryption

## Status: Incompleto!

Este programa escrito em python demonstra uma tecnica de criptação utilizada no mundo todo 

![RSA](https://github.com/EduFreit4s/end-to-end-encryption/blob/master/images/home.PNG)

### Como funciona criptografia assimétrica?

A criptografia é baseada em uma transformada cuja função inversa é muito díficil de calcular. Ficou estranho né? Eu explico! Imagine o sen(*x*) = *m*. Se quisermos encontrar o valor de **x** da função seno cuja resposta é **m**, basta aplicar a função inversa arcoseno(*m*) = *x*. *Exemplo: sen(90) = 1 logo, arcosen(1) é igual a 90.* Até agora fácil né?

A função *assimétrica RSA* depende de 3 números importantes que chamamos de chave pública, módulo e chave privada. Funciona assim:
Com a minha chave pública e módulo, qualquer pessoa no mundo pode achar **m**, mas apenas quem tiver a chave privada e o módulo podem achar **x**!



O primeiro passo é escolher dois números primos bem grandes. Chamaremos esses números de *p* e *q*. Depois é necessário calcular a 
