use strict;
use warnings;
use File::Basename;

my $oc = (dirname $0) . '/../output/wu/08_c.txt';
my $od = (dirname $0) . '/../output/wu/08_d.txt';

sub cifer_c {
  return chr (219 - ord $_[0]) if $_[0] =~ /[a-z]/;
}

sub cifer {
  my $r;
  $r .= cifer_c (substr $_[0], $_ - 1, 1) foreach (1 .. length $_[0]);
  return $r;
}

sub main {
  print 'Solving Q08 ... ';

  my $s = 'message';
  my $rc = cifer $s;
  my $rd = cifer cifer $s;

  my $f;
  open $f, '>', $oc; print $f $rc; close $f;
  open $f, '>', $od; print $f $rd; close $f;

  print "Done.\n";
}

main
