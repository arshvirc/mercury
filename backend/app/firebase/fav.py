from app.firebase.firebase import db


def getFavourites(uid):
  try:
    collection_ref = db.collection("Favourites")
    # Create a query against the collection
    query = collection_ref.where("created_by", '==', uid)
        
    # Execute the query and get the documents
    docs = query.stream()
        
    # Process the documents
    results = []
    for doc in docs:
      results.append(doc.to_dict())
        
    return results
  except Exception as e:
    print(f"An error occurred: {e}")
    return []

def addToFavourites(uid, suggestion):
  try:
    suggestion["created_by"] = uid
    print(f"Suggestion: {suggestion}")
    db.collection("Favourites").document().set(suggestion)

  except Exception as e:
    print(f"An error occurred: {e}")
    return []