# Support Vector Machines (SVM)

Works by creating a "Hyperplane". A hyperplane divides data by using anything that is linear.
> Hyperplane = distance between two closest points from the OPPOSITE class, distance between them and common line is the same.

Therefore we can generate an infinite amount of hyperplanes, but we must find the best

---

## Margins

The margin is the area where there are no other points. We want the distance to the margin to be large as possible, therefore we:
 + separate our datapoints/classes
 + make more accurate predictions

### Soft/Hard Margin
> Soft margin is when a few outliers exist inside the margin.

> Hard margin is when points don't exist within the margin
---

## Kernals (3 Dimensional)

Turns data into a form where we can draw an accurate hyperplane. A kernal is function that take input **f(x1, x2)** and outputs **x3** (a higher dimension/coordinate).
 + By generating a third point, we can divide our data and draw a hyperplane
 + We add a dimension, to allow more accurate classification
> If there is still no way to draw a hyperplane then we reapeat the process and add another 4th dimension with the function
An example of a kernal is (x1)^2 + (x2)^2 = x3

---
