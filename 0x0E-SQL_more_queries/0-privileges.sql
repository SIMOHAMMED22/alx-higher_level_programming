-- lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
FROM information_schema.user_privileges
WHERE grantee = 'user_0d_1@localhost' OR grantee = 'user_0d_2@localhost';
