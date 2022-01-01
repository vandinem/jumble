import sqlite3
import re

database = "./puzzlewords.sqlite"
  
try:
	conn = sqlite3.connect( database )
except Error as e:
	print( e )
	exit()
	
cursor = conn.cursor()

while True:
	
	str = input( "\nEnter a Jumble word? " )
	
	str = str.lower()
	
	if ( str == 'q' ):
		print( "\n" )
		break
	else:
		
		str = re.findall("[\da-z]*", str)[0]
		
		letters  = list( str )
		
		str = "" . join( sorted( letters ) )
		
		if ( len( str ) < 3 ):
			print( "Come on guy ... at least three letters?" )
		
		cursor.execute( f"SELECT word FROM wordlist WHERE sorted = '{ str }'" )
		
		rows = cursor.fetchall()
		
		if ( len( rows ) == 0 ):
			print( "No solutions found!" )
			continue
		
		for row in rows:
			print( f"{ row[ 0 ] }" )