CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT NOT NULL,
	author TEXT NOT NULL,
    year INTEGER NOT NULL
);

INSERT INTO books (title, author, year)
VALUES ('The Myth Of Normal', 'Gabor Mate', 2022);

INSERT INTO books (title, author, year)
VALUES ('Homo Deus', 'Yuval Noah Harari', 2016);

INSERT INTO books (title, author, year)
VALUES ('Unconditional Parenting', 'Alfie Kohn', 2016);

INSERT INTO books (title, author, year)
VALUES ('Big Magic', 'Elisabeth Gilbert', 2015);