\q
CREATE TABLE Users (name varchar, lastname varchar, age int, tel varchar);
\t
\t
\d
\c
\clear
INSERT INTO User (name, lastname, age, tel) VALUES ('Vasya', 'Pupkin', 18, '+37529222222');
INSERT INTO Users (name, lastname, age, tel) VALUES ('Vasya', 'Pupkin', 18, '+37529222222');
select * from users;
INSERT INTO Users (name, lastname, age, tel) VALUES ('Ivan', 'Ivanov', 234, '+375292456456');
select * from users;
INSERT INTO Users (name, lastname) VALUES ('Ivan', 'Ivanov');
select * from users;
create table Test (col1 varchar NOT NULL, col2 int);
insert into test (col1, col2) values ('asdsd', 325);
select * from test ;
insert into test (col2) values (234234325);
insert into test (col1) values ('asdsda');
select * from test ;
select * from users;
UPDATE users SET age = 23, tel = '3453454353' WHERE age is null;
select * from users;
UPDATE users SET name = 'Petr' WHERE age = 23;
select * from users;
DELETE FROM users WHERE name = 'Petr';
select * from users;
UPDATE users SET Age = NULL where name = 'Ivan';
select * from users;
insert into users (name, lastname, age, tel) values ('Ivan', 'Smith', 25, '345346456');
select * from users;
select * from users where name = 'Ivan' and age = 25;
select * from users where name = 'Ivan' and age = '25';
select * from users where name = 'Ivan' and age = 25;
select * from users;
select * from users where name = 'Ivan' and age = 25 or name = 'Vasya';
\timing 
select * from users where name = 'Ivan' and age = 25 or name = 'Vasya';
select * from users ;
ALTER TABLE users ADD COLUMN (id int);
ALTER TABLE users ADD COLUMN id int;
select * from users;
ALTER TABLE users ADD COLUMN not_null_id int NOT NULL;
ALTER TABLE users ADD COLUMN not_null_id int NOT NULL default 100; 
select * from users;
ALTER TABLE users DROP COLUMN not_null_id ;
select * from users;
DROP TABLE test ;
select * from test;
\s ~/Development/tests/python3/teachmeskills/lecture11/1
\d
create table test (
name varchar(10)
);
insert into test (name) values ('1sdfsdfsdfsdfsfsfsdf');
insert into test (name) values ('1sdfsd');
select * from test;
drop table users;
create table users (name varchar NOT NULL UNIQUE, lastname varchar NOT NULL);
insert into users (name, lastname) values ('Ivan', 'Ivanov');
select * from users;
insert into users (name, lastname) values ('Ivan', 'Petrov');
drop table users;
create table users (name varchar NOT NULL, lastname varchar NOT NULL, unique(name, lastname));
insert into users (name, lastname) values ('Ivan', 'Ivanov');
insert into users (name, lastname) values ('Ivan', 'Petrov');
insert into users (name, lastname) values ('Ivan', 'Petrov');
drop table users;
create table users (name varchar NOT NULL, lastname varchar NOT NULL, unique(name, lastname) name_last_unique);
create table users (name varchar NOT NULL, lastname varchar NOT NULL);
ALTER TABLE users ADD CONSTRAINT unique_name_lastname UNIQUE (name, lastname);
insert into users (name, lastname) values ('Ivan', 'Petrov');
insert into users (name, lastname) values ('Ivan', 'Petrov');
drop table users;
create table users (id int NOT NULL UNIQUE, name varchar, lastname varchar);
insert into users (id, name, lastname) values (1, 'Ivan', 'Ivanov');
insert into users (id, name, lastname) values (2, 'Petr', 'Ivanov');
select * from users;
insert into users (id, name, lastname) values (2, 'Petr', 'Petrov');
insert into users (id, name, lastname) values (3, 'Petr', 'Petrov');
select * from users;
select * from users where id = 1
;
drop table users
;
create table users (id SERIAL NOT NULL UNIQUE, name varchar, lastname varchar);
insert into users (name, lastname) values ('Petr', 'Petrov');
select * from users;
insert into users (name, lastname) values ('Petr', 'Invanov');
select * from users;
insert into users (name, lastname) values ('Petr', 'Invanov');
insert into users (name, lastname) values ('Petr', 'Invanov');
A
insert into users (name, lastname) values ('Petr', 'Invanov');

