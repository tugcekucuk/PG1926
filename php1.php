<?php
$saat = date("h");
$message = '';

if($saat >= 0 && $saat <= 5){
    $message = 'esenlikler dilerim';
} else 
if($saat >= 6 && $saat <= 9){
    $message = 'G�nayd�n';
} else 
if($saat >= 10 && $saat <= 16){
    $message = '�yi g�nler';
} else 
if($saat >= 16 && $saat < 19){
    $message = '�yi aksamlar';
} else 
if($saat >= 20 && $saat <= 23){
    $message = '�yi geceler';
}

echo $message;

?>