# postergresql is open source which is 
sudo apt-get install libpq-dev(install this beofre install )
export PATH=$PATH:/path/to/your/postgresql/bin
pip install psycopg2


#getting into Database
sudo -i -u postgres
exit from the database
\q
exit

#input channnel crdential
Password: njUh4iCyP56LP8I
Username: azureuser
Private IP: 10.8.0.5
Psql is successfully installed on this machine.

Username: postgres
Password: PostGres32!@

#commands for postgresql
\q-->quit
\l--->list of all database
\c-->to use the database name that we want to use 
\dt -->list all the tables inside the database

CREATE DATABASE (database_name)
#in mysql we will use auto increment but in postgres we will use serial

#You can store PDF files in PostgreSQL using the BYTEA in sql(BLOB)data type or using the Large Object (LOB) feature.
# any files will be send in the form of binary format .i can directly store the binary format to database.
#Handling Foreign Keys
PostgreSQL does not allow  keys on the same column to different tables directly. To manage this situation, you might consider creating separate columns for drive_config_id and email_config_id or use a more complex design with a polymorphic association (which typically requires more logic in your application
#ON DELETE CASCADE: This clause defines the action that will occur if a row in the drive_config table (the referenced table) is deleted. With CASCADE, if a row in drive_config is deleted, all corresponding rows in scheduling_summary that reference that id will also be automatically deleted

#ENUM Columns: For scan_day, you can only use the defined enum values or NULL.
#INT Columns: For scan_month_day, you can also only use an integer value or NUL
#varchar columns : there we can store empty string 
# you can directly store NULL values in PostgreSQL without explicitly defining columns as NULL or using empty strings (''). By default, columns in PostgreSQL can accept NULL unless they are defined with the NOT NULL constraint.
#psycopg2.errors.InvalidTextRepresentation: invalid input syntax for type integer: ""
LINE 1: ...(2,'folder2',6,'high','daily','01:00 AM','Sunday','','2024-0...
            this is the error i was facing i was inserting the wrong data type value value to it 
i defined int but passing ''(string)

#





                                                             ^
                                                                                                                                                                                                                                                          

