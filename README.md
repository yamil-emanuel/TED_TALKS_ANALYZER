# **TED_TALKS_ANALYZER**
Scripting in order to analyze some ted talks using their transcriptions and some video's metadata.
Full dataset and some extra analysis could be found here: https://www.kaggle.com/yamildaboul/improving-online-presence-using-tedxtalks


##Before running: 
important_lists.py contains variables which must be completed as the date the analytics's data is getting captured, the path where the subtitles files are storaged, the path and name of the database and the Youtube Data's API KEY.
subtitles_list.py includes detailed instructions about how to import all the subtitles files into the subtitles_list variable.


##**main.py**
This file has one main function called run(), which will create the database and all the inner tables using the previusly setted variables (Read "Before running").


SUMMARY_INFO (table):
[VIDEO TITLE],[CATEGORIES (based on youtube's hashtags)], [COUNTRY(where the video was recorded)],[PUBLISHED DATE],[PUBLISHED TIME], [VIEWS], [LIKES],[DISLIKES],[COMMENTS]

VIDEO(table):
["TITLE","CATEGORIES","MINUTE","SECONDS","WORD"]

-----------------------------------------------------------------

##**functions.py**
This file contains filtering, exporting and analysis functions as:

**MakeResume(DATABASE_PATH,DATABASE_NAME,tables_list)**
Will create the table WORDS_TOTAL which is a table with the following attributes: "TITLE","CATEGORIES","MINUTE","SECONDS","WORD". Every row is a single said word during the Ted Talks videos.

**ExportWordsTotal(DATABASE_PATH,DATABASE_NAME,stopwords,tables_list,limit)**
#EXPORT A CSV FILE CALLED TOTAL_WORDS.csv WHICH INCLUDES ALL THE SAID WORDS IN EVERY VIDEO [VIDEO TITLE, VIDEO CATEGORIES, MINUTE, WORD].

**ExportEngagement(engagement_list,difference_days)**
EXPORTING A CSV CALLED ENGAGEMENT.CSV WITH VALUES: TITLE, INTERACTION_RATIO, LIKE_RATE, LIKES_PERCENTAGE, DISLIKES_PERCENTAGE, COMMENT_RATE,VIEWS PER DAY (SINCE IT WAS RELASED) These values are attached to the ANALYTICS_CAPTURED_ON variable in important_lists.py .

**ExportWordPerMinute(DATABASE_PATH,DATABASE_NAME,tables_list)**
WITH THIS FUNCTION YOU WILL CREATE A FILE CALLED WORDS_PER_MINUTE.CSV [VIDEO TITLE + CATEGORIES + MINUTE PER VIDEO + AMOUNT WORDS PER MINUTE]          



##**SOME RELEVANT EXTRA-DATA**:



**tables_list=SelectAllTables(DATABASE_PATH,DATABASE_NAME)**
THIS TUPLE HAS EVERY TABLE'S NAME AS VALUE

**engagement_list=EngagementRate(DATABASE_PATH,DATABASE_NAME,tables_list)**
THIS TUPLE CONTAINS VIDEO NAME + ALL THE ENGAGEMENT INFORMATION EXCEPT VIEWS PER DAY.

**difference_days=DiferenceDays(DATABASE_PATH,DATABASE_NAME,ANALYTICS_CAPTURED_ON)**
TUPLE WHICH CONTAINS N° OF DAYS SINCE RELASED UNTIL THE SPECIFIED DATE.

**categories_and_videos=VideosByCategory(DATABASE_PATH,DATABASE_NAME,categories)**
DICTIONARY WITH EVERY CATEGORY AS KEY AND VIDEOS AS VALUE.

-----------------------------------------------------------------

##**markovs_chain.py**
This file contains an unique main-function called SearchNextWord(search).

**SearchNextWord(search)**
Searches for the next said-word after the search-word value and calculates it's probability. 
Create a new table using the serch value as name [VALUES=ID,WORD,PROBABILITY]. For every episode in the list(table), the search will be made and data will be collected and inserted into the new recently created table.
After the operation, the script will print the results.
