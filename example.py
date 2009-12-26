from mobi import Mobi

book = Mobi("test/CharlesDarwin.mobi");
book.parse();

for record in book:
  print record;