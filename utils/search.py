
database = "Hi Hello King User You I Want"


def search(words):
		filtered_text = []
		for w in words:
			#splitting the word if its animation is not present in database
			if w not in database:
				for c in w:
					filtered_text.append(c + ".mp4")
				#otherwise animation of word
			else:
				filtered_text.append(w + ".mp4")
		return filtered_text