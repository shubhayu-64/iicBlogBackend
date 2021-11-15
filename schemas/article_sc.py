def articleEntity(db_item)-> dict:
    return {
        "id": str(db_item["_id"]),
        "title": db_item["title"],
        "tags": db_item["tags"],
        "author_name": db_item["author_name"],
        "Posted_on": db_item["date_time"],
        "Body": db_item["content"],
        "Image_Link": db_item["img-url"],
        "Likes_count": db_item["likes"],
    }