# Unofficial Course Content Index (UCCI)
This is the Unofficial Course Content Index (from now on, 'UCCI') of the online sessions of the Python Specialization Course that took place from April to July, 2020.

* [To Consider](#to-consider)
* [Language Core](#core)
* [Employability](#emp)
* [Libraries](#libs)
* [Design Patterns](#patterns)
* [Web Development](#web)
* [System Administration](#sys-admin)
* [Desktop Apps](#desktop-apps)
* [Data Science](#data)

## To Consider
The following are the icons included all along the UCCI:

- :vhs: - Link to the recorded classes
- :beginner: - Link to the notes of the official repository, written in Spanish :es:
- :page_with_curl: - Link to information on Wikipedia
- :orange_book: - Link to official documentation
- :es: - Link to Spanish content
- :us: - Link to English content

**Also:**

If not specified, the link to Wikipedia, books or any other content will be in English.

<a name="core"></a>
# Language Core :abc:
## Friday, April 3rd

#### [Link to the recorded session :vhs:](https://us.bbcollab.com/recording/06351d80ce5c468d99d18dadb93329fb)

## Monday, April 6th

#### [Link to the recorded session :vhs:](https://us.bbcollab.com/recording/b91a2b1057a547d084894d7030a075ad)

## Tuesday, April 7th

#### [Link to the recorded session :vhs:](https://us.bbcollab.com/recording/3187b282ec49445ba0148f6267990c5c)

## Wednesday, April 8th

#### [Link to the recorded session :vhs:](https://us.bbcollab.com/recording/cafc1c4cdb4241398bfd7351b6671b11)

<a name="emp"></a>
# Employability :necktie:

## Monday, April 13th

#### [Link to the recorded session :vhs:](https://us.bbcollab.com/recording/dd00af71738a4f949711b3d9cd5997b3) 

## Thusday, May 7th (from 5 to 8 pm)

#### [Link to the recorded session :vhs:](https://us.bbcollab.com/recording/d003cf53abc5400e866b754e64513981)

## Monday, May 18th

#### [Link to the recorded session :vhs:](https://us.bbcollab.com/recording/2014a86fbeaa4439be5e0d87360669ad)

<a name="libs"></a>
# Libraries :aerial_tramway:
## Tuesday, April 14th

#### [Link to the recorded session :beginner:](https://us.bbcollab.com/recording/57d0753cbfa34416befb24c342e70206)

### Content
#### Standard libraries

- **os** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/standard/os/os.ipynb) [:orange_book:](https://docs.python.org/3/library/os.html)(05:40 – 01:30:10) *(Miscellaneous operating system interfaces)*
    - path
    - name
    - listdir()
    - walk()

- **sys** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/standard/sys/sys.ipynb) [:orange_book:](https://docs.python.org/3/library/sys.html?highlight=sys#module-sys)(01:31:10 – 01:55:50) *(System-specific parameters and functions)*
    - argv
    - exc_info()
    - path
    - version
    - platform

- **zlib** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/zlib.html?highlight=zlib#module-zlib) (01:57:25 – 03:00:00) *(Compression and decompression)*
    - compress
    - decompress
    - checksums
        - adler32
	    - crc32

- **gzip** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/gzip.html?highlight=gzip#module-gzip) (03:11:40 – 03:49:50) *(Compression and decompression)*
    - open
    - writelines()

## Wednesday, April 15th

#### [Link to the recorded session :beginner:](https://us.bbcollab.com/recording/6a5eccadc94248d39f73e587677f7442)

### Content
#### Standard libraries
- **zipfile** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/zipfile.html?highlight=zipfile#module-zipfile) (01:00 – 42:20) *(Compression and decompression of ZIP archives)*
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

- **Project:** backup script (42:25 – 01:17:00)

- **time** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/time.html?highlight=time#module-time) (01:35:40 – 02:22:30) *(Time access and conversions)*
    - definitions
    - time()
    - asctime()
    - localtime()
    - gmtime()
    - mktime()

- **datetime** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/datetime.html?highlight=datetime#module-datetime) (02:25:10 – 03:17:45) *(Basic date and time types)*
    - date
        - today, day, month, year
        - fromtimestamp
    - .datetime
        - now()
        - minute, year…

- **base64** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/base64.html?highlight=base64#module-base64) (03:23:40 – 04:00:00) *(Data encodings)* *(part I)*
    - what econding is and what is not
    - b64encode
    - decode

## Thursday, April 16th

#### [Link to the recorded session :beginner:](https://us.bbcollab.com/recording/c9a64768efd04e05b72af6afdb5647a1)

### Content
#### Standard libraries
- **base64** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/base64.html?highlight=base64#module-base64) (04:00 - 16:00) *(Data encodings)* *(part II)*
    - HTML module

- **statistics** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/statistics.html?highlight=statistics#module-statistics) (16:40 – 01:19:20) *(Mathematical statistics functions)*
    - mean
    - geometric_mean
    - median
    - mode
    - stdev & variance

- **collections** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/collections.html?highlight=collections#module-collections) (01:32:35 – 02:32:20) *(Container datatypes)*
    - namedtuple
    - deque
    - Counter
    - OrderedDict
    - defaultdict

- **csv** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/csv.html?highlight=csv#module-csv)(02:32:40 – 02:58:15) *(CSV file reading and writing)*
    - reader
    - writer

- **re** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/re.html?highlight=re#module-re) (03:20:40 – 04:00:00) *(Regular expression operations)* *(part I)*
    - compile

## Friday, April 17th

#### [Link to the recorded session :beginner:](https://us.bbcollab.com/recording/022e4743fea4480793cb5ffa3b9b19d4)

### Content
#### Standard libraries
- **re** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/re.html?highlight=re#module-re) (02:45 - 01:29:40) *(Regular expression operations)* *(part II)*
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

- **logging** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/logging.html?highlight=logging#module-logging) (01:41:40 – 02:38:35) *(Logging facility for Python)*
    - debug()
    - info()
    - warning()
    - error()
    - critical()

- **pdb** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/pdb.html?highlight=pdb#module-pdb) (02:40:00 – 03:04:00) *(The Python debugger)*
    - list
    - help
    - where
    - step
    - next
    - return

- **threading** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/threading.html?highlight=threading#module-threading) (03:20:45 – 03:59:20) *(Thread-based parallelism)*

## Monday, April 20th
#### [Link to the recorded session :beginner:](https://us.bbcollab.com/recording/a27814b5362f40ac9e7a30adad68d1b5)

### Content
#### External libraries
- **arrow** [:beginner:]() [:orange_book:](https://pypi.org/project/arrow/) (03:30 – 01:30:15) *(Create, manipulate, format and convert dates, times and timestamps)*
    - get
    - utcnow
        - span
    - now
        - utccoffset()
        - shift()
    - replace

#### Standard libraries
- **random** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/random.html?highlight=random#module-random) (01:53:25 – 03:30:10) *(Generate pseudo-random numbers)*
    - random()
    - choice()
    - seed()
    - **Project:**  ‘rock, paper, scissors’
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
- **matplotlib** [:beginner:]() [:orange_book:](https://matplotlib.org/3.2.1/contents.html) (03:30:30 – 04:02:40) *(Data visualization tool)* (part I)
    - plot
    - bar
    - hist
    - barh
    - scatter

## Tuesday, April 21st
#### [Link to the recorded session :beginner:](https://us.bbcollab.com/recording/1fbd9ff57ac946099a24fa27213ad203 )

### Content
#### External libraries
- **matplotlib** [:beginner:]() [:orange_book:](https://matplotlib.org/3.2.1/contents.html) (28:20 – 01:08:40) *(Data visualization tool)* (part II)
    - title
    - text
    - xlabel
    - ylabel

- **Project:** Analyze a file tree and make an horizontal bar graph of each type of file. (01:08:45 – 01:52:20)

- **requests** [:beginner:]() [:orange_book:](https://requests.readthedocs.io/en/master/) (02:05:30 – 04:00:30) *(HTTP library for Python)*
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

## Wednesday, April 22nd
#### [Link to the recorded session :beginner:](https://us.bbcollab.com/recording/9b6b74c1e54f49da92b2fb87f0893f88)

### Content
#### Standard libraries
- **json** [:beginner:]() [:orange_book:](https://docs.python.org/3/library/json.html?highlight=json#module-json) (05:30 – 56:00) *(JSON encoder and decoder)*
    - dumps
    - Public APIs *(Application Programming Interface)* (56:55 – 02:00:00)

#### External libraries
- **pillow** [:beginner:]() [:orange_book:](https://pillow.readthedocs.io/en/stable/) (02:01:17 – 04:01:05) *(Support for opening, manipulating and saving images)* *(part I)*
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

## Thursday, April 23rd
#### [Link to the recorded session :beginner:](https://us.bbcollab.com/recording/f17c2054875241678981d2312edeee87)

#### External libraries
### Content
- **pillow** [:beginner:]() [:orange_book:](https://pillow.readthedocs.io/en/stable/) (08:00 – 02:27:50) *(Support for opening, manipulating and saving images)* *(part II)*
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

- **numpy** [:beginner:]() [:orange_book:](https://numpy.org/doc/) (02:29:20 – 03:43:00) *(Scientific computing with Python)*
    - array
    - dtype
    - reshape
    - zeros
    - linspace
    - random
        - rand
    - cos

- **Project:** Backup script (03:45:00 – 04:01:50)

## Friday, April 24th
#### [Link to the recorded session :beginner:](https://us.bbcollab.com/recording/e531751ef17f44589223fbfd4f7de5e8)

### Content
#### External libraries
- **pandas** [:beginner:]() [:orange_book:](https://pandas.pydata.org/docs/) (05:20 - 02:25:10) *(Data structures and data analysis tools for Python)*
    - read_csv()
    - to_numeric()

- **qrcode** [:beginner:]() [:orange_book:](https://pypi.org/project/qrcode/) (02:25:40 – 02.58:15) *(QR code generator)*

- **Links of interest** (02:59:00 – 03:05:00):
    - [Github Trendings](https://github.com/trending/python) (practice Python on GitHub)
    - [Awesome Python repository](https://github.com/vinta/awesome-python)

- **watchdog** [:beginner:]() [:orange_book:](https://pythonhosted.org/watchdog/) (03:06:30 – 03:55:00) *(File system events monitor)*
    - Observer()
        - schedule
        - stop
        - join

<a name="patterns"></a>
# Design Patterns :globe_with_meridians:
## Monday, April 27th
#### [Link to the recorded session :vhs:](https://us.bbcollab.com/recording/9f8fa8bb2743448cbc333656e420cc4b)

### Content
- **Introduction** (04:00 - 02:00:50) [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/00-Introduction.ipynb)
    - Definition [:page_with_curl:](https://en.wikipedia.org/wiki/Software_design_pattern)
    - History
    - Book: [Design Patterns: Elements of Reusable Object-Oriented Software](https://en.wikipedia.org/wiki/Design_Patterns)
    - Types of patterns
    - Design principles
    - How not to use the design patterns

- **Singleton** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/01-Singleton.ipynb) [:page_with_curl:](https://en.wikipedia.org/wiki/Singleton_pattern) (02:02:02 - 02:50:30)

- **Prototype** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/01-Singleton.ipynb) [:page_with_curl:](https://en.wikipedia.org/wiki/Prototype_pattern) (02:50:45 - 03:25:15)

- **Factory Method** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/03-Factory.ipynb) [:page_with_curl:](https://en.wikipedia.org/wiki/Factory_method_pattern) (03:25:30 - 03:44:50)

- **Builder** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/04-Builder.ipynb) [:page_with_curl:](https://en.wikipedia.org/wiki/Builder_pattern) (03:46:50 - 03:57:30)

## Tuesday, April 28th
#### [Link to the recorded session :vhs:](https://us.bbcollab.com/recording/ec154a2062c94378b79f90c5f1a65a09)

### Content
- **Adapter** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/05_Adapter.ipynb) [:page_with_curl:](https://en.wikipedia.org/wiki/Adapter_pattern) (07:49 - 38:15)

- **Bridge** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/06-Bridge.ipynb) [:page_with_curl:](https://en.wikipedia.org/wiki/Bridge_pattern) (38:20 - 01:32:50)

- **Façade** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/09-Facade.ipynb) [:page_with_curl:](https://en.wikipedia.org/wiki/Facade_pattern) (01:56:00 - 02:28:05)

- **Flyweight** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/10-Flyweight.ipynb) [:page_with_curl:](https://en.wikipedia.org/wiki/Flyweight_pattern) (02:28:20 - 03:02:05)

- **Strategy** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/12-Strategy.ipynb) [:page_with_curl:](https://en.wikipedia.org/wiki/Strategy_pattern) (03:18:25 - 04:01:30)

<a name="web"></a>
# Web Design :globe_with_meridians:
## Wednesday, April 29th
#### [Link to the recorded session :vhs:](https://us.bbcollab.com/recording/e2642b90baf24c3c88ece7f992185a18)

## Thursday, April 30th
#### [Link to the recorded session :vhs:]()

## Monday, May 4th
#### [Link to the recorded session :vhs:]()

## Tuesday, May 5th
#### [Link to the recorded session :vhs:]()

## Wednesday, May 6th
#### [Link to the recorded session :vhs:]()

## Thursday, May 7th
#### [Link to the recorded session :vhs:]()

<a name="libs"></a>
# System Administration :cloud:
## Friday, May 8th
#### [Link to the recorded session :vhs:]()

## Monday, May 11th
#### [Link to the recorded session :vhs:]()

## Tuesday, May 12th

## Wednesday, May 13th
#### [Link to the recorded session :vhs:]()

## Thursday, May 14th
#### [Link to the recorded session :vhs:]()

## Friday, May 15th
#### [Link to the recorded session :vhs:]()

## Tuesday, May 19th
#### [Link to the recorded session :vhs:]()

## Wednesday, May 20th
#### [Link to the recorded session :vhs:]()

## Thursday, May 21st
#### [Link to the recorded session :vhs:]()

<a name="libs"></a>
# Desktop Apps :computer:
## Friday, May 22nd
#### [Link to the recorded session :vhs:]()

## Monday, May 25th
#### [Link to the recorded session :vhs:]()

## Tuesday, May 26th
#### [Link to the recorded session :vhs:]()

<a name="libs"></a>
# Data Science :bar_chart:
## Wednesday, May 27th
#### [Link to the recorded session :vhs:]()

