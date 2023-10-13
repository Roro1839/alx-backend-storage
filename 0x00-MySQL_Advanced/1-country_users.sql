--Create table users which doesn't exit
CREATE TABLE IF NOT EXISTS users (
-- Id should be int never nulll
id INTEGER AUTO_INCREMENT PRIMARY KEY,
-- Email unique maximum (255 char)
email VARCHAR(255) NOT  NULL UNIQUE,

-- Name should be a maximum (255 char)
name VARCHAR(255),

country ENUM('US','CO' and 'TN') NOT NULL DEFAULT 'US'
);
