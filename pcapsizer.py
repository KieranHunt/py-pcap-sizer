import pcapy
import sys

reader = pcapy.open_offline(sys.argv[1])

count = 0

while True:
    if count >= int(sys.argv[2]):
        break
    try:
        (header, payload) = reader.next()
	print(str(count) + "," + str(header.getlen()))
    except pcapy.PcapError:
        break
    count+=1
