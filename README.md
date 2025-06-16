
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
- 🆕 **Cadastro de Usuário (com CPF, nome, data de nascimento e endereço)**
- 🏦 **Abertura de Conta Bancária vinculada ao CPF do usuário**
- 📜 **Listagem de Contas**
- 🔧 **Código refatorado usando funções para melhor organização, legibilidade e manutenção**
- 🎨 **Menu aprimorado com melhor apresentação no terminal**

---

## 📜 Regras de Negócio (Válidas para V1 e V2)

- ✅ Cliente pode realizar depósitos de qualquer valor positivo.
- ✅ O saque possui limite de **R$ 500,00 por operação** e no máximo **3 saques por dia**.
- ❌ O sistema não permite operações com valores **negativos** ou **zerados**.
- ✅ Cada conta está vinculada a um **CPF cadastrado**.
- ❌ O sistema não permite dois usuários com o mesmo CPF.
- ✅ Todas as operações ficam registradas no **extrato da conta**.

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

### ▶️ Executar versão 2 (otimizada com funções e cadastro de usuários):
```bash
python sistema_bancario_v2.py
```

> ⚠️ **Pré-requisitos:** É necessário ter o **Python instalado** na sua máquina.  
👉 [Download Python](https://www.python.org/downloads/)

---

## 📂 Estrutura do Projeto

```
📁 sistema-bancario-python
├── 📄 sistema_bancario_v1.py    # Primeira versão (básica)
├── 📄 sistema_bancario_v2.py    # Segunda versão (refatorada com funções e melhorias)
└── 📄 README.md                 # Documentação do projeto
```

---

## 👨‍💻 Autor

Desenvolvido por [**Wendell Ribeiro Nogueira**](https://www.linkedin.com/in/wendell-ribeiro-nogueira-2a285723/) 🧠💻

---

## 🏆 Créditos

Projeto realizado durante o **Bootcamp Santander 2025** promovido pela [DIO - Digital Innovation One](https://www.dio.me/).
