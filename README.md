# Book reading time calculator

 I use this for reading on my Kindle, that's why I use those "location" things.

## Interactive use

 To use the calculator in interactive mode, just run the bookLocations.py file 
 
 ```
 python bookLocations.py
 ```

## Using command line arguments

 ```
 python booklocations.py file locationsPerPage readingTimePerPage
 ```

 where
 * `file` is a text file containing the info of the books you want calulated.
 * `locationPerPage` is how many locations there are per page turn on the Kindle
 * `readingTimePerPage` is how fast you read one page on the kindle in seconds

 So for example I would run

 ```
 python booklocations.py books.txt 10 67
 ```

 If you don't include `locationPerPage` and `readingTimePerPage`, you will be prompted. Set them to `1` if not important.

 The output will be a text file in a subfolder called `Calculated books`. You can change this in one of the first lines of the code.

## Formatting the text file

 * One book per line. 
 * `#` at start of line indicate comments.
 * `title;useLocation;totalPages;totalLocations;days`
   * `title` is the title of the book
   * `useLocation` is whether you're using locations from the kindle or pages. Set `True` for location and `False` for pages.
   * `totalPages` is the amount of pages that there would be in a printed version of the book. I get these from [GoodReads](https://goodreads.com).
   * `totalLocations` is the total amount of locations in the kindle book. If you're using `useLocation` set to `False`, just write the `totalPages` here.
   * `days` is the amount of days you'd like to complete the book in.

 An example file is included.