from sqlalchemy import *

engine = create_engine('postgresql://abr:admin@localhost:5432/netology')
connection = engine.connect()

# Task 2

sel_first = connection.execute('''SELECT name, release_year FROM music.album
                                  WHERE release_year = 2018''').fetchall()
print(sel_first)

sel_second = connection.execute('''SELECT name, duration_m FROM music.track
                                    WHERE duration_m = (SELECT max(duration_m) FROM music.track)''').fetchall()
print(sel_second)

sel_third = connection.execute('''SELECT name, duration_m FROM music.track
                                    WHERE duration_m > 3.5''').fetchall()
print(sel_third)

sel_fourth = connection.execute('''SELECT name, release_year FROM music.collection
                                    WHERE release_year BETWEEN 2018 AND 2020''').fetchall()
print(sel_fourth)

sel_fifth = connection.execute('''SELECT name FROM music.singer
                                    WHERE name NOT LIKE '%% %%' ''').fetchall()
print(sel_fifth)

sel_six = connection.execute('''SELECT name FROM music.track
                                 WHERE name ILIKE '%%my%%' ''').fetchall()
print(sel_six)
