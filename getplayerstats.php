<?php
include_once("config.php");
 
 $week= $_GET["week"];
 

 if( isset($_GET['name'] ) ) {
    $id=$_GET['name'];
 
	if (count($id)>0){
		$response["success"] = 1;
		$response{"players"}=array();
		
		
		foreach($id as &$value){
			//Passing Stats Query
			
			$stats = array();
			$query=mysqli_query($con,"SELECT * FROM passing_stats WHERE player_id ='$value' AND week='$week'") or die(mysqli_error());;
			if (mysqli_num_rows($query) > 0) {
				//$response["players"] = array();
				while($result=mysqli_fetch_assoc($query)){
					//$stats = array();
					
					$stats["pass_att"] = $result["att"];
					$stats["pass_comp"] = $result["comp"];
					$stats["pass_yards"] = $result["yards"];
					$stats["pass_tds"] = $result["td"];
					
				}
				// success
				
			}
			else {
			// if order is empty then player hasn't played yet or played and didn't record any stats. So set all stats to 0.
				
				//$stats["name"] = $value;
				$stats["pass_att"] = 0;
				$stats["pass_comp"] = 0;
				$stats["pass_yards"] = 0;
				$stats["pass_tds"] = 0;
		 
				//$response["passing"]= $stats;
			}
			//Rushing Stasts query
			$query=mysqli_query($con,"SELECT * FROM rushing_stats WHERE player_id ='$value' AND week='$week'") or die(mysqli_error());;
			if (mysqli_num_rows($query) > 0) {
				//$response["players"] = array();
				while($result=mysqli_fetch_assoc($query)){
					
					$stats["rush_att"] = $result["att"];
					$stats["rush_yards"] = $result["yards"];
					$stats["rush_tds"] = $result["tds"];
					
				}
				
			}
			else {
			// if order is empty then player hasn't played yet or played and didn't record any stats. So set all stats to 0.
				
				$stats["rush_att"] = 0;
				$stats["rush_yards"] = 0;
				$stats["rush_tds"] = 0;
		 
				
			}
			//Receiving Stasts query
			$query=mysqli_query($con,"SELECT * FROM receiving_stats WHERE player_id ='$value' AND week='$week'") or die(mysqli_error());;
			if (mysqli_num_rows($query) > 0) {
				
				while($result=mysqli_fetch_assoc($query)){
					
					$stats["rec"] = $result["rec"];
					$stats["rec_yards"] = $result["yards"];
					$stats["rec_tds"] = $result["tds"];
					
					
					
				}
				
			}
			else {
			// if order is empty then player hasn't played yet or played and didn't record any stats. So set all stats to 0.
				$stats["rec"] = 0;
				$stats["rec_yards"] = 0;
				$stats["rec_tds"] = 0;
		 
				
			}
			$query=mysqli_query($con,"SELECT * FROM playerinfo WHERE GSID ='$value'") or die(mysqli_error());;
			if (mysqli_num_rows($query) > 0) {
				//$response["players"] = array();
				while($result=mysqli_fetch_assoc($query)){
					//$stats = array();
					$stats["GSID"] = $result["GSID"];
					$stats["name"] = $result["Name"];
					$stats["team"] = $result["TEAM"];
					$stats["pos"] = $result["Pos"];
					$stats["profile"] = $result["profile"];
					
					
				}
				// success
				
			}
			else {
			// if order is empty then player doesn't exist in database.
				
					$stats["GSID"] = "N/A";
					$stats["name"] = "Player not found";
					$stats["team"] = "N/A";
					$stats["pos"] = "N/A";
					$stats["profile"] = "N/A";
			}
			
			array_push($response["players"], $stats);
			
		}
	}
	else{
		$response["success"] = 0;
		  $response["message"] = "No Items Found";
	}
// echoing JSON response
 }
 else{
	 $response["success"] = 0;
	 $response["message"] = "No Items Found";
	 
 }
echo json_encode($response);
 
?>
