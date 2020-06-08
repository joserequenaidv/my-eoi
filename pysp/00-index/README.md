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
The following are the icons included throughout the UCCI:

- :beginner: - Link to the notes of the official repository, written in Spanish :es:
- :page_with_curl: - Link to information on Wikipedia
- :orange_book: - Link to official documentation
- :es: - Link to Spanish content
- :us: - Link to English content
- :top: - Back to file index

**Also:**

- *(XX:XX - XX:XX:XX)* - This refers to the timeframes of the recorded session of the course
- If not specified, the link to Wikipedia, books or any other content will be in English.

<a name="core"></a>
# Core :abc:
## Friday, April 3rd

### Content
#### Review of the Past Classes
(12:30 - 01:10:55)
- Datatypes [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/02-core/01-data/01-data.ipynb)
    - numbers [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/02-core/02-numbers/02-numbers.ipynb)
    - string [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/02-core/03-strings/03-strings.ipynb)
    - lists and tuples [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/02-core/06-lists/06-lists.ipynb)
    - dicts and sets [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/02-core/07-dicts/07-dicts.ipynb)
- Conditionals [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/02-core/04-conditionals/04-conditionals.ipynb)
- Loops [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/02-core/05-loops/05-loops.ipynb)

#### Functions [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/02-core/08-functions/08-functions.ipynb)
(01:11:20 - 04:00:00)
- What Do I Need Them for?
- Arguments and Parameters
- Docstrings
- Functions Are Also Objects
- Inner Functions
- Lambda Functions
- Generators
- Recursion
- Error Exceptions

