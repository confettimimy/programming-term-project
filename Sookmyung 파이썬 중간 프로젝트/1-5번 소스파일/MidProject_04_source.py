# MidProject_04_source.py
# IT공학과 1614000 박미현



OUT = 0
IN = 1
wordflag = OUT
nch = nword = nline = 0


infilename = input("파일 이름을 입력하세요: ")
infile = open(infilename, "r")
filecontents = infile.read()


for c in filecontents:
    nch += 1
    if(c == '\n'): nline += 1
    if((c != ' ') and (c != '\n') and (c != '\t') and (wordflag == OUT)):
        wordflag = IN
        nword += 1
    if((c == ' ') or (c == '\n') or (c == '\t') and (wordflag == IN)):
        wordflag = OUT


print("Input has %d characters, %d words, and %d lines." %(nch, nword, nline));
        
