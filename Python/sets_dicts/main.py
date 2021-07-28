dictionarySong = {'songName': "Los Dioses", 'albumName': "Los Dioses", 'songDurationMinutes': 4.4,
                  'songDurationSeconds': 280, 'ArtistOne': "Anuel AA", 'ArtistTwo': "Ozuna",
                  'genre': "Latin Trap", 'yearReleased': 2021, 'youtubeViewsToday': 91295833}

for i in dictionarySong:
    print(i + ' : ' + str(dictionarySong[i]))

key = str(input('Guess a key of the dictionary: \n'))
value = str(input('Guess the value of the key: \n'))


def validate_dict(key, value):
    while(True):
        if key in dictionarySong and str(dictionarySong[key]) == value:
            return True
        else:
            return False


validate_dict(key, value)
print(validate_dict(key, value))

''' songName = "Los Dioses"
albumName = "Los Dioses"
songDurationMinutes = "4.4"
songDurationSeconds = 280
ArtistOne = "Anuel AA"
ArtistTwo = "Ozuna"
Artists = ArtistOne + " & " + ArtistTwo
genre = "Latin Trap"
dateReleasedString = "January 22 2021"
yearReleased = 2021
youtubeViewsToday = 91295833

print(songName)
print(albumName)
print(songDurationMinutes)
print(songDurationSeconds)
print(ArtistOne)
print(ArtistTwo)
print(Artists)
print(genre)
print(dateReleasedString)
print(yearReleased)
print(youtubeViewsToday) '''
