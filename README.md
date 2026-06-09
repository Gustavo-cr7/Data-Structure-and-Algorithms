## Data-Structure-and-Algorithms
              
## Fluxograma Simples

                        INÍCIO
                          |
                          v
                 Exibir Menu Principal
                          |
                          v
                Escolher uma Opção
                          |
     +----------+---------+--------+--------+
     |          |         |        |        |
     v          v         v        v        v
    [1]        [2]       [3]      [4]      [5]
     |          |         |        |        |
     v          v         v        v        v   
    Inserir  Visualizar Executar Histórico Encerrar
    Dados     Status    Análise  Leituras Sistema
     |          |         |        |        |
     +----------+---------+--------+--------+
                          |              
                          v
                    Volta ao Menu
                               
## Explicação da Lógica Utilizada

O sistema foi desenvolvido para monitorar informações básicas de uma missão espacial utilizando Python.

Inicialmente é criada uma lista chamada historico, responsável por armazenar todas as leituras realizadas pelo usuário. Cada leitura é salva em formato de dicionário contendo:

Temperatura da nave;
Nível de energia;
Status da comunicação.

A função inserir_dados() recebe os valores informados pelo usuário e os armazena no histórico.

A função visualizar_status() exibe a última leitura cadastrada, mostrando a temperatura, o nível de energia e o estado da comunicação.

A função executar_analise() verifica as condições da missão utilizando estruturas condicionais. Caso a temperatura seja superior a 80°C, é exibido um alerta de superaquecimento. Caso a energia seja inferior a 20%, é exibido um alerta de economia de energia. Caso a comunicação seja igual a 0, é exibido um alerta de falha de comunicação. Se nenhuma condição crítica for encontrada, o sistema informa que a missão está operando normalmente.

A função mostrar_historico() utiliza um laço de repetição para percorrer todas as leituras armazenadas e exibi-las na tela.

Por fim, a função menu() mantém o programa em execução até que o usuário escolha a opção de encerramento.

O código utiliza:

Funções;
Listas;
Dicionários;
Estruturas condicionais;
Estruturas de repetição;
Entrada e saída de dados.

## Vídeo de demonstração
🎥 [Assistir no YouTube](https://youtu.be/IF7J95mupnk)
