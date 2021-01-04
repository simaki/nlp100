use strict;
use warnings;
use File::Basename;

my $o = (dirname $0) . '/../output/wu/07.txt';

sub fmt {
  return $_[1] . ' is ' . $_[2] . ' at ' . $_[0];
}

sub main {
  print 'Solving Q07 ... ';

  my $x = 12;
  my $y = 'temperature';
  my $z = 22.4;
  my $r = fmt $x, $y, $z;

  open my $f, '>', $o; print $f $r; close $f;

  print "Done.\n";
}

main
