#Time-stamp: <Mon Oct 22 00:03:58 JST 2018 hamada>

all:
	git log|grep commit |grep -v initial| tee log.txt
	./simulator.py |tee Estimations.md
