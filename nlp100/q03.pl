use strict;
use warnings;
use File::Basename;

my $o = (dirname $0) . '/../output/wu/03.txt';

sub words {
  my $s = shift;
  $s =~ s/[,\.]//g;
  return split /\ /, $s;
}

sub main {
  print 'Solving Q03 ... ';

  my $s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.';
  my @r = map length, words $s;

  open my $f, '>', $o; print $f (join ' ', @r); close $f;

  print "Done.\n";
}

main
