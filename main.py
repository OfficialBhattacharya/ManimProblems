from manim import *
from complex_unity_correlation import ComplexUnityCorrelation

if __name__ == "__main__":
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
    
    # Render the complex unity correlation scene
    scene = ComplexUnityCorrelation()
    scene.render() 