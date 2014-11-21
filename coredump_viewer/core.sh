#!/bin/bash

#binimg=/home/lherrada/programming/C/coredump/coredump1
binimg=$1
core=$2

mydirname=`dirname $2`
#cd dirname
#cores=`find /tmp -name '*.core' -mtime -1`

  gdblogfile="$mydirname/gdb.txt"
  #gdblogfile="$core-gdb.log"
  #rm $gdblogfile
 
  bininfo=`ls -l $binimg`
  coreinfo=`ls -l $core`
 
gdb --batch-silent \
      -ex "set logging file $gdblogfile" \
      -ex "set logging on" \
      -ex "set pagination off" \
      -ex "printf \"**\n** Process info for $binimg - $core \n** Generated `date`\n\"" \
      -ex "printf \"**\n** $bininfo \n** $coreinfo\n**\n\"" \
      -ex "file $binimg" \
      -ex "core-file $core" \
      -ex "bt" \
      -ex "info proc" \
      -ex "printf \"*\n* Libraries \n*\n\"" \
      -ex "info sharedlib" \
      -ex "printf \"*\n* Memory map \n*\n\"" \
      -ex "info target" \
      -ex "printf \"*\n* Registers \n*\n\"" \
      -ex "info registers" \
      -ex "printf \"*\n* Current instructions \n*\n\"" -ex "x/16i \$pc" \
      -ex "printf \"*\n* Threads (full) \n*\n\"" \
      -ex "info threads" \
      -ex "bt" \
      -ex "thread apply all bt full" \
      -ex "printf \"*\n* Threads (basic) \n*\n\"" \
      -ex "info threads" \
      -ex "thread apply all bt" \
      -ex "printf \"*\n* Done \n*\n\"" \
      -ex "quit" 

