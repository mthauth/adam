all:
	pyuic4 ressources/adamwindow.ui -o adamwindow.py

clean:
	rm adamwindow.py*
	find . -name "*.pyc" -exec rm {} \;
