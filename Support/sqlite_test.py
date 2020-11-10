import sqlite3

conn = sqlite3.connect('neflix_data_store.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS netflix_data_sql(nameofshow TEXT, url TEXT, UNIQUE(nameofshow,url) )")

def data_entry(movie_name, url_link):
    c.execute("""INSERT OR REPLACE INTO netflix_data_sql(nameofshow, url)VALUES(?,?)""",(movie_name, url_link))
    conn.commit()
