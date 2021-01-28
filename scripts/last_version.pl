#!/usr/bin/env perl
use 5.012;
#use JSON::PP;

my ($package, $channel) = @ARGV;

$channel = 'bioconda' unless ($channel);
my $uri = 'https://api.anaconda.org';
my $version_string = `curl --silent -X GET --header 'Accept: application/json' '$uri/package/$channel/$package'| grep latest_version | cut -f4 -d\\"`;
if ($?) {
  die " ERROR retrieving JSON from conda.\n";
} else {
  print $version_string;
}
