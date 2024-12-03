def Binarysearch(library, isbn_to_find, low, high):
    while low <= high:
        mid = low + (high - low) // 2

        
        mid_isbn = library[mid]["ISBN"]

        if isbn_to_find == mid_isbn:
            return mid  
        elif isbn_to_find > mid_isbn:
            low = mid + 1
        else:
            high = mid - 1

    return -1  


library = [
    {"ISBN": 1001, "Title": "Harry Potter"},
    {"ISBN": 1010, "Title": "Python para iniciantes"},
    {"ISBN": 1025, "Title": "Jogos Vorazes"},
    {"ISBN": 1030, "Title": "Memorias postumas de brás cubas"},
    {"ISBN": 1100, "Title": "Dom Casmurro"},
]

isbn_to_find = 1025

result = Binarysearch(library, isbn_to_find, 0, len(library) - 1)

if result != -1:
    print(f"Livro encontrado: {library[result]['Title']} (ISBN: {library[result]['ISBN']})")
else:
    print("Livro não encontrado.")
