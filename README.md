# Metodo-de-Monte-Carlo
Código em Python criado para simular o Método de Monte Carlo, feito como parte do projeto final da disciplina de Fundamentos Matemáticos II
Ao receber o input do usuário com as funções f(x) e g(x), que delimitam a área no eixo Y, e os pontos a e b, que delimitam a área no eixo X, o código usa a função random.uniform do python para gerar pontos [x,y] e estimar o tamanho da área, checando se o ponto [x,y] está dentro da área delimitada pelas funções f(x) e g(x).
O código pede como input também o número de pontos a serem gerados. Um maior número de pontos retorna um resultado mais preciso mas exige mais do computador e precisa de mais tempo para entregar a resposta.
O código retorna o valor da área na mesma unidade de medida dos pontos a e b. (Sejam a e b valores em metro, o retorno será em m²)
