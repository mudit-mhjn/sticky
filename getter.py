import pandas

def get_note():
    df = pandas.read_csv("./note_db.csv")
    print(df)
    pass
