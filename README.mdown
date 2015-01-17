Mobi Python Library
===================
**This should be considered alpha quality software.**

This library provides a little API for accessing the contents of an unencrypted .mobi file.  Here's a short example:

```python
from mobi import Mobi

book = Mobi("test/CharlesDarwin.mobi");
book.parse();
# this will print, 1 record at a time, the entire contents of the book
for record in book:
    print record
```
This library provides quite a lot of access to the metadata included in any mobibook.  For example, Gutenburg's Origin of the Species:
```python
>>> pprint(book.config)
{'exth': {'header length': 356,
          'identifier': 1163416648,
          'record Count': 15,
          'records': {100: 'Charles Darwin',
                      101: 'Project Gutenberg',
                      105: 'Natural selection',
                      106: '1999-12-01',
                      109: 'Public domain in the USA.',
                      112: 'http://www.gutenberg.org/files/2009/2009-h/2009-h.htm',
                      201: '\x00\x00\x00\x00',
                      202: '\x00\x00\x00\x01',
                      203: '\x00\x00\x00\x00',
                      204: '\x00\x00\x00\x01',
                      205: '\x00\x00\x00\x06',
                      206: '\x00\x00\x00\x02',
                      207: '\x00\x00\x00)',
                      300: '\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\xed\xec\xbe@\x94'}},
 'mobi': {'DRM Count': 0,
          'DRM Flags': 0,
          'DRM Offset': 4294967295,
          'DRM Size': 0,
          'EXTH flags': 80,
          'First Image index': 334,
          'First Non-book index': 329,
          'Format version': 6,
          'Full Name': 'The Origin of Species by means of Natural Selection, 6th Edition',
          'Full Name Length': 64,
          'Full Name Offset': 604,
          'Generator version': 6,
          'Has DRM': False,
          'Has EXTH Header': True,
          'Input Language': 0,
          'Language': 9,
          'Mobi type': 2,
          'Output Language': 0,
          'Start Offset': 2808,
          'Unique-ID': 4046349163,
          'header length': 232,
          'identifier': 1297039945,
          'text Encoding': 1252},
 'palmdoc': {'Compression': 2,
             'Encryption Type': 0,
             'Unknown': 0,
             'Unused': 0,
             'record count': 327,
             'record size': 4096,
             'text length': 1336365}}
>>>
```
## Retrieving Author and Title
The author and title of a book can be retrieved using the author() and title()
methods respectively on a Mobi() object. The parse() method needs to have
already been called.
