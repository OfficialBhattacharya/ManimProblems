from manim import *
import numpy as np
from scipy import stats
import os
import sys

# Add MiKTeX to the system PATH
miktex_path = "C:\\Program Files\\MiKTeX\\miktex\\bin\\x64"
if os.path.exists(miktex_path) and miktex_path not in os.environ["PATH"]:
    os.environ["PATH"] = miktex_path + os.pathsep + os.environ["PATH"]
    print(f"Added {miktex_path} to PATH")

# Check if LaTeX is accessible
try:
    import subprocess
    result = subprocess.run(["latex", "--version"], 
                            capture_output=True, 
                            text=True)
    if result.returncode == 0:
        print("LaTeX is accessible for rendering")
    else:
        print("LaTeX is in PATH but not working properly")
except Exception as e:
    print(f"Error checking LaTeX: {e}")

class ComplexUnityCorrelation(Scene):
    def __init__(self, **kwargs):
        # Just use the default template, we've fixed the PATH
        super().__init__(**kwargs)
        
    def setup(self):
        super().setup()
        # Add a black border around the frame
        # 2mm converted to Manim units (based on 8 height units)
        border_width = 0.075  # 2mm in Manim units
        
        # Get the frame dimensions
        frame_width = config.frame_width
        frame_height = config.frame_height
        
        # Create the border rectangle
        self.border = Rectangle(
            width=frame_width,
            height=frame_height,
            stroke_width=border_width * 2,  # Multiply by 2 to make the border 2mm thick
            stroke_color=BLACK,
            fill_opacity=0
        )
        
        # Add the border to the scene
        self.add(self.border)
        
    def construct(self):
        # Introduction
        self.introduction()
        
        # Define and show complex roots of unity
        self.explain_complex_roots()
        
        # Show correlation and regression for different polygons
        self.correlation_and_regression()
        
        # Mathematical explanation with LaTeX
        self.mathematical_explanation()
        
        # Conclusion
        self.conclusion()
        
        # Make sure the border is on top at the end
        self.bring_to_front(self.border)
    
    def introduction(self):
        self.clear()  # Remove lingering objects
        title = Text("Observations about Correlation", font_size=56)  # Larger font size
        subtitle = Text("Episode-1 : Correlation of not-so random points", font_size=36)  # Larger font size
        
        # Better spacing for 16:9 ratio
        VGroup(title, subtitle).arrange(DOWN, buff=0.7).center()
        
        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=DOWN))
        self.wait(3)  # Longer wait time
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Make sure the border stays on top
        self.bring_to_front(self.border)
    
    def explain_complex_roots(self):
        self.clear()  # Remove lingering objects
        # Title (will go in right pane)
        title = MathTex(r"\text{Complex Roots of Unity: } z^n = 1", font_size=42)
        title.to_edge(UP)

        # Setup complex plane for left pane
        plane = ComplexPlane(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2, 2, 1],
            x_length=5.5,  # Slightly smaller to fit double pane
            y_length=4.5
        ).add_coordinates()

        # Axis labels, moved inside axes
        re_label = MathTex(r"\text{Re}(z)", font_size=22).next_to(plane.x_axis.get_end(), RIGHT, buff=-0.3)
        im_label = MathTex(r"\text{Im}(z)", font_size=22).next_to(plane.y_axis.get_end(), UP, buff=-0.3)

        # Group for left pane
        left_pane = VGroup(plane, re_label, im_label)
        left_pane.arrange(DOWN, buff=0.1)
        left_pane.shift(LEFT * 2.5)

        # Prepare right pane (will update contents in loop)
        current_right_pane = VGroup()
        current_right_pane.arrange(DOWN, buff=0.5)
        current_right_pane.shift(RIGHT * 2.5)

        # Show both panes
        self.play(FadeIn(left_pane))
        self.wait(0.5)
        self.play(Write(title))
        self.wait(0.5)

        # Animate n-th roots of unity for n=3 to n=8
        for n in range(3, 9):
            points = [np.array([np.cos(2 * np.pi * k / n), np.sin(2 * np.pi * k / n), 0]) for k in range(n)]
            dots = VGroup(*[Dot(plane.c2p(*p[:2]), color=BLUE, radius=0.08) for p in points])
            lines = VGroup(*[Line(plane.c2p(0, 0), plane.c2p(*p[:2]), color=RED) for p in points])
            polygon = Polygon(*[plane.c2p(*p[:2]) for p in points], color=GREEN)

            formula = MathTex(
                r"z_k = e^{i\frac{2\pi k}{" + str(n) + r"}}, \; k = 0,1,\ldots," + str(n-1),
                font_size=32
            )
            n_label = Text(f"{n}-th roots of unity", font_size=32)

            if n == 3:
                # First iteration: show n_label, formula (no title in right pane)
                new_right = VGroup(n_label, formula).arrange(DOWN, buff=0.4)
                new_right.shift(RIGHT * 2.5)
                self.play(Create(dots), Create(lines), Create(polygon), Write(n_label), Write(formula))
                self.play(Transform(current_right_pane, new_right))
                self.wait(1)
                # Explicitly fade out the first right pane before proceeding
                self.play(FadeOut(current_right_pane))
                current_right_pane = VGroup()  # Reset for next iteration
            else:
                # Only n_label and formula in right pane
                new_right = VGroup(n_label, formula).arrange(DOWN, buff=0.4)
                new_right.shift(RIGHT * 2.5)
                self.play(
                    ReplacementTransform(old_dots, dots),
                    ReplacementTransform(old_lines, lines),
                    ReplacementTransform(old_polygon, polygon),
                    ReplacementTransform(current_right_pane, new_right)
                )
                self.wait(1)
                current_right_pane = new_right
            old_dots, old_lines, old_polygon = dots, lines, polygon

        # Sum formulas (right pane, no title)
        sum_formula = MathTex(
            r"\sum_{k=0}^{n-1} e^{i\frac{2\pi k}{n}} = 0, \; \forall n \geq 2",
            font_size=30
        )
        real_sum = MathTex(
            r"\sum_{k=0}^{n-1} \cos\left(\frac{2\pi k}{n}\right) = 0",
            font_size=28
        )
        imag_sum = MathTex(
            r"\sum_{k=0}^{n-1} \sin\left(\frac{2\pi k}{n}\right) = 0",
            font_size=28
        )
        sum_group = VGroup(sum_formula, real_sum, imag_sum).arrange(DOWN, buff=0.3)
        sum_group.shift(RIGHT * 2.5)
        self.play(Transform(current_right_pane, sum_group))
        self.wait(3)

        # Clean up: fade out both panes, using the last displayed right pane
        self.play(
            FadeOut(left_pane),
            FadeOut(current_right_pane)
        )
        self.wait(0.2)
        # Make sure the border stays on top
        self.bring_to_front(self.border)
    
    def correlation_and_regression(self):
        self.clear()  # Remove lingering objects
        # Title
        title = MathTex(r"\text{Correlation \& Regression for Regular Polygons}", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Setup coordinate system with adjusted dimensions for better fit
        axes = Axes(
            x_range=[-3, 3, 1],  # Smaller range 
            y_range=[-3, 3, 1],
            x_length=6,  # Smaller length
            y_length=6,
            axis_config={"include_tip": False}
        ).scale(0.9)  # Scale down slightly
        
        # Position axes to the left side instead of center
        axes.shift(LEFT * 2.5)
        
        # Create axis labels with larger font
        x_label = MathTex("x", font_size=28).next_to(axes.x_axis.get_end(), RIGHT)
        y_label = MathTex("y", font_size=28).next_to(axes.y_axis.get_end(), UP)
        axis_labels = VGroup(x_label, y_label)
        
        self.play(Create(axes), Write(axis_labels))
        
        # Define statistics for display - position on the right
        stats_group = VGroup()
        
        # Create correlation text with LaTeX
        corr_text = MathTex(r"\text{Correlation: }", font_size=36)
        corr_value = MathTex(r"0.0000", font_size=36)
        corr_group = VGroup(corr_text, corr_value).arrange(RIGHT)
        
        # Create regression equation text with LaTeX
        reg_eq_text = MathTex(r"\text{Regression: }", font_size=36)
        reg_eq_value = MathTex(r"y = 0.0000x + 0.0000", font_size=36)
        reg_eq_group = VGroup(reg_eq_text, reg_eq_value).arrange(RIGHT)
        
        # Create additional info text
        explanation1 = MathTex(r"\text{Properties of regular polygons:}", font_size=32)
        explanation2 = MathTex(r"\text{• All vertices equidistant from center}", font_size=28)
        explanation3 = MathTex(r"\text{• Equal angles between adjacent vertices}", font_size=28)
        explanation4 = MathTex(r"\text{• Zero correlation between $x$ and $y$}", font_size=28)
        explanation5 = MathTex(r"\text{• Horizontal regression line}", font_size=28)
        
        # Arrange all the text in a right-side panel
        right_panel = VGroup(
            corr_group,
            reg_eq_group,
            explanation1,
            explanation2,
            explanation3,
            explanation4,
            explanation5
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        # Position the right panel
        right_panel.move_to(RIGHT * 3).shift(DOWN * 0.2)
        
        self.play(Write(right_panel))
        
        # Show different polygons with correlation and regression line
        polygon_sides = [3, 4, 5, 6, 8]
        polygon_colors = [RED, GREEN, BLUE, YELLOW, PURPLE]
        
        # Function to get regression line
        def get_regression_line(points, axes):
            x_coords = [p[0] for p in points]
            y_coords = [p[1] for p in points]
            
            slope, intercept, r_value, p_value, std_err = stats.linregress(x_coords, y_coords)
            
            x_min, x_max = min(x_coords), max(x_coords)
            extension = (x_max - x_min) * 0.5
            x_line = np.array([x_min - extension, x_max + extension])
            y_line = slope * x_line + intercept
            
            line_start = axes.c2p(x_line[0], y_line[0])
            line_end = axes.c2p(x_line[1], y_line[1])
            
            return Line(line_start, line_end, color=GREEN, stroke_width=3), slope, intercept  # Thicker line
        
        for i, n_sides in enumerate(polygon_sides):
            # Generate points for the regular polygon
            points = []
            for j in range(n_sides):
                angle = 2 * np.pi * j / n_sides
                point = 2 * np.array([np.cos(angle), np.sin(angle), 0])
                points.append(point)
            
            # Create the polygon and dots with improved visibility
            polygon_vertices = [axes.c2p(*p[:2]) for p in points]
            polygon = Polygon(*polygon_vertices, color=polygon_colors[i], stroke_width=3)  # Thicker lines
            dots = VGroup(*[Dot(vertex, color=WHITE, radius=0.08) for vertex in polygon_vertices])  # Larger dots
            
            # Calculate and display correlation
            x_coords = [p[0] for p in points]
            y_coords = [p[1] for p in points]
            correlation = np.corrcoef(x_coords, y_coords)[0, 1]
            
            # Update correlation display with LaTeX - larger font
            new_corr_value = MathTex(f"{correlation:.4f}", font_size=36)
            new_corr_value.move_to(corr_value)
            
            # Calculate and display regression line
            reg_line, slope, intercept = get_regression_line(points, axes)
            
            # Update regression equation - larger font
            sign = "+" if intercept >= 0 else ""
            new_reg_eq_value = MathTex(f"y = {slope:.4f}x {sign} {intercept:.4f}", font_size=36)
            new_reg_eq_value.move_to(reg_eq_value)
            
            # Show polygon with sides count - larger font
            polygon_label = MathTex(f"{n_sides}-\\text{{sided polygon}}", font_size=36)
            polygon_label.next_to(title, DOWN, buff=0.5)
            
            if i == 0:
                self.play(
                    Create(polygon),
                    Create(dots),
                    Create(reg_line),
                    Write(polygon_label),
                    ReplacementTransform(corr_value, new_corr_value),
                    ReplacementTransform(reg_eq_value, new_reg_eq_value)
                )
            else:
                self.play(
                    ReplacementTransform(old_polygon, polygon),
                    ReplacementTransform(old_dots, dots),
                    ReplacementTransform(old_reg_line, reg_line),
                    ReplacementTransform(old_label, polygon_label),
                    ReplacementTransform(old_corr_value, new_corr_value),
                    ReplacementTransform(old_reg_eq_value, new_reg_eq_value)
                )
            
            self.wait(1.5)
            
            old_polygon = polygon
            old_dots = dots
            old_reg_line = reg_line
            old_label = polygon_label
            old_corr_value = new_corr_value
            old_reg_eq_value = new_reg_eq_value
        
        self.wait(2)  # Longer wait time
        
        # Clean up
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(axis_labels),
            FadeOut(old_polygon),
            FadeOut(old_dots),
            FadeOut(old_reg_line),
            FadeOut(old_label),
            FadeOut(right_panel),
            FadeOut(old_corr_value),
            FadeOut(old_reg_eq_value)
        )
        
        # Make sure the border stays on top
        self.bring_to_front(self.border)
    
    def mathematical_explanation(self):
        self.clear()  # Remove lingering objects
        # Title
        title = MathTex(r"\text{Mathematical Proof}", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Explanations using LaTeX - use smaller font size for better readability
        explanation1 = MathTex(r"\text{For a regular $n$-gon, vertices at:}", font_size=30)
        
        explanation2 = MathTex(r"(x_k, y_k) = \left(\cos\left(\frac{2\pi k}{n}\right), \sin\left(\frac{2\pi k}{n}\right)\right)", font_size=30)
        
        explanation3 = MathTex(r"\text{Correlation coefficient formula:}", font_size=30)
        
        explanation4 = MathTex(r"\rho_{x,y} = \frac{\text{Cov}(x,y)}{\sigma_x \sigma_y} = \frac{\sum_{k=0}^{n-1} (x_k - \bar{x})(y_k - \bar{y})}{\sqrt{\sum_{k=0}^{n-1} (x_k - \bar{x})^2 \sum_{k=0}^{n-1} (y_k - \bar{y})^2}}", font_size=26)
        
        explanation5 = MathTex(r"\text{From the properties of roots of unity:}", font_size=30)
        
        explanation6 = MathTex(r"\sum_{k=0}^{n-1} \cos\left(\frac{2\pi k}{n}\right) = 0 \quad \text{and} \quad \sum_{k=0}^{n-1} \sin\left(\frac{2\pi k}{n}\right) = 0", font_size=28)
        
        explanation7 = MathTex(r"\therefore \bar{x} = \bar{y} = 0", font_size=30)
        
        explanation8 = MathTex(r"\text{The correlation simplifies to:}", font_size=30)
        
        explanation9 = MathTex(r"\rho_{x,y} = \frac{\sum_{k=0}^{n-1} x_k y_k}{\sqrt{\sum_{k=0}^{n-1} x_k^2 \sum_{k=0}^{n-1} y_k^2}}", font_size=30)
        
        explanation10 = MathTex(r"\text{From trigonometric identities:}", font_size=30)
        
        explanation11 = MathTex(r"\sum_{k=0}^{n-1} \cos\left(\frac{2\pi k}{n}\right) \sin\left(\frac{2\pi k}{n}\right) = 0", font_size=28)
        
        explanation12 = MathTex(r"\text{And:} \quad \sum_{k=0}^{n-1} \cos^2\left(\frac{2\pi k}{n}\right) = \sum_{k=0}^{n-1} \sin^2\left(\frac{2\pi k}{n}\right) = \frac{n}{2}", font_size=28)
        
        explanation13 = MathTex(r"\therefore \rho_{x,y} = \frac{0}{\sqrt{\frac{n}{2} \cdot \frac{n}{2}}} = 0", font_size=30, color=YELLOW)
        
        explanation14 = MathTex(r"\text{Hence, the correlation is always zero!}", font_size=30, color=YELLOW)
        
        # Organize the explanations with more space between items
        explanations = VGroup(
            explanation1, explanation2, explanation3, explanation4, explanation5, 
            explanation6, explanation7, explanation8, explanation9, explanation10, 
            explanation11, explanation12, explanation13, explanation14
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        
        # Scale and position to fit better in the 16:9 frame
        explanations.scale(0.85).next_to(title, DOWN, buff=0.5)
        
        # Split explanations into two columns to fit better
        explanations_left = VGroup(
            explanation1, explanation2, explanation3, explanation4, 
            explanation5, explanation6, explanation7
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        
        explanations_right = VGroup(
            explanation8, explanation9, explanation10, explanation11, 
            explanation12, explanation13, explanation14
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        
        # Arrange the two columns
        all_explanations = VGroup(explanations_left, explanations_right).arrange(
            RIGHT, buff=0.8, aligned_edge=UP
        )
        
        all_explanations.scale(0.9).next_to(title, DOWN, buff=0.5)
        
        # Display the title and explanations
        self.play(Write(title))
        
        # First column
        for explanation in explanations_left:
            self.play(Write(explanation), run_time=0.8)
            self.wait(0.2)
        
        # Second column
        for explanation in explanations_right:
            self.play(Write(explanation), run_time=0.8)
            self.wait(0.2)
        
        # Wait at the end
        self.wait(3)
        
        # Clean up
        self.play(FadeOut(title), FadeOut(all_explanations))
        
        # Make sure the border stays on top
        self.bring_to_front(self.border)
    
    def conclusion(self):
        self.clear()  # Remove lingering objects
        # Conclusion
        conclusion_title = MathTex(r"\text{Conclusion}", font_size=42)
        conclusion_title.to_edge(UP)
        
        # Use aligned text with proper spacing for 16:9 aspect ratio
        conclusion_text = MathTex(
            r"""
            \begin{aligned}
            &\text{1. Regular polygons correspond to roots of unity in the complex plane.} \\[0.5em]
            &\text{2. The sum of all roots of unity is always zero.} \\[0.5em]
            &\text{3. The correlation between $x$ and $y$ coordinates is always zero.} \\[0.5em]
            \end{aligned}
            """,
            font_size=36  # Increased font size for better readability
        )
        
        conclusion_text.next_to(conclusion_title, DOWN, buff=0.7)
        
        self.play(Write(conclusion_title))
        self.play(Write(conclusion_text))
        
        self.wait(3)
        
        # Final clean up
        self.play(FadeOut(conclusion_title), FadeOut(conclusion_text))
        
        # Final title with improved positioning
        final_title = MathTex(r"\text{CHorizon}", font_size=52)  # Larger font size
        subtitle = MathTex(r"\text{Where Concepts Converge}", font_size=40)  # Larger font size
        
        # Position in center of the 16:9 frame
        VGroup(final_title, subtitle).arrange(DOWN, buff=0.6).center()
        
        self.play(Write(final_title))
        self.play(FadeIn(subtitle, shift=DOWN))
        self.wait(3)  # Longer wait time
        self.play(FadeOut(final_title), FadeOut(subtitle))
        
        # Make sure the border stays on top
        self.bring_to_front(self.border)


if __name__ == "__main__":
    pass 