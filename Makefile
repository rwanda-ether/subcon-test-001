#Time-stamp: <Sun Oct 21 23:44:52 JST 2018 hamada>

all:
	git log|grep commit |grep -v initial| tee log.txt
	./calc.py |tee Estimations.md
