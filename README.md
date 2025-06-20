Autoavaliação de Desempenho
Este projeto é uma aplicação web para realizar autoavaliações de desempenho, apresentando os resultados em um gráfico radar interativo e mantendo um histórico das avaliações feitas.

Funcionalidades
Formulário para avaliação com notas de 1 a 5 para várias competências.

Validação dos valores de entrada no frontend.

Gráfico radar dinâmico com cores indicativas para cada nota (vermelho, amarelo e verde).

Histórico das avaliações apresentadas em tabela.

Download do gráfico gerado como imagem PNG.

Tecnologias Utilizadas
HTML5, CSS3 e JavaScript (Chart.js)

Backend Python com Flask

Templates Jinja2 para renderização dinâmica

Como Rodar Localmente
Clone o repositório:
git clone https://github.com/WallanDavid/assessment-disc.git
cd assessment-disc

Crie e ative o ambiente virtual:
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows

Instale as dependências:
pip install flask

Execute a aplicação:
flask run

Abra no navegador:
http://127.0.0.1:5000

Estrutura do Projeto
app.py — arquivo principal do backend Flask

templates/ — arquivos HTML com Jinja2

static/ — arquivos estáticos (CSS, JS, imagens)

results.json e users.json — armazenamento local de dados simples

Autor
Wallan David

Licença
MIT License
