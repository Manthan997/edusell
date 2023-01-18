-- this file is a sql file and thus uses sql syntax
/*
used to define the structure of .db file
all tables to be made with there colums are defined here
you can add other DMLs here as an sql file but better keep ot seperate for understanding 
*/

DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS suser;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title VARCHAR NOT NULL,
    content VARCHAR NOT NULL,
    price FLOAT NOT NULL,
    seller_ID INTEGER NOT NULL,
    seller_name VARCHAR ,
    FOREIGN KEY(seller_ID) REFERENCES suser(id),
    FOREIGN KEY(seller_name) REFERENCES suser(sname)
);

CREATE TABLE suser(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sname VARCHAR NOT NULL,
    gr_no INTEGER NOT NULL UNIQUE,
    branch VARCHAR NOT NULL,
    email VARCHAR NOT NULL UNIQUE, 
    passw VARCHAR(60) NOT NULL
);