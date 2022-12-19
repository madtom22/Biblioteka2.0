from flask import Flask, request, render_template, redirect
from app import app, db
from app.models import Author, Book


@app.route("/")
def book_list():
    books = Book.query.all()
    authors = Author.query.all()
    return render_template("books.html", books=books, authors=authors)


@app.route("/book/", methods=["POST"])
def add_book():
    title = request.form["title"]
    genre = request.form["genre"]
    pages = request.form["pages"]
    if not title:
        return "Error"

    book = Book(title=title, genre=genre, pages=pages)
    db.session.add(book)
    db.session.commit()
    return redirect("/")


@app.route("/author/", methods=["POST"])
def add_author():
    name = request.form["name"]
    surname = request.form["surname"]
    birth = request.form["birth"]
    if not name:
        return "Error"

    author = Author(name=name, surname=surname, birth=birth)
    db.session.add(author)
    db.session.commit()
    return redirect("/")


@app.route("/assign/", methods=["POST"])
def assign_book():  # assign book to author
    book_id = request.form["books_id"]
    author_id = request.form["author_id"]

    book = Book.query.get(book_id)
    book.author_id = author_id

    db.session.add(book)
    db.session.commit()
    return redirect("/")


@app.route("/delete/<int:book_id>")
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return redirect("/")

    db.session.delete(book)
    db.session.commit()
    return redirect("/")


@app.route("/delete/<int:author_id>")
def delete_author(author_id):

    author = Author.query.get(author_id)
    if not author:
        return redirect("/")

    db.session.delete(author)
    db.session.commit()
    return redirect("/")


@app.route("/out_stock/<int:book_id>")
def book_in_stock(book_id):
    book = Book.query.get(book_id)
    print(f"def book:  ", book)
    if not book:
        return redirect("/")
    if book.stock == False:
        book.stock = True

    db.session.add(book)
    db.session.commit()
    return redirect("/")


@app.route("/in_stock/<int:book_id>")
def book_out_of_stock(book_id):
    book = Book.query.get(book_id)
    print(f"def book:  ", book)
    if not book:
        return redirect("/")
    if book.stock == True:
        book.stock = False

    db.session.add(book)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)