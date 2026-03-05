-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- use the database
USE hbtn_0d_usa

-- create table
CREATE TABLE states (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);