use strict;
use warnings;
use File::Basename;

my $o = (dirname $0) . '/../output/wu/00.txt';

sub main {
  print 'Solving Q00 ... ';

  my $s = 'stressed';
  my $r = reverse $s;

  open my $f, '>', $o; print $f $r; close $f;

  print "Done.\n";
}

main
