/*CREATE DATABASE test1;
GO
 
USE test1;
GO 

CREATE TABLE tbl_users(
	id INT IDENTITY(1,1) PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	gender VARCHAR(10) NOT NULL,
	age INT NOT NULL
);
GO*/
USE test1;
GO
SELECT * FROM tbl_users;
GO

BACKUP DATABASE test1
TO DISK = 'C:\Users\elmar\OneDrive\Escritorio\GitHub\mvc_1_practice\Py_SQL\test1_backup.bak'
GO