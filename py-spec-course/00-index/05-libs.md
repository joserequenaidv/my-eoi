#LD. Librerías destacadas / libs :aerial_tramway:
##Martes, 14 de abril

#### [Enlace a la sesión grabada :beginner:](https://us.bbcollab.com/recording/57d0753cbfa34416befb24c342e70206).

###Contenido:
####Librerías estándar

- Librería **os** (05:40 – 01:30:10)
*(Llamadas al sistema operativo)*
◦ path
◦ name
◦ listdir()
◦ walk()

- Librería **sys** (01:31:10 – 01:55:50)
*(Configuración específica del sistema)*
◦ argv
◦ exc_info()
◦ path
◦ version
◦ platform

- Librería **zlib** (01:57:25 – 03:00:00)
*(Librería de comprensión)*
◦ compress
◦ decompress
◦ checksums
    ▪ adler32
	▪ crc32

- Librería **gzip** (03:11:40 – 03:49:50)
*(Librería de comprensión)*
◦ open
◦ writelines()

##Miércoles, 15 de abril

#### [Enlace a la sesión grabada :beginner:](https://us.bbcollab.com/recording/6a5eccadc94248d39f73e587677f7442) 

###Contenido:
####Librerías estándar
- Librería **zipfile** (01:00 – 42:20)
*(Librería de comprensión)*
◦ is_zipfile()
◦ clase ZipFile
    ▪ getinfo(name)
    ▪ extract(member, path=None, pwd=None)
    ▪ extractall(path=None, members=None, pwd=None)
    ▪ printdir()
    ▪ setpassword(pwd)
    ▪ read(name, pwd=None)
    ▪ testzip()
    ▪ write (filename, arcname=None, compress_type=None, compresslevel=None)
    ▪ writestr (zinfo_or_arcname, data, compress_type=None, compresslevel=None)

- **Miniproyecto:** programa de backup (42:25 – 01:17:00)


- Librería **time** (01:35:40 – 02:22:30)
◦ Definiciones
◦ time()
◦ asctime()
◦ localtime()
◦ gmtime()
◦ mktime()

- Librería **datetime** (02:25:10 – 03:17:45)
◦ date
    ▪ today, day, month, year
    ▪ fromtimestamp
◦ .datetime
    ▪ now()
    ▪ minute, year…

- Librería **base64** (03:23:40 – 04:00:00) *(parte I)*
*(Codificar y decodificar información binaria usando ASCII)*
◦ ¿Qué es codificar y decodificar?
◦ b64encode
◦ decode

##Jueves, 16 de abril

#### [Enlace a la sesión grabada :beginner:](https://us.bbcollab.com/recording/c9a64768efd04e05b72af6afdb5647a1)

###Contenido:
####Librerías estándar
- Librería **base64** (04:00 – 16:00) *(parte II)*
*(Codificar y decodificar información binaria usando ASCII)*
◦ Módulo HTML

- Librería **statistics** (16:40 – 01:19:20)
*(Contiene funciones matemáticas para realizar cálculos estadísticos)*
◦ mean
◦ geometric_mean
◦ median
◦ mode
◦ stdev y variance

- Librería **collections** (01:32:35 – 02:32:20)
*(Implementa contenedores especializados a partir de los básicos: diccionarios, listas, conjuntos y tuplas)*
◦ namedtuple
◦ deque
◦ Counter
◦ OrderedDict
◦ defaultdict

- Librería **csv** (02:32:40 – 02:58:15)
*(Intercambio de información de hojas de cálculo o bases de datos)*
◦ reader
◦ writer

- Librería **re** (03:20:40 – 04:00:00) *(parte I)*
*(Expresiones regulares)*
◦ compile

##Viernes, 17 de abril

#### [Enlace a la sesión grabada :beginner:](https://us.bbcollab.com/recording/022e4743fea4480793cb5ffa3b9b19d4)

###Contenido:
- Librería **re** (02:45 - 01:29:40) *(parte II)*
*(Expresiones regulares)*
◦ Caracteres especiales
    ▪ ^
    ▪ ?
    ▪ [ y ]
    ▪ |
    ▪ { y }
    ▪ \
◦ Secuencias especiales
    ▪ \b y \B
    ▪ \d y \D
    ▪ \s y \S
    ▪ \w
◦ Caracteres especiales ‘(‘ y ‘)’
◦ search, match y findall

- Librería **logging** (01:41:40 – 02:38:35)
*(Define un sistema de registro de eventos o log a nuestra aplicación o librerías)*
◦ debug()
◦ info()
◦ warning()
◦ error()
◦ critical()

- Librería **pdb** (02:40:00 – 03:04:00)
*(Debugger interactivo para programas Python)*
◦ list
◦ help
◦ where
◦ step
◦ next
◦ return

