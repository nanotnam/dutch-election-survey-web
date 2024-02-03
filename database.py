from sqlalchemy import create_engine, text
import pandas as pd
import os
db_connection_string = os.environ.get('db_connection_string')

engine = create_engine(db_connection_string,
                       connect_args={
        "ssl": {
            "ca": "/etc/ssl/cert.pem"
        }
    })

def load_year_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT distinct year_survey FROM dutch_election_survey.survey"))
        year = []
        for row in result.all():
            year.append(row._mapping)
            df = pd.DataFrame(year).fillna('N/A')
        return df



def load_data_w_year(year_list):
    with engine.connect() as conn:
        query = f"SELECT * FROM dutch_election_survey.survey WHERE year_survey IN ({', '.join(str(year) for year in year_list)})"
        result = conn.execute(text(query))
        
        return result.all()
