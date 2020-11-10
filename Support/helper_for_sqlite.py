import sqlite3

def readSingleRow(developerId):
    try:
        sqliteConnection = sqlite3.connect('neflix_data_store.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        print("request in helper: " + developerId)
        sqlite_select_query = """SELECT * from netflix_data_sql where nameofshow LIKE ?"""
        cursor.execute(sqlite_select_query, ('%' + developerId + '%',))
        print("Reading single row \n")
        record = cursor.fetchone()
        print("nameofshow: ", record[0])
        print("url: ", record[1])
        return_sqlUrl= (record[1])
        cursor.close()

    #except sqlite3.Error as error:
    except TypeError as error:
        print("Failed to read single row from sqlite table", error)
        return_sqlUrl = 'not_in_database'
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")
    #print(return_sqlUrl)        
    return return_sqlUrl
        

def delete_all_raws():
    sqliteConnection  = sqlite3.connect('neflix_data_store.db')
    cursor = sqliteConnection .cursor()

# delete all rows from table
    cursor.execute('DELETE FROM netflix_data_sql;',);

    print('We have deleted', cursor.rowcount, 'records from the table.')

    sqliteConnection.commit()
    sqliteConnection.close()


