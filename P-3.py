class ArrayStack:
    
    def __init__(self,capacity):
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.top = -1
        
    def isEmpty(self):
        return self.top == -1
    
    def isFull( self ):
        return self.top == self.capacity-1
    
    def push(self,e):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = e
        else: pass
        
    def pop (self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]
        else: pass
    
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:pass
    
def isValidPos(x,y,map):
    MAZE_SIZE = len(map)
    if 0<= x < MAZE_SIZE and 0<= y < MAZE_SIZE:
        if map[y][x] == '0' or map[y][x] == 'x':
            return True
    return False
    
    


def DFS(map):
    print('DFS: ')
    stack= ArrayStack(100)
    stack.push((0,1))
    move=0
    while not stack.isEmpty():
        here = stack.pop()
        print(here,end='')
        (x,y)=here
        
        if(map[y][x]=='x'):
            print(f'이동 거리={move}')
            return True
        else:
            map[y][x] ='.'
            move +=1
            if isValidPos(x,y-1,map): stack.push((x,y-1))
            if isValidPos(x,y+1,map): stack.push((x,y+1))
            if isValidPos(x-1,y,map): stack.push((x-1,y))
            if isValidPos(x+1,y,map): stack.push((x+1,y))
        print(f'현재 스택:{stack}')
        
    return False

map = [
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['e', '0', '0', '0', '0', '0', '1', '0', '0', '1'],
    ['1', '0', '1', '1', '1', '0', '1', '1', '0', '1'],
    ['1', '0', '0', '0', '1', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '0', '1', '1', '1', '1', '0', '1'],
    ['1', '0', '1', '0', '0', '0', '0', '1', '0', 'x'],
    ['1', '0', '1', '1', '1', '1', '0', '1', '1', '1'],
    ['1', '0', '0', '0', '0', '1', '0', '0', '0', '1'],
    ['1', '1', '1', '1', '0', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
]

DFS(map)