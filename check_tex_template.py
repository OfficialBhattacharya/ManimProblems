from manim import *
import os
import subprocess
import sys

def check_latex_installation():
    print("Checking LaTeX installation...")
    try:
        # Check if latex is available in PATH
        result = subprocess.run(["latex", "--version"], 
                                capture_output=True, 
                                text=True)
        if result.returncode == 0:
            print("LaTeX is installed and accessible:")
            print(result.stdout.split("\n")[0])
        else:
            print("LaTeX command failed with error:")
            print(result.stderr)
    except FileNotFoundError:
        print("LaTeX not found in PATH")
        
        # Check common installation locations
        possible_paths = [
            "C:\\Program Files\\MiKTeX\\miktex\\bin\\x64\\latex.exe",
            "C:\\texlive\\2024\\bin\\win32\\latex.exe",
            os.path.expanduser("~\\AppData\\Local\\Programs\\MiKTeX\\miktex\\bin\\x64\\latex.exe")
        ]
        for path in possible_paths:
            if os.path.exists(path):
                print(f"Found LaTeX at: {path}")
                
def check_available_tex_templates():
    print("\nAvailable TeX templates in Manim:")
    for name, template in TexTemplateLibrary.__dict__.items():
        if isinstance(template, TexTemplate):
            print(f"- {name}")
            
def check_current_tex_template():
    print("\nCurrent Manim TeX template settings:")
    template = config["tex_template"]
    print(f"Template type: {type(template)}")
    print(f"TeX compiler: {template.tex_compiler}")
    print(f"Output format: {template.output_format}")
    print(f"Document class: {template.documentclass}")
    print(f"Preamble (first 100 chars): {template.preamble[:100]}...")
    
def create_test_scene():
    print("\nCreating a simple test scene with LaTeX...")
    
    # Create a simple scene class
    class TestScene(Scene):
        def construct(self):
            # Test basic Text
            text = Text("Testing Text rendering", font_size=36)
            self.add(text)
            self.wait(1)
            
            # Test MathTex
            try:
                math = MathTex(r"e^{i\pi} + 1 = 0")
                math.shift(DOWN)
                self.add(math)
                print("MathTex created successfully!")
            except Exception as e:
                print(f"MathTex creation failed: {e}")
                
            self.wait(1)
    
    # Configure for a quick test
    config.preview = True
    config.disable_caching = True
    config.pixel_width = 480
    config.pixel_height = 270
    config.frame_rate = 15
    
    try:
        print("Rendering test scene (this may take a moment)...")
        scene = TestScene()
        scene.render()
        print("Test scene rendered successfully!")
    except Exception as e:
        print(f"Test scene rendering failed: {e}")
        import traceback
        traceback.print_exc()
    
if __name__ == "__main__":
    check_latex_installation()
    check_available_tex_templates()
    check_current_tex_template()
    
    # Uncomment to try rendering a test scene
    # create_test_scene() 