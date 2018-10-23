#!/usr/bin/env gnuplot
#Time-stamp: <Mon Oct 22 12:24:15 JST 2018 hamada>

# graph1 -----------------
set y2tics
set xlabel "commit"

set log y
#set log y2
set ylabel "balance [JPY]"
set y2label "client's budget [JPY]"
set key left top box lt 3 lw 1 
set grid

plot "plotdata.log" u 1:4 axis x1y1 w lp lt 1 title "balance [JPY]", \
     "plotdata.log" u 1:5 axis x1y2 w lp lt 2 title "client's budget [JPY]"

pause -1

set term gif
set output "graph1.gif"
replot

# graph2 -----------------
set log y
set log y2
set ylabel "balance [JPY]"
set y2label "X(n) [JPY]"
set key left top box lt 3 lw 1 
set grid

plot "plotdata.log" u 1:4 axis x1y1 w lp lt 1 title "balance [JPY]", \
     "plotdata.log" u 1:2 axis x1y2 w lp lt 2 title "X(n) [JPY]"

set term gif
set output "graph2.gif"
replot

# graph3 -----------------
set log y
unset log y2
set ylabel "X(n) [JPY]"
set y2label "C(n)"
set key left top box lt 3 lw 1 
set grid
set y2range [1.0:4.0]

plot "plotdata.log" u 1:2 axis x1y1 w lp lt 1 title "X(n) [JPY]", \
     "plotdata.log" u 1:3 axis x1y2 w lp lt 2 title "C(n)"

set term gif
set output "graph3.gif"
replot

