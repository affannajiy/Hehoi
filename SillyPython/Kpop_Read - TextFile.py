#Read Kpop Members in text files

#Open the text file: open("filename", "mode")
print("Reading All TXT Info")
txt = open("Kpop_TXTInfo.txt", "r")
print(txt.read())

#Read parts of the text file
print("\nReading Part of TXT Info")
txt = open("Kpop_TXTInfo.txt", "r")
print(txt.read(37))

#Close the text file
print("\nClosing TXT Info....")
txt.close()