def valid_pos(x,y):

    if 0 <= x < 8 and 0 <= y < 8:
        return True
    else:
        return False
    
def solution(pos):
    x, y = int(ord(pos[0]) - ord("a")), int(pos[1])-1
    
    counter = 0
    traj = ["RRU", "RRD", "RLU", "RLD", "LLU", "LLD", "LRU", "LRD", "UUR", "UUL", "UDR", "UDL", "DUR", "DUL", "DDR", "DDL"]
    dir_dict = {
        "R": [0, 1],
        "L": [0, -1],
        "U": [-1, 0],
        "D": [1, 0]
    }

    for dir in traj:
        for i, d in enumerate(dir): 
            dy, dx = dir_dict[d]
            new_x, new_y = x+dx, y+dy

            if not valid_pos(new_x, new_y):
                break
        else:
            counter += 1
    
    return counter

if __name__ == "__main__":
    answer = solution("a1")
    print(answer)
