#!/usr/bin/perl

use utf8;
use strict;
use warnings;
use Term::ProgressBar; # Facultatif : affiche une barre d'état (*)
 
open( my $file, '<:utf8', $ARGV[0] ) or die( "Impossible d'ouvrir le fichier $ARGV[0]" );

my $num_lines = ( stat $file )[7]; # (*)
my ( $compteur_modif, $progress_byte, $next_update ) = ( 0, 0, 0 ); 
my $progress = Term::ProgressBar->new( 
    {   name  => "[Lecture] ", 
        count => $num_lines, 
        ETA   => 'linear', 
    } 
);

my %count; # Table de hachage
 
readfile:while ( my $line = <$file> ) {
 
	$progress_byte += length($line); # (*)
    $next_update = $progress->update($progress_byte) if ( $progress_byte > $next_update && $progress_byte < $num_lines );
 
    $line = lc $line; # Minuscule
 
    my @col = split( /\t/, $line ); # TSV
  
    if ($col[0] !~ /[àa-z]/ or $col[0] =~ /[^a-z\s^àâçéèêëîïôùûüÿæœ]|[\^]|(.)(\1{2,})|\b([b-zâçéèêëîïôùûüÿæœ])\b(\1{0,})/g or $col[1] =~ /\b1/) {
        next readfile;
    }
 
    $count{$col[0]} += $col[2]; # Somme pour fusionner les doublons
}
 
close( $file );
 
$\ = "\n";
open( my $file2, '>:utf8', $ARGV[1] ) or die( "Impossible d'ouvrir le fichier $ARGV[1]" );
print {$file2} (join ',', ($_, $count{$_})) for sort keys %count;  # CSV (+ tri)
close( $file2 );

$progress->update($num_lines) if $num_lines >= $next_update; print "\n"; # (*)