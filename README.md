# Constante de Kaprekar (6174)

## Introdução

Este projeto implementa a **Rotina de Kaprekar**, um processo matemático que, a partir de um número de 4 dígitos válido, reorganiza seus dígitos e realiza subtrações sucessivas até atingir o valor **6174**.

O programa foi desenvolvido conforme regras específicas da disciplina, com foco em lógica de programação e uso de estruturas básicas.

---

## Tecnologias

* Python (Google Colab)
* Estruturas utilizadas:

  * `if`, `elif`, `else`
  * `while`
  * Operações aritméticas (`//` e `%`)

---

## Como funciona

1. O usuário informa um número de até 4 dígitos
2. O programa valida:

   * Número positivo
   * Intervalo válido (0000 a 9999)
   * No máximo dois dígitos iguais
3. O algoritmo:

   * Forma o maior número possível (NDD)
   * Forma o menor número possível (NDC)
   * Subtrai: `NDD - NDC`
4. Repete o processo até chegar em **6174**

---

## Como rodar o projeto

1. Abra o Google Colab
2. Copie e cole o código no ambiente
3. Execute a célula
4. Insira um número válido quando solicitado

O programa exibirá todas as iterações até atingir a constante de Kaprekar.

---

## Contribuição

Este projeto foi desenvolvido para fins acadêmicos.
