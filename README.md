# 🎮 Projeto Final - Sistema de Gerenciamento de Loja de Jogos

## 📌 Objetivo do Projeto

Este projeto tem como finalidade principal o desenvolvimento de um **sistema de gerenciamento para uma loja de jogos**. Ele foi elaborado como parte do **projeto final de curso**, integrando conhecimentos de desenvolvimento de software, banco de dados e interfaces gráficas.

O sistema visa permitir o gerenciamento completo de uma loja, incluindo **cadastro de clientes, controle de produtos, gerenciamento de vendas, login de usuários** e geração de relatórios.

---

## 🧩 Tecnologias e Conceitos Utilizados

- Python (linguagem principal)
- Tkinter (interfaces gráficas)
- MySQL (banco de dados relacional)
- Arquitetura MVC (Model - View - Controller)
- Boas práticas de organização de código e documentação

---

## 🛠️ Funcionalidades do Sistema

- Cadastro, edição e remoção de **produtos**
- Registro de **clientes**
- Processamento e controle de **vendas**
- Sistema de **login com autenticação de usuários**
- Geração de **relatórios de vendas**
- Interface gráfica intuitiva
- Estrutura em **camadas** para fácil manutenção

---

## 🧱 Estrutura de Diretórios

A organização do projeto foi feita de forma modular para facilitar a manutenção, separando responsabilidades de acordo com o padrão MVC:

``` 
projeto_loja_jogos/
│
├── app/
│ ├── controllers/ # Controladores da lógica de negócio
│ │ ├── cliente_controller.py
│ │ ├── produto_controller.py
│ │ ├── usuario_controller.py
│ │ └── venda_controller.py
│ │
│ ├── models/ # Definição das entidades e suas regras
│ │ ├── cliente_model.py
│ │ ├── produto_model.py
│ │ ├── usuario_model.py
│ │ ├── venda_model.py
│ │ └── itens_venda_model.py
│ │
│ ├── views/ # Telas (GUI) desenvolvidas com Tkinter
│ │ ├── cliente_view.py
│ │ ├── login_view.py
│ │ ├── main_view.py
│ │ ├── produto_view.py
│ │ ├── relatorio_view.py
│ │ └── venda_view.py
│ │
│ ├── database/ # Scripts e conexão com o banco de dados
│ │ ├── conexao.py
│ │ └── criar_tabelas.sql
│ │
│ ├── main.py # Arquivo principal para executar o sistema
│ └── init.py
│
├── docs/ # Documentos e diagramas do projeto
│ ├── algoritmo.txt
│ ├── DER.txt
│ ├── modelo_banco.png
│ └── requeriments.txt
│
├── .env.example # Exemplo de configuração de ambiente
├── .gitignore # Padrões de arquivos ignorados pelo Git
└── README.md # Apresentação geral do projeto

```

---

## 🗃️ Banco de Dados

O banco de dados utilizado é **SQLite**, simples e eficiente para aplicações desktop. O arquivo `criar_tabelas.sql` contém todos os comandos necessários para criação das tabelas.

As principais tabelas são:

- `cliente`
- `produto`
- `usuario`
- `venda`
- `itens_venda`

O relacionamento entre essas tabelas foi previamente modelado com base no **DER** presente na pasta `docs`.

---

## 🖥️ Interface do Usuário

A interface foi criada com a biblioteca **Tkinter**, nativa do Python, proporcionando uma experiência gráfica amigável para o usuário. As telas contemplam:

- Tela de login
- Cadastro de clientes
- Cadastro de produtos
- Tela de vendas
- Geração de relatórios

Cada tela possui validações e está conectada às camadas de modelo e controle.

---

## 📄 Documentação Complementar

A pasta `docs/` contém os seguintes arquivos de apoio:

- `algoritmo.txt`: Explicação textual da lógica implementada
- `DER.txt`: Descrição das entidades e relacionamentos do banco de dados
- `modelo_banco.png`: Imagem do modelo do banco
- `requeriments.txt`: Lista de bibliotecas utilizadas no projeto

---

## 📌 Conclusão

Este projeto representa o **trabalho final de um curso de programação**, integrando conhecimento em desenvolvimento de software com banco de dados, interfaces gráficas e estruturação de projetos.

Ele fornece uma base sólida para evolução futura, podendo ser facilmente adaptado para aplicações comerciais, lojas físicas ou virtuais.

---

## Autor: Nathan Lemos, com orientações do chat gpt