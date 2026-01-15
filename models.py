from pydantic import BaseModel, Field
from db import insert_mongodb


def file_handling(df):
    df = df.sort_values(by=["danger_rate"], ascending=[False])
    return selecting_the_top(df)


def selecting_the_top(df):
    df = df.head()
    return validation(df)


class Person(BaseModel):
    name: str
    location: str
    danger_rate: int = Field(..., ge=1, le=10)


def validation(df):
    validated = []
    for i, row in df.iterrows():
        person = Person(name=row["name"], location=row["location"], danger_rate=int(row["danger_rate"])
                        )
        validated.append(person)
    response = {"count": len(validated), "top": [person.dict() for person in validated]
                }
    try:
        insert_mongodb(response)
    except:
        raise 'Cant find the database.'
    return response
