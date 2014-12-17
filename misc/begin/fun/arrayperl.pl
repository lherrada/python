#!/usr/bin/perl


my @array=("Luis","Silvia");

foreach $i (@array) {
print $i."\n";
}


$myhash={"luis"=>37,"silvia"=>36};

foreach $key (keys(%$myhash)){
print "$key: $myhash->{$key}\n"
}

