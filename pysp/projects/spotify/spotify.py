class Song:
    def __init__(self, track, artist, genre, bpm, energy, danceability, length):
        '''This is the constructor of the class Song which obtains the
        following parameters'''
        self.track = track
        self.artist = artist
        self.genre = genre
        self.bpm = bpm
        self.energy = energy
        self.danceability = danceability
        self.length = length

    def __str__(self):
        what_we_will_print = f'{self.track},{self.artist},{self.genre},{str(self.bpm)},{str(self.energy)},{str(self.danceability)},{str(self.length)}\n'
        return what_we_will_print

    def change_speed(self, relative_bpm):
        '''If we increase x bpms:
            - The energy increases 2 times that value.
            - The danceability increases 3 times that value.
            - The length is decreased by x.
           If we decrease x bpms:
            - The energy decreases 2 times that value.
            - The danceability decreases 3 times that value.
            - The length is increased by x.'''
        self.bpm = int(self.bpm) + relative_bpm
        self.danceability = int(self.danceability) + 3 * (relative_bpm)
        self.energy = int(self.energy) + 2 * (relative_bpm)
        self.length = int(self.length) - relative_bpm

    @staticmethod
    def load_songs(path):
        '''This method loads all lines of our document and divides all parameters
        by commas in a list of lists as objects, in order to be able to use them later'''
        our_file = open(path, encoding = "utf-8") #Encoding for UTF-8
        songs = []
        n = 0
        for each_line in our_file:
            parameters = each_line.split(',')
            my_object = Song(
                parameters[0],
                parameters[1],
                parameters[2],
                parameters[3],
                parameters[4],
                parameters[5],
                parameters[6])
            songs.append(my_object) #Adding parameters as objects to the list
            n += 1
        return songs
        our_file.close()

    @staticmethod
    def save_songs(songs, path):
        '''This method saves every line with the changes already updated in a
        new file'''
        with open('./files/top50_mod.csv', 'w') as path:
            n = 0
            for _ in range(0, 50):
                path.write(songs[n].__str__())
                n += 1
