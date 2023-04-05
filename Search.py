from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# load the medicine data from an Excel file into a pandas DataFrame
medicines = pd.read_excel('Sheet.xlsx')

@app.route('/')
def index():
    return render_template('Web.html')

@app.route('/search', methods=['POST'])
def search():
    # get the medicine name entered by the user
    medicine_name = request.form['medicine_name']
    
    # search for the medicine in the DataFrame and retrieve its usage and side effects
    try:
        medicine_data = medicines.loc[medicines['drug_name'] == medicine_name]
        usage = medicine_data.iloc[0]['medicine_condition']
        side_effects = medicine_data.iloc[0]['side_effects']
        return render_template('result.html', name=medicine_name, usage=usage, side_effects=side_effects)
    except IndexError:
        return render_template('error.html', name=medicine_name)

if __name__ == '__main__':
    app.run(debug=True)
