#!/usr/bin/env gnuplot
#Time-stamp: <Mon Oct 22 12:02:38 JST 2018 hamada>


set y2tics
set xlabel "commit"

set log y
set log y2
set ylabel "balance [JPY]"
set y2label "X(n) [JPY]"
set key left top box lt 3 lw 1 
set grid

plot "plotdata.log" u 1:4 axis x1y1 w lp lt 1 title "balance [JPY]", \
     "plotdata.log" u 1:2 axis x1y2 w lp lt 2 title "X(n) [JPY]"

pause -1

set term tgif
set output "tgif.obj"
replot

set term gif
set output "img.gif"
replot
