import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="netflixDB"
)
c = mydb.cursor()

def getLogin(loginId, password):
    c.execute("SELECT * FROM loginCredentials WHERE LoginId = %s AND password = %s", (loginId, password))
    if c.fetchone():
        c.execute("SELECT * FROM logincredentials, user WHERE logincredentials.LoginId = %s AND logincredentials.password = %s AND logincredentials.LoginId = user.LoginId", (loginId, password))
        return c.fetchone()

def signUp(newLoginId, newPassword, name, emailId, phoneNo):
    c.execute("INSERT INTO loginCredentials VALUES (%s, %s)", (newLoginId, newPassword))
    mydb.commit()
    c.execute("SELECT COUNT(*) FROM loginCredentials")
    userId = c.fetchone()[0] + 1
    subId = 1
    c.execute("INSERT INTO user VALUES (%s, %s, %s, %s, %s, %s)", (userId, name, emailId, phoneNo, newLoginId, subId))
    mydb.commit()

def getUserDetails(user):
    c.execute("SELECT * FROM user WHERE LoginId = %s", (user,))
    return c.fetchone()

def getMovies():
    c.execute("SELECT * FROM movie")
    return c.fetchall()

def getAvgRating():
    c.execute("SELECT AVG(rating) FROM movie")
    return c.fetchone()[0]

def getCast(movieId):
    c.execute("SELECT * FROM movieCast WHERE movieId = %s", (movieId,))
    return c.fetchall()

def updateRating(movieId, rating):
    c.execute("SELECT rating FROM movie WHERE movieId = %s", (movieId,))
    newRating = (c.fetchone()[0] + rating) / 2
    c.execute("UPDATE movie SET rating = %s WHERE movieId = %s", (newRating, movieId))
    mydb.commit()

def getMovieCount():
    c.execute("SELECT COUNT(*) FROM movie")
    return c.fetchone()[0]

def getMovieGenre():
    c.execute('SELECT genre, COUNT(*) AS numberOfMovies FROM movie GROUP BY genre')
    return c.fetchall()

