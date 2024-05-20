import matplotlib.pyplot as plt
class Point2D:
    "A class representing a 2D point with x and y coordinates."
    def __init__(self , x , y):
        "Initialise the point object with the given x and y coordinates"
        self.x = x
        self.y = y
    def translate(self,dx ,dy):
        "Translates the point by dx units in x-direction and dy in y-direction"
        self.x +=dx
        self.y +=dy

    def __str__(self):
        "Returns a string representation of the point"
        return f"({self.x} , {self.y})"
    def plot(self,color ='green'):
        "Plots the point on a scatterplot with given color "
        plt.scatter(self.x , self.y , color=color ,marker="v")

