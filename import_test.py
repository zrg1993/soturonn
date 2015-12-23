import rake
if True:
    f = open("result_pdf.txt",'r')
    
    text = f.read()
    
    rake = rake.Rake("SmartStoplist.txt")
    keywords = rake.run(text)
    f.close()
    print("keyword word_score")
    for keyword in keywords:  
        
        print keyword[0],keyword[1]
