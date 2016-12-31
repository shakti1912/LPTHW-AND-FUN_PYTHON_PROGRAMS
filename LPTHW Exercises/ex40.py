class Song(object):

	def __init__(self, lyrics, writer):
		self.lyrics = lyrics
		self.writer = writer
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
	def writer(self):
		for line in self.writer:
			print line
	
happy_bday = Song(["Happy birthday to you", 
					"I don't want to get sued", 
					"So I'll stop right there"], ["Shakti"])
					
bulls_on_parade = Song(["They rally around the family",
						 "With pockets full of shells"], ["Singh"])
			
			
ly = ["HI", "wow", "How you doing"]			 
song = Song(ly,["Rathore"])
						 
happy_bday.sing_me_a_song()
happy_bday.writer()
bulls_on_parade.sing_me_a_song()
song.sing_me_a_song()

		