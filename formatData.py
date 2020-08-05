import os
import sys
import fileinput

def directorySelect():
    #if arguments are provided in command line, use first one as target directory, else use current directory
    currentDirectory = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    if len(sys.argv) > 1:
        inputDirectory = sys.argv[1]
        #check to make sure input is valid before formatting
        if os.path.isdir(inputDirectory):
            formatDirectory(inputDirectory)
        else:
            print("Invalid Directory")
    else:
        print('No directory provided, formatting current directory')
        formatDirectory(currentDirectory)

def formatDirectory(targetDir):
    #gets Directory, and makes each file in it(except this python script) available for stripWhiteSpace function
    print('Formatting files in Folder:' + targetDir)
    for filename in os.listdir(targetDir):
        if filename != os.path.basename(__file__) and filename.endswith('.txt'):
            stripWhiteSpace(targetDir,filename)

def stripWhiteSpace(location,filename):
    #open file, check to make sure it starts with EASI , else don't change file(reprint directly without changes)
    currentFile = fileinput.input(location+"/"+filename,inplace=True)
    skipFile = False
    for idx,line in enumerate(currentFile):
        if skipFile == True:
            print(line, end = '')
            continue
        if idx==0:
            if not("EASI" in line):
                skipFile = True
        #if line has leading spaces, continue to skip,(deletes line) else delete just trailing spaces. if EASX inline, its the last line dont print newline after last line.
        if (line[0].isspace()):
            continue
        noSpaceTrail = line.rstrip()
        #last line has extra endline (new blank line on bottom) without the code below:
        last_line = False
        if "EASX" in line:
            last_line = True
        if last_line:
            print(noSpaceTrail, end = '')
        else:
            print(noSpaceTrail)

def main():
    directorySelect()

if __name__ == "__main__":
    main()
