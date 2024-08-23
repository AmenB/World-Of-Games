CREATE DATABASE IF NOT EXISTS db;

USE db;

CREATE TABLE score(
    Name varchar(100) NOT NULL,
    Score int NOT NULL,
    PRIMARY KEY (Name)
);

INSERT INTO score(Name, Score)
VALUES("Amen", 10)

