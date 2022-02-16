import sqlite3
import pandas as pd             #importing pandas lib to work on databases with python

USER_MOVIE = pd.read_excel('database_exceltables/main1.xlsx')        #reading database from excel
MOVIE_STATISTICS = pd.read_excel('database_exceltables/main2.xlsx')
MOVIES = pd.read_excel('database_exceltables/main3.xlsx')
PLATFORM = pd.read_excel('database_exceltables/platform.xlsx')
LANGUAGE= pd.read_excel('database_exceltables/language.xlsx')
COUNTRY = pd.read_excel('database_exceltables/country.xlsx')
CASTING = pd.read_excel('database_exceltables/casting.xlsx')
PERSON = pd.read_excel('database_exceltables/person.xlsx')
GENRE = pd.read_excel('database_exceltables/genre.xlsx')
db_conn = sqlite3.connect('movies.db')              #create SQLite database
cursor_obj = db_conn.cursor()       #create cursor object


 #filling the database with sql codes
# USER_MOVIE TABLE, MAIN1
cursor_obj.execute(            
    """
    CREATE TABLE USER_MOVIE (
        MovieID INTEGER ,
        Title VARCHAR(80) NOT NULL,
        Rank_in_website INTEGER,
        Num_of_search INTEGER,
        Num_of_likes INTEGER,
        Num_of_dislikes INTEGER,
        PRIMARY KEY(MovieID)
        )
     """
)
# MOVIE_STATISTICS TABLE, MAIN2
cursor_obj.execute(
    """
    CREATE TABLE MOVIE_STATISTICS (
        MovieID INTEGER ,
        Title VARCHAR(80) NOT NULL,
        Rotten_tomatoes FLOAT,
        IMDB FLOAT,
        Average_score FLOAT,
        Oscar_award_year INTEGER,
        PRIMARY KEY(MovieID)
        )
    """
)

# MOVIES TABLE, MAIN3
cursor_obj.execute(
    """
    CREATE TABLE MOVIES (
        MovieID INTEGER ,
        Title VARCHAR(80) NOT NULL,
        Runtime INTEGER,
        Age INTEGER,
        Year INTEGER,
        poster_link TEXT,
        PRIMARY KEY(MovieID)
        )
    """
)

# EXTRA TABLE 1
cursor_obj.execute(
    """
    CREATE TABLE PLATFORM (
        MovieID INTEGER ,
        PlatformName VARCHAR(80),
        PRIMARY KEY(MovieID,PlatformName),
        FOREIGN KEY(MovieID) REFERENCES MOVIES(MovieID)
        )
    """
)

# EXTRA TABLE 2
cursor_obj.execute(
    """
    CREATE TABLE LANGUAGE (
        MovieID INTEGER,
        LanguageName VARCHAR(80),
        PRIMARY KEY(MovieID,LanguageName),
        FOREIGN KEY(MovieID) REFERENCES MOVIES(MovieID)
        )
    """
)

# EXTRA TABLE 3
cursor_obj.execute(
    """
    CREATE TABLE COUNTRY (
        MovieID INTEGER,
        CountryName VARCHAR(80),
        PRIMARY KEY(MovieID,CountryName),
        FOREIGN KEY(MovieID) REFERENCES MOVIES(MovieID)
        )
    """
)

# EXTRA TABLE 4
cursor_obj.execute(
    """
    CREATE TABLE CASTING (
        MovieID INTEGER ,
        PersonID INTEGER,
        PRIMARY KEY(PersonID,MovieID),
        FOREIGN KEY(PersonID) REFERENCES PERSON(PersonID),
        FOREIGN KEY(MovieID) REFERENCES MOVIES(MovieID)
        )
    """
)

# EXTRA TABLE 5
cursor_obj.execute(
    """
    CREATE TABLE PERSON (
        PersonID INTEGER,
        PersonName VARCHAR(80),
        CastType VARCHAR(80) NOT NULL,
        Rank_of_person FLOAT,
        PRIMARY KEY(PersonID)
        )
    """
)

# EXTRA TABLE 6
cursor_obj.execute(
    """
    CREATE TABLE GENRE (
        MovieID INTEGER,
        GenreName VARCHAR(80),
        PRIMARY KEY(MovieID,GenreName),
        FOREIGN KEY(MovieID) REFERENCES MOVIES(MovieID)
        )
    """
)



USER_MOVIE.to_sql('USER_MOVIE', db_conn, if_exists='append', index=False)           #using "to_sql" function to fill the tables with revelant data from excel tables
MOVIE_STATISTICS.to_sql('MOVIE_STATISTICS', db_conn, if_exists='append', index=False)
MOVIES.to_sql('MOVIES', db_conn, if_exists='append', index=False)
PLATFORM.to_sql('PLATFORM', db_conn, if_exists='append', index=False)
LANGUAGE.to_sql('LANGUAGE', db_conn, if_exists='append', index=False)
COUNTRY.to_sql('COUNTRY', db_conn, if_exists='append', index=False)
CASTING.to_sql('CASTING', db_conn, if_exists='append', index=False)
PERSON.to_sql('PERSON', db_conn, if_exists='append', index=False)
GENRE.to_sql('GENRE', db_conn, if_exists='append', index=False)
db_conn.commit()
db_conn.close()         #closing database connection
