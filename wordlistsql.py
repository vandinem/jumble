import urllib.request
import sqlite3

# --------------------------------------------------------------------
# Get a sqlite table ready for data

database = "./puzzlewords.sqlite"
  
try:
	conn = sqlite3.connect( database )
except Error as e:
	print( e )
	exit()
	
cursor = conn.cursor()

# Creating table
table = """CREATE TABLE IF NOT EXISTS wordlist( word VARCHAR( 30 ), sorted VARCHAR( 30 ), UNIQUE( word, sorted ) );"""
cursor.execute( table )

# --------------------------------------------------------------------
# Get the words at https://www.mit.edu/~ecprice/wordlist.10000, and store
# each word and its sorted version in our sqlite table.

# url  = "https://www.mit.edu/~ecprice/wordlist.10000"
url  = "http://www-personal.umich.edu/~jlawler/wordlist"
file = urllib.request.urlopen( url )

maxlen = 0;

ctr = 0

for line in file:
	decoded_line = line.decode( "utf-8" )
	
	if ( decoded_line[ 0 ] == '#' ): # skip comments
		continue
	
	word = decoded_line.rstrip()
	word = word.lower()
	
	letters  = list( word )
	
	sortword = "" . join( sorted( letters ) )
	
	# print( f"{ word }, { sortword }" )
	
	try:
		cursor.execute( "INSERT OR IGNORE INTO wordlist ( word, sorted ) VALUES ( ?, ? );", ( word, sortword ) )
	except:
		print( f"Failed INSERT to wordlist (DB open in browser?): { word }, { sortword }" )
		conn.close()
		exit()
	
	if ( len( word ) > maxlen ):
		maxlen = len( word )
		
	ctr = ctr + 1


conn.commit()

conn.close()
	
print( f"Read the page and found { ctr } words and max length is { maxlen }" )
