CREATE TABLE students2 (
	id serial PRIMARY KEY,
	fname VARCHAR ( 40 ) NOT NULL,
	lname VARCHAR ( 40 ) NOT NULL,
	email VARCHAR ( 40 ) NOT NULL,
	profile_pic VARCHAR ( 150 ) NULL
);

SELECT * FROM students2