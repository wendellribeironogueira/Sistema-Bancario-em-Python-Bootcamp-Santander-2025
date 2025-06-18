
# 🏦 Sistema Bancário em Python - **Bootcamp Santander 2025**

Este projeto foi desenvolvido como parte do **Bootcamp Santander 2025** da [Digital Innovation One (DIO)](https://www.dio.me/). O objetivo é construir um sistema bancário simples, rodando no terminal, que simula operações bancárias como **depósito, saque, extrato, cadastro de usuários e criação de contas**.

---

## 🚀 Funcionalidades por Versão

### 🔖 **Versão 1 - sistema_bancario_v1.py**
- 📥 **Depósito**
- 💸 **Saque** (limite de até R$ 500 por operação e até 3 saques diários)
- 📑 **Extrato**
- ⛔ **Sair**
- ✅ **Menu simples e funcional**

---

### 🔖 **Versão 2 - sistema_bancario_v2.py**
- Todas as funcionalidades da **versão 1**
- 🆕 **Cadastro de Usuário** (CPF, nome, data de nascimento e endereço)
- 🏦 **Abertura de Conta Bancária vinculada ao CPF do usuário**
- 📜 **Listagem de Contas**
- 🔧 **Código refatorado usando funções**, melhorando organização, legibilidade e manutenção
- 🎨 **Menu aprimorado com melhor apresentação no terminal**

---

### 🔖 **Versão 3 - sistema_bancario_v3.py**
- 🔥 **Refatoração completa aplicando Programação Orientada a Objetos (POO)**
- 🧠 Uso de conceitos como:
  - ✅ Classes e Objetos
  - ✅ Herança (`Cliente` → `PessoaFisica`, `Conta` → `ContaCorrente`)
  - ✅ Abstração e Classes Abstratas (`Transacao`)
  - ✅ Composição (`Conta` possui um `Historico`)
- 📜 Histórico de transações com registro de data, tipo e valor
- 🔗 Sistema permite múltiplas contas por cliente (CPF)
- ✅ Validação de limites de saque por valor e quantidade
- 🏦 Cadastro de clientes, abertura de contas, depósitos, saques e extrato por conta
- ✨ Código mais modular, robusto e preparado para expansão futura (como transferências ou API)

---

## 📜 Regras de Negócio

- ✅ Cliente pode realizar depósitos de qualquer valor **positivo**.
- ✅ O saque possui limite de **R$ 500,00 por operação** e no máximo **3 saques por dia**.
- ❌ O sistema não permite operações com valores **negativos** ou **zerados**.
- ✅ Cada conta está vinculada a um **CPF cadastrado**.
- ❌ O sistema não permite dois usuários com o mesmo CPF.
- ✅ Todas as operações ficam registradas no **extrato da conta**, com **data, tipo e valor**.
- ✅ Clientes podem possuir **múltiplas contas bancárias**.

---

## 🛠️ Tecnologias Utilizadas

- 🐍 **Python 3.x**
- 🔗 **Git e GitHub** para versionamento

---

## ▶️ Como Executar o Projeto

1. ✅ Clone este repositório:

```bash
git clone https://github.com/wendellribeironogueira/sistema-bancario-python.git
```

2. ✅ Acesse o diretório do projeto:

```bash
cd sistema-bancario-python
```

3. ✅ Execute a versão desejada:

### ▶️ Executar versão 1 (básica):
```bash
python sistema_bancario_v1.py
```

### ▶️ Executar versão 2 (com funções e cadastro de usuários):
```bash
python sistema_bancario_v2.py
```

### ▶️ Executar versão 3 (orientada a objetos):
```bash
python sistema_bancario_v3.py
```

> ⚠️ **Pré-requisitos:** Ter o **Python instalado** na sua máquina.  
👉 [Download Python](https://www.python.org/downloads/)

---

## 📂 Estrutura do Projeto

```
📁 sistema-bancario-python
├── 📄 sistema_bancario_v1.py    # Primeira versão (básica, com funções simples)
├── 📄 sistema_bancario_v2.py    # Segunda versão (funções aprimoradas, cadastro de usuário e conta)
├── 📄 sistema_bancario_v3.py    # Terceira versão (POO completa)
└── 📄 README.md                 # Documentação do projeto
```

---

## 👨‍💻 Autor

Desenvolvido por [**Wendell Ribeiro Nogueira**](https://www.linkedin.com/in/wendell-ribeiro-nogueira-2a285723/) 🧠💻

---

## 🏆 Créditos

Projeto realizado durante o **Bootcamp Santander 2025** promovido pela [DIO - Digital Innovation One](https://www.dio.me/).

---
