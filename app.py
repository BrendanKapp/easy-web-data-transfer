from flask import Flask, request, render_template
import os

app = Flask(__name__)

def save_text(text, name: str):
    filename = "data/" + name + ".txt"
    if os.path.exists(filename):
        return False, "File " + filename + ".txt already exists!"
    try:
        with open(filename, 'w') as file:
            file.writelines(text)
    except:
        return False, "Writing data failed!"
    return True, "Success"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['data']
        name = request.form['name']
        success, message = save_text(data, name)
        if success == False:
            return render_template('index.html', data=data, name=name, result="Error: " + message)
        return render_template('index.html', data='', name='', result=("Saved data to: " + name + ".txt"))
    return render_template('index.html', data='', name='', result="No Data Saved")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
