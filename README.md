# Manim Correlation Animation

This project uses the Manim library to create animations demonstrating that the correlation of points on a regular polygon in a 2D plane is 0.

## Animations

The project contains two main animations:

1. **CorrelationOnRegularPolygon**: Demonstrates that the correlation between x and y coordinates of vertices of any regular polygon is exactly zero.

2. **RotatingRegressionLine**: Shows how the regression line behaves when rotating a regular polygon, demonstrating that it rotates at half the rate of the polygon.

## Requirements

- Python 3.7 or higher
- Manim Community Edition
- NumPy
- SciPy

## Virtual Environment Setup

This project uses a Python virtual environment to manage dependencies:

1. Create a virtual environment:
   ```
   python -m venv manim_venv
   ```

2. Activate the virtual environment:
   - Windows: 
     ```
     .\manim_venv\Scripts\Activate.ps1
     ```
   - Linux/Mac: 
     ```
     source manim_venv/bin/activate
     ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the animations

### Using the render script

The easiest way to render the animations is using the render.py script:

```
python render.py --scene correlation --quality medium --preview
```

Options:
- `--scene`: Which animation to render ('correlation', 'regression', or 'both')
- `--quality`: Rendering quality ('low', 'medium', or 'high')
- `--preview`: Open the video after rendering

### Using Manim directly

You can also use Manim commands directly:

```
manim -pql correlation_regular_polygon.py CorrelationOnRegularPolygon
manim -pql correlation_regular_polygon.py RotatingRegressionLine
```

Or using the main.py script:

```
python main.py
```

## Video Output

All rendered videos are saved to the `./videos` directory.

## Configuration

You can modify the resolution and frame rate in main.py or render.py by changing the config settings.

## Mathematical Background

The animations demonstrate two key mathematical properties:

1. The correlation between x and y coordinates of points on a regular polygon is exactly zero.

2. When rotating a regular polygon, its regression line rotates at exactly half the rate of the polygon's rotation.

These properties arise from the symmetrical arrangement of points on regular polygons and the mathematical properties of sine and cosine functions.

For a detailed mathematical explanation, see the [mathematical_explanation.md](mathematical_explanation.md) file.