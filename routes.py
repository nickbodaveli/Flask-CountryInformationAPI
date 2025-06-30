from flask import render_template, request
import requests

def register_routes(app):
    
    @app.route('/', methods=['GET', 'POST'])
    def index():
        country_info = None
        error = None

        if request.method == 'POST':
            country_name = request.form.get('country')
            url = f"https://restcountries.com/v3.1/name/{country_name}"

            try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()[0]

                country_info = {
                    'name': data['name']['common'],
                    'capital': data['capital'][0],
                    'region': data['region'],
                    'population': data['population'],
                    'flag': data['flags']['svg'],
                    'languages': ', '.join(data['languages'].values())
                }

            except Exception as e:
                error = "Country not found or API error"

        return render_template('index.html', country=country_info, error=error)
