<a name="top"></a>
# Unofficial Course Content Index (UCCI)
This is the Unofficial Course Content Index (from now on, 'UCCI') of the online sessions of the Python Specialization Course that took place from April to July, 2020.

* [To Consider](#to-consider)
* [Core](#core)
* [Employability](#emp)
* [Libraries](#libs)
* [Design Patterns](#patterns)
* [Web Development](#web)
* [System Administration](#sys-admin)
* [Desktop Apps](#desktop-apps)
* [Data Science](#data)

## To Consider
The following are the icons included all along the UCCI:

- :beginner: - Link to the notes of the official repository, written in Spanish :es:
- :page_with_curl: - Link to information on Wikipedia
- :orange_book: - Link to official documentation
- :es: - Link to Spanish content
- :us: - Link to English content
- :top: - Back to file index

**Also:**

If not specified, the link to Wikipedia, books or any other content will be in English.

<a name="core"></a>
# Core :abc:
## Friday, April 3rd

[:top:](#top)

## Monday, April 6th

[:top:](#top)

## Tuesday, April 7th

[:top:](#top)

## Wednesday, April 8th

[:top:](#top)

<a name="emp"></a>
# Employability :necktie:
## Monday, April 13th

[:top:](#top)

## Thursday, May 7th (from 5 to 8 pm)

[:top:](#top)

## Monday, May 18th

[:top:](#top)

<a name="libs"></a>
# Libraries :aerial_tramway:
## Tuesday, April 14th

### Content
#### Standard libraries

- **os** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/standard/os/os.ipynb) [:orange_book:](https://docs.python.org/3/library/os.html) *(Miscellaneous operating system interfaces)*
    - path
    - name
    - listdir()
    - walk()

- **sys** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/standard/sys/sys.ipynb) [:orange_book:](https://docs.python.org/3/library/sys.html?highlight=sys#module-sys) *(System-specific parameters and functions)*
    - argv
    - exc_info()
    - path
    - version
    - platform

- **zlib** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/zlib.html?highlight=zlib#module-zlib) *(Compression and decompression)*
    - compress
    - decompress
    - checksums
        - adler32
	    - crc32

- **gzip** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/gzip.html?highlight=gzip#module-gzip) *(Compression and decompression)*
    - open
    - writelines()

[:top:](#top)

## Wednesday, April 15th

### Content
#### Standard libraries
- **zipfile** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/zipfile.html?highlight=zipfile#module-zipfile) *(Compression and decompression of ZIP archives)*
    - is_zipfile()
    - ZipFile class
        - getinfo(name)
        - extract(member, path=None, pwd=None)
        - extractall(path=None, members=None, pwd=None)
        - printdir()
        - setpassword(pwd)
        - read(name, pwd=None)
        - testzip()
        - write (filename, arcname=None, compress_type=None, compresslevel=None)
        - writestr (zinfo_or_arcname, data, compress_type=None, compresslevel=None)

- **time** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/time.html?highlight=time#module-time) *(Time access and conversions)*
    - definitions
    - time()
    - asctime()
    - localtime()
    - gmtime()
    - mktime()

- **datetime** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/datetime.html?highlight=datetime#module-datetime) *(Basic date and time types)*
    - date
        - today, day, month, year
        - fromtimestamp
    - .datetime
        - now()
        - minute, year…

- **base64** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/base64.html?highlight=base64#module-base64) *(Data encodings)* *(part I)*
    - what econding is and what is not
    - b64encode
    - decode

[:top:](#top)

## Thursday, April 16th

### Content
#### Standard libraries
- **base64** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/base64.html?highlight=base64#module-base64) *(Data encodings)* *(part II)*
    - HTML module

- **statistics** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/statistics.html?highlight=statistics#module-statistics) *(Mathematical statistics functions)*
    - mean
    - geometric_mean
    - median
    - mode
    - stdev & variance

- **collections** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/collections.html?highlight=collections#module-collections) *(Container datatypes)*
    - namedtuple
    - deque
    - Counter
    - OrderedDict
    - defaultdict

- **csv** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/csv.html?highlight=csv#module-csv) *(CSV file reading and writing)*
    - reader
    - writer

- **re** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/re.html?highlight=re#module-re) *(Regular expression operations)* *(part I)*
    - compile

[:top:](#top)

## Friday, April 17th

### Content
#### Standard libraries
- **re** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/re.html?highlight=re#module-re) *(Regular expression operations)* *(part II)*
    - special characters
        - ^
        - ?
        - [ & ]
        - |
        - { & }
        -  \
        - \b & \B
        - \d & \D
        - \s & \S
        - \w
        - ( & )
    - search, match & findall

- **logging** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/logging.html?highlight=logging#module-logging) *(Logging facility for Python)*
    - debug()
    - info()
    - warning()
    - error()
    - critical()

- **pdb** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/pdb.html?highlight=pdb#module-pdb) *(The Python debugger)*
    - list
    - help
    - where
    - step
    - next
    - return

- **threading** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/threading.html?highlight=threading#module-threading) *(Thread-based parallelism)*

[:top:](#top)

## Monday, April 20th

### Content
#### External libraries
- **arrow** [:beginner:]() [:orange_book:](https://pypi.org/project/arrow/) *(Create, manipulate, format and convert dates, times and timestamps)*
    - get
    - utcnow
        - span
    - now
        - utccoffset()
        - shift()
    - replace

#### Standard libraries
- **random** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/random.html?highlight=random#module-random) *(Generate pseudo-random numbers)*
    - random()
    - choice()
    - seed()
    - choices()
        - cum_weights
    - sample()
    - randrange()
    - randint()
    - shuffle()
    - uniform()
    - paretovariate()
    - gauss()

#### External libraries
- **matplotlib** [:beginner:]() [:orange_book:](https://matplotlib.org/3.2.1/contents.html) *(Data visualization tool)* (part I)
    - plot
    - bar
    - hist
    - barh
    - scatter

[:top:](#top)

## Tuesday, April 21st

### Content
#### External libraries
- **matplotlib** [:beginner:]() [:orange_book:](https://matplotlib.org/3.2.1/contents.html) *(Data visualization tool)* (part II)
    - title
    - text
    - xlabel
    - ylabel

- **requests** [:beginner:]() [:orange_book:](https://requests.readthedocs.io/en/master/) *(HTTP library for Python)*
    - get
        - status_code
        - headers
        - text
        - json()
        - url
        - history
        - cookies
    - post
    - put
    - delete
    - head
    - options
    - Session()

[:top:](#top)

## Wednesday, April 22nd

### Content
#### Standard libraries
- **json** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/json.html?highlight=json#module-json) *(JSON encoder and decoder)*
    - dumps
    - Public APIs *(Application Programming Interface)*

#### External libraries
- **pillow** [:beginner:]() [:orange_book:](https://pillow.readthedocs.io/en/stable/) *(Support for opening, manipulating and saving images)* *(part I)*
    - format, size y mode
    - open
    - save
    - thumbnail
    - crop
    - transpose
    - paste
    - split
    - merge
    - resize

[:top:](#top)

## Thursday, April 23rd

#### External libraries
### Content
- **pillow** [:beginner:]() [:orange_book:](https://pillow.readthedocs.io/en/stable/) *(Support for opening, manipulating and saving images)* *(part II)*
    - rotate
    - convert
    - ImageFilter()
        - BLUR
        - CONTOUR
        - DETAIL
        - …
    - point
    - ImageEnhance
        - Color
        - Contrast
        - Brightness
        - Sharpness
    - ImageDraw
      - Draw
      - arc
      - pieslice
      - polygon
      - rectangle
      - text
      - textsize
      - floodfill
      - ellipse
    - getpixel
    - putpixel
    - load()
    - Image.new()
    - paste

- **numpy** [:beginner:]() [:orange_book:](https://numpy.org/doc/) *(Scientific computing with Python)*
    - array
    - dtype
    - reshape
    - zeros
    - linspace
    - random
        - rand
    - cos

- **Project:** Backup script

[:top:](#top)

## Friday, April 24th

### Content
#### External libraries
- **pandas** [:beginner:]() [:orange_book:](https://pandas.pydata.org/docs/) *(Data structures and data analysis tools for Python)*
    - read_csv()
    - to_numeric()

- **qrcode** [:beginner:]() [:orange_book:](https://pypi.org/project/qrcode/) *(QR code generator)*

- **Links of interest**:
    - [Github Trendings](https://github.com/trending/python) (practice Python on GitHub)
    - [Awesome Python repository](https://github.com/vinta/awesome-python)

- **watchdog** [:beginner:]() [:orange_book:](https://pythonhosted.org/watchdog/) *(File system events monitor)*
    - Observer()
        - schedule
        - stop
        - join

[:top:](#top)

<a name="patterns"></a>
# Design Patterns :globe_with_meridians:
## Monday, April 27th

### Content
- **Introduction** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/00-Introduction.ipynb)
    - Definition [:page_with_curl:](https://en.wikipedia.org/wiki/Software_design_pattern)
    - History
    - Book: [Design Patterns: Elements of Reusable Object-Oriented Software](https://en.wikipedia.org/wiki/Design_Patterns)
    - Types of patterns
    - Design principles
    - How not to use the design patterns

- **Singleton** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/01-Singleton.ipynb) [:page_with_curl:](https://en.wikipedia.org/wiki/Singleton_pattern)

- **Prototype** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/01-Singleton.ipynb) [:page_with_curl:](https://en.wikipedia.org/wiki/Prototype_pattern)

- **Factory Method** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/03-Factory.ipynb) [:page_with_curl:](https://en.wikipedia.org/wiki/Factory_method_pattern)

- **Builder** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/04-Builder.ipynb) [:page_with_curl:](https://en.wikipedia.org/wiki/Builder_pattern)

[:top:](#top)

## Tuesday, April 28th

### Content
- **Adapter** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/05_Adapter.ipynb) [:page_with_curl:](https://en.wikipedia.org/wiki/Adapter_pattern)

- **Bridge** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/06-Bridge.ipynb) [:page_with_curl:](https://en.wikipedia.org/wiki/Bridge_pattern)

- **Façade** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/09-Facade.ipynb) [:page_with_curl:](https://en.wikipedia.org/wiki/Facade_pattern)

- **Flyweight** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/10-Flyweight.ipynb) [:page_with_curl:](https://en.wikipedia.org/wiki/Flyweight_pattern)

- **Strategy** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/12-Strategy.ipynb) [:page_with_curl:](https://en.wikipedia.org/wiki/Strategy_pattern)

[:top:](#top)

<a name="web"></a>
# Web Development :globe_with_meridians:
## Wednesday, April 29th

[:top:](#top)

## Thursday, April 30th

[:top:](#top)

## Monday, May 4th

[:top:](#top)

## Tuesday, May 5th

[:top:](#top)

## Wednesday, May 6th

[:top:](#top)

## Thursday, May 7th (from 4 to 5 pm)

[:top:](#top)

<a name="sys-admin"></a>
# System Administration :cloud:
## Friday, May 8th

[:top:](#top)

## Monday, May 11th

[:top:](#top)

## Tuesday, May 12th
#### Link to the... OH, WAIT
<img src="https://i.imgur.com/di6JDM4.png" width="300" height="300">

[:top:](#top)

## Wednesday, May 13th

[:top:](#top)

## Thursday, May 14th

[:top:](#top)

## Friday, May 15th

[:top:](#top)

## Tuesday, May 19th

[:top:](#top)

## Wednesday, May 20th

[:top:](#top)

## Thursday, May 21st

[:top:](#top)

<a name="desktop-apps"></a>
# Desktop Apps :computer:
## Friday, May 22nd

- **Qt for Python** [:page_with_curl:](https://doc.qt.io/qtforpython/)

[:top:](#top)

## Monday, May 25th

[:top:](#top)

## Tuesday, May 26th

[:top:](#top)

## Wednesday, May 27th (from 4 to 7 pm)

- **Kivy** [:page_with_curl:](https://kivy.org/doc/stable/)(00:07 - 02:40:00) *(Open source software for the rapid development of applications equipped with novel user interfaces, such as multi-touch apps)*

[:top:](#top)

<a name="data"></a>
# Data Science :bar_chart:
## Wednesday, May 27th (from 7 to 8 pm)
#### [Link to the recorded session :vhs:]()

- [Python Data Science Handbook](jakevdp.github.io/PythonDataScienceHandbook)
- IPython: Beyond Normal Python [:page_with_curl:](https://jakevdp.github.io/PythonDataScienceHandbook/01.00-ipython-beyond-normal-python.html)
    - Help and Documentation in IPython:
	- ?
	- TAB
	- dir(library)
	- globals(), locals()
	- **Built-in Functions in Python** [:page_with_curl:](https://docs.python.org/3/library/functions.html)
    - Keyboard Shortcuts
	- standard shortcuts
	    - CTRL + A (go to bol)
	    - CTRL + K 
	    - CTRL + E (go to eol)
	    - CTRL + U
	- [installing vim commands on IPython](stackoverflow.com/a/38329940/1911099)
    - Magic Commands
	- timeit
	- ½lsmagic
    - Input and Output
    - IPython and Shell Commands
    - Errors and Debugging
