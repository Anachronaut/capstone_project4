import sqlite3


db = 'bookmark_db.sqlite'


def create_db():
    conn = sqlite3.connect(db)

    conn.execute('CREATE TABLE IF NOT EXISTS bookmarks (' +
                'primaryKey INTEGER PRIMARY KEY, ' +
                'trackID TEXT, trackArtist TEXT, trackName TEXT, trackURI TEXT, ' +
                'imageID INTEGER, imageURL TEXT)')
    conn.commit()
    conn.close()



def add_track(track, image):
    add_track_sql = 'INSERT INTO bookmarks (trackID, trackArtist, trackName, trackURI, imageID, imageURL) VALUES (?, ?, ?, ?, ?, ?)'

    with sqlite3.connect(db) as conn:
        added = conn.execute(add_track_sql, (track, image))
        added_count = added.rowcount
    conn.close()

    if added_count != 0:
        return True
    else:
        return False



def display_all():
    conn = sqlite3.connect(db)
    display_all_tracks_sql = 'SELECT * FROM bookmarks'

    cur = conn.execute(display_all_tracks_sql)
    all_urls = cur.fetchall()
    allList = []
    for item in all_urls:
        allList.append(item)
    conn.close()

    return allList



def search_track(pk):
    conn = sqlite3.connect(db)
    search_track_url = 'SELECT * FROM bookmarks WHERE primaryKey = ?'

    cur = conn.execute(search_track_url, (pk, ))
    item = cur.fetchone()

    conn.close()
    return item