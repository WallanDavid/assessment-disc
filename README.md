# 🚀 Autoavaliação de Desempenho

Uma aplicação web para realizar **autoavaliações de desempenho**, com resultados exibidos em um **gráfico radar interativo** e um histórico completo das avaliações feitas.

---

## ✨ Funcionalidades

- 📝 Formulário para avaliação com notas de 1 a 5 para várias competências  
- ✅ Validação de entrada no frontend para garantir dados corretos  
- 📊 Gráfico radar colorido (vermelho, amarelo, verde) indicando desempenho  
- 📚 Histórico de avaliações exibido em tabela clara e organizada  
- 📥 Download do gráfico gerado como imagem PNG  

---

## 🛠 Tecnologias Utilizadas

- 🐍 Python 3 + Flask  
- 🌐 HTML5, CSS3, JavaScript  
- 📈 Chart.js para gráficos dinâmicos  
- 🧩 Jinja2 para templates HTML  

---

## ⚙️ Como Rodar Localmente

```bash
git clone https://github.com/WallanDavid/assessment-disc.git
cd assessment-disc
python -m venv venv

# Ative o ambiente virtual:
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

pip install flask
flask run
Abra no navegador: http://127.0.0.1:5000


📂 Estrutura do Projeto
.
├── app.py            # Backend Flask
├── results.json      # Armazenamento de resultados
├── users.json        # Armazenamento de usuários
├── templates/        # Templates Jinja2 (HTML)
│   ├── base.html
│   ├── history.html
│   └── index.html
└── static/           # Arquivos estáticos (CSS, JS, imagens)


✍️ Autor
Wallan David

📄 Licença
Este projeto está sob a licença MIT License — sinta-se livre para usar, modificar e compartilhar!
