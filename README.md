conference
==========

Conference web-site


Before the django server can be run you need to set the path to the installation.

In code/pydata/pydata/settings.py add an entry to the ROOTS variable (if needed):

	ROOTS = {
	    'aws': '/home/pydata',
	    'trent_mac': '/Volumes/Development/continuum/pydata/conference.json/conference',
	    'trent_windows': '/Users/Trent/Documents/GitHub/conference',
	    'your_machine': '/Path/to/your/installation'
	}

change which path is the actual root path on the machine:

	ROOT_PATH = ROOTS['trent_mac']

