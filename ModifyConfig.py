class HeaderUpdate :
    def __init__(self, filePath, insertAfter, linesToInsert):
        self.filePath = filePath
        self.insertAfter = insertAfter
        self.linesToInsert = linesToInsert

def parseHeadConfigurationFile():
    file = open("Configuration.txt", "r")
    lines = file.readlines()
    i = 0
    finished = False

    directory = ""
    files = []
    insertAfter = -1
    linesToAdd = []
    headerUpdates = []

    while not finished:
        if lines[i].startswith("//"):
            continue

        if lines[i].startswith("main dir"):
            directory = lines[i+1].strip()
            i += 1

        if lines[i].startswith("header"):  #adding headers
            while not lines[i].startswith("end"):
                if lines[i].startswith("files"):
                    i += 1
                    while len(lines[i].strip()) > 0:
                        files.append(lines[i].strip())
                        i += 1

                if lines[i].startswith("insert after line"):
                    insertAfter = int(lines[i+1])
                    i += 1

                if lines[i].startswith("lines to insert"):
                    i += 1
                    while len(lines[i].strip()) > 0:
                        linesToAdd.append(lines[i])
                        i += 1

                    # Create HeaderUpdateObjects
                    for f in files:
                        headerUpdates.append(HeaderUpdate(directory + f, insertAfter, linesToAdd))

                    files = []
                    insertAfter = -1
                    linesToAdd = []

                i += 1

            finished = True

        i += 1

    file.close()

    return headerUpdates
