# 🔐 Gerador de Senhas Seguras (Tkinter)

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/) 
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)](https://docs.python.org/3/library/tkinter.html) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  
[![Contribuições](https://img.shields.io/badge/Contribuições-Bem--vindas-orange.svg)](../../issues)

Um aplicativo em **Python + Tkinter** para gerar senhas seguras de forma prática.  
As senhas podem ser copiadas para a área de transferência e também são salvas automaticamente em um arquivo de histórico (`senhas_geradas.txt`).

---

## 📸 Screenshot

<p align="center">
  <img src="screenshot.png" alt="Interface do Gerador de Senhas" width="500"/>
</p>

---

## 🚀 Funcionalidades
- Gerar senhas seguras com:
  - Apenas **Letras** (maiúsculas e minúsculas)
  - **Letras + Números**
  - **Completa** (letras, números e símbolos)
- Escolher o tamanho da senha
- Copiar a senha gerada para a área de transferência
- Salvar automaticamente todas as senhas em `senhas_geradas.txt`
- Tela de **Sobre** com informações do app
- Interface gráfica amigável feita com **Tkinter**

---

## 🖥️ Pré-requisitos

- Python **3.10+** (recomendado)
- Nenhuma biblioteca externa é necessária (apenas módulos padrão `tkinter`, `secrets` e `string`)

Verifique se o Tkinter está instalado (vem por padrão na maioria das instalações do Python).  
Para testar:

```bash
python -m tkinter

📦 Como executar

Clone este repositório ou baixe os arquivos:

git clone https://github.com/seu-usuario/gerador-senhas.git
cd gerador-senhas

Execute o programa:

python pass.py

A interface gráfica será aberta:

Escolha o tamanho e o tipo da senha

Clique em Gerar Nova Senha

Copie ou utilize a senha como desejar


📂 Estrutura do Projeto

📦 gerador-senhas
 ┣ 📜 gerador_senhas.py      # Código principal do aplicativo
 ┣ 📜 senhas_geradas.txt     # Arquivo onde as senhas são salvas
 ┗ 📜 README.md              # Documentação do projeto


📖 Sobre

Gerador de Senhas v1.2
Criado por m4ntonio
 – 2025 😎
Desenvolvido com Python e Tkinter

⚖️ Licença

Distribuído sob a licença MIT. Veja o arquivo LICENSE
 para mais detalhes.
