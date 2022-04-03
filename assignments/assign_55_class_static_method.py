# Assignment: 55
# Write a program to calculate the area of a Circle.
# Circle diameter and measurement metric (‘ft’, ‘inch’, ‘cm’; only these
# three are allowed) will be passed to initialize the object.
# Write an instance method to calculate the area of the circle.
# Only inches will be used for area calculation, write a static method to
# convert the diameter into inches before calculating the area.
# Use three class variables and a class method to maintain count of the circles as per the area.
# If the area is less than 10, add to small; if between 11 to 15, add to medium;
# if greater than 15, add to large.
import math


class CalCircleArea:

    # Class variables to hold count of circles as per size
    small_circles = 0
    medium_circles = 0
    large_circles = 0
    valid_metric_list = ["ft", "inch", "cm"]

    def __init__(self, diameter, metric):
        self.diameter = diameter
        self.metric = metric
        # Validate the metric, if it is not one of inch or ft or cm
        # raise ValueError
        if self.metric not in CalCircleArea.valid_metric_list:
            raise ValueError("Invalid metric.")

    def calc_area(self):
        # Before calculating the area, convert the metric to inches
        if not self.metric == "inch":
            self.diameter = CalCircleArea.conv_metric(self.diameter, self.metric)

        area = math.pi * (self.diameter/1) * (self.diameter/2)
        CalCircleArea.count_circles(area)

        return area

    @staticmethod
    def conv_metric(dia, met):
        dia_inch = 0
        if met == "ft":
            dia_inch = dia * 12
        elif met == "cm":
            dia_inch = dia * 0.393701

        return dia_inch

    @classmethod
    def count_circles(cls, area):
        if area < 10:
            cls.small_circles = cls.small_circles + 1
        elif area >= 11 and area <= 15:
            cls.medium_circles = cls.medium_circles + 1
        else:
            cls.large_circles = cls.large_circles + 1

    @classmethod
    def display_circles_count(cls):
        print("Number of small circles: ", cls.small_circles)
        print("Number of medium circles: ", cls.medium_circles)
        print("Number of large circles: ", cls.large_circles)


c1_area = CalCircleArea(10, "inch")
print("Area of the circle: ", c1_area.calc_area())

c2_area = CalCircleArea(0.25, "ft")
print("Area of the circle: ", c2_area.calc_area())

c3_area = CalCircleArea(1, "cm")
print("Area of the circle: ", c3_area.calc_area())

CalCircleArea.display_circles_count()

# Below will throw exception
c1_area = CalCircleArea(10, "m")
