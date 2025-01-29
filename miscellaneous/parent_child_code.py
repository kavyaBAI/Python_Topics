

#if there is parent child realtion first work on child part then the parent parent part,use recursive function 
def build_tree(ls, ms):
    children = []
    
    for child_id, nested in ls.items():
        child_data = ms.get(child_id)
        if child_data:
            child_entry = {
                "key": child_id,
                "title": child_data["name"],
                "children": build_tree(nested,ms)  # Recursively build children
            }
            children.append(child_entry)
    
    return children
def main(ls,ms):
    result = []

    for parent_id, nested in ls.items():
        #print(parent_id)
        parent_data = ms.get(parent_id)
        #print(parent_data)
        if parent_data:
            result.append({
                "key": parent_id,
                "title": parent_data["name"],
                "children": build_tree(nested,ms)
            })

    return result