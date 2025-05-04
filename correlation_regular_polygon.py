from manim import *
import numpy as np
from scipy import stats

class CorrelationOnRegularPolygon(Scene):
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
        
        # Demonstrate correlation of points on a circle
        self.demonstrate_circle()
        
        # Demonstrate correlation of points on regular polygons
        self.demonstrate_regular_polygons()
        
        # Show mathematical explanation
        self.mathematical_explanation()
        
        # Conclusion
        self.conclusion()
        
        # Make sure the border is on top at the end
        self.bring_to_front(self.border)
    
    def introduction(self):
        title = Text("Correlation of Points on Regular Polygons", font_size=48)
        subtitle = Text("A Statistical Curiosity", font_size=36)
        VGroup(title, subtitle).arrange(DOWN, buff=0.5)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=DOWN))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Make sure the border stays on top
        self.bring_to_front(self.border)
    
    def demonstrate_circle(self):
        # Title
        title = Text("Correlation of Points on a Circle", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Setup coordinate system - position to the left side
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": False}
        ).scale(0.9)
        
        # Position axes to the left side
        axes.shift(LEFT * 2.5)
        
        # Create custom axis labels
        x_label = Text("x", font_size=24).next_to(axes.x_axis.get_end(), RIGHT)
        y_label = Text("y", font_size=24).next_to(axes.y_axis.get_end(), UP)
        axis_labels = VGroup(x_label, y_label)
        
        self.play(Create(axes), Write(axis_labels))
        
        # Create a circle
        circle = Circle(radius=2, color=BLUE)
        # Position the circle on the axes
        circle.move_to(axes.c2p(0, 0))
        self.play(Create(circle))
        self.wait(1)
        
        # Create right panel for information
        explanation1 = Text("Properties of points on a circle:", font_size=30)
        explanation2 = Text("• All points equidistant from center", font_size=26)
        explanation3 = Text("• Evenly distributed around center", font_size=26)
        
        # Correlation text
        corr_text = Text("Correlation: ", font_size=30)
        corr_value = Text("0.0000", font_size=30)
        corr_group = VGroup(corr_text, corr_value).arrange(RIGHT)
        
        # Arrange right panel
        right_panel = VGroup(
            explanation1,
            explanation2,
            explanation3,
            corr_group
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        # Position the right panel
        right_panel.move_to(RIGHT * 3).shift(DOWN * 0.2)
        
        self.play(Write(right_panel))
        
        # Generate points on the circle
        n_points = 3
        points = [2 * np.array([np.cos(2*np.pi*i/n_points), np.sin(2*np.pi*i/n_points), 0]) for i in range(n_points)]
        dots = VGroup(*[Dot(axes.c2p(*p[:2]), color=RED) for p in points])
        
        # Display points
        self.play(Create(dots))
        
        # Calculate and display coordinates and correlation
        coords = [(p[0], p[1]) for p in points]
        x_coords, y_coords = zip(*coords)
        
        correlation = np.corrcoef(x_coords, y_coords)[0, 1]
        new_corr_value = Text(f"{correlation:.4f}", font_size=30)
        new_corr_value.move_to(corr_value)
        
        self.play(ReplacementTransform(corr_value, new_corr_value))
        self.wait(2)
        
        # Add more points to the circle
        n_points = 12
        points = [2 * np.array([np.cos(2*np.pi*i/n_points), np.sin(2*np.pi*i/n_points), 0]) for i in range(n_points)]
        new_dots = VGroup(*[Dot(axes.c2p(*p[:2]), color=YELLOW) for p in points])
        
        # Calculate new correlation
        coords = [(p[0], p[1]) for p in points]
        x_coords, y_coords = zip(*coords)
        new_correlation = np.corrcoef(x_coords, y_coords)[0, 1]
        
        # Update correlation value
        newer_corr_value = Text(f"{new_correlation:.4f}", font_size=30)
        newer_corr_value.move_to(new_corr_value)
        
        # Animate transition
        self.play(FadeOut(dots), Create(new_dots))
        self.play(ReplacementTransform(new_corr_value, newer_corr_value))
        self.wait(2)
        
        # Clean up
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(axis_labels),
            FadeOut(circle),
            FadeOut(new_dots),
            FadeOut(right_panel),
            FadeOut(newer_corr_value)
        )
        
        # Make sure the border stays on top
        self.bring_to_front(self.border)
    
    def demonstrate_regular_polygons(self):
        # Title
        title = Text("Correlation of Points on Regular Polygons", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Setup coordinate system - position to the left side
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": False}
        ).scale(0.9)
        
        # Position axes to the left side
        axes.shift(LEFT * 2.5)
        
        # Create custom axis labels
        x_label = Text("x", font_size=24).next_to(axes.x_axis.get_end(), RIGHT)
        y_label = Text("y", font_size=24).next_to(axes.y_axis.get_end(), UP)
        axis_labels = VGroup(x_label, y_label)
        
        self.play(Create(axes), Write(axis_labels))
        
        # Create right panel for information
        explanation1 = Text("Properties of regular polygons:", font_size=30)
        explanation2 = Text("• All vertices equidistant from center", font_size=26)
        explanation3 = Text("• Equal angles between adjacent vertices", font_size=26)
        explanation4 = Text("• Zero correlation between x and y", font_size=26)
        
        # Correlation text
        corr_text = Text("Correlation: ", font_size=30)
        corr_value = Text("0.0000", font_size=30)
        corr_group = VGroup(corr_text, corr_value).arrange(RIGHT)
        
        # Arrange right panel
        right_panel = VGroup(
            explanation1,
            explanation2,
            explanation3,
            explanation4,
            corr_group
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        # Position the right panel
        right_panel.move_to(RIGHT * 3).shift(DOWN * 0.2)
        
        self.play(Write(right_panel))
        
        # Create different regular polygons
        polygon_sides = [3, 4, 5, 6, 8]
        polygon_colors = [RED, GREEN, BLUE, YELLOW, PURPLE]
        
        for i, n_sides in enumerate(polygon_sides):
            # Generate points for the regular polygon
            points = []
            for j in range(n_sides):
                angle = 2 * np.pi * j / n_sides
                point = 2 * np.array([np.cos(angle), np.sin(angle), 0])
                points.append(point)
            
            # Create the polygon and dots
            polygon_vertices = [axes.c2p(*p[:2]) for p in points]
            polygon = Polygon(*polygon_vertices, color=polygon_colors[i], stroke_width=3)
            dots = VGroup(*[Dot(vertex, color=WHITE, radius=0.08) for vertex in polygon_vertices])
            
            # Calculate correlation
            x_coords = [p[0] for p in points]
            y_coords = [p[1] for p in points]
            correlation = np.corrcoef(x_coords, y_coords)[0, 1]
            
            # Update correlation display
            new_corr_value = Text(f"{correlation:.4f}", font_size=30)
            new_corr_value.move_to(corr_value)
            
            # Show polygon with sides count
            polygon_label = Text(f"{n_sides}-sided polygon", font_size=28)
            polygon_label.next_to(title, DOWN)
            
            if i == 0:
                self.play(
                    Create(polygon),
                    Create(dots),
                    Write(polygon_label),
                    ReplacementTransform(corr_value, new_corr_value)
                )
            else:
                self.play(
                    ReplacementTransform(old_polygon, polygon),
                    ReplacementTransform(old_dots, dots),
                    ReplacementTransform(old_label, polygon_label),
                    ReplacementTransform(old_corr_value, new_corr_value)
                )
            
            self.wait(1.5)
            
            old_polygon = polygon
            old_dots = dots
            old_label = polygon_label
            old_corr_value = new_corr_value
        
        self.wait(1)
        
        # Clean up
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(axis_labels),
            FadeOut(old_polygon),
            FadeOut(old_dots),
            FadeOut(old_label),
            FadeOut(right_panel),
            FadeOut(old_corr_value)
        )
        
        # Make sure the border stays on top
        self.bring_to_front(self.border)
    
    def mathematical_explanation(self):
        # Title
        title = Text("Mathematical Explanation", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Split explanations into two columns for better layout
        left_column = VGroup(
            Text("For a regular polygon with n sides:", font_size=28),
            Text("Points lie at positions given by:", font_size=28),
            Text("(cos(2πk/n), sin(2πk/n)) for k = 0,1,...,n-1", font_size=28),
            Text("Due to the symmetry properties of sine and cosine:", font_size=28)
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        
        right_column = VGroup(
            Text("The sum of x coordinates = 0", font_size=28),
            Text("The sum of y coordinates = 0", font_size=28),
            Text("The sum of products of x and y = 0", font_size=28),
            Text("Therefore, the correlation = 0", font_size=28, color=YELLOW)
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        
        # Arrange columns side by side
        explanation_columns = VGroup(left_column, right_column).arrange(
            RIGHT, buff=1.0, aligned_edge=UP
        )
        explanation_columns.next_to(title, DOWN, buff=0.5)
        
        # Display explanations by column
        self.play(Write(left_column))
        self.wait(0.5)
        self.play(Write(right_column))
        
        self.wait(2)
        
        # Clean up
        self.play(FadeOut(title), FadeOut(explanation_columns))
        
        # Make sure the border stays on top
        self.bring_to_front(self.border)
    
    def conclusion(self):
        # Conclusion
        conclusion_title = Text("Conclusion", font_size=42)
        conclusion_title.to_edge(UP)
        
        conclusion_text = Text(
            "The correlation between x and y coordinates of vertices\n"
            "of any regular polygon is exactly zero.\n\n"
            "This is a beautiful mathematical property that connects\n"
            "geometry and statistics.",
            font_size=32,
            line_spacing=1.5
        )
        conclusion_text.next_to(conclusion_title, DOWN, buff=0.5)
        
        self.play(Write(conclusion_title))
        self.play(Write(conclusion_text))
        
        self.wait(3)
        
        # Final clean up
        self.play(FadeOut(conclusion_title), FadeOut(conclusion_text))
        
        # Final title
        final_title = Text("Correlation in Regular Polygons", font_size=48)
        subtitle = Text("A Mathematical Harmony", font_size=36)
        VGroup(final_title, subtitle).arrange(DOWN, buff=0.5)
        
        self.play(Write(final_title))
        self.play(FadeIn(subtitle, shift=DOWN))
        self.wait(2)
        self.play(FadeOut(final_title), FadeOut(subtitle))
        
        # Make sure the border stays on top
        self.bring_to_front(self.border)


class RotatingRegressionLine(Scene):
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
        # Title
        title = Text("Regression Lines in Regular Polygons", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Setup coordinate system - position to the left side
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": False}
        ).scale(0.9)
        
        # Position axes to the left side
        axes.shift(LEFT * 2.5)
        
        # Create custom axis labels
        x_label = Text("x", font_size=24).next_to(axes.x_axis.get_end(), RIGHT)
        y_label = Text("y", font_size=24).next_to(axes.y_axis.get_end(), UP)
        axis_labels = VGroup(x_label, y_label)
        
        self.play(Create(axes), Write(axis_labels))
        
        # Create right panel for information
        explanation1 = Text("Properties of rotating polygons:", font_size=30)
        explanation2 = Text("• Regression line rotates at half the", font_size=26)
        explanation3 = Text("  rate of the polygon", font_size=26)
        explanation4 = Text("• Zero correlation is preserved during", font_size=26)
        explanation5 = Text("  rotation", font_size=26)
        
        # Angle text
        angle_text = Text("θ = 0°", font_size=30)
        
        # Arrange right panel
        right_panel = VGroup(
            explanation1,
            explanation2,
            explanation3,
            explanation4,
            explanation5,
            angle_text
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        # Position the right panel
        right_panel.move_to(RIGHT * 3).shift(DOWN * 0.2)
        
        self.play(Write(right_panel))
        
        # Create a regular triangle
        n_points = 3
        radius = 2
        
        def get_rotated_polygon_points(angle, n_sides, r):
            return [
                r * np.array([
                    np.cos(angle + 2*np.pi*i/n_sides),
                    np.sin(angle + 2*np.pi*i/n_sides),
                    0
                ]) for i in range(n_sides)
            ]
        
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
            
            return Line(line_start, line_end, color=GREEN, stroke_width=3)
        
        # Initial polygon and regression line
        initial_angle = 0
        polygon_points = get_rotated_polygon_points(initial_angle, n_points, radius)
        polygon_vertices = [axes.c2p(*p[:2]) for p in polygon_points]
        polygon = Polygon(*polygon_vertices, color=BLUE, stroke_width=3)
        dots = VGroup(*[Dot(vertex, color=RED, radius=0.08) for vertex in polygon_vertices])
        
        # Calculate and draw regression line
        reg_line = get_regression_line(polygon_points, axes)
        
        # Display initial setup
        self.play(
            Create(polygon),
            Create(dots),
            Create(reg_line)
        )
        self.wait(1)
        
        # Animate rotation and regression line updates
        max_angle = 2 * np.pi
        rotation_steps = 60
        
        for i in range(1, rotation_steps + 1):
            angle = initial_angle + (max_angle * i / rotation_steps)
            new_points = get_rotated_polygon_points(angle, n_points, radius)
            new_vertices = [axes.c2p(*p[:2]) for p in new_points]
            new_polygon = Polygon(*new_vertices, color=BLUE, stroke_width=3)
            new_dots = VGroup(*[Dot(vertex, color=RED, radius=0.08) for vertex in new_vertices])
            new_reg_line = get_regression_line(new_points, axes)
            
            # Update angle label
            new_angle_text = Text(f"θ = {int(angle * 180 / np.pi) % 360}°", font_size=30)
            new_angle_text.move_to(angle_text)
            
            # Animate transitions
            self.play(
                ReplacementTransform(polygon, new_polygon),
                ReplacementTransform(dots, new_dots),
                ReplacementTransform(reg_line, new_reg_line),
                ReplacementTransform(angle_text, new_angle_text),
                run_time=0.2
            )
            
            polygon = new_polygon
            dots = new_dots
            reg_line = new_reg_line
            angle_text = new_angle_text
        
        self.wait(1)
        
        # Clean up
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(axis_labels),
            FadeOut(polygon),
            FadeOut(dots),
            FadeOut(reg_line),
            FadeOut(right_panel)
        )
        
        # Final explanation
        explanation_title = Text("Key Observation", font_size=42)
        explanation_title.to_edge(UP)
        
        explanation = Text(
            "For a regular polygon, the regression line\n"
            "rotates at exactly half the rate of the polygon's rotation.",
            font_size=32,
            line_spacing=1.5
        )
        explanation.next_to(explanation_title, DOWN, buff=0.5)
        
        self.play(Write(explanation_title))
        self.play(Write(explanation))
        
        self.wait(3)
        self.play(FadeOut(explanation_title), FadeOut(explanation))
        
        # Make sure the border stays on top
        self.bring_to_front(self.border)


if __name__ == "__main__":
    pass 