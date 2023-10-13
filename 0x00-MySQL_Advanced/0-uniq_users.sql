-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
CREATE TABLE users (
-- Unique identifier for each user
id INTEGER PRIMARY KEY  AUTO_INCREMENT,
-- String (255 characters), never null and unique
email VARCHAR(255) NOT NULL UNIQUE,

-- Name of the user (maximum 255 characters)
name VARCHAR(255)
);
