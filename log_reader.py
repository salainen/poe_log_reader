import time
from win10toast import ToastNotifier

# reading log file location from a config file:
with open('config.txt') as f:
	log_file = f.readlines()

# reading a list of maps from a file:
with open('list_of_maps.txt') as f:
	list_of_maps = f.read().splitlines()

# convert to string:
log_file_name = ''.join(log_file)

# init toasts
toaster = ToastNotifier()

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(1)
            continue
        yield line

if __name__ == '__main__':
    logfile = open(log_file_name,"r")
    loglines = follow(logfile)
    for line in loglines:
        if "You have entered" in line:
			for maps in list_of_maps:
				if maps in line:
					toaster.show_toast("WARNING!", "You just entered " + maps)
