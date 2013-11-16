<?php

// Test row:
// print json_encode(getClosestStations(57.947082690244,14.047643900878));

function getClosestStation($latitude, $longitude, $maxdist = 100){
	$handle = fopen("gtfs-stop-reader/stops.txt", "r");
	$head = preg_split('/,/',$buffer = fgets($handle, 4096));
	$closest = new stdClass;
	$closest->distance = $maxdist;
	$closest->error = "No stop found.";
	while (($buffer = fgets($handle, 4096)) !== false)
		{
		$data = preg_split('/,/',$buffer);
		$row = new stdClass;
		foreach($data as $no => $col)
			{
			$row->{$head[$no]} = $col;
			}
		$row->distance = getDistance($latitude, $longitude, floatval($row->stop_lat), floatval($row->stop_lon));
		if($row->distance < $closest->distance ){
			$closest = $row;
		}
 	   }
	fclose($handle);
	
	return $closest;
}

function getDistance($latitude1, $longitude1, $latitude2, $longitude2) {  
    $earth_radius = 6371;  
      
    $dLat = deg2rad($latitude2 - $latitude1);  
    $dLon = deg2rad($longitude2 - $longitude1);  
      
    $a = sin($dLat/2) * sin($dLat/2) + cos(deg2rad($latitude1)) * cos(deg2rad($latitude2)) * sin($dLon/2) * sin($dLon/2);  
    $c = 2 * asin(sqrt($a));  
    $d = $earth_radius * $c;  
      
    return $d;  
}

?>