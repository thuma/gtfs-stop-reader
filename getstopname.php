<?php

// Test row:
// print json_encode(getClosestStations(57.947082690244,14.047643900878));

// Store alla stations in memory for later access:
$handle = fopen("gtfs-stop-reader/stops.txt", "r");
$head = preg_split('/,/',$buffer = fgets($handle, 4096));
$allstops = array();

while (($buffer = fgets($handle, 4096)) !== false)
		{
		$data = preg_split('/,/',$buffer);
		$row = new stdClass;
		foreach($data as $no => $col)
			{
			$row->{$head[$no]} = $col;
			}
	    $allstops[] = $row;
 	   }
fclose($handle);

// Get the closest station:
function getClosestStation($latitude, $longitude, $maxdist = 100){
	global $allstops;

	$closest = new stdClass;
	$closest->distance = $maxdist;
	$closest->error = "No stop found.";
	foreach($allstops as $row ){
	// Convert to float:
	$row->stop_lat = floatval($row->stop_lat);
	$row->stop_lon = floatval($row->stop_lon);
		if(abs($latitude - $row->stop_lat) < 0.2 AND abs($longitude - $row->stop_lon) < 0.2 ){
			$row->distance = getDistance($latitude, $longitude, $row->stop_lat, $row->stop_lon);
			if($row->distance < $closest->distance )
				{
				$closest = $row;
				}
			}
 	   }
	return $closest;
}

// Calculate closest distanse.
// Code from: http://www.codecodex.com/wiki/Calculate_distance_between_two_points_on_a_globe
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