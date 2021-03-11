# Objetivo

Pretende-se que implemente um interpretador de uma linguagem de
programação orientada à stack, chamado $0M. O seu programa deverá
permitir ler comandos do *stdin* ou de um ficheiro, interpretá-los, e
imprimir o conteúdo da stack no *stdout*.

# Expressões matemáticas

    + - * /         Somar, subtrair, multiplicar e dividir
    ( )             Decrementar e incrementar um valor
    %               Módulo
    #               Exponenciação
    & | ^ ~         E, ou, xor e not (bitwise) para inteiros

# Stack

    _       Duplicar
    ;       Pop
    \       Trocar os dois elementos do topo da stack
    @       Rodar os 3 elementos no topo da stack
    n $     Copiar n-ésimo elemento para o topo da stack

# Lógica

    =       Igual
    <       Menor
    >       Maior
    !       Não
    e&      E
    e|      Ou
    e<      Colocar o menor dos 2 valores na stack
    e>      Colocar o maior dos 2 valores na stack

# Variáveis

    A até Z     Coloca no topo da stack o conteúdo da variável
    :<Letra>    Copia topo da stack à variável
    A       Valor por omissão: 10
    B       Valor por omissão: 11
    C       Valor por omissão: 12
    D       Valor por omissão: 13
    E       Valor por omissão: 14
    F       Valor por omissão: 15
    N       Valor por omissão: '\n'
    S       Valor por omissão: ' '
    X       Valor por omissão: 1
    Y       Valor por omissão: 2
    Z       Valor por omissão: 0

# Input/Output

    l       Ler linha
    t       Ler todas as linhas
    p       Imprimir topo da stack

# Conversões

    i       Converter o topo da stack num inteiro
    f       Converter o topo da stack num double
    c       Converter o topo da stack para caratere

# Arrays e strings

    ""      Criar uma string
    []      Criar um array
    ~       Colocar na stack todos os elementos do array
    +       Concatenar strings ou arrays
            (ou array com elemento)
    *       Repetir strings ou arrays
    ,       Tamanho ou range
    =       Ir buscar um valor por índice
    < >     Ir buscar X carateres do início ou fim
    ( )     Remover 1º ou últ. elt. e colocar na stack
    $       Ordenar
    #       Procurar subarray em array e devolver o índice
    S/      Separar uma string por espaços
    N/      Separar uma string por newlines

# Blocos e Controlo de execução

    {}      Criar um bloco
    ~       Executar bloco
    %       Aplicar o bloco a todos os elementos de um array
    *       Fold sobre um array/string usando o bloco
    ,       Filtrar um array/string utilizando um bloco
    ?       If-Then-Else
    w       Enquanto

# Exemplos

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Input</th>
<th style="text-align: left;">Resultado</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">1 2 3 ?</td>
<td style="text-align: left;">2</td>
</tr>
<tr class="even">
<td style="text-align: left;">0 2 3 ?</td>
<td style="text-align: left;">3</td>
</tr>
<tr class="odd">
<td style="text-align: left;">5 ,</td>
<td style="text-align: left;">01234</td>
</tr>
<tr class="even">
<td style="text-align: left;">5 , ~ \</td>
<td style="text-align: left;">01243</td>
</tr>
<tr class="odd">
<td style="text-align: left;">[ 1 2 3 ] 2 * [ 4 5 ] \ +</td>
<td style="text-align: left;">45123123</td>
</tr>
<tr class="even">
<td style="text-align: left;">[ l l l ] { i 3 * } %<br />
1<br />
2<br />
3</td>
<td style="text-align: left;">369</td>
</tr>
<tr class="odd">
<td style="text-align: left;">[ 3 1 9 ] ) 7 * + 3 *</td>
<td style="text-align: left;">316331633163</td>
</tr>
<tr class="even">
<td style="text-align: left;">t N/ ~ #<br />
planetas<br />
neta</td>
<td style="text-align: left;">3</td>
</tr>
<tr class="odd">
<td style="text-align: left;">“planetas” 3 &gt;</td>
<td style="text-align: left;">netas</td>
</tr>
</tbody>
</table>

# Guião 1

  - Pretende-se que implemente a parte das expressões matemáticas
  - O seu programa deve:
    1.  ler uma linha;
    2.  correr o código correspondente
    3.  imprimir o conteúdo da stack no fim da execução

