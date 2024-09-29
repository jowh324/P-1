from ArrayList import ArrayList
import re
from collections import defaultdict

list = ArrayList()
while True:
    command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, m-단어빈도수, q-종료=>")
    
    if command =='i':
        pos = int(input(" 입력행 번호:"))
        str = input("입력행 내용:")
        list.insert(pos,str)
    
    elif command == 'd':
        pos = int(input(" 삭제행 번호"))
        list.delete(pos)
    
    elif command == 'r':
         pos = int(input(" 변경행 번호"))
         str = input("변경행 내용:")
         list.replace(list,pos,str)
    
    elif command == 'p':
       print("Line Editor")
       for i in range (list.size):
           print('[%2d]'%i, end='')
           print(list.getEntry(i))
       
        
    elif command == 'q': exit()
    
    elif command == 'l':
        filename= 'text.txt'
        infile = open(filename,"r")
        lines = infile.readlines();
        for line in lines:
            list.insert(list.size,line.rstrip('\n'))
        infile.close()
        
    elif command == 's':
        filename = 'text.txt'
        outfile = open(filename,'w')
        len = list.size
        for i in range(len):
            outfile.write(list.getEntry(i)+'\n')
        outfile.close()
        
    elif command == 'm':
      
      
       
       word_freq = defaultdict(int)
        
       for i in range(list.size):
            line1 = list.getEntry(i)
            line = re.sub(r'[^\w\s]', '', line1)
            words = line.split()  # 공백을 기준으로 단어 추출
            for word in words:
                word_freq[word] += 1
        
        
       print("단어 빈도수:")
       for word, freq in sorted(word_freq.items()):
            print(f'{word}: {freq}')
        
        
       with open('dic.txt', 'w') as dicfile:
            for word, freq in sorted(word_freq.items()):
                dicfile.write(f'{word}: {freq}\n')
       print("dic.txt에 저장")   
           
           

       
       
       
            
    