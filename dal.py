import sqlite3

# we have a reviews table with type (text), link (text), review (text), extra (json text), date (text), brand (text)
def create_reviews_table():
    conn = sqlite3.connect("reviews.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS reviews (type text, link text, review text, extra text, date text, brand text)")
    conn.commit()

def add_review(type, link, review, extra, date, brand):
    conn = sqlite3.connect("reviews.db")
    cur = conn.cursor()
    # insert if row with review doesn't exist
    cur.execute("INSERT INTO reviews (type, link, review, extra, date, brand) SELECT ?, ?, ?, ?, ?, ? WHERE NOT EXISTS (SELECT 1 FROM reviews WHERE review=?)", (type, link, review, extra, date, brand, review))
    conn.commit()

def get_reviews_by_column(column, value):
    conn = sqlite3.connect("reviews.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM reviews WHERE {}=?".format(column), (value,))
    return cur.fetchall()

def get_reviews_by_type_brand_and_date(type, brand, date):
    conn = sqlite3.connect("reviews.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM reviews WHERE type=? AND brand=? AND date=?", (type, brand, date))
    return cur.fetchall()

def get_reviews_by_brand_and_date(brand, date):
    conn = sqlite3.connect("reviews.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM reviews WHERE brand=? AND date=?", (brand, date))
    return cur.fetchall()


