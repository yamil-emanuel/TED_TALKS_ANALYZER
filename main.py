import sqlite3
import webvtt 
import requests
from bs4 import BeautifulSoup
import json
from important_lists import *
from subtitles_list import subtitles_list
import string
from functions import *


#SECONDARY FUNCTIONS------------------------------------------------------------

#THIS TUPLE HAS EVERY TABLE'S NAME AS VALUE
tables_list=SelectAllTables(DATABASE_PATH,DATABASE_NAME)
engagement_list=EngagementRate(DATABASE_PATH,DATABASE_NAME,tables_list)
top_words=TopWords(DATABASE_PATH,DATABASE_NAME,stopwords,tables_list,10)
difference_days=DiferenceDays(DATABASE_PATH,DATABASE_NAME,'2021-04-09')
categories_and_videos=VideosByCategory(DATABASE_PATH,DATABASE_NAME,categories)


#--------------------------------------------------------------------------------


def Subtitles_Processor(subtitle,video_title,video_title_summary,video_categories_list):
    #OPENS A .VTT FILE, REPLACE SIMBOLS, PARCE IT AND INSERT EVERY SINGLE WORD INTO A DATABASE.
    print(("INSERTING DATA INTO {} TABLE. THIS PROCESS CAN TAKE A WHILE.").format(video_title))
    for caption in webvtt.read(PATH+subtitle):
        minute=(caption.start)[3:5]
        seconds=(caption.start)[6:8]
        caption=caption.text
        #REPLACING UNNECESARY SYMBOLS.
        caption=caption.replace("\\"," ")
        caption=caption.replace("\n"," ")
        caption=caption.replace("'d"," would")
        caption=caption.replace("'t", " not")
        caption=caption.replace("'s", " is")
        caption=caption.replace("'m"," am")
        caption=caption.replace("'ll", " will")
        caption=caption.replace("'re", " are")
        caption=caption.replace('?'," ")
        caption=caption.replace('"'," ")
        caption=caption.replace("."," ")
        caption=caption.replace(','," ")
        caption=caption.replace('-'," ")
        caption=caption.replace(':'," ")
        caption=caption.replace(';',"")
        caption=caption.replace("'","")

        #SPLITTING SENTENCES INTO WORDS
        sentence=caption.split(' ')
        for word in sentence:
            #INSERT WORD BY WORD INTO THE VIDEO'S TABLE
            word=word.lower()
            InsertData(minute, seconds, word,video_title,video_title_summary,video_categories_list)
    print("COMPLETED\n----------------\n")

def DataCapure(video_id,subtitle,video_title):
    print("CAPTURING VIDEO'S DATA.")
    #PULL NAME, UPLOAD DATE, TAGS AND DESCRIPTION FROM A VIDEO.
    url=requests.get(('https://www.googleapis.com/youtube/v3/videos?id={}&part=snippet,statistics,recordingDetails&key={}').format(video_id,YOUTUBE_DATA_API_V3))
    soup = BeautifulSoup(url.content, 'lxml')
    dictionary=(soup.body.p).get_text()
    RAW_CAPTURE=json.loads(dictionary)
    RAW_CAPTURE_SNIPPET=RAW_CAPTURE["items"][0]['snippet']
    RAW_CAPTURE_STATISTICS=RAW_CAPTURE["items"][0]

    #SUMMARY VARIABLES INDICATE THE VALUES WHICH WILL BE INSERTED INTO THE SUMMARY TABLE
    video_title_summary=RAW_CAPTURE_SNIPPET.get("title")
    video_title_summary=video_title_summary.replace('"',"")

    #TAGS
    video_tags_summary=[]
    video_tags_raw=RAW_CAPTURE_SNIPPET.get("tags")
    #CLEANING THE TAGS, AVOIDING STRING-FORMAT CRASHES.
    for tag in video_tags_raw:
        tag=tag.replace("'","")
        video_tags_summary.append(tag)

    #GETTING PUBLISHED TIMES
    video_publishedAt_summary=((RAW_CAPTURE_SNIPPET.get("publishedAt")[:-1])).split('T')
    video_published_date_summary=video_publishedAt_summary[0]
    video_published_time_summary=(video_publishedAt_summary[1])[:-1]

    #GETTING VIDEO STATISTICS
    video_views_summary=RAW_CAPTURE_STATISTICS.get('statistics',{}).get('viewCount')
    video_likes_summary=RAW_CAPTURE_STATISTICS.get('statistics',{}).get('likeCount')
    video_dislikes_summary=RAW_CAPTURE_STATISTICS.get('statistics',{}).get('dislikeCount')
    video_comments_summary=RAW_CAPTURE_STATISTICS.get('statistics',{}).get('commentCount')



    #CAPTURING FROM TAGS THE TED's CATEGORIES
    video_categories_list=[]
    country_final=['']
    tags=RAW_CAPTURE_SNIPPET.get("tags")
    for category in tags:
        if category in categories:
            video_categories_list.append(category)
    
    for country in tags:
        if country in countries_list:
            country_final.insert(0,country)

    video_categories_summary=(str(video_categories_list))[1:-1]
    country_summary=country_final[0]
    #CALLING SUMMARYINFO(), CREATES A RESUME OF THE VIDEO'S DATA.
    print("INSERTING VALUES INTO SUMMARY_INFO.")
    SummaryInfo(video_title_summary,video_categories_summary,country_summary,video_published_date_summary,video_published_time_summary,video_views_summary,video_likes_summary,video_dislikes_summary, video_comments_summary,video_tags_summary,video_id)
    Subtitles_Processor(subtitle,video_title,video_title_summary,video_categories_summary)

