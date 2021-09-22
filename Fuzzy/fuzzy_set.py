from matplotlib import pyplot as plt

class FuzzySet: #interface
    def get_fuzzy_value(self,val):
        pass

    def draw(self,fig=None,number_of_points=100):
        if fig is None:
            fig = plt.figure(self.label)
        vals=[]
        x=[]
        step=(self.right-self.left)/number_of_points
        current_x=self.left
        for _ in range(number_of_points+1):
            x.append(current_x)
            vals.append(self.get_fuzzy_value(current_x))
            current_x+=step
        plt.plot(x,vals)
        plt.text(self.centroid,1.02,self.label,ha='center')


class FuzzySetTringular(FuzzySet):
    def __init__(self,label,points):
        self.label=label
        self.left=points[0]
        self.middle = points[1]
        self.right = points[2]
        self.centroid = sum(points)/3

    def get_fuzzy_value(self,val):
        return min([max((val-self.left)/(self.middle-self.left),0),
                    max(1-(val-self.middle)/(self.right-self.middle),0),
                    1])

class FuzzySetTringularSymetric(FuzzySetTringular):
    def __init__(self,label,points):
        self.label=label
        self.left=points[0]
        self.middle = (points[0]+points[1])/2
        self.right = points[1]
        self.centroid = self.middle


