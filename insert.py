from sqlalchemy import *
from random import randint, uniform
from music_data import singers, genres, albums, tracks, collections

engine = create_engine('postgresql://abr:admin@localhost:5432/netology')
connection = engine.connect()

# Task 1

# Inserting Singers
for singer_name in singers:
    connection.execute(f'''INSERT INTO music.singer(name) VALUES ('{singer_name}');''')

# Inserting Genres
for genre_name in genres:
    connection.execute(f'''INSERT INTO music.genre(name) VALUES ('{genre_name}');''')

# Singer_Genre assigning
for singer_id in range(1, len(singers) + 1):
    connection.execute(f'''INSERT INTO music.singer_genre(singer_id, genre_id)
    VALUES ('{singer_id}', '{randint(1, 5)}');''')

# Inserting Albums
for album_name in albums:
    connection.execute(f'''INSERT INTO music.album(name, release_year)
    VALUES ('{album_name}', '{randint(1988, 2019)}');''')

# Singer_Album assigning (as in our case first id goes for both singer and album) and there are equal
for n in range(1, len(singers) + 1):
    connection.execute(f'''INSERT INTO music.singer_album(singer_id, album_id)
    VALUES ('{n}', '{n}');''')

# Inserting Track and Assigning album ID
for track_n in range(len(tracks)):
    for track in tracks[track_n]:
        connection.execute(f'''INSERT INTO music.track(name, duration_m, album_id)
        VALUES ('{track}', '{round(uniform(1.10, 4.15), 2)}', '{track_n + 1}');''')

# Inserting Collection
for coll_name in collections:
    connection.execute(f'''INSERT INTO music.collection(name, release_year)
    VALUES ('{coll_name}', '{randint(1988, 2021)}');''')

# Tracks and Collection assigning
track_id = 0
for coll_id in range(len(tracks)):
    for n in range(len(tracks[coll_id])):
        track_id += 1
        connection.execute(f'''INSERT INTO music.track_collection(track_id, collection_id)
        VALUES ('{track_id}', '{coll_id + 1}');''')

