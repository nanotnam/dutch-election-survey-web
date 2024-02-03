from sqlalchemy import create_engine, text
import os
import pandas as pd 

db_connection_string = "mysql+pymysql://c9d38g1a0fhpdct3x9yv:pscale_pw_Y5bQqjknhHupgdAnBdrV3KEUxev1XBOucxYAdzUxgKZ@aws.connect.psdb.cloud/dutch_election_survey_test?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={
        "ssl": {
            "ca": "/etc/ssl/cert.pem"
        }
    })


with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM dutch_election_survey_test.survey where year_survey = 2023"))
    data2023 = []
    for row in result.all():
        data2023.append(row._mapping)
print(data2023)

df = pd.DataFrame(data2023).fillna('N/A')

df.to_html('templates/data_2023.html')


