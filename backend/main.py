from db.mongo import raw_articles

doc = raw_articles.find_one()

print(doc)