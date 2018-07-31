my @col = split( /,/, $line ); # CSV
$count{$col[0]} += $col[1]; # Somme pour fusionner les doublons entre fichiers

while (my ($key,$count) = each %count) {
    print {$file2} "$key,$count";  # CSV (pas de tri)
}