use strict;
use warnings;
use File::Basename;

my $ou = (dirname $0) . '/../output/wu/06_u.txt';
my $os = (dirname $0) . '/../output/wu/06_s.txt';
my $od = (dirname $0) . '/../output/wu/06_d.txt';
my $ox = (dirname $0) . '/../output/wu/06_x.txt';
my $oy = (dirname $0) . '/../output/wu/06_y.txt';

sub letter_ngram {
  my ($s, $n) = @_;
  my @r;
  push @r, join '', substr $s, $_, $n foreach (0 .. (length $s) - $n);
  return @r;
}

sub uni {
  my @a = @{$_[0]};
  my @b = @{$_[1]};
  my %r = ();
  $r{$_} = 1 foreach @a;
  $r{$_} = 1 foreach @b;
  return sort keys %r
}

sub sec {
  my @a = @{$_[0]};
  my @b = @{$_[1]};
  my %r = ();
  my %in = ();
  $in{$_} = 1 foreach @a;
  foreach (@b) {
    if ($in{$_}) {$r{$_} = 1};
  }
  return sort keys %r
}

sub dif {
  my @a = @{$_[0]};
  my @b = @{$_[1]};
  my %r = ();
  $r{$_} = 1 foreach @a;
  delete $r{$_} foreach (@b);
  return sort keys %r
}

sub in {
  my $e = $_[0];
  my @a = @{$_[1]};
  my $r = '0';
  $r ||= ($_ eq $e) foreach @a;
  return $r;
}

sub main {
  print 'Solving Q06 ... ';

  my $s0 = 'paradise';
  my $s1 = 'paragraph';

  my @x = letter_ngram $s0, 2;
  my @y = letter_ngram $s1, 2;

  my @ru = uni \@x, \@y;
  my @rs = sec \@x, \@y;
  my @rd = dif \@x, \@y;
  my $ix = in 'se', \@x;
  my $iy = in 'se', \@y;

  my $f;
  open $f, '>', $ou; print $f join ' ', @ru; close $f;
  open $f, '>', $od; print $f join ' ', @rd; close $f;
  open $f, '>', $os; print $f join ' ', @rs; close $f;
  open $f, '>', $ox; print $f int $ix; close $f;
  open $f, '>', $oy; print $f int $iy; close $f;

  print "Done.\n";
}

main
