import csv
from task2_class import Point2D
import matplotlib.pyplot as plt
def read_coordinates_from_file():
    "Read x , y coordinates from a csv file and returns a list of point objects"
    points = []
    with open("coordinate_file.csv" , "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            x =float (row[0])
            y = float(row[1])
            points.append(Point2D(x ,y))
        plt.style.use('dark_background')
        return points
def plot_points(points, color="green"):
    "Plot a list of Point objects on a scatter with given color."
    for point in points:
        point.plot(color=color)

def translate_points(points , dx , dy):
    "Translates a list of Point objects by dx units in x-diection and dy units in y-direction "
    for point in points:
        point.translate(dx , dy)



# Read points from file

points = read_coordinates_from_file()

#plots original points in blue

plot_points(points)
#translate points by dx =3 and dy = 4

translate_points(points , dx =3 , dy = 4)

#replot translated points in red
plot_points(points , color="red")

#Shows the plot
plt.xlabel("x-coordinates")
plt.style.use('dark_background')
plt.ylabel("y-coordinates")
plt.title("Coordinates of 2D Points")
plt.grid(True)
plt.show()
