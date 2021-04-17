from functions import tables_list
from important_lists import *
import sqlite3


def NextWord(search):
    #CONNECT TO DATABASE.
    conn = sqlite3.connect(DATABASE_PATH+DATABASE_NAME)
    cursor = conn.cursor()

    #SEARCH FOR THE IDs VALUE IN THE WORDS_TOTAL TABLE 
    cursor.execute(('SELECT ID FROM WORDS_TOTAL where WORD = "{}"').format(search))
    results=cursor.fetchall()
    conn.close()

    ids_for_searching=[]
    second_word_list=[]


    for result in results:
        #RESULTS OF THE SEARCH (IDs) ARE STORED IN A TEMPORARY TUPLE CALLED IDS_FOR_SEARCHING.
        result=result[0]
        ids_for_searching.append(result)
    
    for id in ids_for_searching:
        #GATHERING THE WORDS FROM THE NEXT ID FOR EVERY RESULT.

        #FINDING NEXT ID NUMBER
        id=id+1

        #SEARCHING THE WORD IN THE NEW ID.
        conn = sqlite3.connect(DATABASE_PATH+DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute(('SELECT WORD FROM WORDS_TOTAL where ID = "{}"').format(id))

        #FINDING THE SECOND WORD
        second_word=cursor.fetchall()
        conn.close()
        final_result=(second_word[0][0])
        final_result=final_result.replace('"',"")

        
        #INSERTING THE NEXT'S WORD IN THE TABLE NAMED AS THE SEARCH VALUE.
        print(("Inserting data in {}.").format(search))
        conn = sqlite3.connect(DATABASE_PATH+DATABASE_NAME)
        conn.execute(('INSERT INTO {} (WORD) VALUES ("{}")').format(search ,final_result))
        conn.commit()
        conn.close()
        print("COMPLETED")

def CreateSearchTable(search):
    #CREATE A NEW TABLE USING THE SEARCH VALUE AS NAME, ATTRIBUTES ARE: ID, WORD AND PROBABILITY
    print(("Creating {} table in the database.").format(search))
    conn = sqlite3.connect(DATABASE_PATH+DATABASE_NAME)
    conn.execute(('CREATE TABLE "{}" ("ID" INTEGER NOT NULL UNIQUE,"WORD" TEXT, "PROBABILITY" INTEGER, PRIMARY KEY("ID" AUTOINCREMENT));').format(search))
    conn.close
    print("COMPLETED")

def UpdateProbabilities(search):
    #CONNECT TO DATABASE.
    conn = sqlite3.connect(DATABASE_PATH+DATABASE_NAME)
    cursor = conn.cursor()

    #SEARCH HOW MUCH TIMES DOES THE SECOND WORD APPEAR FOR THE CURRENT TIME
    cursor.execute(('SELECT WORD, COUNT(*) FROM {} group by WORD ORDER BY COUNT(*) DESC').format(search))
    results=cursor.fetchall()
    conn.close() 

    
    """THIS COULD BE A FUNCTION THAT RETURNS THE TOTAL_TIMES_LIST"""
    #CAPUTING THE TOTAL AMOUNT OF TIMES SECOND'S WORDS WERE USED.
    total_times_list=[]
    #GETTING ALL THE TIMES, WORDS WERE USED
    for result in results:
        times=result[1]
        total_times_list.append(times)
    #SUM THEM.
    total_times=sum(total_times_list)

    #CALCULING THE PROBABILITY FOR EVERY WORD.
    for result in results:
        word=result[0]
        probability=result[1]/total_times

        print(("Updating probability for {} in {}.").format(word,search))
        conn = sqlite3.connect(DATABASE_PATH+DATABASE_NAME)
        conn.execute(('UPDATE {} SET PROBABILITY={} WHERE WORD="{}"').format(search ,probability,word))
        conn.commit()
        conn.close()
        print("COMPLETED")

def PrintingOutput(search):
    #CONNECT TO DATABASE.
    conn = sqlite3.connect(DATABASE_PATH+DATABASE_NAME)
    cursor = conn.cursor()

    #SEARCH FOR THE IDs VALUE IN THE WORDS_TOTAL TABLE 
    cursor.execute(('SELECT WORD,PROBABILITY FROM {}').format(search))
    results=cursor.fetchall()
    conn.close()
    print(results)

def SearchNextWord(search):
    #Create a new table using the serch value as name/ VALUES=ID,WORD,PROBABILITY.
    CreateSearchTable(search)

    #For every episode in the list(TABLE), the search will be made and data will be collected and inserted into the search-table.
    NextWord(search)
    UpdateProbabilities(search)
    PrintingOutput(search)
    
"""
COMPLETE HERE FOR MAKING A NEXT-VALUE SEARCH . 
IT WILL CREATE A NEW TABLE IN THE DATABASE WITH THE RESULTS
EXAMPLE:

ID  WORD    PROBABILITY
01  HI      0.0156
02  THERE   0.0128

SearchNextWord("HI")
Output--> New table named "HI" with the value "THERE" and an ID.
Printed Output-->



"""
#SearchNextWord("smartphone")
