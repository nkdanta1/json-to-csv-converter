from flask import Flask, render_template, request, make_response
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    json_data = request.json
    df = pd.json_normalize(json_data)
    csv_data = df.to_csv(index=False)

    response = make_response(csv_data)
    response.headers['Content-Disposition'] = 'attachment; filename=data.csv'
    response.headers['Content-Type'] = 'text/csv'

    return response

if __name__ == "__main__":
    app.run(debug=True)