[:top:](#top)

## Monday, April 6th

### Content
#### Objects and Classes [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/02-core/09-objects/09-objects.ipynb)
(18:00 - 04:00:00)
- What Are Objects? (18:00 - 01:35:00)
- Inheritance (01:35:05 - 03:40:00)
- Accessing Attributes (03:40:35 - 04:00:00)

[:top:](#top)

## Tuesday, April 7th

### Content
#### Objects and Classes [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/02-core/09-objects/09-objects.ipynb)
- Object-Oriented Programming (05:00 - 03:18:00)

#### File Handling [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/02-core/10-files/10-files.ipynb)
(03:23:00 - 04:01:15)
- Open and Create Files
- Write Files
- Read Files

[:top:](#top)

## Wednesday, April 8th

### Content
#### File Handling [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/02-core/10-files/10-files.ipynb)
(01:30 - 02:38:40)
- Close Files Automatically
- Iterate Files
- **Import** Modules (01:27:30 - 01:44:20)
- How to Organize a Script on Python (01:44:25 - 02:38:40)
    - sys.argv
- Project (02:39:00 - 03:03:03)

[:top:](#top)

<a name="emp"></a>
# Employability :necktie:
## Monday, April 13th


[:top:](#top)

## Thursday, May 7th (from 5 to 8 pm)

[:top:](#top)

## Monday, May 18th

[:top:](#top)

## Wednesday, June 3rd

[:top:](#top)

<a name="libs"></a>
# Libraries :aerial_tramway:
## Tuesday, April 14th

### Content
#### Standard libraries

- **os** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/standard/os/os.ipynb) [:orange_book:](https://docs.python.org/3/library/os.html) (05:40 - 01:30:10) *(Miscellaneous operating system interfaces)*
    - path
    - name
    - listdir()
    - walk()

- **sys** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/standard/sys/sys.ipynb) [:orange_book:](https://docs.python.org/3/library/sys.html?highlight=sys#module-sys) (01:31:10 - 01:55:50) *(System-specific parameters and functions)*
    - argv
    - exc_info()
    - path
    - version
    - platform

- **zlib** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/standard/zlib/zlib.ipynb) [:orange_book:](https://docs.python.org/3/library/zlib.html?highlight=zlib#module-zlib) (01:57:25 - 03:00:00) *(Compression and decompression)*
    - compress
    - decompress
    - checksums
        - adler32
	    - crc32

- **gzip** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/standard/gzip/gzip.ipynb) [:orange_book:](https://docs.python.org/3/library/gzip.html?highlight=gzip#module-gzip) (03:11:40 – 03:49:50) *(Compression and decompression)*
    - open
    - writelines()

[:top:](#top)

## Wednesday, April 15th

### Content
#### Standard libraries
- **zipfile** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/standard/zipfile/zipfile.ipynb) [:orange_book:](https://docs.python.org/3/library/zipfile.html?highlight=zipfile#module-zipfile) (01:00 – 42:20) *(Compression and decompression of ZIP archives)*
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

- **time** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/standard/time/time.ipynb) [:orange_book:](https://docs.python.org/3/library/time.html?highlight=time#module-time) (01:35:40 – 02:22:30) *(Time access and conversions)*
    - definitions
    - time()
    - asctime()
    - localtime()
    - gmtime()
    - mktime()

- **datetime** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/standard/datetime/datetime.ipynb) [:orange_book:](https://docs.python.org/3/library/datetime.html?highlight=datetime#module-datetime) (02:25:10 – 03:17:45) *(Basic date and time types)*
    - date
        - today, day, month, year
        - fromtimestamp
    - .datetime
        - now()
        - minute, year…

- **base64** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/standard/base64/base64.ipynb) [:orange_book:](https://docs.python.org/3/library/base64.html?highlight=base64#module-base64) (03:23:40 – 04:00:00) *(Data encodings)* *(part I)*
    - what econding is and what is not
    - b64encode
    - decode

[:top:](#top)

## Thursday, April 16th

### Content
#### Standard libraries
- **base64** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/standard/base64/base64.ipynb) [:orange_book:](https://docs.python.org/3/library/base64.html?highlight=base64#module-base64) (04:00 - 16:00) *(Data encodings)* *(part II)*
    - HTML module

- **statistics** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/standard/statistics/statistics.ipynb) [:orange_book:](https://docs.python.org/3/library/statistics.html?highlight=statistics#module-statistics) (16:40 – 01:19:20) *(Mathematical statistics functions)*
    - mean
    - geometric_mean
    - median
    - mode
    - stdev & variance

- **collections** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/standard/collections/collections.ipynb) [:orange_book:](https://docs.python.org/3/library/collections.html?highlight=collections#module-collections) (01:32:35 – 02:32:20) *(Container datatypes)*
    - namedtuple
    - deque
    - Counter
    - OrderedDict
    - defaultdict

- **csv** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/standard/csv/csv.ipynb) [:orange_book:](https://docs.python.org/3/library/csv.html?highlight=csv#module-csv) (02:32:40 – 02:58:15) *(CSV file reading and writing)*
    - reader
    - writer

- **re** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/standard/re/re.ipynb) [:orange_book:](https://docs.python.org/3/library/re.html?highlight=re#module-re) (03:20:40 – 04:00:00) *(Regular expression operations)* *(part I)*
    - compile

[:top:](#top)

## Friday, April 17th

### Content
#### Standard libraries
- **re** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/standard/re/re.ipynb) [:orange_book:](https://docs.python.org/3/library/re.html?highlight=re#module-re) (02:45 - 01:29:40) *(Regular expression operations)* *(part II)*
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

- **logging** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/standard/logging/logging.ipynb) [:orange_book:](https://docs.python.org/3/library/logging.html?highlight=logging#module-logging) (01:41:40 – 02:38:35) *(Logging facility for Python)*
    - debug()
    - info()
    - warning()
    - error()
    - critical()

- **pdb** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/standard/pdb/pdb.ipynb) [:orange_book:](https://docs.python.org/3/library/pdb.html?highlight=pdb#module-pdb) (02:40:00 – 03:04:00) *(The Python debugger)*
    - list
    - help
    - where
    - step
    - next
    - return

- **threading** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/standard/threading/threading.ipynb) [:orange_book:](https://docs.python.org/3/library/threading.html?highlight=threading#module-threading) (03:20:45 – 03:59:20) *(Thread-based parallelism)*

[:top:](#top)

## Monday, April 20th

### Content
#### External libraries
- **arrow** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/external/arrow/arrow.ipynb) [:orange_book:](https://pypi.org/project/arrow/) (03:30 – 01:30:15) *(Create, manipulate, format and convert dates, times and timestamps)*
    - get
    - utcnow
        - span
    - now
        - utccoffset()
        - shift()
    - replace

#### Standard libraries
- **random** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/standard/random/random.ipynb) [:orange_book:](https://docs.python.org/3/library/random.html?highlight=random#module-random) (01:53:25 – 03:30:10) *(Generate pseudo-random numbers)*
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
- **matplotlib** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/external/matplotlib/matplotlib.ipynb) [:orange_book:](https://matplotlib.org/3.2.1/contents.html) (03:30:30 – 04:02:40) *(Data visualization tool)* (part I)
    - plot
    - bar
    - hist
    - barh
    - scatter

[:top:](#top)

## Tuesday, April 21st

### Content
#### External libraries
- **matplotlib** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/external/matplotlib/matplotlib.ipynb) [:orange_book:](https://matplotlib.org/3.2.1/contents.html) (28:20 – 01:08:40) *(Data visualization tool)* (part II)
    - title
    - text
    - xlabel
    - ylabel

- **requests** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/external/requests/requests.ipynb) [:orange_book:](https://requests.readthedocs.io/en/master/) (02:05:30 – 04:00:30) *(HTTP library for Python)*
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
- **json** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/standard/json/json.ipynb) [:orange_book:](https://docs.python.org/3/library/json.html?highlight=json#module-json) (05:30 – 56:00) *(JSON encoder and decoder)*
    - dumps
    - Public APIs *(Application Programming Interface)*

#### External libraries
- **pillow** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/external/pillow/pillow.ipynb) [:orange_book:](https://pillow.readthedocs.io/en/stable/) (02:01:17 – 04:01:05) *(Support for opening, manipulating and saving images)* *(part I)*
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
- **pillow** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/external/pillow/pillow.ipynb) [:orange_book:](https://pillow.readthedocs.io/en/stable/) (08:00 – 02:27:50) *(Support for opening, manipulating and saving images)* *(part II)*
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

- **numpy** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/external/numpy/numpy.ipynb) [:orange_book:](https://numpy.org/doc/) (02:29:20 – 03:43:00) *(Scientific computing with Python)*
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
- **pandas** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/external/pandas/pandas.ipynb) [:orange_book:](https://pandas.pydata.org/docs/) (05:20 - 02:25:10) *(Data structures and data analysis tools for Python)*
    - read_csv()
    - to_numeric()

- **qrcode** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/external/qrcode/qrcode.ipynb) [:orange_book:](https://pypi.org/project/qrcode/) (02:25:40 – 02.58:15) *(QR code generator)*

- **Links of interest** (02:59:00 – 03:05:00):
    - [Github Trendings](https://github.com/trending/python) (practice Python on GitHub)
    - [Awesome Python repository](https://github.com/vinta/awesome-python)

- **watchdog** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/05-libs/external/watchdog/watchdog.ipynb) [:orange_book:](https://pythonhosted.org/watchdog/) (03:06:30 – 03:55:00) *(File system events monitor)*
    - Observer()
        - schedule
        - stop
        - join

[:top:](#top)

<a name="patterns"></a>
# Design Patterns :globe_with_meridians:
## Monday, April 27th

### Content
- **Introduction** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/00-Introduction.ipynb) (04:00 - 02:00:50)
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

[:top:](#top)

## Tuesday, April 28th

### Content
- **Adapter** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/05_Adapter.ipynb) [:page_with_curl:](https://en.wikipedia.org/wiki/Adapter_pattern) (07:49 - 38:15)

- **Bridge** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/06-Bridge.ipynb) [:page_with_curl:](https://en.wikipedia.org/wiki/Bridge_pattern) (38:20 - 01:32:50)

- **Façade** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/09-Facade.ipynb) [:page_with_curl:](https://en.wikipedia.org/wiki/Facade_pattern) (01:56:00 - 02:28:05)

- **Flyweight** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/10-Flyweight.ipynb) [:page_with_curl:](https://en.wikipedia.org/wiki/Flyweight_pattern) (02:28:20 - 03:02:05)

- **Strategy** [:beginner:](https://github.com/pythoncanarias/eoi/blob/master/04-patterns/12-Strategy.ipynb) [:page_with_curl:](https://en.wikipedia.org/wiki/Strategy_pattern) (03:18:25 - 04:01:30)

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

### Content
- **Hardware** (25:00 - 01:31:00)
    - Central Processing Unit
    - Random-Access Memory
    - Hard Disk Drive
    - Net
- **Software Information** (01:33:20 - 03:24:00)
    - lscpu
    - uptime
    - htop
    - free
    - lsblk
- **File System Permissions** (03:24:15 - 03:54:00)
    - chmod
    - chown
    - chgrp
- **Installing Virtual Box** (03:59:50 - 04:04:00)

[:top:](#top)

## Monday, May 11th

### Content

- **Installing Virtual Box** (10:00 - 52:00)
- **What Is The OSI Model?** (53:58 - 04:00:00)
    - Physical Layer
    - Data Link Layer
        - MAC (01:10:35 - 01:26:30)
    - Network Layer
        - IP (01:28:10 - 03:29:00)
        - NAT (03:29:35 - 03:38:00)
    - Transport Layer
        - Ports (03:39:45 - 04:00:00)
            - TCP
            - UDP
    - Session Layer
    - Presentation Layer
    - Application Layer

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

- [Python Data Science Handbook](jakevdp.github.io/PythonDataScienceHandbook)
- IPython: Beyond Normal Python [:page_with_curl:](https://jakevdp.github.io/PythonDataScienceHandbook/01.00-ipython-beyond-normal-python.html)
    - Help and Documentation in IPython:
	- ?
	- TAB
	- dir(library)
	- globals(), locals()
	- **Built-in Functions in Python** [:page_with_curl:](https://docs.python.org/3/library/functions.html)
    - Keyboard Shortcuts
	- Standard Shortcuts
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

## Thursday, May 28th
- IPython: Beyond Normal Python [:page_with_curl:](https://jakevdp.github.io/PythonDataScienceHandbook/01.00-ipython-beyond-normal-python.html)
    - IPython and Shell Commands
	- Shell Commands in IPython
	    - !
	- Shell-Related **Magic Commands**
	    - ½cd
    - Errors and Debugging
	- Controlling Exceptions
    - Profiling and Timing Code
    - More IPython Resources

- Introduction to NumPy []()
    - Understanding Data Types in Python
    - The Basics of NumPy Arrays
    - Computation on NumPy Arrays: Universal Functions
    - Aggregations: Min, Max, and Everything In Between
    - Computation on Arrays: Broadcasting
    - Comparisons, Masks, and Boolean Logic
    - Fancy Indexing
    - Sorting Arrays
    - Structured Data: NumPy's Structured Arrays


## Friday, May 29th

[:top:](#top)

## Monday, June 1st

[:top:](#top)

## Tuesday, June 2nd

[:top:](#top)

## Thursday, June 4th

[:top:](#top)

## Friday, June 5th

[:top:](#top)

## Monday, June 8th

[:top:](#top)

## Tuesday, June 9th

[:top:](#top)

## Wednesday, June 10th

[:top:](#top)

## Thursday, June 11th (from 4 to 6 pm)

[:top:](#top)
