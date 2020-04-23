def extract_info(note_list):
    result = []
    for note in note_list:
        title = note.find("a", {"class" : "N=a:bta.title"}).string
        img_src = note.find("img")["src"]
        link = note.find("a", {"class" : "N=a:bta.title"})["href"]
        author = note.find("a", {"class" : "txt_name N=a:bta.author"}).string
        publisher = note.find("a", {"class" : "N=a:bta.publisher"}).string
        price_box = note.find("em", {"class" : "price"})
        if price_box == None:
            price = "없음"
        else:
            price = price_box.string
        note_info = {
            "title" : title,
            "img_src" : img_src,
            "link" : link,
            "author" : author,
            "publisher" : publisher,
            "price" : price
        }
        result.append(note_info)
    return result