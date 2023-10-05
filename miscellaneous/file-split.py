ls = ["132-file.pdf","22.pdf","res.txt","72.txt","slove.png","output.png"]
res_dict = {}
ls1 = []
for i in ls:
    value = i.split(".")
    if "pdf" in value:
        res_dict[value[-1]] = value[0]
    elif "txt" in value:
        res_dict[value[-1]] = value[0]
    elif "png" in value:
        res_dict[value[-1]] = value[0]

print(res_dict)
        