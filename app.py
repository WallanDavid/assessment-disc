from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

competencias = [
    "Comunicação",
    "Trabalho em equipe",
    "Organização",
    "Criatividade",
    "Responsabilidade",
    "Liderança"
]

RESULTS_FILE = 'results.json'

def salvar_resultado(notas):
    resultados = []
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, 'r', encoding='utf-8') as f:
            try:
                resultados = json.load(f)
            except json.JSONDecodeError:
                resultados = []
    resultados.append(notas)
    with open(RESULTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)

def calcular_media(notas):
    return round(sum(notas) / len(notas), 2)

def classificacao(media):
    if media < 2:
        return "Ruim"
    elif media < 3.5:
        return "Regular"
    else:
        return "Bom"

def perfil_automatico(notas):
    max_index = notas.index(max(notas))
    return competencias[max_index]

@app.route('/')
def index():
    return render_template('index.html', competencias=competencias)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    notas = data.get('notas')

    # Validar notas
    if not notas or not all(isinstance(n, int) and 1 <= n <= 5 for n in notas):
        return jsonify({"erro": "Notas inválidas. Cada nota deve ser entre 1 e 5."}), 400

    salvar_resultado(notas)

    media = calcular_media(notas)
    classific = classificacao(media)
    perfil = perfil_automatico(notas)

    return jsonify({
        "competencias": competencias,
        "notas": notas,
        "media": media,
        "classificacao": classific,
        "perfil": perfil
    })

@app.route('/history')
def history():
    resultados = []
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, 'r', encoding='utf-8') as f:
            try:
                resultados = json.load(f)
            except json.JSONDecodeError:
                resultados = []
    return render_template('history.html', resultados=resultados, competencias=competencias)

if __name__ == '__main__':
    app.run(debug=True)