insert into users (name, lastname) values ('Petr', 'Invanov');
select * from users;
\dt
insert into users (id, name, lastname) values (6, 'Petr', 'Invanov');
select * from users;
insert into users (id, name, lastname) values (8, 'Petr', 'Invanov');
select * from users;
insert into users (name, lastname) values ('Petr', 'Invanov');
insert into users (name, lastname) values ('Petr', 'Invanov');
insert into users (name, lastname) values ('Petr', 'Invanov');
insert into users (name, lastname) values ('Petr', 'Invanov');
select * from users;
drop table users;
create table users (id SERIAL PRIMARY KEY, name varchar, lastname varchar);
insert into users (name, lastname) values ('Petr', 'Invanov');
select * from users;
insert into users (name, lastname) values ('Ivan', 'Petrov');
select * from users;
select * from users;
create table phones (id serial primary key, tel varchar, user_id int);
insert into phones (tel, user_id) values ('325345345', 1);
insert into phones (tel, user_id) values ('32556756756', 1);
insert into phones (tel, user_id) values ('3453456756', 1);
insert into phones (tel, user_id) values ('123123', 2);
select * from phones;
select * from users;
insert into phones (tel, user_id) values ('123123', 100500);
select * from phones;
drop table phones;
create table phones (id serial primary key, tel varchar, user_id int REFERENCE users (id));
create table phones (id serial primary key, tel varchar, user_id int REFERENCES users (id));
insert into phones (tel, user_id) values ('123123', 1);
insert into phones (tel, user_id) values ('123123', 100500);
select * from phones;
select * from users;
delete from users where id = 1;
drop table phones;
create table phones (id serial primary key, tel varchar, user_id int REFERENCES users (id) ON DELETE CASCADE);
insert into phones (tel, user_id) values ('123123', 1);
select * from phones;
select * from users;
delete from users where id = 1;
select * from users;
select * from phones;
\d
select * from users_id_seq;
\d+
\dt+ users
\dt users
\d+ users
\d+ users
select * from phones;
select * from users;
insert into users (name, lastname) values ('Petr', 'Ivanov');
insert into phones (tel, user_id) values ('234234234', 1);
insert into phones (tel, user_id) values ('234234234', 2);
insert into phones (tel, user_id) values ('567567567', 2);
insert into phones (tel, user_id) values ('1111567567567', 3);
insert into phones (tel, user_id) values ('1111333567', 3);
select * from users;
select * from phones;
select * from users as u join phones as p ON u.id = p.user_id;
select name from (select * from users as u join phones as p ON u.id = p.user_id);
select s.name from (select * from users as u join phones as p ON u.id = p.user_id) as s;
insert into users (name, lastname) values ('John', 'Smith')
;
select * from users;
select * from users as u join phones as p ON u.id = p.user_id;
select * from users as u left inner join phones as p ON u.id = p.user_id;
select * from users as u left  join phones as p ON u.id = p.user_id;
select * from users as u inner join phones as p ON u.id = p.user_id;
select * from users as u left join phones as p ON u.id = p.user_id;
select * from users as u right join phones as p ON u.id = p.user_id;
select count(*) from users;
select count(*) from users as u right join phones as p ON u.id = p.user_id;
select * from users;
insert into users (name, lastname) values ('John', 'Hopkins')
;
select * from users;
select name from users;
select distinct(name) from users;
select * from users;
\q
\q
\s
\s teachmeskills/lecture11/lecture.sql
