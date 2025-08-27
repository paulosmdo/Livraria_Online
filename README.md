
# 📚 Desafio TSMX - Livraria Online  

Este projeto consiste em um desafio de desenvolvimento utilizando o framework **Django** para a criação de uma aplicação de **Livraria Online**.  
A camada de estilização foi implementada com **TailwindCSS**, e o banco de dados utilizado é o **PostgreSQL**.  

---

## Tecnologias Utilizadas
- **Django** – Backend & Frontend
- **TailwindCSS** – Estilização responsiva e moderna  
- **PostgreSQL** – Banco de dados relacional  
- **Docker + Docker Compose** – Gerenciamento do ambiente de execução  



---

## Como rodar o projeto
### 1ª Opção – Docker (Recomendada)  
⚙️ **Pré-requisito**: Docker instalado na máquina  
1. Clone este repositório:  
   ```bash
   git clone https://github.com/paulosmdo/Livraria_Online.git
   cd Livraria_Online   
2. Construa e inicialize os containers com o Docker Compose:
	 ```bash
	 docker compose build --no-cache && docker compose up -d
3. Acesse a aplicação no navegador:
	```bash	
	http://localhost:8000
### 2° Opção Instalação Manual:
⚙️ Pré-requisitos: Python v3,12 + PostgreSQL >= 14
1. Clone este repositório:  
   ```bash
   git clone https://github.com/paulosmdo/Livraria_Online.git
   cd Livraria_Online/Livraria   
 2. Crie e ative um ambiente virtual:
	 ```bash
	 python -m venv venv
	 source venv/bin/activate
 3. Instale as dependências:
	 ```bash
	 pip  install  -r  requirements.txt
 4. Configure as variáveis de ambiente:
	 No arquivo `config/settings.py`, localize as chamadas para `os.getenv` e insira os valores diretamente, caso não utilize variáveis de ambiente.
 5. Execute as migrações do banco de dados:
	 ```bash
	 python manage.py migrate
 6. Inicie a aplicação:
	 ```bash
	 python manage.py runserver
7. Acesse a aplicação no navegador:
	```bash	
	http://localhost:8000
### 3° Opção – Hospedagem em Nuvem (Vercel + NeonDB):
**Observação:** a funcionalidade de **exportação de PDF** foi removida devido a limitações da infraestrutura gratuita da Vercel.
1. Acesse a aplicação diretamente pelo link:
	```bash	
	https://livraria-online-tsmx.vercel.app/
