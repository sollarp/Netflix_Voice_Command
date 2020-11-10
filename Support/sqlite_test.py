import sqlite3


conn = sqlite3.connect('neflix_data_store.db')
c = conn.cursor()

#def create_table():
c.execute("CREATE TABLE IF NOT EXISTS netflix_data_sql(nameofshow TEXT, url TEXT, UNIQUE(nameofshow,url) )")

def data_entry(movie_name, url_link):
    #num = input('Salesman ID:')
    #movie_name = input('Name:')
    #url_link = input('City:')
    c.execute("""INSERT OR REPLACE INTO netflix_data_sql(nameofshow, url)VALUES(?,?)""",(movie_name, url_link))
    print("searching...")
    
    conn.commit()
    #c.close()
    #conn.close()
#create_table()
#data_entry()