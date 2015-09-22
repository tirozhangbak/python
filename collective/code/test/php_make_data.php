<?php
$data = file_get_contents('data.txt');
$row = explode("\n",$data);
foreach( $row as $val ){
    $temp = explode( "\t",trim($val));
    $users[$temp[0]][$temp[1]] = $temp[2];
}
//echo serialize($users);
//print_r($users);


// vim600:ts=4 st=4 foldmethod=marker foldmarker=<<<,>>>
// vim600:syn=php commentstring=//%s
