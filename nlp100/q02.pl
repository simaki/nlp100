use strict;
use warnings;
use File::Basename;

my $o = (dirname $0) . '/../output/wu/02.txt';

sub main {
  print 'Solving Q02 ... ';

  my $s0 = 'shoe';
  my $s1 = 'cold';
  my $r;
  for my $i (0 .. length $s0) {
    $r .= substr $s0, $i, 1;
    $r .= substr $s1, $i, 1;
  }

  open my $f, '>', $o; print $f $r; close $f;

  print "Done.\n";
}

main
