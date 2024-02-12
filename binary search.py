import pyglet

# Create a window
window = pyglet.window.Window(width=800, height=200, caption='Binary Search Visualization')
batch = pyglet.graphics.Batch()

# Define the alphabets within the desired scope and sort them
alphabets = (['A', 'A#', 'B', 'B#', 'C', 'C#', 'D', 'D#', 'E', 'E#', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'B#'])

# Set the target alphabet to find
target_alphabet = 'C#'

# Variables to control the animation and search
left, right = 0, len(alphabets) - 1
mid = (left + right) // 2
found = False
search_complete = False

def binary_search():
    global left, right, mid, found, search_complete
    if left <= right and not found:
        mid = (left + right) // 2
        if alphabets[mid] == target_alphabet:
            found = True
        elif alphabets[mid] < target_alphabet:
            left = mid + 1
        else:
            right = mid - 1
    else:
        search_complete = True

# Schedule the binary search to run every 0.5 seconds
pyglet.clock.schedule_interval(lambda dt: binary_search(), 3)

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
        if left <= i <= right and not search_complete:
            color = (100, 100, 255)  # Blue for the current search interval
        elif i == mid and not search_complete:
            color = (255, 0, 0)  # Red for the middle element
        elif found and i == mid:
            color = (0, 255, 0)  # Green if the target alphabet is found
        else:
            color = (200, 200, 200)  # Grey for eliminated elements
        
        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        # Draw the alphabet inside the box
        label = pyglet.text.Label(alphabet, x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

pyglet.app.run()


