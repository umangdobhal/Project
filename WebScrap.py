from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Web.html')

@app.route('/search', methods=['GET'])
def search():
    drug_name = request.args.get('drug_name')
    search_url = f'https://www.1mg.com/search/all?name={drug_name}'
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = soup.find_all('div', {'class': 'col-md-3 col-sm-4 col-xs-6 style__container___jkjSb'})
    if len(search_results) == 0:
        return '<p>No results found.</p>'
    else:
        first_result = search_results[0]
        drug_url = first_result.find('a')['href']
        drug_response = requests.get(drug_url)
        drug_soup = BeautifulSoup(drug_response.text, 'html.parser')
        drug_info = drug_soup.find('div', {'class': 'DrugOverview__container___z4JUt'})
        return str(drug_info)

if __name__ == '__main__':
    app.run(debug=True)
