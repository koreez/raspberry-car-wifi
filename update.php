<?php
	$file = 'script/input.txt';
	
	/*
	 * move:
	 *  - 1: Up
	 *  - 2: Down
	 *  - 3: Left
	 *  - 4: Right
	 */
	
	if(isset($_GET['move'])) {
		$input = $_GET['move'];
		file_put_contents($file, $input);
	}
	
?>
