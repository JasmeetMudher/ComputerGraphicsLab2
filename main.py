import cairo
import math

def draw_house(width=1500, height=1500):
    # Create surface and context
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    # Set background to white
    ctx.set_source_rgb(1, 1, 1)
    ctx.paint()

    ### ROOF ###

    # Left Half
    ctx.set_source_rgb(0, 25 / 255, 51 / 255)
    ctx.move_to(300 * 1.875, 250 * 1.875)  # Start of left half
    ctx.line_to(250 * 1.875, 250 * 1.875)  # Left side of roof
    ctx.line_to(450 * 1.875, 170 * 1.875)  # Peak of the roof
    ctx.line_to(500 * 1.875, 170 * 1.875)  # Right side of roof
    ctx.close_path()
    ctx.fill()

    # Right Half
    ctx.set_source_rgb(0, 51 / 255, 102 / 255)
    ctx.move_to(500 * 1.875, 170 * 1.875)  # Right side of roof
    ctx.line_to(550 * 1.875, 250 * 1.875)  # Right base of roof
    ctx.line_to(350 * 1.875, 330 * 1.875)  # Left base of roof
    ctx.line_to(300 * 1.875, 250 * 1.875)  # Left side of roof
    ctx.close_path()
    ctx.fill()

    ## BASE ###

    # Move to center of canvas
    ctx.translate(width / 2, height / 1.5)

    # Define the isometric angle (45 degrees)
    iso_angle = math.pi / 4

    # Scale for isometric projection
    ctx.scale(1, math.cos(iso_angle))

    # Rotate for isometric view
    ctx.rotate(iso_angle)

    # Define base dimensions
    base_width = 390
    base_height = 40
    base_depth = 650

    # Draw the green base
    ctx.set_source_rgb(0.7, 0.9, 0.5)  # Light green color
    ctx.move_to(-base_width / 2, -base_depth / 2)
    ctx.line_to(base_width / 2, -base_depth / 2)
    ctx.line_to(base_width / 2, base_depth / 2)
    ctx.line_to(-base_width / 2, base_depth / 2)
    ctx.close_path()
    ctx.fill()

    # Add slight darker green for side faces of the base
    ctx.set_source_rgb(0.6, 0.8, 0.4)

    # Right side of the base
    ctx.move_to(base_width / 2, -base_depth / 2)
    ctx.line_to(base_width / 2 + base_height / 2, -base_depth / 2 + base_height / 2)
    ctx.line_to(base_width / 2 + base_height / 2, base_depth / 2 + base_height / 2)
    ctx.line_to(base_width / 2, base_depth / 2)
    ctx.close_path()
    ctx.fill()

    # Front side of the base
    ctx.set_source_rgb(0.7, 0.9, 0.7)
    ctx.move_to(-base_width / 2, base_depth / 2)
    ctx.line_to(base_width / 2, base_depth / 2)
    ctx.line_to(base_width / 2 + base_height / 2, base_depth / 2 + base_height / 2)
    ctx.line_to(-base_width / 2 + base_height / 2, base_depth / 2 + base_height / 2)
    ctx.close_path()
    ctx.fill()

    # Define cuboid dimensions
    cuboid_width = 280
    cuboid_height = 800
    cuboid_depth = 350

    ctx.save()

    # Translate the cuboid
    ctx.translate(-420,-450)

    # Draw the cuboid
    ctx.set_source_rgb(0.7, 0.9, 0.5)
    ctx.move_to(-cuboid_width / 2, -cuboid_depth / 2)
    ctx.line_to(cuboid_width / 2, -cuboid_depth / 2)
    ctx.line_to(cuboid_width / 2, cuboid_depth / 2)
    ctx.line_to(-cuboid_width / 2, cuboid_depth / 2)
    ctx.close_path()
    ctx.fill()

    # Add slight darker green for side faces of the cuboid
    ctx.set_source_rgb(0.82, 0.79, 0.77)

    # Right side of the cuboid
    ctx.move_to(cuboid_width / 2, -cuboid_depth / 2)
    ctx.line_to(cuboid_width / 2 + cuboid_height / 2, -cuboid_depth / 2 + cuboid_height / 2)
    ctx.line_to(cuboid_width / 2 + cuboid_height / 2, cuboid_depth / 2 + cuboid_height / 2)
    ctx.line_to(cuboid_width / 2, cuboid_depth / 2)
    ctx.close_path()
    ctx.fill()

    # Front side of the cuboid
    ctx.set_source_rgb(0.89, 0.85, 0.84)

    ctx.move_to(-cuboid_width / 2, cuboid_depth / 2)
    ctx.line_to(cuboid_width / 2, cuboid_depth / 2)
    ctx.line_to(cuboid_width / 2 + cuboid_height / 2, cuboid_depth / 2 + cuboid_height / 2)
    ctx.line_to(-cuboid_width / 2 + cuboid_height / 2, cuboid_depth / 2 + cuboid_height / 2)
    ctx.close_path()
    ctx.fill()

    # Save the image
    surface.write_to_png('house.png')

draw_house()
