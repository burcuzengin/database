import sqlite3
from sqlite3 import Error

def create_connection(movies):

    conn= None

    try:
        conn= sqlite3.connect(movies)
    except Error as e:
        print(e)

    return conn


def main():
    database="movies.db"
    conn= create_connection(database)
    with conn:
        #MAIN MENU QUERIES(1ST AND 2ND)
        cur=conn.cursor()
        update= "UPDATE MOVIE_STATISTICS SET Average_score=(IMDB*0.7)+(Rotten_tomatoes*0.3)"  #column update(average_score)
        cur.execute(update)

        cur.execute("SELECT DISTINCT GenreName FROM GENRE ORDER BY GenreName ASC") #Genres 1st query
        genre=cur.fetchall()
        for row in genre:
            query="SELECT MOVIES.Title,GENRE.GenreName FROM MOVIES, GENRE WHERE((GENRE.MovieID= MOVIES.MovieID) AND(GENRE.GenreName='%s'))" %(row[0],)
            cur.execute(query) #Genres 2nd query
            rows=cur.fetchall()
            """for row in rows:
                print(row)"""

        cur.execute("SELECT DISTINCT LanguageName FROM LANGUAGE ORDER BY LanguageName ASC") #Languages 1st query
        language=cur.fetchall()
        for row in language:
            cur.execute("SELECT MOVIES.Title,LANGUAGE.LanguageName FROM MOVIES, LANGUAGE WHERE((LANGUAGE.MovieID= MOVIES.MovieID) AND(LANGUAGE.LanguageNAme='%s'))" %(row[0],)) #Languages 2nd query
            """rows=cur.fetchall()
            for row in rows:
                print(row)"""

        cur.execute("SELECT PersonName,Rank_of_person FROM PERSON WHERE(CastType='Director')") #Directors 1st query
        director=cur.fetchall()
        for i in range(len(director)): #Directors 2nd query
            cur.execute("SELECT MOVIES.Title FROM PERSON, CASTING, MOVIES WHERE((PERSON.PersonID=CASTING.PersonID) AND (CASTING.MovieID=MOVIES.MovieID) AND(PERSON.PersonID='%d'))"%(i,)) 
            """rows=cur.fetchall()
            for row in rows:
                print(row)"""

        cur.execute("SELECT PersonName,Rank_of_person FROM PERSON WHERE((CastType='Actor')  OR (CastType='Actress'))") #Actors/Actresses 1st query
        act=cur.fetchall()
        for i in range(len(act)): #Actors/Actresses 2nd query
            cur.execute("SELECT MOVIES.Title FROM PERSON, CASTING, MOVIES WHERE((PERSON.PersonID=CASTING.PersonID) AND (CASTING.MovieID=MOVIES.MovieID) AND(PERSON.PersonID='%d'))"%(i,)) 
            """rows=cur.fetchall()
            for row in rows:
                print(row)"""

        #TABLE DELETIONS
        """
        cur.execute("DROP TABLE USER_MOVIE")
        cur.execute("DROP TABLE MOVIE_STATISTICS")
        cur.execute("DROP TABLE MOVIES")
        """
        #INSETING VALUES WHEN NEEDED
        
        cur.execute("SELECT MovieID FROM MOVIE_STATISTICS")
        moveid_list=cur.fetchall()
        last_movieid=len(moveid_list)
        cur.execute("SELECT Title FROM MOVIE_STATISTICS")
        title_list=cur.fetchall()
        #TO MAKE UNIQUE, I COMMENTED THE CODES
        """for i in range(len(moveid_list)):
            cur.execute("INSERT INTO USER_MOVIE (MovieID, Title) VALUES (%d,'%s')" %(moveid_list[i][0],title_list[i][0],))"""
        """
        cur.execute("INSERT INTO MOVIES VALUES ( )")
        cur.execute("INSERT INTO MOVIE_STATISTICS VALUES ( )")
        cur.execute("INSERT INTO USER_MOVIE VALUES ()")"""
        #cur.execute("DELETE FROM MOVIES WHERE(MovieID>=9516)")
        #cur.execute("DELETE FROM MOVIE_STATISTICS WHERE(MovieID>=9516)")
        #cur.execute("INSERT INTO MOVIE_STATISTICS VALUES (%d,'The Matrix Resurrections',88/100,5.7/10,NULL,NULL)" %(last_movieid+1,))
        #cur.execute("INSERT INTO MOVIES VALUES (%d,'The Matrix Resurrections',1680,13,2021,'https://www.imdb.com/title/tt10838180/mediaviewer/rm3704744193/')" %(last_movieid+1,))
        #cur.execute("SELECT MovieID,Title FROM MOVIE_STATISTICS")
        cur.execute("DELETE FROM MOVIES WHERE(MovieID=9494)")

if __name__ == '__main__':
    main()