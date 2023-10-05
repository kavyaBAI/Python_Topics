#__________________________________________________________________
#like query in mongocompass
  
            export_data.deletedata(db_str1, collection, query)
#----------------------------------------------------------------------
#to update the values we will use set opeartor
  query = {"type":"session_host"}
    new_values = {"$set":{"max_id":res1}}
    val = export_data.updatedata(db_str, "citrix_report_id", query, new_values)
#____________________________________________________________________________________

#$in opeartor 
{date :{$in:["2023-09-08","2023-09-09","2023-09-011"]}}
#________________________________________________________________