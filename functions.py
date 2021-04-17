import sqlite3
import csv
from important_lists import *


def SelectAllTables(DATABASE_PATH,DATABASE_NAME):
    #CREATES A LIST WITH EVERY TABLE NAME AS A VALUE

    #CREATING CONNECTION AND CURSOR
    conn = sqlite3.connect(DATABASE_PATH+DATABASE_NAME)
    cursor=conn.cursor()
    #PULLING ALL TABLE's NAME.
    cursor.execute(("SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT IN ('sqlite_sequence','SUMMARY_INFO','WORDS_TOTAL');"))
    results=cursor.fetchall()    
    conn.close()

    #FORMATTING RESULTS.
    tables_list=[]
    for result in results:
        tables_list.append(result[0])
    
    return tables_list

def MakeResume(DATABASE_PATH,DATABASE_NAME,tables_list):
    # Creates the WORDS_TOTAL TABLE and insert there every word said in all the videos attributes: video title, categories, minute, seconds, word
    print("CREATING WORDS_TOTAL TABLE INTO THE DATABASE.")
    conn = sqlite3.connect(DATABASE_PATH+DATABASE_NAME)
    conn.execute('CREATE TABLE "WORDS_TOTAL" ("ID" INTEGER NOT NULL UNIQUE,"TITLE" TEXT, "CATEGORIES" TEXT, "MINUTE" INTEGER, "SECONDS" INTEGER, "WORD" TEXT, PRIMARY KEY("ID" AUTOINCREMENT));')
    conn.close
    print("COMPLETED")

    for table_name in tables_list:
        print(("Creating resume for {} in WORDS_TOTAL.").format(table_name))
        #CREATING CONNECTION AND CURSOR
        conn = sqlite3.connect(DATABASE_PATH+DATABASE_NAME)
        cursor=conn.cursor()
        #INSERTING EVERY SAID WORD IN WORDS_TOTAL
        cursor.execute(('''INSERT INTO "WORDS_TOTAL" ("TITLE","CATEGORIES","MINUTE","SECONDS","WORD") SELECT "TITLE","CATEGORIES","MINUTE","SECONDS","WORD" FROM "{}" WHERE WORD != "";''').format(table_name))
        conn.commit()
        conn.close()
        print("COMPLETED")

def EngagementRate(DATABASE_PATH,DATABASE_NAME,tables_list):
    #CREATING CONNECTION AND CURSOR
    conn = sqlite3.connect(DATABASE_PATH+DATABASE_NAME)
    cursor=conn.cursor()
    #PULLING TITLE, VIEWS, LIKES, DISLIKES AND COMMENTS FOR ALL THE VIDEOS.
    cursor.execute(("select TITLE, VIEWS, LIKES, DISLIKES,COMMENTS,CATEGORIES FROM SUMMARY_INFO;"))
    results=cursor.fetchall()    
    conn.close()
    return results

def DiferenceDays(DATABASE_PATH,DATABASE_NAME,RECORD_DATE):
    #RETURNS A TUPLE WITH DAYS SINCE THE VIDEO WAS RELASED AND NAME OF VIDEO FOR EVERY VIDEO IN THE DATASET.

    #IMPORTING TITLE AND PUBLISHED DATE FROM EVERY VIDEO IN SUMMARY VIDEO
    #CREATING CONNECTION AND CURSOR
    conn = sqlite3.connect(DATABASE_PATH+DATABASE_NAME)
    cursor=conn.cursor()
    #PULLING TITLE AND PUBLISHED DATE.
    cursor.execute("SELECT TITLE, PUBLISHED_DATE FROM SUMMARY_INFO")
    results=cursor.fetchall()
    conn.close()

    #HERE WILL THE INFO GET STORED AS [('diference','video_title')]
    difference_days=[]

    for result in results:
        #ORGANIZING THE INFORMATION, SPLITING IT INTO TITLE AND DATE
        title=result[0]
        date=result[1]    

        #CREATING CONNECTION AND CURSOR
        conn = sqlite3.connect(DATABASE_PATH+DATABASE_NAME)
        cursor=conn.cursor()
        #CALCULATE DIFERENCE BETWEEN DATE AND RECORD's DATE (YYYY-MM-DD).
        cursor.execute(('''Select Cast ((JulianDay("{}") - JulianDay(PUBLISHED_DATE)) As Integer), TITLE FROM SUMMARY_INFO WHERE TITLE="{}";''').format(RECORD_DATE,title))
        results=cursor.fetchall()
        conn.close()

        for video in results:
            difference_days.append(video)

        
    return difference_days

def VideosByCategory(DATABASE_PATH,DATABASE_NAME,categories):
    #THE FUNCTION'S RETURN IS A DICTIONARY WITH CATEGORIES'S NAME AS KEY AND VIDEO'S NAME AS VALUES (categories_and_videos)
    categories_and_videos={}

    for category in categories:    
        category=category.replace("'","")
        #CREATING CONNECTION AND CURSOR
        conn = sqlite3.connect(DATABASE_PATH+DATABASE_NAME)
        cursor=conn.cursor()
        #PULLING TITLE, VIEWS, LIKES, DISLIKES AND COMMENTS FOR ALL THE VIDEOS.
        cursor.execute(("""SELECT TITLE FROM SUMMARY_INFO WHERE CATEGORIES LIKE '%{}%' """).format(category))
        categories_with_vids=cursor.fetchall()    
        conn.close()
        if categories_with_vids==[]:
            pass
        else:
            categories_and_videos[category]=categories_with_vids
    
    return categories_and_videos

