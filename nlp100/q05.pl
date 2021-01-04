use strict;
use warnings;
use File::Basename;

my $o = (dirname $0) . '/../output/wu/05.txt';

sub words {
  my $s = shift;
  $s =~ s/[,\.]//g;
  return split /\ /, $s;
}

sub ngram {
  my ($s, $n) = @_;
  my @w = words $s;
  my @r;
  push @r, join ' ', @w[$_ .. ($_ + $n - 1)] foreach (0 .. ~~@w - $n);
  return @r;
}

sub main {
  print 'Solving Q05 ... ';

  my $s = 'I am an NLPer';
  my @r = ngram $s, 2;

  open my $f, '>', $o; print $f (join "\n", @r); close $f;

  print "Done.\n";
}

main
