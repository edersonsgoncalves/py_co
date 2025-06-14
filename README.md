# Sistema Bancário Simplificado

Este é um projeto simples de um sistema bancário em console, desenvolvido em Python, com funcionalidades básicas de depósito, saque e extrato. Ideal para fins didáticos e para consolidar conceitos fundamentais de programação em Python, como loops, condicionais e tratamento de entrada/saída.

## 🚀 Funcionalidades

* **Depósito (`[d]`):** Permite ao usuário depositar valores na conta, com validação para garantir que o valor seja positivo e numérico.
* **Saque (`[s]`):** Permite ao usuário sacar valores da conta, com as seguintes validações:
    * Verifica se há saldo suficiente.
    * Verifica se o valor do saque excede o limite por operação (R$ 500).
    * Verifica se o limite diário de 3 saques foi atingido.
* **Extrato (`[e]`):** Exibe o histórico de todas as transações (depósitos e saques) e o saldo atual da conta.
* **Sair (`[q]`):** Encerra o sistema bancário.

## 💼 Regras de Negócio Implementadas

Este sistema simula algumas regras de negócio comuns em operações bancárias:

* **Saldo Inicial:** A conta inicia com saldo zero.
* **Limite de Saque por Operação:** Cada saque não pode exceder R$ 500.
* **Limite Diário de Saques:** São permitidos no máximo 3 saques por dia.
* **Valores Positivos:** Depósitos e saques devem ser de valores positivos.
* **Saldo Suficiente:** Não é possível sacar um valor maior do que o saldo disponível.

## 🛠️ Como Usar

Para executar este sistema bancário, siga os passos abaixo:

1.  **Clone o Repositório (ou baixe o arquivo):**
    ```bash
    git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
    cd SEU_REPOSITORIO
    ```
    (Substitua `SEU_USUARIO` e `SEU_REPOSITORIO` pelos seus dados)

2.  **Execute o Script Python:**
    Abra um terminal na pasta onde o arquivo `banco.py` (ou o nome que você deu ao seu arquivo) está salvo e execute o seguinte comando:
    ```bash
    python banco.py
    ```

3.  **Interaja com o Menu:**
    O sistema exibirá um menu. Digite a letra correspondente à opção desejada e pressione `Enter`:
    * `d` para Depositar
    * `s` para Sacar
    * `e` para ver o Extrato
    * `q` para Sair

    Durante as operações de depósito e saque, você será perguntado se deseja continuar na mesma operação ou voltar ao menu inicial.

## 💡 Observações de Desenvolvimento

* Este projeto é uma ferramenta didática e não deve ser usado para transações financeiras reais.
* Todas as informações (saldo, extrato) são voláteis e não são salvas após o fechamento do programa.
* A validação de entrada de valores numéricos foi feita usando `isdigit()` e conversão para `float()`. Para aceitar valores decimais (ex: `10.50`), o código converte a string para float. Note que `isdigit()` por si só não valida decimais, mas a conversão para `float` lida com isso. Mensagens de erro apropriadas são exibidas para entradas inválidas.

## 🤝 Como Contribuir (Opcional para Iniciantes)

Se você estiver estudando Python e quiser praticar, sinta-se à vontade para:

* Abrir "Issues" para sugerir melhorias ou encontrar bugs.
* Fazer um "Fork" do projeto e enviar "Pull Requests" com suas implementações, como:
    * Adicionar validação de CPF ou número de conta.
    * Implementar a criação de usuários/contas.
    * Salvar dados em um arquivo (CSV, TXT, JSON) para persistência.
    * Melhorar a interface do usuário no console.

## Licença

Este projeto está sob a licença [MIT](https://opensource.org/licenses/MIT).
