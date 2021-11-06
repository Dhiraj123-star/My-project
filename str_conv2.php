<?php

# declare multi_dimensional array

$values =array("name"=>"Vijay",array("hobby"=>"coding","address"=>"Bhiwadi"));

#use json_encode() function

$json= json_encode($values);

# display the output

echo($json);



?>
