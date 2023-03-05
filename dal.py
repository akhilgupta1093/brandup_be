import sqlite3

con = sqlite3.connect("reviews.db", check_same_thread=False)
cur = con.cursor()

# we have a reviews table with type (text), link (text), review (text), extra (json text), date (text), brand (text)
def create_reviews_table():
    cur.execute("CREATE TABLE IF NOT EXISTS reviews (type text, link text, review text, extra text, date text, brand text)")
    con.commit()

def add_review(type, link, review, extra, date, brand):
    # insert if row with review doesn't exist
    cur.execute("INSERT INTO reviews (type, link, review, extra, date, brand) SELECT ?, ?, ?, ?, ?, ? WHERE NOT EXISTS (SELECT 1 FROM reviews WHERE review=?)", (type, link, review, extra, date, brand, review))
    con.commit()

def get_reviews_by_column(column, value):
    cur.execute("SELECT * FROM reviews WHERE {}=?".format(column), (value,))
    return cur.fetchall()

def get_reviews_by_type_brand_and_date(type, brand, date):
    cur.execute("SELECT * FROM reviews WHERE type=? AND brand=? AND date=?", (type, brand, date))
    return cur.fetchall()


