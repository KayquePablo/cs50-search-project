from flask import Flask, render_template, request

app = Flask(__name__)

# Lista simulada de resultados de pesquisa
search_results = [
    "Apple", "Banana", "Orange", "Pineapple", "Grapes", "Mango", "Lemon", "Strawberry"
]

# Função para buscar o termo dentro da lista
def search(query):
    return [result for result in search_results if query.lower() in result.lower()]

@app.route("/", methods=["GET", "POST"])
def index():
    query = None
    results = []
    
    # Se o método for POST, processa a pesquisa
    if request.method == "POST":
        query = request.form.get("query")
        if query:
            results = search(query)
    
    return render_template("index.html", query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)
