from sqlalchemy import create_engine, text
import pandas as pd
db_connection_string = "mysql+pymysql://eczhgv400sk3tzauhqvx:pscale_pw_i55LhYRqEiKAvz5YDs4e6K4hePrUbQXMcZD5V5mvsh8@aws.connect.psdb.cloud/dutch_election_survey?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={
        "ssl": {
            "ca": "/etc/ssl/cert.pem"
        }
    })

def load_year_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT distinct year_survey FROM dutch_election_survey.survey"))
        data2023 = []
        for row in result.all():
            data2023.append(row._mapping)
            df = pd.DataFrame(data2023).fillna('N/A')
        return df


def load_data_w_year(year_list):
    with engine.connect() as conn:
        query = text("SELECT * FROM dutch_election_survey.survey WHERE year_survey IN (:years)")
        result = conn.execute(query, {'years': year_list})
        data2023 = []
        for row in result.all():
            data2023.append(row._mapping)
            df = pd.DataFrame(data2023).fillna('N/A')
        return df
