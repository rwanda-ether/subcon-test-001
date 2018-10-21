#Time-stamp: <Sun Oct 21 23:39:18 JST 2018 hamada>

all:
	git log|grep commit |grep -v initial| tee log.txt
	./calc.py
