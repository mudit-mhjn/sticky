import pandas

def get_note(num):
    df = pandas.read_csv("./note_db.csv")
    if num == "all":
        print(df.loc[:,['note_id','note_head','note_body']])
    else:
        n = int(num)
        print(df.loc[n-1,['note_id','note_head','note_body']])
