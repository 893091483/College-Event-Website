CREATE TABLE Users (
    id INT PRIMARY KEY NOTNULL,
    password VARCHAR(128) NOTNULL,
    last_login DATATIME,
    is_superuser BOOL NOTNULL,
    username VARCHAR(150) NOTNULL,
    first_name VARCHar(150) NOTNULL,
    last_name VARCHAR(150) NOTNULL,
    email VARCHAR(254) NOTNULL,
    is_staff BOOL NOTNULL,
    is_active BOOL NOTNULL,
    data_joined DATETIME,
    is_admin BOOL NOTNULL,
    is_super_admin BOOL NOTNULL,
    university_id INT
);


INSERT INTO Users_users (
    id,	
    last_login,	
    is_superuser,	
    username,	
    first_name,	
    last_name,	
    email,	
    is_staff,	
    is_active,	
    date_joined,	
    is_admin,
    is_super_admin,	
    university_id,	
    password
)

VALUES(
    1,	
    "2021-04-15 16:46:21.398589",	
    0,	
    "tman1",
    "Tom",
    "Mann",	
    "tommann@gmail.com",	
    0,
    1,	
    "2021-04-10 17:18:50.190694,	
    1,	
    0,	
    1,	
    "gAAAAABgcd36t4EBlJJ7jZ6BA9lpJVrBWAe4jHNgDVlIqui85oB_
    7JBwLvT4flYfC6Rqp9jDSmDpepurZSv-fvzaa5ZuYGlfoQ=="
)
