# PYzza_projeto_ADS 🍕💻📚
<div align= "left">
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" /> <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" /> <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" /> <img src="ttps://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" /> 
</div>
<h3>Sistemas de Informação para pizzarias</h3>

Projeto desenvolvido para a conclusão do curso de ADS - Faculdade Impacta

O projeto teve seu início com o levantamento e análise dos problemas mais comuns encontrados por restaurantes que nos levou a formular uma lista de necessidades desencadeando numa descrição dos processos de negócio, análise de eventos e modelo conceitual para então elencar os requisitos de sistema de maneira mais assertiva. 

Como resultado de toda esta análise, a escolha do grupo foi começar a desenvolver o sistema a partir do gerenciamento de estoque, ainda que outros problemas como delivery e controle do salão também fossem relevantes. Tendo como princípio as metodologias ágeis de desenvolvimento, o plano de ação foi implementar funcionalidades aos poucos para que fosse possível realizar entregas progressivas e constantes, de um sistema funcional. 

Com o objetivo de colocar em prática alguns dos conhecimentos adquiridos durante o curso, optamos por fazer uso do framework Django que tem por base a linguagem de programação Python. O sistema utiliza o banco de dados SQLite, que já vem integrado com Django. Pensando na interface com usuário, fizemos uso do boostrap com o objetivo de proporcionar uma aparência mais amigável. 

A escolha das ferramentas citadas foi feita considerando também o curto prazo para o desenvolvimento, que aconteceu dentro de um período de 4 meses. 

Ao final do semestre foi possível entregar um sistema que cumpre as seguintes funções:
<!--ts-->
* Cadastro de Fornecedores
* Cadastro de Produtos
* Registro de entrada de Produtos
* Registro de saída de Produtos 
* Visualização do histórico de entradas e saídas
* Consulta e alteração de dados de Fornecedores
* Consulta da quantidade de produtos em estoque
<!--te-->

<h3> Instruções para instalação: </h3>
---> Instale as biliotecas listadas no requirements.txt

Em seguida será necessário criar as tabelas no banco de dados através dos comandos:
```
python manage.py makemigrations
python manage.py migrate
```
Feito isso já é possível inicializar o sistema com o comando
```
python manage.py runserver
```
<div align: "center">
<h3>Grupo:</h3>
● Hariel Cardoso Lopes <br>● Lethícia Antunes Soares ● Luis Felipe Ortega Ventura <br>● Stalin Fernando Santos Oliveira Miranda <br>● Thiago dos Santos Soares <br>● Wellington Jorge Vieira
</div>
