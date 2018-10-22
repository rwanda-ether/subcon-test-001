#Time-stamp: <Mon Oct 22 13:13:43 JST 2018 hamada>

all:
	git log|grep commit |grep -v initial| tee log.txt
	./simulator.py |tee Estimations.md


install.gnuplot.macOS:
	brew install gnuplot --with-aquaterm --with-x11

plot:
	./plot.sh

clean:
	rm -rf *~ .*~

c: clean
