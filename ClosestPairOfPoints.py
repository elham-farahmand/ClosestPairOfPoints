#Elham Farahmand

import math

#The output is indices of pairs of points that are closest of all to each other.
def ClosestPairOfPoints(t):


    def xSort(t):
    	
        return [l for (l,v) in sorted(enumerate(t), key = lambda p: p[1][0])]


    def ySort(t):
    	
        return [l for (l,v) in sorted(enumerate(t), key = lambda p: p[1][1])]


    iX = xSort(t)
    iY = ySort(t)


    def DistanceOfPoints(i,j):
    	
        dx = i[0] - j[0]
        dy = i[1] - j[1]
        
        return dx*dx + dy*dy


    def SearchPoints(i,j):   
	     
        if j<=i:
            return None
            
        elif 1+i==j:
            return (iX[i], iX[j])
            
        else: 
            q = (i+j) // 2
            start = SearchPoints(i, q)
            end = SearchPoints(q+1, j)

            if start is None:
                (iMin, jMin) = end
                
            elif end is None:
                (iMin, jMin) = start
                
            else:
                (iStart, jStart) = start
                (iEnd, jEnd) = end
                dStart = DistanceOfPoints(t[iStart], t[jStart])
                dEnd = DistanceOfPoints(t[iEnd], t[jEnd])
                
                if dStart < dEnd:
                    (iMin, jMin) = (iStart, jStart)
                    
                else:
                    (iMin, jMin) = (iEnd, jEnd)

            d = DistanceOfPoints(t[iMin], t[jMin])
            x = (t[iX[q]][0] + t[iX[q + 1]][0]) / 2
            a = [j for j in iY if abs(t[j][0] - x) <= d]

            for w in range(len(a)):
                z = w + 1
                
                while z < len(a) and (t[iY[z]][1] - t[iY[w]][1]) < d and z - w <= 6:
                    g = DistanceOfPoints(t[iY[w]], t[iY[z]])
                    
                    if g < d:
                        d = g
                        iMin = w
                        jMin = z
                        
                    z = z + 1                  
            return (iMin, jMin)

    return SearchPoints(0, len(t) - 1)


print(ClosestPairOfPoints([(2, 3), (2, 4), (10, 20)]))
print(ClosestPairOfPoints([(1, 2)]))
print(ClosestPairOfPoints([(-567, -31), (-444, -1), (-321, -16), (-84, -50), (-1, 9), (0, 0), (2, 9), (36, 7), (264, 27), (391, 239)]))
print(ClosestPairOfPoints([(2, 6),(8, 2),(3, 6),(11, 15),(13, 7)]))
print(ClosestPairOfPoints([]))
print(ClosestPairOfPoints([(5, 9), (7, 8)]))
print(ClosestPairOfPoints([(0, 3),(5, 10),(4, 4),(7, 4),(9, 7),(10, 8),(20, 11),(19, 3),(1, 9)]))
print(ClosestPairOfPoints([(63, 19), (5, 9), (78, 39), (5, 9)]))

