#!/usr/bin/env gnuplot

set term tgif
set output "tgif.obj"

set log y
plot "plotdata.log" u 1:4 w po


