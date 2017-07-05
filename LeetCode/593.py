class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        def dist(p1,p2):
            return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

        d1 = dist(p1,p2)
        d2 = dist(p1,p3)
        d3 = dist(p1,p4)
        if (p1==p2==p3==p4):
            return False                       
        if (d1==d2 and d2*2==d3):           
            if (dist(p4,p2)==dist(p4,p3)):                
                return True
        if (d2==d3 and d3*2==d1):            
            if (dist(p4,p2)==dist(p2,p3)):               
                return True
        if (d3==d1 and d1*2==d2):            `
            if (dist(p4,p3)==dist(p2,p3)):                
                return True 
        return False

# NEVER USE under root for distance, just keep everything in square. 2^(0.5) makes things very very difficult with the extra precision
# ALWAYS DRAW THE FIGURE AND DESGIN THE ALGORITHM
# Reference : http://www.geeksforgeeks.org/check-given-four-points-form-square/


# ALternative solution using itertools
# class Solution(object):
# def validSquare(self, p1, p2, p3, p4):
#     def D((P, Q)):
#         return (P[0] - Q[0]) ** 2 + (P[1] - Q[1]) ** 2
#     S = set(map(D, itertools.combinations((p1, p2, p3, p4), 2)))
#     return len(S) == 2 and 0 not in S