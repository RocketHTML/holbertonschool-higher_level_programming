-- creates database hbtn_0d_2 and user user_0d_2
-- user's password is user_0d_2_pwd
-- doesn't fail if database already exists
-- doesn't fail if user already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS `user_0d_2`@`localhost` IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
FLUSH PRIVILEGES;
