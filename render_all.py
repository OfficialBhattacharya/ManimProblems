#!/usr/bin/env python
from manim import *
from correlation_regular_polygon import CorrelationOnRegularPolygon, RotatingRegressionLine
from complex_unity_correlation import ComplexUnityCorrelation

def main():
    """
    Renders all scenes with consistent border and layout settings
    """
    # Configuration settings with proper 16:9 aspect ratio and improved rendering
    config.media_dir = "./videos"
    config.pixel_height = 1080
    config.pixel_width = 1920  # Ensures 16:9 aspect ratio (1920/1080 = 16/9)
    config.frame_rate = 30
    config.quality = "high_quality"
    
    # Set background color to ensure borders are visible
    config.background_color = "#000000"
    
    # Additional settings for better readability
    config.frame_height = 8.0  # Adjust frame height for better scaling
    config.frame_width = config.frame_height * 16/9  # Maintain 16:9 aspect ratio
    
    # Render all scenes in sequence
    print("Rendering correlation scene...")
    scene1 = CorrelationOnRegularPolygon()
    scene1.render()
    
    print("Rendering regression scene...")
    scene2 = RotatingRegressionLine()
    scene2.render()
    
    print("Rendering complex unity correlation scene...")
    scene3 = ComplexUnityCorrelation()
    scene3.render()
    
    print("All scenes rendered successfully. Videos saved to ./videos directory.")
    print("All scenes have consistent 2mm black borders and double-paned layouts.")

if __name__ == "__main__":
    main() 