from mobi import Mobi
from pprint import pprint

if __name__ == '__main__':
  book = Mobi("test/CharlesDarwin.mobi");
  book.parse();

  for record in book:
    # this prints the entire book out to the console
    # it can be piped to an html file
    print record
