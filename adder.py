import pandas

def add_note(note_head, note_main):
    df = pandas.read_csv("./note_db.csv")
    present_rows = df.shape[0]
    new_tuple = pandas.DataFrame({'note_id':present_rows+1,'note_head':note_head,'note_body':note_main,'active':1,'note_created':None,'note_updated':None},index=[present_rows])
    df = pandas.concat([new_tuple,df]).reset_index(drop=True)
    print(df)
