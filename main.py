import cairo
import math


def draw_green_base(width=800, height=800):
    # Create surface and context
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    # Set background to white
    ctx.set_source_rgb(1, 1, 1)
    ctx.paint()

    # Move to center of canvas
    ctx.translate(width / 2, height / 1.5)

    # Define the isometric angle (45 degrees)
    iso_angle = math.pi / 4

    # Scale for isometric projection
    ctx.scale(1, math.cos(iso_angle))

    # Rotate for isometric view
    ctx.rotate(iso_angle)

    # Define base dimensions
    base_width = 180
    base_height = 20
    base_depth = 250

    # Draw the top face (green rectangle)
    ctx.set_source_rgb(0.7, 0.9, 0.5)  # Light green color
    ctx.move_to(-base_width / 2, -base_depth / 2)
    ctx.line_to(base_width / 2, -base_depth / 2)
    ctx.line_to(base_width / 2, base_depth / 2)
    ctx.line_to(-base_width / 2, base_depth / 2)
    ctx.close_path()
    ctx.fill()

    # Add slight darker green for side faces for 3D effect
    ctx.set_source_rgb(0.6, 0.8, 0.4)

    # Right side
    ctx.move_to(base_width / 2, -base_depth / 2)
    ctx.line_to(base_width / 2 + base_height / 2, -base_depth / 2 + base_height / 2)
    ctx.line_to(base_width / 2 + base_height / 2, base_depth / 2 + base_height / 2)
    ctx.line_to(base_width / 2, base_depth / 2)
    ctx.close_path()
    ctx.fill()


    ctx.set_source_rgb(0.7, 0.9, 0.7)

    # Front side
    ctx.move_to(-base_width / 2, base_depth / 2)
    ctx.line_to(base_width / 2, base_depth / 2)
    ctx.line_to(base_width / 2 + base_height / 2, base_depth / 2 + base_height / 2)
    ctx.line_to(-base_width / 2 + base_height / 2, base_depth / 2 + base_height / 2)
    ctx.close_path()
    ctx.fill()

    surface.write_to_png('house.png')


draw_green_base()