# PyTurtle3D

PyTurtle3D is based on the popular idea of a programmable entity which can be given directions to construct drawings with the added
option of generating these diagrams in 3 dimensions.

## Creating and Using a Turtle

To draw we need to create an instance of PyTurtle which we can then control using a set of basic commands:

```
import pyturtle as pt

my_turtle = pt.PyTurtle()

my_turtle.pendown()   # Lower the pen onto the canvas
my_turtle.forward(40) # Move forward 40 units
my_turtle.right(45)   # Rotate 45 degrees right
my_turtle.forward(40)

my_turtle.plot()      # Plot result in Matplotlib
```

commands can easily be looped to make shapes:

```
import pyturtle as pt

my_turtle = pt.PyTurtle()
my_turtle.pendown()

for i in range(8):
    my_turtle.right(45)
    my_turtle.forward(40)

my_turtle.plot()
```

To clear the canvas use the `clear()` function.

In addition we can draw in the 3D plane using the commands `declinate` and `elevate` and specifying an angle:


```
import pyturtle as pt

my_turtle = pt.PyTurtle()
my_turtle.pendown()

for i in range(8):
    my_turtle.elevate(45)
    my_turtle.forward(40)

my_turtle.plot()
```
