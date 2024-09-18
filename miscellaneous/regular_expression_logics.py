#str_ = "manigandan.v@sonata-software.com;girish@cogniquest.ai" in this i need to extract the emails
# here comes regular expression we use pattern if the pattern matches it will retrn those strings
str_ = "manigandan.v@sonata-software.com;girish@cogniquest.ai"
emial_col1 = re.findall(r"[A-Za-z0-9._%+-]+"r"@[A-Za-z0-9.-]+"r"\.[A-Za-z]{2,4}", str(str_)) 
#______________________________________________________________________________________________________

