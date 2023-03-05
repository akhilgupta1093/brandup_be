import sqlite3

con = sqlite3.connect("reviews.db")
cur = con.cursor()

# we have a reviews table with type (text), link (text), review (text), extra (json text), date (text)
def create_reviews_table():
    cur.execute("CREATE TABLE IF NOT EXISTS reviews (type text, link text, review text, extra text, date text)")

def add_review(type, link, review, extra, date):
    cur.execute("INSERT INTO reviews VALUES (?, ?, ?, ?, ?)", (type, link, review, extra, date))
    con.commit()

def get_reviews_by_column(column, value):
    cur.execute("SELECT * FROM reviews WHERE {}=?".format(column), (value,))
    return cur.fetchall()

def get_reviews_by_type_and_date(type, date):
    cur.execute("SELECT * FROM reviews WHERE type=? AND date=?", (type, date))
    return cur.fetchall()


