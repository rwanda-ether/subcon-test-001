all:
	git log|grep commit |grep -v initial| tee log.txt
