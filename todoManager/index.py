# DATABASE MANAGEMENT SYSTEMS
# database => a collection data 
# DBMS => a software system that allows you to manage data in a database
# SQL => Structured query language

# 1 RELATIONAL DATABASE MANAGEMENT SYSTEMS(SQL)

# TABLE RELATIONSHIP 
# 1. One-To-One (1:1)
# user_table:profile_table

'''
USER TABLE
user_id(PRIMARY KEY)__________fullname_________email________password
1__________John Doe________john.doe@gmail.com________123456
2__________Jane Doe________jane.doe@gmail.com________123456


PROFILE TABLE
profile_id(PRIMARY KEY)__________user_id(FOREIGN KEY)___________address__________phone_number
    1________________________________2________________________123 Main St__________123-456-7890
    2________________________________1________________________45 Elm St__________987-654-3210
'''

# 2. ONE-TO-MANY
# user_table:order_table
'''
order_id _______________ user_id(FOREIGN KEY)_____________order_date__________total_cost
1        __________         1__________                     2022-01-01__________100.00
2        __________         1__________                     2022-01-02__________200.00
3        __________         1__________                     2022-01-05__________500.00

'''

# 3. MANY-TO-MANY
# user_table:order_table:transaction_table

'''
transaction table

trans_id ____________________ user_id(FOREIGN KEY)__________order_id(FOREIGN KEY)__________item
1        ____________________ 1__________                     1__________                   item1
2        ____________________ 1__________                     1__________                   item2
3        ____________________ 1__________                     2__________                   item1


'''

# SUB LANGUAGES IN SQL
# 1. DDL -> Data Definition Language
# e.g CREATE TABLE/DATABASE, ALTER TABLE/DATABASE, DROP TABLE/DATABASE
"""
CREATE TABLE user_table(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    fullname VARCHAR(50) NULL,
    email VARCHAR(50) UNIQUE,
    `password` VARCHAR(50),
    date_created DATETIME DEFAULT CURRENT_TIMESTAMP
)

CREATE TABLE product_table( id INT AUTO_INCREMENT PRIMARY KEY, product_name VARCHAR(50) UNIQUE, description TEXT, price FLOAT, quantity INT, image VARCHAR(50) created_by INT, FOREIGN KEY (created_by) REFERENCES user_table(user_id) ON DELETE CASCADE );


DROP TABLE product_table;

ALTER TABLE product_table2 RENAME product_table;
ALTER TABLE product_table CHANGE product_name title VARCHAR(50);
ALTER TABLE product_table ADD created_at DATETIME DEFAULT CURRENT_TIMESTAMP;
ALTER TABLE product_table DROP COLUMN created_at;

"""

# 2. DATA MANIPULATION LANGUAGE (DML):
# e.g INSERT, UPDATE, DELETE
"""
INSERT INTO user_table(fullname, email, password) VALUES('Aolat', 'aolat@gmail.com', 'password');
INSERT INTO product_table(title, description, quantity, price, user_id) VALUES('product 2', 'product 2 description', 23, 2333, 2);

"""