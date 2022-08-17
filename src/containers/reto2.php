<?php
$n1=0;
$n2=1;

echo $n1;

for ($i=0;$i<50;$i++) {
	$var=$n1;
	$n1=$n2;
	$n2=$var + $n1;
	
	echo $n1;
}