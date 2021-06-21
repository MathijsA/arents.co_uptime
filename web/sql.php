

<table>
  <tr>
    <th>id</th>
    <th>time</th>
    <th>server</th>
    <th>currentstatus</th>
  </tr>

<?php

include "dbhost.php";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * FROM vpsde ORDER BY id DESC ";
$result = $conn->query($sql);


$statusboolean = 1;
if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    $status = $row["currentstatus"];
    if ($status === "up") {
      echo "<tr class='green'><td> " . $row["id"]. " </td><td>  " . $row["time"]. " </td><td> " . $row["server"]. " </td><td> ". $row["currentstatus"]. "</td></tr>";
    }else{
      echo "<tr class='red'><td> " . $row["id"]. " </td><td>  " . $row["time"]. " </td><td> " . $row["server"]. " </td><td> ". $row["currentstatus"]. "</td></tr>";
    }


    if ($statusboolean == 1){
      $status = $row["currentstatus"];
    }
    $statusboolean = 0;

  }


} else {
  echo "0 results";
}
$conn->close();
?>
