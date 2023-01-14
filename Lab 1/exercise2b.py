file = open("earthquake.txt") # Opening the file
read_lines = file.readlines() # Reads the lines from the file
file.close() # Closes the file because we've already read the lines

earthquake_results = [] # list to store the results of the earthquakes 

for i in range(len(read_lines)): # Looping through every line in .txt file
    found = False
    split = read_lines[i].split() # splits the line
    information = []
    information.append(split[1])
    information.append(split[0])
    
    for j in range(len(earthquake_results)):
        if earthquake_results[j][0] == split[len(split) - 1]:
            earthquake_results[j].append(information)
            found = True
            break
        if found == False:
            region = []
            region.append(split[len(split) - 1])
            region.append(information)
            earthquake_results.append(region)
new_file = open("earthquakefmt.txt", "w")
for i in range(len(earthquake_results)):
    new_file.write(str(earthquake_results[i]))
    new_file.wrute("\n")

new_file.close()


