# TASK: You're in charge of a library, "National Library Mariano Moreno".
# Libraries in real life use stamps to label the books as theirs...
# ...so let's do just that! :D
#
#
# In this example, we're going to use the " for ... in ... " control flow structure
# to add watermarks to our books.

# Example:
# Book without watermark: book1 = "Martin Fierro"
# Book with watermark:    book1 = "Martin Fierro - National Library Mariano Moreno"


books = ["Martin Fierro", "Lord of the Rings", "Harry Potter: The Philosopher's Stone", "Geography I", "Geography II", "Easy Cooking Recipes for Kids"]

watermark = "- National Library Mariano Moreno"
for book in books:
    book_with_watermark = book + watermark
    books_with_watermark.append(book_with_watermark)



print(books)