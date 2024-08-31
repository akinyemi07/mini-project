from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for tasks
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    if request.method == 'POST':
        tasks[task_id] = request.form['task']
        return redirect(url_for('index'))
    return render_template('edit_task.html', task=tasks[task_id])

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
