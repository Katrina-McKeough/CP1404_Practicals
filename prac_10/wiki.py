import wikipedia

search_phrase = input("Enter a page title or phrase to search: ")
while search_phrase:
    try:
        print(wikipedia.summary(search_phrase))
    except wikipedia.exceptions.DisambiguationError as e:
        print("Try searching one of: {}".format(e.options))
    except wikipedia.exceptions.PageError:
        print("Sorry, page does not exist :(")
    search_phrase = input("Enter a page title or phrase to search: ")
print("Have a nice day :)")
