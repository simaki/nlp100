use strict;
use warnings;
use File::Basename;

my $o = (dirname $0) . '/../output/wu/01.txt';

sub main {
  print 'Solving Q01 ... ';

  my $s = 'schooled';
  my $r;
  for (my $i = 0; $i < length $s; $i += 2) {
    $r .= substr $s, $i, 1;
  }

  open my $f, '>', $o; print $f $r; close $f;

  print "Done.\n";
}

main
