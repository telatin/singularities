#!/usr/bin/env perl
use 5.012;
use FindBin qw($RealBin);
my $template = shift @ARGV;

die "USAGE:
  templater.pl TemplateFile Var=Value  V2=Value2...

Template not found.\n" if (! -e "$template");


# Get all the var=value pairs
my %values = ();

for (my $i = 0; $i <= $#ARGV; $i++) {
  my ($var, $value) = split /=/, $ARGV[$i];
  die "Syntax error: expecting var=value\n" unless ($value);
  say STDERR "$var=$value";
  $values{$var} = $value;
}

# Autoselect template: if the user supplies package=NAME *and* ./templates/NAME.tmp exists:
if (-e "$RealBin/templates/$values{package}.tmp") {
 print STDERR " * Using custom template $RealBin/templates/$values{package}.tmp\n";
 $template =  "$RealBin/templates/$values{'package'}.tmp";
}


my $template = load_template($template);
say $template;


sub load_template {
 my $file = shift @_;
 open(my $i, '<', "$file") || die "Unable to open file: $file\n";
 while (my $line = readline($i) ) {
  while ($line =~/{(\w+)}/g) {
   my $t = $1;
   say STDERR "WARNING <template_requires> $1";
   if ($values{$t}) {
      $line =~s/{$t}/$values{$t}/g;
   }
  }
  $template .= $line;


 }
 return ($template);
}
