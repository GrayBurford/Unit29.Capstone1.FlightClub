# -- EXAMPLE

# -- DROP DATABASE IF EXISTS  movies_db;
# -- CREATE DATABASE movies_db;

# \c movies_db
# DROP TABLE IF EXISTS movies;
# CREATE TABLE movies
# (
#   id SERIAL PRIMARY KEY,
#   title TEXT NOT NULL,
#   release_year INTEGER NOT NULL,
#   runtime INTEGER NOT NULL,
#   rating TEXT NOT NULL
# );

# INSERT INTO movies
#   (title, release_year, runtime, rating)
# VALUES
#   ('Star Wars: The Force Awakens', 2015, 136, 'PG-13'),
#   ('Avatar', 2009, 160, 'PG-13'),
#   ('Titanic', 1997, 194, 'PG-13'),
#   ('Jurassic World', 2015, 124, 'PG-13'),
#   ('Marvel''s The Avengers', 2012, 142, 'PG-13'),
#   ('Star Wars: The Last Jedi', 2017, 151, 'PG-13'),
#   ('Black Panther', 2018, 140, 'PG-13');