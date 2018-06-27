-- creates a test user `user_0d_1` with pw `user_0d_1_pwd` for the database
CREATE USER IF NOT EXISTS `user_0d_1`@`localhost` IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO `user_0d_1`@`localhost`;
