# end-to-end-encryption

### Status: Incompleto!

Este programa escrito em python demonstra uma tecnica de criptação utilizada no mundo todo 

![RSA](https://github.com/EduFreit4s/end-to-end-encryption/blob/master/images/home.PNG)

## Como funciona criptográfia assimétrica?

A criptográfia é baseada em uma transformada cuja função inversa é muito díficil de calcular. Ficou estranho né? Eu explico! Imagine o sen(*x*) = *m*. Se quisermos encontrar o valor de **x** da função seno cuja resposta é **m**, basta aplicar a função inversa arcoseno(*m*) = *x*. *Exemplo: sen(90) = 1 logo, arcosen(1) é igual a 90.* Até agora fácil né?

A função *assimétrica RSA* depende de 3 números importantes que chamamos de chave pública, módulo e chave privada. Funciona assim:
Com a minha chave pública e módulo, qualquer pessoa no mundo pode achar **m**, mas apenas quem tiver a chave privada e o módulo podem achar **x**!

A função assimétrica de criptográfia é dada por (*x*^*chave pública*) mod *módulo* = **m** e a função inversa ou de descriptografia é dada por (**m**^*chave privada*) mod *módulo* = **x**. Na nossa analogia, **x** representa o texto que eu quero codificar, enquanto o **m** é o mesmo texto já embaralhado.  

*Observe que apenas a chave privada é capaz de desfazer a criptográfia. A segurança do sistema depende de ninguém conhecê-la ou quão díficil é tentar descobrir-la*

### *Chave pública, privada e módulo*

*Não é todo número que funciona, por isso, é necessário conhecer o algoritmo gerador de tais números tão especiais*

São necessários dois números primos bem grandes. Chamaremos esses números de **p** e **q**. O nosso primeiro número mágico **módulo** é o produto de *p e q*. Vamos chamar esse produto de **n**.
Depois é necessário calcular Phi(**n**) que é dado por (**p**-1) * (**q**-1).

Vamos chamar a nossa **chave pública** de *e*. A matemática garante que existe um 1 < *e* < Phi(**n**) cujo o máximo divisor comum entre **e** e Phi(**n**) é igual a um. Neste caso, **e** um coprimo de Phi.

Por último, a **chave privada** ou **d**, é a pôtencia de **m** cujo o resto da divisão por Phi(**n**) tem valor igual a um. *Exemplo: e * d mod phi(n) = 1*

