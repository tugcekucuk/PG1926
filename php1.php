<?php
$saat = date("h");
$message = '';

if($saat >= 0 && $saat <= 5){
    $message = 'esenlikler dilerim';
} else 
if($saat >= 6 && $saat <= 9){
    $message = 'Günaydın';
} else 
if($saat >= 10 && $saat <= 16){
    $message = 'İyi günler';
} else 
if($saat >= 16 && $saat < 19){
    $message = 'İyi aksamlar';
} else 
if($saat >= 20 && $saat <= 23){
    $message = 'İyi geceler';
}

echo $message;

?>