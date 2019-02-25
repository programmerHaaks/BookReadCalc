import time
import math
import sys
import os

bookDir = "Calculated books"

locationsInPage = 0
timeToReadPage = 0


class Book:

    def __init__(self, title, location, grPages, totalLocation, days):

        self.title = title
        self.location = location
        self.grPages = int(grPages)
        self.totalLocation = int(totalLocation)
        self.days = int(days)


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1', 'True'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0', 'False'):
        return False
    else:
        raise Exception('Boolean value expected.')


def populateBooksFromFile(filename):
    books = []
    f = open("books.txt")

    for line in f:
        if line.strip()[0] != '#':
            currentBook = line.split(";")
            books.append(Book(currentBook[0].strip(), str2bool(currentBook[1].strip(
            )), currentBook[2].strip(), currentBook[3].strip(), currentBook[4].strip()))

    return books


def getReaderStats():
    global locationsInPage
    global timeToReadPage
    locationsInPage = int(
        input("How many locations on average per page turn on Kindle? "))

    timeToReadPage = int(
        input("How long does it take you to read a page on average (in seconds)? "))


def processBook(title, location, grPages, totalLocation, days, locationsInPage, timeToReadPage):

    date = time.strftime("%H:%M %d.%m.%Y")

    # Locations per day
    step = math.ceil(totalLocation / days)

    # Create dir
    if not os.path.exists(bookDir):
        os.makedirs(bookDir)

    # Open file
    Outfile = open("%s\%s.txt" % (bookDir, title), "w")

    # Write legend
    Outfile.write("%s\n%s\n\n" % (title, date))

    Outfile.write("Day\t\t%s\t%%%s\n" % (
        "Page" if not location else "Location", "\t\tPage" if location else ""))

    currentDay = 0
    # Write lines
    for i in range(step, totalLocation+step, step):
        currentDay += 1
        currentLocation = i
        currentPercentage = math.floor(100*(i / totalLocation))
        currentPage = math.ceil(currentPercentage / 100 *
                                (grPages if location else totalLocation))
        Outfile.write("%03d\t\t%s\t\t%03d%s\n" % (currentDay, "%05d" % (currentLocation) if location else "%03d" % (currentLocation),
                                                  currentPercentage, "\t\t%03d" % (currentPage) if location else ""))

    timeToReadBook = timeToReadPage * totalLocation / \
        (locationsInPage if location else 1)
    seconds = math.floor(timeToReadBook % 60)
    minutes = math.floor((timeToReadBook % 3600) / 60)
    hours = math.floor(timeToReadBook / 3600)

    Outfile.write("\nIt will take you about %sh%sm%ss to read this book\n" % (
        hours, minutes, seconds))

    timeToReadPerDay = timeToReadBook / days
    seconds = math.floor(timeToReadPerDay % 60)
    minutes = math.floor((timeToReadPerDay % 3600) / 60)
    hours = math.floor(timeToReadPerDay / 3600)

    Outfile.write("if you read about %sh%sm%ss per day" %
                  (hours, minutes, seconds))

    Outfile.close()


def getBookFromInput():
    title = input("What's the title of the book? ")
    location = False

    # It's all locations really, it's only different in the legend
    if input("Locations or pages (l/P)? ").lower().strip() == "l":
        location = True
        grPages = int(
            input("What's the total number of pages on goodreads (or wherever)? "))

    totalLocation = int(input("What's the total number of %s? " %
                              ("pages" if not location else "locations")))

    if not location:
        grPages = totalLocation

    days = int(input("How many days are you planning to read the book over? "))

    return Book(title, location, grPages, totalLocation, days)


def main():
    books = []
    global locationsInPage
    global timeToReadPage
    timeToReadPage = 3
    if (len(sys.argv) >= 3):
        locationsInPage = int(sys.argv[2])
        timeToReadPage = int(sys.argv[3])
        books = populateBooksFromFile(sys.argv[1])
    else:
        getReaderStats()
        books.append(getBookFromInput())

    for book in books:
        processBook(book.title, book.location, book.grPages,
                    book.totalLocation, book.days, locationsInPage, timeToReadPage)


if __name__ == "__main__":
    main()
