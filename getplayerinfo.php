<?php
include_once("config.php");


$pos= $_GET["pos"];
$team= $_GET["team"];
if( isset($_GET['id'] ) ) {
    $id=$_GET['id'];
	
	
	
	if (count($id)>0){
		$response["success"] = 1;
		$response{"players"}=array();
		
		
		foreach($id as &$value){
			//Passing Stats Query
			
			$stats = array();
			$query=mysqli_query($con,"SELECT * FROM playerinfo WHERE GSID ='$value' AND TEAM='$team' AND Pos='$pos'") or die(mysqli_error());;
			if (mysqli_num_rows($query) > 0) {
				//$response["players"] = array();
				while($result=mysqli_fetch_assoc($query)){
					//$stats = array();
					$stats["GSID"] = $result["GSID"];
					$stats["name"] = $result["Name"];
					$stats["team"] = $result["TEAM"];
					$stats["pos"] = $result["Pos"];
					array_push($response["players"], $stats);
					
				}
				// success
				
			}
			else {
			// if order is empty then player doesn't exist in database.
				
					$stats["GSID"] = "N/A";
					$stats["name"] = "N/A";
					$stats["team"] = "N/A";
					$stats["pos"] = "N/A";
					array_push($response["players"], $stats);
			}
			
	}
	}
	else{
	$response["success"] = 0;
      $response["message"] = "No Items Found";
	}
}
else{
	 $response["success"] = 0;
	 $response["message"] = "No Items Found";
	 
 }

echo json_encode($response);
?>