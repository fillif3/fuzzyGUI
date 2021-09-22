from matplotlib import pyplot as plt

from Fuzzy.utlis import getBoundsOfSet

class Universe:
    def __init__(self,fuzzy_sets,label):
        self.fuzzy_sets=fuzzy_sets
        self.label=label
        (self.left, self.right)=getBoundsOfSet(fuzzy_sets)

    def draw(self,fig = None,number_of_points=100):
        if fig is None:
            fig = plt.figure(self.label)
        for f in self.fuzzy_sets:
            f.draw(fig,number_of_points=number_of_points)
        plt.plot([self.left,self.right],[0,0],color='black')
        plt.plot([self.left,self.right],[1,1], color='black')





