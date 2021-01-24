import time

# A List of Items
items = list(range(0, 100))

prefix = "Downloading:"
printEnd = "\r"
fill = "█"
decimals = 1

for i, item in enumerate(items):
    time.sleep(0.1)
    percent = ("{0:." + str(decimals) + "f}").format(100 * ((i) / float(len(items))))
    filledLength = int((50 * (i+1)) // 100)
    bar = fill * filledLength + '-' * (50- filledLength)
    print(f'\r{prefix} |{bar}| {percent}%', end = printEnd)