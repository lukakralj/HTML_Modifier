import ModifyConfig
import time


def modifyFileHeader(headerUpdate):
    print("Modifying file: " + headerUpdate.filePath + ".")
    file = open(headerUpdate.filePath, "r")
    lines = file.readlines()
    file.close()
    before = len(lines)
    insertAt = headerUpdate.insertAfter

    for line in headerUpdate.linesToInsert:
        lines.insert(insertAt, line)
        insertAt += 1

    print("Adding " + str(len(lines) - before) + " line(s).")
    file = open(headerUpdate.filePath, "w")
    file.writelines(lines)
    print("Modifying file finished.\n")
    file.close()


start = time.time()
print("Running HTML Modifier")
headerUpdates = ModifyConfig.parseHeadConfigurationFile()
for update in headerUpdates:
    modifyFileHeader(update)

print("Modifying ended in: {0: .3f} s.".format(time.time() - start))