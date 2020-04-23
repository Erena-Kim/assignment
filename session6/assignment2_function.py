def extract_info(node_list):
    result = []
    for node in node_list:
        city = node.find_all("td")[0].string
        town = node.find_all("td")[1].string
        name = node.find_all("td")[2].text
        number = node.find_all("td")[3].string
        node_info = {
            "city" : city,
            "town" : town,
            "name" : name,
            "number" : number
        }
        result.append(node_info)
    return result