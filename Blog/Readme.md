# To do list

## Table creation

### 'Posts'
- [x] id            => INT UNSIGNED NOT NULL AUTO_INCREMENT
- [x] title         => VARCHAR(150) NOT NULL
- [x] post_text     => TEXT NOT NULL
- [x] sample        => TEXT NOT NULL
- [x] post_date     => DATETIME NOT NULL
- [x] author_id     => INT UNSIGNED NOT NULL

### 'Users'
- [x] id            => INT UNSIGNED NOT NULL AUTO_INCREMENT
- [x] pseudo        => VARCHAR(150)
- [x] mail          => VARCHAR(150)
- [x] password      => TEXT

### 'Categories'
- [x] id            => INT UNSIGNED NOT NULL AUTO_INCREMENT
- [x] name          => VARCHAR(150) NOT NULL
- [x] description   => TEXT NOT NULL

### 'Post_categories'
- [x] post_id       => INT UNSIGNED NOT NULL
- [x] category_id   => INT UNSIGNED NOT NULL

### 'Comments'
- [x] id            => INT UNSIGNED NOT NULL AUTO_INCREMENT
- [x] comment       => TEXT NOT NULL
- [x] comment_date  => DATETIME NOT NULL
- [x] post_id       => INT UNSIGNED NOT NULL
- [x] author_id     => INT UNSIGNED

## Selection requests

### Home page
- [x] Posts.title
- [x] Posts.post_date
- [x] user.name
- [x] Posts.sample
- [x] ORDER BY Posts.post_date DESC

### User page
- [x] Posts.title
- [x] Posts.post_date
- [x] Posts.sample
- [x] WHERE user.id = 1
- [x] ORDER BY Posts.post_date DESC

### Category page
- [x] Posts.title
- [x] Posts.post_date
- [x] Posts.sample
- [x] WHERE category_id = 2
- [x] ORDER BY Posts.post_date

### Post page
- [ ] Posts.title
- [ ] Posts.post_text
- [ ] Posts.post_date
- [ ] Comments.comment (ORDER BY Comments.comment_date DESC)
- [ ] WHERE Posts.id = 1
