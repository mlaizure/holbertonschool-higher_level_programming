-- creates database hbtn_0d_usa and table states (in database hbtn_0d_usa)
-- state has int primary key and name can't be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(256) NOT NULL);
