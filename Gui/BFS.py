from pyMaze import maze,agent,textLabel,COLOR
from collections import deque

def BFS(m,start=None):
    if start is None:
     start=(m.rows,m.cols)
    frontier = deque()
    frontier.append(start)
    bfsPath = {}
    explored = [start]
    bSearch=[]

    while len(frontier)>0:
        currCell=frontier.popleft()
        if currCell==m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = currCell
                bSearch.append(childCell)
                
    fwdPath={}
    cell=m._goal
    while cell!=(m.rows,m.cols):
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return bSearch,bfsPath,fwdPath

if __name__=='__main__':
    m=maze(20,20)
    m.CreateMaze(loopPercent=40)
    bSearch,bfsPath,fwdPath=BFS(m)
    a=agent(m,footprints=True,filled=False,shape='square',color=COLOR.green)
    b=agent(m,footprints=True,color=COLOR.red,shape='arrow',filled=False)
    c=agent(m,1,1,footprints=True,color=COLOR.cyan,shape='square',filled=True,goal=(m.rows,m.cols))
    l=textLabel(m,'length of the shortest path',len(bfsPath)+1)
    m.tracePath({a:bSearch},delay=200)
    m.tracePath({c:bfsPath},delay=200)
    m.tracePath({b:fwdPath},delay=200)
    
    m.run()