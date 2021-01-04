use strict;
use warnings;
use File::Basename;
use List::Util qw/shuffle/;

my $o = (dirname $0) . '/../output/wu/09.txt';

sub sw {
  my $r;
  $r .= (substr $_[0], $_ - 1, 1) foreach shuffle (1 .. length $_[0]);
  return $r;
}

sub typoglycemia {
  my @ws = split /\ /, $_[0];
  my @r;
  foreach (@ws) {
    my $w = $_;
    if (length $w > 4) {
      my $w0 = substr $w, 0, 1;
      my $w1 = sw (substr $w, 1, (length $w) - 2);
      my $w2 = substr $w, -1, 1;
      $w = $w0 . $w1 . $w2;
    }
    push @r, $w;
  }
  return join ' ', @r;
}

sub main {
  print 'Solving Q09 ... ';

  srand 42;
  my $s = "I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind";
  my $r = typoglycemia $s;

  open my $f, '>', $o; print $f $r; close $f;

  print "Done.\n";
}

main
