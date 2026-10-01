# # ######################################################### Practice Problem ############################################################

# # # 20 questions to master oops fundamentals

# # #######################################################################################################################################

# # -------------------------------------------------------------------------------------
# # -------------------------------------------------------------------------------------

# Dunder Methods (Problems 16-17)

# 16. Point with Operators
# Create Point(x, y) with:
# __str__ → "(3, 4)"
# __eq__ → two points are equal if x and y match
# __add__ → adds two points and returns a new Point
# Test: print(p1), p1 == p2, print(p1 + p2).
# Concepts: __str__, __eq__, __add__
# Hint: __str__ must return a string (not print). __add__(self, other) returns Point(self.x + other.x, self.y + other.y).
#  __eq__ returns a boolean expression.

# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return "({}, {})".format(self.x, self.y)

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __add__(self, other):
#         return f"{self.x + self.x}, {self.y + other.y}"

# p1 = Point(3,4)
# p2 = Point(3,4)
# p3 = Point(1,1)

# print(p1)
# print(type(p1))

# print(p1 == p2)
# print(p2 == p3)

# print(p1 + p2)


# # -------------------------------------------------------------------------------------

# 17. Playlist
# Create Playlist that stores a list of song names. Add:
# add_song(name)
# __len__ so len(playlist) works
# __getitem__ so playlist[0] works
# __str__ that shows all songs
# Concepts: __len__, __getitem__, __str__
# Hint: Keep self.songs = [] in __init__. __len__ returns len(self.songs). __getitem__(self, index) returns self.songs[index].
#  For __str__, use ", ".join(self.songs).

# class Playlist:
#     def __init__(self):
#         self.song = []

#     def add_song(self, song):
#         self.song.append(song)

#     def __len__(self):
#         return len(self.song)

#     def __getitem__(self, key):
#         return self.song[key]

#     def __str__(self):
#         return ", ".join(self.song)

# music = Playlist()
# music.add_song("Die with smile")
# music.add_song("Faded")
# music.add_song("Sailor")

# print(music)
# print(len(music))
# print(music[2])


# # -------------------------------------------------------------------------------------

# Composition and Putting It Together (Problems 18-20)
# 18. Car Has an Engine
# Create Engine with start() and stop(). Create Car that has an Engine object (created inside Car.__init__).
#  Car's start() calls the engine's start() and then prints "Car ready".
# Concepts: composition (has-a)
# Hint: Inside Car.__init__, write self.engine = Engine(). Then Car.start calls self.engine.start().
# Do not inherit from Engine, because a Car is not an Engine.

# class Engine:
#     def start(self):
#         print("Engine started")

#     def stop(self):
#         print("Engine off")

# class Car:
#     def __init__(self):
#         self.engine = Engine()       # Car HAS an Engine

#     def start(self):
#         self.engine.start()
#         print("Car is ready to drive")

#     def stop(self):
#         self.engine.stop()
#         print("turn off the car")

# Car().start()
# Car().stop()




# # -------------------------------------------------------------------------------------

# 19. Library System
# Create Book (title, author, is_available). Create Library that has a list of books, with:
# add_book(book)
# remove_book(title)
# search_by_title(text) (returns matching books)
# lend_book(title), which sets is_available to False if available, otherwise prints a message
# Concepts: composition, working with lists of objects
# Hint: Library keeps self.books = [] and stores Book objects in it. To search or remove, loop through self.books and compare book.title. 
# Use .lower() on both sides for case-insensitive search.

class Book:
    def __init__(self, title, author, is_available):
        self.title = title
        self.author = author
        self.is_available = is_available

class library:
    def __init__(self):
        self.book = []

    def add_book(self, books):
        self.book.append(books)

    def remove_book(self, title):
        self.book.remove(title)

    def search_by_title(self, text):
        return text in 




# # -------------------------------------------------------------------------------------


# 20. ETL Pipeline Skeleton (from your roadmap)
# Abstract ETLStep with abstract run(), and a name stored in __init__
# ExtractStep, TransformStep, LoadStep that implement run() (just print what they would do)
# __str__ on ETLStep that returns the step name
# Pipeline class that holds a list of steps, has add_step(step), and execute() that runs each in order
# Concepts: abstraction, inheritance, polymorphism, composition, dunder methods together
# Hint: Pipeline.execute is a loop: for step in self.steps: print(step); step.run(). Because every step has run(), the pipeline does not care which step it is (polymorphism). Test by adding the steps in order: Extract, Transform, Load.





# # -------------------------------------------------------------------------------------