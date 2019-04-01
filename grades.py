
class Grades:
    
    def __init__(self,min_val,max_val):
        self.rounding = 2
        self.grades = [ 1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0, 5.0 ]
        self.levels = [ max_val ]
        d = (max_val - min_val) / 9
        
        for i in range(1,len(self.grades)-2):
            self.levels.append( self.levels[i-1] - d )
        self.levels.append(min_val) # 4.0
        self.levels.append(0.0)   # 5.0
        
        for i in range(0,len(self.levels)-1):
            self.levels[i] = round(self.levels[i],self.rounding)
            
    def worst(self):
        return self.grades[-1]

    def lookup(self,p):
        p = round(p,self.rounding)
        # print('p',p)
        for i in range(0,len(self.levels)):
            # print('i',i,'p',p,'l',self.levels[i])
            if p >= self.levels[i]:
                return self.grades[i]

if __name__ == "__main__":
    g = Grades(0.40,0.95)
    print(g.grades)
    print(g.levels)
        
    print(g.lookup(0.81293))
    print(g.lookup(0.3999))
    print(g.lookup(0.4001))
    print(g.lookup(0.39))
    print(g.lookup(0.71))
    
    