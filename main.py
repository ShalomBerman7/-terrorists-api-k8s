from fastapi import UploadFile, FastAPI
import pandas as pd
import uvicorn
from models import file_handling

app = FastAPI()


@app.post('/top-threats')
def load_csv_file(file: UploadFile):
    try:
        df = pd.read_csv(file.file)
        return file_handling(df)
    except:
        raise 'No file was inserted or the inserted file is not a csv.'


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