- Librería **threading** (03:20:45 – 03:59:20)
*(Gestionar operaciones concurrentes dentro de un proceso)*

##Lunes, 20 de abril
####[Enlace a la sesión grabada :beginner:](https://us.bbcollab.com/recording/a27814b5362f40ac9e7a30adad68d1b5)

###Contenido:
####Librerías externas
- Librería **arrow** (03:30 – 01:30:15)
*(Facilita el trabajo con fechas)*
◦ get
◦ utcnow
    ▪ span
◦ now
    ▪ utccoffset()
    ▪ shift()
◦ replace

- Librería **random** (01:53:25 – 03:30:10)
*(Generador de números (pseudo)aleatorios)*
◦ random()
◦ choice()
◦ seed()
◦ **Miniproyecto:** programa ‘piedra, papel o tijera’
◦ choices()
    ▪ cum_weights
◦ sample()
◦ randrange()
◦ randint()
◦ shuffle()
◦ uniform()
◦ paretovariate()
◦ gauss()

- Librería **matplotlib** (03:30:30 – 04:02:40) (parte I)
*(Herramienta para visualización de datos)*
◦ plot
◦ bar
◦ hist
◦ barh
◦ scatter

##Martes, 21 de abril

#### [Enlace a la sesión grabada :beginner:](https://us.bbcollab.com/recording/1fbd9ff57ac946099a24fa27213ad203 )

###Contenido: 
- Librería **matplotlib** (28:20 – 01:08:40) *(parte II)*
*(Herramienta para visualización de datos)*
◦ title
◦ text
◦ xlabel
◦ ylabel

- **Miniproyecto:** Analizar árbol de ficheros y hacer un gráfico de barras horizontal que represente el número de archivos encontrados de cada tipo. (01:08:45 – 01:52:20)

- Librería **requests** (02:05:30 – 04:00:30)
*(Módulo para HTTP escrito en Python)*
◦ get
    ▪ status_code
    ▪ headers
    ▪ text
    ▪ json()
    ▪ url
    ▪ history
    ▪ cookies
◦ post
◦ put
◦ delete
◦ head
◦ options
◦ Session()

##Miércoles, 22 de abril

#### [Enlace a la sesión grabada :beginner:](https://us.bbcollab.com/recording/9b6b74c1e54f49da92b2fb87f0893f88)

###Contenido:
####Librería estándar
- Librería **json** (05:30 – 56:00)
*(Trabajar con ficheros en formato JSON)*
◦ dumps
◦ APIs públicas (56:55 – 02:00:00)
  *(Interfaz de programación de aplicaciones)*

####Librerías externas
- Librería **pillow** (02:01:17 – 04:01:05) *(parte I)*
*(Proceso de imágenes)*
◦ format, size y mode
◦ open
◦ save
◦ thumbnail
◦ crop
◦ transpose
◦ paste
◦ split
◦ merge
◦ resize

##Jueves, 23 de abril

#### [Enlace a la sesión grabada :beginner:](https://us.bbcollab.com/recording/f17c2054875241678981d2312edeee87)

###Contenido:
- Librería **pillow** (08:00 – 02:27:50) *(parte II)*
*(Proceso de imágenes)*
◦ rotate
◦ convert
◦ ImageFilter()
    ▪ BLUR
    ▪ CONTOUR
    ▪ DETAIL
    ▪ …
◦ point
◦ ImageEnhance
    ▪ Color
    ▪ Contrast
    ▪ Brightness
    ▪ Sharpness
◦ ImageDraw
  ▪ Draw
  • arc
  • pieslice
  • polygon
  • rectangle
  • text
  • textsize
  • floodfill
  • ellipse
◦ getpixel
◦ putpixel
◦ load()
◦ Image.new()
◦ paste

- Librería **numpy** (02:29:20 – 03:43:00)
*(Para trabajar con vectores y matrices de forma eficiente)*
◦ array
◦ dtype
◦ reshape
◦ zeros
◦ linspace
◦ random
    ▪ rand
◦ cos

- **Miniproyecto:** Copia de seguridad (03:45:00 – 04:01:50)

##Viernes, 24 de abril

#### [Enlace a la sesión grabada :beginner:](https://us.bbcollab.com/recording/e531751ef17f44589223fbfd4f7de5e8)

###Contenido:
- Librería **pandas** (05:20 - 02:25:10)
*(Extensión de NumPy para manipulación y análisis de datos)*
◦ read_csv()
◦ to_numeric()

- Librería **qrcode** (02:25:40 – 02.58:15)
*(Generador códigos QR)*

- **De interés** (02:59:00 – 03:05:00):
◦ Github Trendings
  *(aportar y practicar con Python en GitHub)*
◦ Repositorio **Awesome Python**

- Librería **watchdog** (03:06:30 – 03:55:00)
◦ Observer()
    ▪ schedule
    ▪ stop
    ▪ join
