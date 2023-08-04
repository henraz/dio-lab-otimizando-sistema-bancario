# dio-lab-otimizando-sistema-bancario

Resolução do lab "Otimizando o Sistema Bancário com Funções Python", do Bootcamp **"Potência Tech powered by iFood | Ciência de Dados"** da [dio](https://www.dio.me/bootcamp/potencia-tech-powered-ifood-ciencias-de-dados-com-python).

**Desafio:** Otimizar o sistema bancário criado no lab anterior ["Criando um Sistema Bancário com Python"](https://github.com/henraz/dio-lab-sistema-bancario). Para esse desafio é necessário realizar as seguintes alterações:

1. Tornar o código mais modularizado: Criar funções para as operações **sacar**, **depositar** e **extrato**;
2. Criar duas novas funções: **criar cliente** e **criar conta corrente** (Essas funções não precisam ainda se relacionar com as anteriores. Ou seja, basta ser possível criar um cliente e uma conta);
3. Regras para cada função:
    - `saque`: Deve receber os argumentos apenas por nome (*keyword only*);
    - `deposito`: Deve receber os argumentos apenas por posição (*positional only*);
    - `extrato`: Deve receber os argumentos por posição e nome. Argumentos posicionais: `saldo`. Argumentos nomeados: `extrato`.
    - `criar usuario`: Deve armazenar os usuários em uma lista. Um usuário é composto por: `nome`, `data de nascimento`, `cpf` e `endereco`. O endereco possui o formato: `logradouro, nro - bairro - cidade/sigla estado`. Deve ser armazenado somente os números do CPF e não deve ser possível cadastrar 2 usuários com o mesmo CPF.
    - `criar conta`: Deve armazenar as contas em uma lista. Uma conta é composta por: `agencia`, `numero da conta` e `usuario`. O número da conta é sequencial e começa em 1. O número da agência é fixo: "0001". Um usuário pode ter mais de uma conta, mas uma conta pertence a apenas um usuário.