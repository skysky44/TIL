-- 문제 1
CREATE TABLE users (
    userid INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    birthday DATE NOT NULL,
    city VARCHAR(100) NULL,
    country VARCHAR(100) NULL,
    email VARCHAR(100) NULL,
    created_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (userid)
);


SHOW COLUMNS FROM users;

-- 문제 2
SELECT * FROM users;

INSERT INTO 
    users (first_name, last_name, birthday, city, country, email)
VALUES
    ('Beemo', 'Jeong', '1000-01-01', NULL, NULL, 'beemo@hphk.kr'),
    ('Jieun', 'Lee', '1993-05-16', 'Seoul', 'Korea', NULL),
    ('Dami', 'Kim',	'1995-04-09', 'Seoul', 'Korea', NULL),
    ('Kwangsoo', 'Lee', '1985-07-14', 'Seoul', 'Korea', NULL);

-- 문제 3
INSERT INTO 
    users (first_name, last_name, birthday, city, country, email)
VALUES
    ('Aeemo', 'Jeong', '1000-01-01', NULL, NULL, 'beemo@hphk.kr'),
    ('Bieun', 'Lee', '1993-05-16', 'Seoul', 'Korea', NULL),
    ('Cami', 'Kim',	'1995-04-09', 'Seoul', 'Korea', NULL),
    ('Dwangsoo', 'Lee', '1985-07-14', 'Seoul', 'Korea', NULL),
    ('Dwangsoo', 'Lee', '1985-07-14', 'Seoul', 'Korea', NULL);

-- 문제 4
UPDATE users
SET
    first_name = replace(first_name, 'Jieun', 'Jeonghwan'),
    last_name = replace(last_name, 'Lee', 'An'),
    birthday = replace(birthday, '1993-05-16', '1993-01-01')
WHERE
    userid = 2;

-- SET SQL_SAFE_UPDATES = 0; 
 
-- 문제 5
UPDATE users
SET 
    country = 'Korea'
WHERE
    country IS NULL; 
    -- NULL인 데이터 변경 시 IS 사용

    
-- 문제 6
DELETE FROM users
WHERE
    first_name = 'Beemo';

-- 문제 7
DELETE FROM users
WHERE
    first_name = 'Kwangsoo'
AND last_name = 'Lee';

-- 문제 8
DELETE FROM users
ORDER BY
    created_at DESC
LIMIT 1;

-- SELECT 
--     created_at
-- FROM
--     users
-- ORDER BY
--     created_at DESC;

-- SELECT * FROM users;
    


    