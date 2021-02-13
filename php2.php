<?php
$i=0; //Aranan sayi
$toplam=0; //Bulunan sayi adedi
while($toplam<=3) //Bulunacak sayi adedi -1
{
	$i++; // Aranan sayiyi arttir
	$itoplam=0;
	for($k=1;$k<$i;$k++) 
	{
		
		if($i  % $k == 0) //Sayi, sayinin tam b�lenimi
		{
			$itoplam+=$k; //B�l�nenlerin toplamina ekle
		}
	}
	if($itoplam==$i) //B�l�nenlerin toplami aranan sayiya esitmi
	{
		echo "$i <br />";
		$toplam++;//Arattirmarya devam ettirmek i�in sayaci arttir
	}
}
?>