
-- /!\ REMOVE BEFORE SENDING /!\

DROP DATABASE IF EXISTS p2p_blog;

-- /!\ CAREFULL /!\

-- Create the database
CREATE DATABASE p2p_blog CHARACTER SET 'utf8';

-- Switch for using the database
USE p2p_blog;

-- Create a table for the categories
CREATE TABLE Categories (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(150) NOT NULL,
    description TEXT NOT NULL,
    PRIMARY KEY (id)
);

-- Create a table for the users
CREATE TABLE Users (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    pseudo VARCHAR(150) NOT NULL UNIQUE,
    mail VARCHAR(150) NOT NULL UNIQUE,
    password TEXT NOT NULL,
    PRIMARY KEY (id)
);

-- Create a table for posts
CREATE TABLE Posts (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    title VARCHAR(150) NOT NULL,
    post_text TEXT NOT NULL,
    sample TEXT NOT NULL,
    post_date DATETIME NOT NULL,
    author_id INT UNSIGNED,
    PRIMARY KEY (id),
    CONSTRAINT fk_author_user_id
        FOREIGN KEY (author_id)
        REFERENCES Users(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Create a table for comments
CREATE TABLE Comments (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    comment TEXT NOT NULL,
    comment_date DATETIME NOT NULL,
    post_id INT UNSIGNED NOT NULL,
    author_id INT UNSIGNED,
    PRIMARY KEY (id),
    CONSTRAINT fk_comment_post_id
        FOREIGN KEY (post_id)
        REFERENCES Posts(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_comment_author_id
        FOREIGN KEY (author_id)
        REFERENCES Users(id) 
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Create the intermediate table for associate categories with posts
CREATE TABLE Post_categories (
    post_id INT UNSIGNED NOT NULL,
    category_id INT UNSIGNED NOT NULL,
    PRIMARY KEY (category_id, post_id),
    CONSTRAINT fk_category_id
        FOREIGN KEY (category_id)
        REFERENCES Categories(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_post_id
        FOREIGN KEY (post_id)
        REFERENCES Posts(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


-- Insert three categories for the example
INSERT INTO Categories (name, description)
VALUES ('First category', 'The first category for the blog'),
       ('Second category', 'The second one'),
       ('Third category', 'The third and last category on this blog');

SELECT * FROM Categories;

-- Insert three users
INSERT INTO Users (pseudo, mail, password)
VALUES ('User 1', 'user1@gmail.com', '$[o$xbD!}S}Q%E]rmhXR2P1M5p7$dXUy'),
       ('User 2', 'user2@gmail.com', 'QKmoC]6(t4Adk3uhM|Q3{QsreHf>YsjK'),
       ('User 3', 'user3@gmail.com', '7Wj8{Sr{I]p>]^EA<C>F<4p>%qNjXpHr');

SELECT * FROM Users;

-- Insert six posts
INSERT INTO Posts (title, post_text, sample, post_date, author_id)
VALUES
    (
        'Title 1 for the first post on the blog !',
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis hendrerit.',
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit...',
        '2019-10-05 20:44:00',
        1
    ),
    (
        'Title 2 for the second post on the blog !',
        'Aliquam sagittis nibh quis laoreet aliquet. Curabitur pellentesque.',
        'Aliquam sagittis nibh quis laoreet aliquet...',
        '2019-10-13 18:37:33',
        2
    ),
    (
        'Title 3',
        'Phasellus pharetra volutpat velit quis sollicitudin. Praesent porttitor.',
        'Phasellus pharetra volutpat velit quis sollicitudin...',
        '2019-10-27 08:58:46',
        2
    ),
    (
        'Title 4',
        'Mauris posuere eu urna id rutrum. Cras enim lacus, condimentum et porttitor ac.',
        'Mauris posuere eu urna id rutrum. Cras enim lacus..',
        '2019-11-07 12:02:13',
        1
    ),
    (
        'Title 5',
        'In ut porttitor tellus, sit amet egestas sem. Aenean vestibulum tortor .',
        'In ut porttitor tellus, sit amet egestas sem...',
        '2019-11-11 16:30:27',
        1
    ),
    (
        'Title 6',
        'Nam nisi velit, consectetur at libero sed, suscipit accumsan arcu. ',
        'Nam nisi velit, consectetur at libero sed, suscipit...',
        '2019-11-18 08:09:39',
        1
    );

SELECT id, title, post_date FROM Posts;

-- Insert categories for posts
INSERT INTO Post_categories
VALUES (1, 2),
       (1, 3),
       (2, 1),
       (3, 3),
       (3, 2),
       (3, 1),
       (4, 2),
       (5, 1),
       (6, 2);

SELECT * FROM Post_categories;

-- Insert comments for the post 1
INSERT INTO Comments (comment, comment_date, post_id, author_id)
VALUES ('One comment for all humans', '2019-11-05 13:36:00', 1, 2),
       ('Wonderfull!', '2019-11-06 13:36:00', 1, NULL),
       ('Why it is so complicated to read?', '2019-11-18 00:36:00', 1, 1),
       ('Maybe because it\'s to late...', '2019-11-18 01:36:00', 1, 1);

SELECT * FROM Comments;

-- Home page
SELECT 'Home page';
SELECT Posts.title,
       Posts.post_date,
       Users.pseudo AS author,
       Posts.sample
FROM Posts
INNER JOIN Users ON Users.id = Posts.author_id
ORDER BY Posts.post_date DESC;

-- User page
SELECT 'Page for user 1';
SELECT Posts.title,
       Posts.post_date,
       Posts.sample
FROM Posts
WHERE Posts.author_id = (SELECT id FROM Users WHERE pseudo = 'User 1')
ORDER BY Posts.post_date DESC;

-- Category page
SELECT 'Page for category 2';
SELECT Posts.title,
       Posts.post_date,
       Posts.sample
FROM Posts
WHERE Posts.id IN
    (SELECT post_id FROM Post_categories WHERE category_id = 2)
ORDER BY Posts.post_date DESC;

-- Post page
SELECT 'Page for post number 1';
SELECT Posts.title,
       Posts.post_date,
       Posts.post_text,
       Users.pseudo AS author_name
FROM Posts
INNER JOIN Users ON Users.id = Posts.author_id
WHERE Posts.id = 1;

SELECT Comments.comment,
       Comments.comment_date,
       Users.pseudo AS author_name
FROM Comments
INNER JOIN Users ON Users.id = Comments.author_id
WHERE Comments.post_id = 1
ORDER BY Comments.comment_date DESC;
