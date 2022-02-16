import sqlite3
from sqlite3 import Error
import numpy as np

def create_connection(movies):

    conn= None

    try:
        conn= sqlite3.connect(movies)
    except Error as e:
        print(e)

    return conn

"""def findMaxGenre(value,arr):
    max=0
    index=0
    for i in range(len(arr)):
        if value==arr[i][2] and arr[i][1] > max:
            max=arr[i][1]
            index=i
    
    print(arr[index])"""

def findMaxGenre(arr):
    max=0
    index=0
    for i in range(len(arr)):
        if  arr[i][1] > max:
            max=arr[i][1]
            index=i
    if index in range(len(arr)):
        print(arr[index])

def findMaxCountry(arr):
    max=0
    index=0
    for i in range(len(arr)):
        if  arr[i][1] > max:
            max=arr[i][1]
            index=i
    if index in range(len(arr)):
        print(arr[index])

def main():
    database="movies.db"
    conn= create_connection(database)
    with conn:
        cur=conn.cursor()
        cur.execute("SELECT PlatformName, COUNT(MovieID) FROM PLATFORM GROUP BY(PlatformName) ORDER BY PlatformName") #for every platform, how many movie exists in
        platform=cur.fetchall()
        """for row in platform:
            print(row) """         

        cur.execute("SELECT DISTINCT PlatformName FROM PLATFORM ORDER BY PlatformName") #PlatformName list
        platformlist=cur.fetchall()
        for row in platformlist:
            query="SELECT PLATFORM.PlatformName, GENRE.GenreNAME, COUNT(GENRE.MovieID) FROM GENRE,PLATFORM WHERE((GENRE.MovieID= PLATFORM.MovieID) AND(PLATFORM.PlatformName='%s')) GROUP BY GENRE.GenreName ORDER BY GENRE.GenreName" %(row[0],)
            cur.execute(query) #for every platform, what genre does it have the most
            """rows=cur.fetchall()
            for row in rows:
                print(row)"""
        
        #for every director, which genre do they film the most
        cur.execute("SELECT PersonName FROM PERSON WHERE(CastType='Director')") #Directors list
        directorlist=cur.fetchall()
        """for i in range(len(directorlist)):
            cur.execute("SELECT GENRE.GenreName, COUNT(GENRE.GenreName) ,PERSON.PersonName FROM GENRE,PERSON,CASTING WHERE((GENRE.MovieID=CASTING.MovieID) AND (CASTING.PersonID=PERSON.PersonID) AND (PERSON.PersonID=%d)) GROUP BY GENRE.GenreName"%(i,))
            director=cur.fetchall()
            findMaxGenre(director)"""
        #for row in directorlist:
        #findMaxGenre(row[0],director)
            

        #Teen safe movies, their score and duration list
        cur.execute("SELECT MOVIE_STATISTICS.Title,MOVIE_STATISTICS.IMDB,MOVIES.Runtime,MOVIES.Age FROM MOVIE_STATISTICS, MOVIES WHERE((MOVIE_STATISTICS.MovieID=MOVIES.MovieID) AND(MOVIES.Age<19) AND (MOVIE_STATISTICS.IMDB>7.0))")
        teen_movies=cur.fetchall()
        """for row in teen_movies:
            print(row)"""

        #Children safe movies, their score and duration list
        cur.execute("SELECT MOVIE_STATISTICS.Title,MOVIE_STATISTICS.IMDB,MOVIES.Runtime,MOVIES.Age FROM MOVIE_STATISTICS, MOVIES WHERE((MOVIE_STATISTICS.MovieID=MOVIES.MovieID) AND(MOVIES.Age<8)AND (MOVIE_STATISTICS.IMDB>7.0))")
        children_movies=cur.fetchall()
        """for row in children_movies:
            print(row)"""

        #Platforms movie number that are teen-safe (<=18)
        cur.execute("SELECT PLATFORM.PlatformName, COUNT(MOVIES.MovieID) FROM PLATFORM, MOVIES WHERE((PLATFORM.MovieID=MOVIES.MovieID) AND (MOVIES.Age<19)) GROUP BY PLATFORM.PlatformName")
        teen_platform=cur.fetchall()
        """for row in teen_platform:
            print(row)"""

        #Platforms movie number that are children-safe (<=7)
        cur.execute("SELECT PLATFORM.PlatformName, COUNT(MOVIES.MovieID) FROM PLATFORM, MOVIES WHERE((PLATFORM.MovieID=MOVIES.MovieID) AND (MOVIES.Age<8)) GROUP BY PLATFORM.PlatformName")
        child_platform=cur.fetchall()
        """for row in child_platform:
            print(row)"""
        

        cur.execute("SELECT DISTINCT GenreName FROM GENRE  WHERE(GenreName IS NOT NULL) ORDER BY GenreName") #GenreName list
        genrelist=cur.fetchall()
        cur.execute("SELECT DISTINCT CountryName FROM COUNTRY WHERE(CountryName IS NOT NULL) ORDER BY CountryName") #CountryName list
        countrylist=cur.fetchall()
        """for row in countrylist:
            print(row[0])"""
    
        #For every country, which genre was filmed the most in?
        for row in countrylist:
            cur.execute("SELECT GENRE.GenreName,COUNT(GENRE.MovieID), COUNTRY.CountryName FROM GENRE, COUNTRY WHERE((GENRE.MovieID=COUNTRY.MovieID) AND (COUNTRY.CountryName='%s')) GROUP BY GENRE.GenreName"%(row[0],))
            country=cur.fetchall()
            #findMaxGenre(country)


        #All genres and their most filmed country names 
        for row in genrelist:
            cur.execute("SELECT GENRE.GenreName,COUNT(GENRE.MovieID), COUNTRY.CountryName FROM GENRE, COUNTRY WHERE((GENRE.MovieID=COUNTRY.MovieID) AND (GENRE.GenreName='%s')) GROUP BY COUNTRY.CountryName"%(row[0],))
            genre=cur.fetchall()
            #findMaxCountry(genre)

        conn.commit()




if __name__ == '__main__':
    main()