from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    erro = None

    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'].replace(',', '.'))  # aceita vírgula como separador decimal
            num2 = float(request.form['num2'].replace(',', '.'))
            operacao = request.form['operacao']

            if operacao == 'soma':
                resultado = num1 + num2
            elif operacao == 'subtracao':
                resultado = num1 - num2
            elif operacao == 'multiplicacao':
                resultado = num1 * num2
            elif operacao == 'divisao':
                if num2 == 0:
                    erro = "Erro: Divisão por zero não é permitida!"
                else:
                    resultado = num1 / num2
            else:
                erro = "Operação inválida!"

            # Formata o resultado (remove .0 quando inteiro)
            if resultado is not None and isinstance(resultado, float) and resultado.is_integer():
                resultado = int(resultado)

        except ValueError:
            erro = "Por favor, insira apenas números válidos!"

    return render_template('index.html', resultado=resultado, erro=erro)

if __name__ == '__main__':
    app.run(debug=True)
