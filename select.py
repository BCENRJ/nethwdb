from sqlalchemy import *

engine = create_engine('postgresql://abr:admin@localhost:5432/netology')
connect = engine.connect()

# Genres and number of singers in each genre
sel_first = connect.execute('''SELECT name, count(*) FROM music.genre g
JOIN music.singer_genre sg ON g.id = sg.genre_id
GROUP BY name;''').fetchall()
print(sel_first)

# Number of tracks released in 2019 and 2020
sel_second = connect.execute('''SELECT count(*) FROM music.track t
JOIN music.album a ON t.album_id = a.id
WHERE a.release_year BETWEEN 2019 AND 2020;''').fetchall()
print(sel_second)

# Avg for tracks by per album
sel_third = connect.execute('''SELECT a.name, round(avg(t.duration_m), 2) FROM music.album a
JOIN music.track t ON a.id = t.album_id
GROUP BY a.name;''').fetchall()
print(sel_third)

# Singers without 2020 album release
sel_fourth = connect.execute('''SELECT s.name FROM music.singer s
JOIN music.singer_album sa ON s.id = sa.singer_id
JOIN music.album a on sa.album_id = a.id
WHERE a.release_year <> 2020;''').fetchall()
print(sel_fourth)

# Name of the collection where a certain singer participating
sel_five = connect.execute('''SELECT c.name FROM music.collection c
JOIN music.track_collection tc ON c.id = tc.collection_id
JOIN music.track t ON tc.track_id = t.id
JOIN music.album a ON t.album_id = a.id
JOIN music.singer_album sa ON a.id = sa.album_id
JOIN music.singer s ON s.id = sa.singer_id
WHERE s.name = 'Marvin'
GROUP BY c.name;''').fetchall()
print(sel_five)

# Albums of those singers who are in more than 1 genre singing
sel_six = connect.execute('''SELECT a.name FROM music.album a
JOIN music.singer_album sa ON a.id = sa.album_id
JOIN music.singer s ON s.id = sa.singer_id
JOIN music.singer_genre sg on s.id = sg.singer_id
JOIN music.genre g on g.id = sg.genre_id
GROUP BY a.name
HAVING count(sg.genre_id) > 1;''').fetchall()
print(sel_six)

# Tracks - out of any music collection
sel_seven = connect.execute('''SELECT t.name FROM music.track t
LEFT JOIN music.track_collection tc ON t.id = tc.track_id
WHERE tc.track_id IS NULL;''').fetchall()
print(sel_seven)

# Singers with min duration track
sel_eight = connect.execute('''SELECT s.name FROM music.singer s
JOIN music.singer_album sa on s.id = sa.singer_id
JOIN music.album a on a.id = sa.album_id
JOIN music.track t on a.id = t.album_id
WHERE t.duration_m = (SELECT MIN(duration_m) FROM music.track);''').fetchall()
print(sel_eight)

# Albums with min number of tracks
sel_nine = connect.execute('''SELECT a.name FROM music.album a
JOIN music.track t on a.id = t.album_iD
GROUP BY a.name
HAVING count(a.name) = (SELECT min(count) FROM (SELECT COUNT(*) FROM music.track GROUP BY album_id) t);''').fetchall()
print(sel_nine)
