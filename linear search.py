import pyglet

# Create a window
window = pyglet.window.Window(width=800, height=200, caption='Linear Search Visualization')
batch = pyglet.graphics.Batch()

# Define the alphabets within the desired scope and sort them
alphabets = ['A', 'A#', 'B', 'B#', 'C', 'C#', 'D', 'D#', 'E', 'E#', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'B#']

# Set the target alphabet to find
target_alphabet = 'C#'

# Variables to control the animation and search
current_index = 0
found_index = -1
search_complete = False

def linear_search(target):
    global current_index, found_index, search_complete
    if current_index < len(alphabets):
        if alphabets[current_index] == target:
            found_index = current_index
            search_complete = True
        current_index += 1
    else:
        search_complete = True

# Schedule the linear search to run every 0.5 seconds
pyglet.clock.schedule_interval(lambda dt: linear_search(target_alphabet), 3)

@window.event
def on_draw():
    window.clear()
    for i, alphabet in enumerate(alphabets):
        # Define the position and size of each 'box'
        x = i * 40 + 10
        y = window.height // 2
        width = 40
        height = 40

        # Draw the box
        if i == current_index and not search_complete:
            color = (255, 0, 0)  # Red for the current box being checked
        elif i == found_index:
            color = (0, 255, 0)  # Green if the target alphabet is found
        else:
            color = (222, 192, 241)  # Grey for unchecked or passed boxes
        
        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        # Draw the alphabet inside the box
        label = pyglet.text.Label(alphabet, x=x+width//2, y=y+height//2, font_size=20, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

pyglet.app.run()




