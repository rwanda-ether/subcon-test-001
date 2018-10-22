#Time-stamp: <Mon Oct 22 11:36:51 JST 2018 hamada>

all:
	git log|grep commit |grep -v initial| tee log.txt
	./simulator.py |tee Estimations.md


install.gnuplot.macOS:
	brew install gnuplot --with-aquaterm --with-x11

