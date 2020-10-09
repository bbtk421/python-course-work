import sqlite3

conn = sqlite3.connect('test2.db')

with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_files( \
                        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                        col_fname TEXT)')
    conn.commit()
conn.close()

fileList = ('info.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conn = sqlite3.connect('test2.db')

with conn:
    cur = conn.cursor()
    for file in fileList:
        if file.endswith('.txt'):
            cur.execute('INSERT INTO tbl_files(col_fname) VALUES(?)',(file,))
            print(file)
    conn.commit()
conn.close()

conn = sqlite3.connect('test2.db')

with conn:
    cur = conn.cursor()
    cur.execute('SELECT * FROM tbl_files')
    results = cur.fetchall()
    print(results)
conn.close()
