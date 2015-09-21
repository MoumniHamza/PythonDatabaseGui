import sqlite3
connection = sqlite3.connect('game.db')



def createTable():
    connection.execute("CREATE TABLE if not exists persons(id INTEGER PRIMARY KEY AUTOINCREMENT, \
                                         name TEXT, \
                                         gender TEXT, \
                                         occupation TEXT, \
                                         age INT);")

def printData(data):
    for name in data:
        print " id: ", name[0]
        print "name: ", name[1]
        print "gender: ", name[2]
        print "occupation: ", name[3]
        print "age: ", name[4]



def newPerson(name,gender,age,occupation):
    print(" Adding a new character")
    string_value = (" '{}', '{}', '{}', {} ").format(name,gender,occupation,age) 
    print(string_value)
    insert_value = "INSERT INTO PERSONS(name,gender,occupation,age) VALUES({});".format(string_value)
    print(insert_value)
    connection.execute(insert_value)
    connection.commit()
    return connection.total_changes

def checkPerson():
    select_value = "SELECT * FROM persons";
    selection = connection.execute(select_value)
    rows = selection.fetchall()
    return rows

def updateCharacter(change_id,name,gender,age,occupation):
    # Create values part of sql command
    val_str = "NAME='{}', GENDER='{}',\
              AGE={}, OCCUPATION='{}'".format(\
              name, gender, age, occupation)
    
    sql_str = "UPDATE persons set \
       {} where ID={};".format(val_str,change_id)
    print sql_str
    
    conn.execute(sql_str)
    conn.commit()
    return conn.total_changes


def deletePerson(change_id):
       select_specificperson = "DELETE FROM persons WHERE ID = '{}';".format(change_id)
       connection.execute(select_specificperson)
       connection.commit()
       return connection.total_changes


createTable()
