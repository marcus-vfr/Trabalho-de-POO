# Trabalho-de-POO

# Sistema de Caixa Eletrônico em Python

## Descrição

Este projeto consiste na implementação de um sistema de caixa eletrônico (ATM) utilizando **Programação Orientada a Objetos (POO)** em Python.

O sistema permite a criação e gerenciamento de contas bancárias, simulando operações básicas como depósito, saque, consulta de saldo e histórico de transações.

---

## Funcionalidades

* Criar conta (Corrente ou Poupança)
* Depositar dinheiro
* Sacar dinheiro
* Consultar saldo
* Visualizar histórico de operações

---

## Conceitos de POO Aplicados

### Pacotes

O sistema foi organizado em múltiplos módulos para melhor separação de responsabilidades:

```
banco/
├── contas/
├── clientes/
├── operacoes/
├── historico/
├── sistema/
├── utils/
└── main.py
```

---

### Classes e Objetos

Foram implementadas as seguintes classes principais:

* `Conta`
* `Cliente`
* `Operacao`
* `Historico`
* `Banco`

---

### Herança

As classes:

* `ContaCorrente`
* `ContaPoupanca`

herdam da classe base `Conta`.

---

### Polimorfismo

O método `sacar()` foi sobrescrito nas subclasses:

* Conta Corrente permite limite extra
* Conta Poupança não permite saldo negativo

---

### Agregação

A classe `Banco` mantém várias contas, mas as contas podem existir independentemente.

---

### Composição

Cada `Conta` possui um `Historico`, que só existe junto com ela.

---

### Encapsulamento

Os atributos das classes são privados e acessados por métodos (getters), garantindo segurança dos dados.

---

## Regras de Negócio

* Não é permitido sacar com saldo insuficiente
* Todas as operações são registradas no histórico
* Entradas do usuário são validadas
* Mensagens claras são exibidas no terminal

---

## Interface

O sistema utiliza uma interface simples via terminal com menu interativo:

```
1 - Criar Conta
2 - Depositar
3 - Sacar
4 - Consultar Saldo
5 - Histórico
0 - Sair
```

---


