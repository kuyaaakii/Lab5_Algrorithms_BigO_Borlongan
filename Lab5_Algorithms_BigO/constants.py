LAST_NAME = "Borlongan"
STUDENT_ID = "TUPM-26-1837"
FAVORITE_ARTIST = "Typecast"
SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)
ARTIST_LENGTH = len(FAVORITE_ARTIST)
ARTIST_SUM = sum(ord(c.lower())-96 for c in FAVORITE_ARTIST)
