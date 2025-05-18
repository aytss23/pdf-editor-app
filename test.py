import sqlite3 

database_conn = sqlite3.connect('utils\\database\\recent_pdfs.db')

database_cursor = database_conn.cursor()

is_already_logged = False

recent_pdf = "Deneme3.pdf"
recent_pdfs = database_cursor.execute(""" SELECT FILE_PATH, LAST_EXEC_TIME FROM recent_pdfs """).fetchall()

print(recent_pdfs)

for row_data in range(len(recent_pdfs)):
    if recent_pdf == recent_pdfs[row_data][0]: is_already_logged = True


if not is_already_logged: print("data logged!")

else: print("data already logged!")
