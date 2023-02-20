-- taransaction

DROP TABLE users;

SET autocommit = 0;

CREATE TABLE users (
    id INT AUTO_INCREMENT,
    name VARCHAR(10) NOT NULL,
    PRIMARY KEY(id)
);

START TRANSACTION;

INSERT INTO users (name)
VALUES ('harry'), ('test');

SELECT * FROM users;

-- ROLLBACK; 

COMMIT;


-- trigger

DROP TABLE articles;

CREATE TABLE articles ( 
    id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    updatedAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);


INSERT INTO articles (title, createdAt, updatedAt)
VALUES ('title1', current_time(), current_time());

SELECT * FROM articles;


DELIMITER // -- 여기서부터 종료 조건은 이제'//'
CREATE TRIGGER myTrigger
-- 언제?
    BEFORE UPDATE
    ON articles FOR EACH ROW
BEGIN  -- 여러개 일 때
    SET NEW.updatedAt = current_time(); -- 여기 때문에 ;를 // 로
END//
DELIMITER; -- 여기서부터 다시 ;로 복구

DELIMITER //
CREATE TRIGGER myTrigger
-- 언제?
    BEFORE UPDATE
    ON articles FOR EACH ROW
BEGIN
    SET NEW.updatedAt = current_time();
END//
DELIMITER ;

SHOW TRIGGERS;

UPDATE articles
SET title = 'new title'
WHERE id =1;

CREATE TABLE articleLogs (
    id INT AUTO_INCREMENT,
    description VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

-- DELIMITER에 주석 사용하면 실행 안됨
DELIMITER //
CREATE TRIGGER articlelog
    AFTER INSERT
    ON articles FOR EACH ROW
BEGIN
    INSERT INTO articlelogs (description, createdAt)
    VALUES ('글이 작성되었어요.', CURRENT_TIME());
END//
DELIMITER ;


SHOW TRIGGERS;

INSERT INTO articles (title, createdAt, updatedAt)
VALUES ('title2', CURRENT_TIME(), CURRENT_TIME());

SELECT * FROM articles;

SELECT * FROM articlelogs;

DROP TRIGGER  backupArticle;


DELIMITER //
CREATE TRIGGER articlelog
    AFTER INSERT
    ON articles FOR EACH ROW
BEGIN
    INSERT INTO articlelogs (description, createdAt)
    VALUES (CONCAT(NEW.id, '번글이 작성되었어요.'), CURRENT_TIME());
END// -- NEW가 포인트
DELIMITER ;

INSERT INTO articles (title, createdAt, updatedAt)
VALUES ('title2', CURRENT_TIME(), CURRENT_TIME());

SELECT * FROM articlelogs;
SELECT * FROM articles;

CREATE TABLE backupArticles ( 
    id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    updatedAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

DELIMITER //
CREATE TRIGGER backupArticle
    AFTER DELETE
    ON articles FOR EACH ROW
BEGIN
    INSERT INTO backuparticles(title, createdAt, updatedAt)
    VALUES (OLD.title, OLD.createdAt, OLD.updatedAt); -- OLD 사용
END//
DELIMITER ;

SHOW TRIGGERS;

DELETE FROM articles
WHERE  id = 1;