| Input            | Resultado |
| :--------------- | :-------- |
| 5 4 -            | 1         |
| 5 3 ) \#         | 625       |
| 2 4 5 \* +       | 22        |
| 1 ) ) 7 ( ( ( \# | 81        |
| 5 2 %            | 1         |
| 2 5 ^            | 7         |
| 2 5 &            | 0         |
| 12 7 2 & |       | 14        |

# Guião 2

  - Pretende-se que implemente a parte correspondente à:
      - manipulação da stack,
      - conversão de tipos e
      - comando l

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Input</th>
<th style="text-align: left;">Resultado</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">1 2 3 @</td>
<td style="text-align: left;">231</td>
</tr>
<tr class="even">
<td style="text-align: left;">1 2 3 _ @ ;</td>
<td style="text-align: left;">133</td>
</tr>
<tr class="odd">
<td style="text-align: left;">7 2 3 2 $</td>
<td style="text-align: left;">7237</td>
</tr>
<tr class="even">
<td style="text-align: left;">1 2 3 4 5 \ ; @</td>
<td style="text-align: left;">1352</td>
</tr>
<tr class="odd">
<td style="text-align: left;">2 3 4 @ ; _ # \ _ # +</td>
<td style="text-align: left;">283</td>
</tr>
<tr class="even">
<td style="text-align: left;">79 c 108 c 97 c</td>
<td style="text-align: left;">Ola</td>
</tr>
<tr class="odd">
<td style="text-align: left;">79 108 97 c @ c @ c @</td>
<td style="text-align: left;">Ola</td>
</tr>
<tr class="even">
<td style="text-align: left;">l i l i #<br />
2<br />
4</td>
<td style="text-align: left;">16</td>
</tr>
</tbody>
</table>

# Guião 3

  - Pretende-se que implemente um debugger
  - A parte correspondente às:
      - variáveis
      - condições

| Input                   | Resultado |
| :---------------------- | :-------- |
| A B \*                  | 110       |
| C ) :C C                | 1313      |
| 1 2 3 :A @ :B A + A B   | 23431     |
| l i :A l i :B + B A 2 4 | 642       |
| 1 3 e&                  | 3         |
| 1 3 e& 5 e|             | 3         |
| 3 2 1 + =               | 1         |
| 3 5 = \! 7 2 \>         | 11        |
| 3 5 2 e\<               | 32        |
| 3 5 2 e\< e\<           | 2         |

# Guião 4

  - Pretende-se que implemente a parte correspondente aos arrays

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Input</th>
<th style="text-align: left;">Resultado</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">1 [ 2 3 ] + 3 *</td>
<td style="text-align: left;">123123123</td>
</tr>
<tr class="even">
<td style="text-align: left;">[ 3 5 4 1 2 ] $ 3 &lt;</td>
<td style="text-align: left;">123</td>
</tr>
<tr class="odd">
<td style="text-align: left;">[ 3 5 7 1 2 ] 2 =</td>
<td style="text-align: left;">7</td>
</tr>
<tr class="even">
<td style="text-align: left;">[ 1 2 3 ] [ 4 5 ] \ +</td>
<td style="text-align: left;">45123</td>
</tr>
<tr class="odd">
<td style="text-align: left;">[ 1 2 3 ] ( + [ 7 5 ] +</td>
<td style="text-align: left;">23175</td>
</tr>
<tr class="even">
<td style="text-align: left;">t S/ ,<br />
tres tristes tigres</td>
<td style="text-align: left;">3</td>
</tr>
<tr class="odd">
<td style="text-align: left;">[ 7 2 3 ] _ ,</td>
<td style="text-align: left;">7233</td>
</tr>
<tr class="even">
<td style="text-align: left;">[ 1 2 3 ] 3 *</td>
<td style="text-align: left;">123123123</td>
</tr>
<tr class="odd">
<td style="text-align: left;">[1 2 3] ~ * +</td>
<td style="text-align: left;">7</td>
</tr>
</tbody>
</table>

# Guião 5

  - Pretende-se que implemente a parte correspondente aos blocos

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Input</th>
<th style="text-align: left;">Resultado</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">2 { 3 * }</td>
<td style="text-align: left;">2{ 3 * }</td>
</tr>
<tr class="even">
<td style="text-align: left;">2 { 3 * } ~</td>
<td style="text-align: left;">6</td>
</tr>
<tr class="odd">
<td style="text-align: left;">[ 1 2 3 ] { 2 # } %</td>
<td style="text-align: left;">149</td>
</tr>
<tr class="even">
<td style="text-align: left;">l { (( } %<br />
qnc</td>
<td style="text-align: left;">ola</td>
</tr>
<tr class="odd">
<td style="text-align: left;">5 , { ) } %</td>
<td style="text-align: left;">12345</td>
</tr>
<tr class="even">
<td style="text-align: left;">5 , { 2 % } ,</td>
<td style="text-align: left;">13</td>
</tr>
<tr class="odd">
<td style="text-align: left;">10 , { 3 % ! } ,</td>
<td style="text-align: left;">0369</td>
</tr>
<tr class="even">
<td style="text-align: left;">5 :A ; 1 { A * A ( :A } w</td>
<td style="text-align: left;">120</td>
</tr>
<tr class="odd">
<td style="text-align: left;">10 , { ) } % { * } *</td>
<td style="text-align: left;">3628800</td>
</tr>
<tr class="even">
<td style="text-align: left;">t S/ { i } % { e&gt; } *<br />
2 7 13 4</td>
<td style="text-align: left;">13</td>
</tr>
</tbody>
</table>
