import sqlite3


db = 'bookmark_db.sqlite'


def create_db():
    conn = sqlite3.connect(db)

    conn.execute('CREATE TABLE IF NOT EXISTS bookmarks (tracks TEXT, images TEXT)')
    conn.commit()
    conn.close()



def add_urls(track, image):
    add_urls_sql = 'INSERT INTO bookmarks (tracks, images) VALUES (?, ?)'

    with sqlite3.connect(db) as conn:
        added = conn.execute(add_urls_sql, (track, image))
        added_count = added.rowcount
    conn.close()

    if added_count != 0:
        return True
    else:
        return False



def show_urls():
    conn = sqlite3.connect(db)
    show_urls_sql = 'SELECT * FROM bookmarks'

    cur = conn.execute(show_urls_sql)
    all_urls = cur.fetchall()
    allList = []
    for item in all_urls:
        allList.append(item)
    conn.close()

    return allList