from flask import Flask, render_template, request
from sqlalchemy import create_engine, text
from database import load_year_from_db, load_data_w_year

app = Flask(__name__)


@app.route("/")
def hello_world():
    a = load_year_from_db()
    year_list = a['year_survey'].tolist()
    return render_template("home.html",
                           year_list = year_list)

@app.route('/filter', methods=['GET'])
def filter_data():
    # Fetch checkbox options from the request object
    selected_years = []
    for year in range(2020, 2034):  # Assuming the range of years
        if request.args.get(str(year)):
            selected_years.append(str(year))
    # Query the database based on selected options using SQLAlchemy
    # Use selected_options dictionary to construct your filter query
    filtered_data = load_data_w_year(selected_years)
    # Render template with filtered data
    return render_template('filtered.html', filtered_data=filtered_data)

if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug=True)

