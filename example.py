from mobi import Mobi
import os
path = os.path.dirname(__file__)
book = Mobi(f"{path}/test/CharlesDarwin.mobi");
book.parse();

for record in book:
  print(record)

import pprint
pprint.pprint(book.config)