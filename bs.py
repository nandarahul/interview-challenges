
import sys
line = sys.stdin.readline()

filter_start = False
all_requests, filters, request = [], [], []
request_count = 0
while line:
    if line == "\n":
        line = sys.stdin.readline()
        continue
    line = line[:-1]
    if line.startswith("Started"):
        all_requests.append(request)
        request = []
    if line == "***************###############***************":
        all_requests.append(request)
        filter_start=True
        line = sys.stdin.readline()
        line = line[:-1]
    if filter_start:
        filters.append(line)
    else:
        request.append(line)
    line = sys.stdin.readline()

all_requests = all_requests[1:]
result = [0, 0, 0, 0, 0]

for nrequest in all_requests:
    # Filter 1
    words = nrequest[0].split()
    if words[1] == filters[0]:
        result[0] += 1
    # Filter 2
    if words[2].strip('"') == filters[1]:
        result[1] += 1
    #Filter 3
    if words[4] == filters[2]:
        result[2] += 1
    #Filter 4
    words = nrequest[1].split()
    if words[0] == "Processing":
        if len(words) == 5:
            if words[4] == filters[3]:
                result[3] += 1
            elif words[4] == "HTML" and (filters[3] == "null" or filters[3] == "blank"):
                result[3] += 1
        elif len(words) == 4 and filters[3] in ["null","blank","HTML"]:
            result[3] += 1
    #Filter 5
    if nrequest[-1].startswith("Completed"):
        if filters[4] in nrequest[-1]:
            result[4] += 1


for r in result:
    print r

