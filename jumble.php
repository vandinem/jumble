<!DOCTYPE HTML>
<html lang="en">
<head>
    <title>Solve the Jumble</title>
</head>
<body>
	
    <form name="form1" method="post" action="<?php echo $_SERVER["PHP_SELF"]; ?>">
		<strong>Enter 'Jumbled' word:</strong><BR/>
		
		<input 
			name="scrambled" 
			type="text" 
			style="width: 80px; padding: 2px; border: 1px solid black" 
			value="<?php echo $scrambled; ?>"
		>
		<input 
			type="submit" 
			name="Submit" 
			value="Unscramble!"
		>

	</form>

	<?php

	    if ( isset( $_POST[ "scrambled" ] ) && ( strlen( $_POST[ "scrambled" ] ) > 0 ) ) {
			
			process_jumble( $_POST[ "scrambled" ], 1 );
			
		}
		else {
			
			jumble_form( "elbmuj" , 0 );
		
		}

	?>
    
</body>
</html>

<?php 

	function jumble_form( $scrambled, $flag ) {
			
		global $wordlist;
		
		if ( $flag ) {
			
			$ctr = count( $wordlist );
			
			if ( isset( $_POST[ "scrambled" ] ) && ( $ctr == 0 ) ) {
				
				print "<strong>Nothing found!</strong><BR>";
				
			}
			else {
				
				print "<BR/>";
				
				for ( $i = 0;$i < $ctr;$i++ ) {
					
					print ( $i + 1 ) . ": <strong>$wordlist[$i]</strong><BR/>";
					
				}
				
			}
			
		}

	}

	function process_jumble( $scrambledStr ) {
		
		global $wordlist;

        $db = new SQLite3( './puzzlewords.sqlite', SQLITE3_OPEN_READONLY);
		
		$wordlist = array();

		$chars  = str_split( strtolower( $scrambledStr ) );
            
        sort( $chars );
            
        $sorted = join( "", $chars );
		
		// Get any rows from the wordlist with a matching 'sorted' key
		
		$res = $db -> query( "SELECT word FROM wordlist WHERE sorted=\"$sorted\" ORDER BY word" );

		while ( $row = $res -> fetchArray() ) {
			
			$wordlist[] = $row[ 0 ];
			
		}
		
	} 
	
	jumble_form( $scrambledStr, 1 );
	
?>