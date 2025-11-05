# Formula del area de Gauss (formula de cordon del zapato)

def xyz2area(xyz):
    n = len(xyz)
    area = 0
    for i in range(n):
        j = (i+1) % n
        area += xyz[i,0]*xyz[j,1]
        area -= xyz[j,0]*xyz[i,1]
    area = abs(area)/2
    return area