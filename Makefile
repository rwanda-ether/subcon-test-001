#Time-stamp: <Sun Oct 21 23:52:24 JST 2018 hamada>

all:
	git log|grep commit |grep -v initial| tee log.txt
	./simulation.py |tee Estimations.md
