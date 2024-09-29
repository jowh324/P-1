import time

def hanoi_tower(n,fr,tmp,to):
    cnt=0
    
    if(n==1):
        print("원판 1:%s --> %s"%(fr,to))
        cnt=1
    else:
        cnt += hanoi_tower(n-1,fr,to,tmp)
        print("원판 %d: %s -->%s"%(n,fr,to))
        cnt += 1
        cnt += hanoi_tower(n-1,tmp,fr,to)
    return cnt
       
        
        
        
    
def main():
   
    n=int(input("최대 층수 입력"))
    start=time.time()
    move=hanoi_tower(n,'A','B','C')
    end=time.time()
    
    print(f'움직임 {move}')
    print(f'걸린 시간{end-start}')
    
main()