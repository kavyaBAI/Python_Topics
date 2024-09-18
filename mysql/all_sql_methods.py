#if the customer is smtg like this cust_name = "Dr. Reddy's Laboratories Ltd"
sql = "SELECT customer_id FROM customer_mgmt where customer_name = '%s';"
#will give error MySQLdb.ProgrammingError: (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 's Laboratories Ltd'' at line 1")
sql = 'SELECT customer_id FROM customer_mgmt where customer_name = "%s";'
#_______________________________________________________________________________________________________________________________

