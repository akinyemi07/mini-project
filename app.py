from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for expenses
expenses = []

@app.route('/')
def index():
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        name = request.form['name']
        amount = float(request.form['amount'])
        expenses.append({'name': name, 'amount': amount})
        return redirect(url_for('index'))
    return render_template('add_expense.html')

@app.route('/view')
def view_expenses():
    return render_template('view_expenses.html', expenses=expenses)

if __name__ == '__main__':
    app.run(debug=True)
