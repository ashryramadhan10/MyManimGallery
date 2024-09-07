# MyManimGallery

## 1. Animation

List of animation functions:
* Create
* Rotate
* Transform
* Shift
* MoveAlong

## 2. Object

List of Mobject:
* VMobject (Vector)

### 2.1. VMObject

In Manim, a VMobject (Vectorized Mobject) is a class for creating vectorized shapes (shapes made of lines and curves). VMobject is a parent class for many commonly used shapes like Circle, Square, and other geometric objects, as well as paths and curves.

```python
from manim import *

class CustomShape(Scene):
    def construct(self):
        # Create a VMobject
        shape = VMobject()
        
        # Define points for the shape
        shape.set_points_as_corners([
            [-2, 1, 0],  # Top left
            [2, 1, 0],   # Top right
            [1, -1, 0],  # Bottom right
            [-1, -1, 0], # Bottom left
            [-2, 1, 0],  # Back to top left
        ])

        # Set stroke color and width
        shape.set_stroke(color=YELLOW, width=6)
        
        # Add the custom shape to the scene
        self.play(Create(shape))
        self.wait(2)
```