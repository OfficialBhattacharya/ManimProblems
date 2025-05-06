#!/usr/bin/env python
import argparse
from manim import *
from complex_unity_correlation import ComplexUnityCorrelation

def main():
    parser = argparse.ArgumentParser(description='Render Manim animations for complex roots of unity.')
    parser.add_argument('--scene', type=str, choices=['complex_unity', 'all'], 
                        default='complex_unity', help='Which scene to render')
    parser.add_argument('--quality', type=str, choices=['low', 'medium', 'high'], 
                        default='medium', help='Rendering quality')
    parser.add_argument('--preview', action='store_true', help='Open the rendered video after completion')
    
    args = parser.parse_args()
    
    # Set configuration based on arguments
    config.media_dir = "./videos"
    
    # Set background color to ensure borders are visible
    config.background_color = "#000000"
    
    # Ensure equal frame sizes across all scenes
    if args.quality == 'low':
        config.pixel_height = 480
        config.pixel_width = 854
        config.frame_rate = 15
    elif args.quality == 'medium':
        config.pixel_height = 720
        config.pixel_width = 1280
        config.frame_rate = 30
    else:  # high
        config.pixel_height = 1080
        config.pixel_width = 1920
        config.frame_rate = 60
    
    # Set preview flag
    config.preview = args.preview
    
    # Maintain consistent frame dimensions for all scenes
    # This ensures the black border looks the same across all animations
    config.frame_height = 8.0
    config.frame_width = config.frame_height * 16/9  # Maintain 16:9 aspect ratio
    
    # Render the requested scenes
    if args.scene in ['complex_unity', 'all']:
        print("Rendering complex unity correlation scene...")
        scene = ComplexUnityCorrelation()
        scene.render()
    
    print("Rendering complete. Videos saved to ./videos directory.")

if __name__ == "__main__":
    main() 