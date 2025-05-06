# Manim Mathematical Animations

This project contains mathematical animations created using Manim, focusing on the relationship between regular polygons and correlation.

## Available Animations

1. **CorrelationOnRegularPolygon**: Demonstrates how regular polygons have zero correlation between their x and y coordinates.
2. **RotatingRegressionLine**: Shows the behavior of regression lines on rotating regular polygons.
3. **ComplexUnityCorrelation**: An animation explaining the connection between complex roots of unity and the zero correlation property of regular polygons.

## Requirements

- Python 3.8+
- Manim
- LaTeX (for mathematical expressions)
- Dependencies:
  - manim>=0.17.2
  - numpy==1.26.4
  - scipy==1.12.0

## Installation

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install LaTeX if not already installed (required for mathematical expressions)

## Usage

### Using the render script

The easiest way to render the animations is using the render.py script:

```bash
python render.py --scene correlation --quality medium --preview
```

Available options:
- `--scene`: Which animation to render ('correlation', 'regression', 'complex_unity', or 'all')
- `--quality`: Rendering quality ('low', 'medium', 'high')
- `--preview`: Open the rendered video after completion

### Manual rendering

You can also render individual scenes directly using Manim:

```bash
# Basic animations
manim -pql correlation_regular_polygon.py CorrelationOnRegularPolygon
manim -pql correlation_regular_polygon.py RotatingRegressionLine
manim -pql complex_unity_correlation.py ComplexUnityCorrelation
```

## Features

- High-quality mathematical animations
- Clear visualization of mathematical concepts
- Support for different rendering qualities
- Preview option for immediate feedback
- Consistent frame dimensions across all scenes

## License

This project is licensed under the MIT License - see the LICENSE file for details.