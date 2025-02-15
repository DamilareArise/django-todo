# DATABASE MANAGEMENT SYSTEMS
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

# 3. MANY-TO-MANY
# user_table:order_table:transaction_table


# SUB LANGUAGES IN SQL
# 1. DDL -> Data Definition Language
# e.g CREATE TABLE/DATABASE, ALTER TABLE/DATABASE, DROP TABLE/DATABASE