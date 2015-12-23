import os

count = 0
total = 0
inFile = open('content.csv', 'r')
chapter = inFile.readline()
OUTPUT = os.path.join(os.path.dirname(os.path.realpath(__file__)),"OUT/")
while (chapter):
   if chapter.startswith("chapter"):
       print(chapter)
       pagedir = OUTPUT+"chapter"+str(count+1)+"/"
       os.makedirs(pagedir)   
       count = count+1
       
   else:
       filename = pagedir+chapter+".txt"
       open(filename,'a')               
       
       
   chapter = inFile.readline()   

print("Total chapters: " + str(count))
