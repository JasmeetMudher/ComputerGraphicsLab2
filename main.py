import cairo
import math
def draw_door_on_front_face(ctx, x, y, door_width, door_height):
    # Draw the door body
    ctx.set_source_rgb(0.6, 0.3, 0.1)  # Brown color for the door
    ctx.move_to(x, y)
    ctx.line_to(x + door_width, y - door_width / 2)  # Top-right
    ctx.line_to(x + door_width, y + door_height - door_width / 2)  # Bottom-right
    ctx.line_to(x, y + door_height)  # Bottom-left
    ctx.close_path()
    ctx.fill()

    # Draw the lite (glass window on the door)
    lite_margin = 10  # Margin from door edges
    lite_width = door_width - lite_margin * 2
    lite_height = door_height / 4  # Glass occupies top quarter of the door

    ctx.set_source_rgb(0.78, 0.85, 0.90)  # Glass-like blue
    ctx.move_to(x + lite_margin, y + lite_margin)
    ctx.line_to(x + lite_margin + lite_width, y + lite_margin - lite_width / 2)  # Top-right of glass
    ctx.line_to(
        x + lite_margin + lite_width,
        y + lite_margin + lite_height - lite_width / 2,
    )  # Bottom-right of glass
    ctx.line_to(x + lite_margin, y + lite_margin + lite_height)  # Bottom-left of glass
    ctx.close_path()
    ctx.fill()

def draw_window_on_front_face(ctx, x, y, window_width, window_height):
    window_x_offset = 20  # Horizontal offset within the face
    window_y_offset = 50  # Vertical offset within the face

    # Compute window corners in isometric space
    tlw, tlh = x - window_x_offset, y + window_y_offset  # Top-left of the window
    trw, trh = tlw - window_width / 2, tlh - window_width / 2  # Top-right
    blw, blh = tlw, tlh + window_height  # Bottom-left
    brw, brh = trw, trh + window_height  # Bottom-right

    # Draw the window
    ctx.set_source_rgb(0.78, 0.85, 0.90)  # Glass-like blue
    ctx.move_to(tlw, tlh)
    ctx.line_to(trw, trh)
    ctx.line_to(brw, brh)
    ctx.line_to(blw, blh)
    ctx.close_path()
    ctx.fill_preserve()

    # Outline
    ctx.set_source_rgb(0, 0, 0)  # Dark border
    ctx.set_line_width(3)
    ctx.stroke()

def draw_window_on_left_face(ctx, x, y, width, height):
    """Draws a window on the front face of the house (aligned with XY axes)."""
    # Define the window size
    window_width = width
    window_height = height

    # Position window with offsets (you can adjust these as needed)
    window_x_offset = 40  # Horizontal offset within the front face
    window_y_offset = 30  # Vertical offset within the front face

    # Draw the window on the front face (no skewing, just simple translation)
    tlw, tlh = x - window_x_offset, y + window_y_offset  # Top-left
    trw, trh = tlw + window_width, tlh  # Top-right
    blw, blh = tlw + window_width + window_x_offset, tlh + window_height  # Bottom-left
    brw, brh = trw + window_width + window_x_offset, trh + window_height  # Bottom-right

    ctx.set_source_rgb(0.78, 0.85, 0.90)  # Glass-like blue color
    ctx.move_to(tlw, tlh)
    ctx.line_to(trw, trh)
    ctx.line_to(brw, brh)
    ctx.line_to(blw, blh)
    ctx.close_path()
    ctx.fill_preserve()

    # Window outline
    ctx.set_source_rgb(0, 0, 0)  # Dark border
    ctx.set_line_width(3)
    ctx.stroke()

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

    draw_window_on_front_face(ctx, 300, 80, 170, 60)
    draw_window_on_front_face(ctx, 300, 10, 170, 60)

    draw_window_on_left_face(ctx, 20, 200, 60, 100)
    draw_window_on_left_face(ctx, 90, 200, 60, 100)

    draw_window_on_left_face(ctx, 240, 350, 60, 100)
    draw_window_on_left_face(ctx, 170, 350, 60, 100)

    draw_door_on_front_face(ctx, 430, 190, door_width=60, door_height=150)

    # Save the image
    surface.write_to_png('house.png')

draw_house()
