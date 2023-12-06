class Music():
    def __init__(self, artist, track_title, album, year):
        self.artist = artist
        self.song = track_title
        self.album = album
        self.year = year
    def __str__(self):
        return f"Performer: {self.artist} \nSong: \t {self.song} \nAlbum: \t {self.album} \nYear: \t {self.year}"

song1 = Music("abcd", "efgh", "jklm", 1800)
song2 = Music("qwer", "asdf", "zxcv", 2100)
print(song1)
print(song2)