def ExportWordsTotal(DATABASE_PATH,DATABASE_NAME,stopwords,tables_list,n):
    # n == N° OF RESULTS YOU WANT TO GET.
    #EXPORT A CSV FILE CALLED TOTAL_WORDS WHICH INCLUDES ALL THE SAID WORDS IN EVERY VIDEO
    # [VIDEO TITLE, VIDEO CATEGORIES, MINUTE, WORD]

    temporal_data=[]

    for table in tables_list:
        #CREATING CONNECTION AND CURSOR
        conn = sqlite3.connect(DATABASE_PATH+DATABASE_NAME)
        cursor=conn.cursor()
        #PULLING TITLE, VIEWS, LIKES, DISLIKES AND COMMENTS FOR ALL THE VIDEOS.
        cursor.execute(("SELECT TITLE, CATEGORIES,  MINUTE, WORD FROM {} WHERE WORD NOT IN ({}) LIMIT({});").format(table,stopwords,n))
        results=cursor.fetchall()    
        conn.close()
        

        
        for result in results:
            title=result[0]
            categories=result[1]
            word=result[3]
            minute=result[2]
            temporal_data.insert(-1,(title,categories,minute,word))

    with open ('TOTAL_WORDS.csv','w', newline='') as file:
                writer=csv.writer(file)
                writer.writerow(["TITLE","CATEGORIES","MINUTE","WORD"])
                for element in temporal_data:
                    title=element[0]
                    categories=element[1]
                    minute=element[2]
                    word=element[3]
                    writer.writerow([title,categories,minute,word])

def ExportEngagement(engagement_list,difference_days):
	#EXPORTING A CSV CALLED ENGAGEMENT.CSV WITH VALUES: TITLE, INTERACTION_RATIO, LIKE_RATE, LIKES_PERCENTAGE, DISLIKES_PERCENTAGE, COMMENT_RATE,VIEWS PER DAY (SINCE IT WAS RELASED)

    temporal_data=[]
    
    for table,video in zip(difference_days,engagement_list):
        title=video[0]
        views=int(video[1])
        likes=int(video[2])
        dislikes=int(video[3])
        categories_engagement_list=(video[5])

        if video[4] == "None":
            comments=0
        else:
            comments=int(video[4])

        like_rate=(likes/views)
        comment_rate=(comments/views)
        like_dislike_ratio=(likes-dislikes)/(likes+dislikes)
        likes_percentage=(likes*100)/(likes+dislikes)
        dislikes_percentage=(dislikes*100)/(likes+dislikes)
        interaction_ratio=(likes+comments+dislikes)/views

        diference=table[0]
        vpd=views/diference



        temporal_data.insert(-1,(title,categories_engagement_list,interaction_ratio,like_rate,likes_percentage,dislikes_percentage,comment_rate,vpd))  
        
    with open ('engagement.csv','w', newline='') as file:
        writer=csv.writer(file)
        writer.writerow(["TITLE","CATEGORIES","INTERACTION RATIO","LIKES RATE","LIKES PERCENTAGE", "DISLIKES PERCENTAGE","COMMENTS RATE","AVERAGE VIEWS PER DAY"])
        for element in temporal_data:
            title=element[0]
            categories=element[1]
            interaction_ratio=element[2]
            like_rate=element[3]
            likes_percentage=element[4]
            dislikes_percentage=element[5]
            comment_rate=element[6]
            vpd=element[7]
            writer.writerow([title,categories,interaction_ratio,like_rate,likes_percentage,dislikes_percentage,comment_rate,vpd])

def ExportWordPerMinute(DATABASE_PATH,DATABASE_NAME,tables_list):
    #WITH THIS FUNCTION YOU WILL CREATE A FILE CALLED WORDS_PER_MINUTE.CSV
    # WITH THE FOLLOWING DATA: VIDEO TITLE + CATEGORIES + MINUTE PER VIDEO + AMOUNT WORDS PER MINUTE.          
    temporal_data=[]
    for table in tables_list:
        #GETTING THE WORD-PER-MINUTES VALUE
        #CREATING CONNECTION AND CURSOR
        conn = sqlite3.connect(DATABASE_PATH+DATABASE_NAME)
        cursor=conn.cursor()
        cursor.execute(("SELECT MINUTE,count(*),CATEGORIES FROM {} where word not in ('') GROUP by MINUTE ").format(table))
        results=cursor.fetchall()
        conn.close()
        for result in results:
            minute=result[0]
            words_amount=result[1]
            categories=result[2]
            title=table
            temporal_data.insert(-1,(title,categories,minute,words_amount))
    with open ('words_per_minute.csv','w', newline='') as file:
                writer=csv.writer(file)
                writer.writerow(["TITLE","CATEGORIES","MINUTE","WORDS_AMOUNT"])
                for element in temporal_data:
                    title=element[0]
                    categories=element[1]
                    minute=element[2]
                    words_amount=element[3]
                    writer.writerow([title,categories,minute,words_amount])
            
 #SECONDARY FUNCTIONS------------------------------------------------------------

#THIS TUPLE HAS EVERY TABLE'S NAME AS VALUE
tables_list=SelectAllTables(DATABASE_PATH,DATABASE_NAME)

#THIS TUPLE CONTAINS VIDEO NAME + ALL THE ENGAGEMENT INFORMATION EXCEPT VIEWS PER DAY.
engagement_list=EngagementRate(DATABASE_PATH,DATABASE_NAME,tables_list)

#TUPLE WHICH CONTAINS N° OF DAYS SINCE RELASED UNTIL THE SPECIFIED DATE
difference_days=DiferenceDays(DATABASE_PATH,DATABASE_NAME,ANALYTICS_CAPTURED_ON)

#DICTIONARY WITH EVERY CATEGORY AS KEY AND VIDEOS AS VALUE.
categories_and_videos=VideosByCategory(DATABASE_PATH,DATABASE_NAME,categories)      

