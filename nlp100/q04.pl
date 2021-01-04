use strict;
use warnings;
use File::Basename;

my $o = (dirname $0) . '/../output/wu/04.txt';

sub words {
  my $s = shift;
  $s =~ s/[,\.]//g;
  return split /\ /, $s;
}

sub main {
  print 'Solving Q04 ... ';

  my $s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.';
  my @n = (2) x 20;
  @n[0, 4, 5, 6, 7, 8, 14, 15, 18] = (1) x 9;
  my @w = words $s;
  my @r;
  push @r, (substr $w[$_], 0, $n[$_]) foreach (0 .. ~~@w - 1);

  open my $f, '>', $o; print $f (join ' ', @r); close $f;

  print "Done.\n";
}

main