def CreateTable(video_title):
    print(("CREATING {} TABLE INTO THE DATABASE.").format(video_title))
    conn = sqlite3.connect(DATABASE_PATH+DATABASE_NAME)
    conn.execute(('CREATE TABLE "{}" ("ID" INTEGER NOT NULL UNIQUE,"TITLE" TEXT, "CATEGORIES" TEXT, "MINUTE" INTEGER, "SECONDS" INTEGER, "WORD" TEXT, PRIMARY KEY("ID" AUTOINCREMENT));').format(video_title))
    conn.close
    print("COMPLETED")

def InsertData(minute, seconds, word,video_title,video_title_summary,video_categories_list):
    #IF WORD IS NOT A BLANK SPACE, INSERT THE VALUES
    if word!=" ":
        formated_insert_data=('"{}","{}","{}","{}","{}"').format(video_title_summary,video_categories_list,minute,seconds,word)
        #Excecuting he command
        conn = sqlite3.connect(DATABASE_PATH+DATABASE_NAME)
        conn.execute(("INSERT INTO {} (TITLE,CATEGORIES,MINUTE,SECONDS,WORD) VALUES ({})").format(video_title,formated_insert_data))
        conn.commit()
        conn.close()
    else:
        pass

def CreateSummaryInfo():
    #CREATE THE SUMMARY_INFO TABLE
    print("CREATING SUMMARY_INFO TABLE IN THE DATABASE.")
    conn = sqlite3.connect(DATABASE_PATH+DATABASE_NAME)
    conn.execute('CREATE TABLE "SUMMARY_INFO" ("ID" INTEGER NOT NULL UNIQUE,"TITLE" TEXT,"CATEGORIES" TEXT,"COUNTRY" TEXT, "PUBLISHED_DATE" TEXT, "PUBLISHED_TIME" TEXT,"VIEWS" TEXT, "LIKES" INTEGER, "DISLIKES" INTEGER, "COMMENTS" INTEGER, "TAGS" TEXT, "URL" TEXT, PRIMARY KEY("ID" AUTOINCREMENT));')
    conn.close
    print("COMPLETED\n----------------\n")

def SummaryInfo(video_title_summary,video_categories_summary,country_summary,video_published_date_summary,video_published_time_summary,video_views_summary,video_likes_summary,video_dislikes_summary,video_comments_summary,video_tags_summary,video_id):
    #INSERT VIDEO TITLE, PUBLISHED AT, TAGS AND VIDEO'S URL INTO THE SUMMARY_INFO TABLE.
    print(("INSERTING RESUME INTO SUMMARY_INFO FOR {}").format(video_title_summary))
    summary_format=('"{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}"').format(video_title_summary,video_categories_summary,country_summary,video_published_date_summary,video_published_time_summary,video_views_summary,video_likes_summary,video_dislikes_summary,video_comments_summary,video_tags_summary,video_id)
    conn = sqlite3.connect(DATABASE_PATH+DATABASE_NAME)
    conn.execute(("INSERT INTO SUMMARY_INFO (TITLE, CATEGORIES, COUNTRY, PUBLISHED_DATE, PUBLISHED_TIME, VIEWS, LIKES, DISLIKES, COMMENTS, TAGS, URL) VALUES ({}) ;").format(summary_format))
    conn.commit()
    conn.close()
    print("COMPLETED")

def run():
    #CreateSummaryInfo()

    for subtitle in subtitles_list:

        #GET VIDEO_ID (URL) FROM THE FILE NAME
        video_id=subtitle[-18:-7]

        #GET THE TITLE OF THE VIDEO <30 CHAR.
        video_title_raw=subtitle.replace(" ","_")
        video_title_raw=video_title_raw.replace("'","")
        video_title_raw=video_title_raw[:30]
        video_title_raw=video_title_raw.replace(',',"")
        video_title_raw=video_title_raw.replace('.',"_")
        video_title_raw=video_title_raw.replace('-',"")
        video_title_raw=video_title_raw.replace('--',"")
        video_title_raw=video_title_raw.replace('(',"")
        video_title_raw=video_title_raw.replace(')',"")
        video_title_raw=video_title_raw.replace("'","")

        if video_title_raw[0] in (string.digits):
            video_title=video_title_raw[1:]
            CreateTable(video_title)
            DataCapure(video_id,subtitle,video_title)
            
        else:
            video_title=video_title_raw
            CreateTable(video_title)
            DataCapure(video_id,subtitle,video_title)
            

"""
if __name__ == "__main__":
    run()
"""

