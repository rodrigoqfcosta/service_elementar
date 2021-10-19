# TRABALHO DA DISCIPLINA LABORATÓRIO DE ENGENHARIA DE SOFTWARE,
## CALCULADORA ORIENTADA A SERVIÇOS:

Desenvolver um sistema simples que se comporte como uma calculadora orientada a serviços.
A calculadora deve ser provida, pelo menos de 3 operações, divididas em duas categorias:
1. Operações Elementares (e.g.: soma, subtração);
2. Operações envolvendo funções transcendentes (e.g.: seno, cosseno, tangente, exponencial, tangente hiperbólica)
ou computação composta de uma fórmula que faça uso de uma operação elementar (e.g.: x3 + x2).
Essa operação deverá ser única para cada trabalho e especificada no canal “Tema trabalho prático”.
Para cada operação realizada, um log é criado informando qual operação foi realizada, em qual horário.
Esse log é armazenado em um banco de dados que deve conter:
- Data da operação;
- Tipo de operação;
- Operação específica;
- Argumentos utilizados;

A calculadora deve ser estruturada utilizando orientação a serviços (service oriented architecture - SOA).
Mais especificamente, por serem serviços simples, são chamados de microsserviços.
1. As operações elementares devem ser implementadas por um serviço independente de qualquer outro serviço.
2. As operações transcendentes ou de fórmulas, devem ser implementadas de modo
independente (e.g: seno) ou consumindo o serviço das funções elementares
(e.g: x3 + x2 calcula isoladamente o cubo, o quadrado e, depois, consome o serviço de cálculo de soma).
3. O log deve ser implementado em um serviço totalmente independente.
4. O log não deve possuir persistência em tabela única. Deve haver, no mínimo uma
associação à uma tabela que classifica a operação como “elementar” ou “transcendente”.
O sistema para a internet deve possuir ao menos 2 interfaces totalmente distintas:
1. Interface para execução das operações.
2. Interface para exibição do log de operações, podendo filtrar os logs, para exibição, por data e por tipo de operação. 
