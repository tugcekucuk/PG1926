
<?php
$float para=0;
	int birlira=0, ellikurus=0, yirmibeskurus=0, onkurus=0, beskurus=0, birkurus=0;
	
	echo f(" Para miktarini TL olarak giriniz : "); /**/ scanf("%f", &para);
	
	$birlira = para/1;
	$para -= 1*birlira;
	
	$ellikurus = para/0.5;
	$para -= 0.5*ellikurus;
	
	$yirmibeskurus = para/0.25;
	$para -= 0.25*yirmibeskurus;
	
	$onkurus = para/0.1;
	$para -= 0.1*onkurus;
	
	$beskurus = para/0.05;
	$para -= 0.05*beskurus;
	
	$birkurus = para/0.01;
	$para -= 0.01*birkurus;
	
	
	echo f("\n%s%d adet\n%s%d adet\n%s%d adet\n%s%d adet\n%s%d adet\n%s%d adet\n%s%d adet\n\n",
			"- 1 TL : ", birlira,
			"- 0.5 TL : ", ellikurus,
			"- 0.25 TL : ", yirmibeskurus,
			"- 0.10 TL : ", onkurus,
			"- 0.05 TL : ", beskurus,
			"- 0.01 TL : ", birkurus,;
	
	system("PAUSE");
	return 0;	
?>