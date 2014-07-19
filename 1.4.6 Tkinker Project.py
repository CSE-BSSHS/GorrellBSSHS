'''
We HOPE it creates a GUI in which a mouse drag creates a circle. 
Not fully implemented.
Refer to:
    
Lundh, Fredrik. (2005). An Introduction to Tkinter, Draft revision.  
Retrieved from http://effbot.org/tkinterbook/ 

Shipman, John. (2013) Tkinter 8.5 reference. 
Retrieved from http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html

Lundh, Fredrik. (1999) An Introduction to Tkinter.  
Retrieved from http://www.pythonware.com/library/tkinter/introduction/index.htm

For animation, see after() documentation in Lundh's draft:
http://effbot.org/tkinterbook/widget.htm
'''
from Tkinter import * #don't import like this except for Tkinter
root = Tk() #create main window

# A slider to set red
red_input = IntVar()
redSlider = Scale(root, variable=red_input, from_=0, to=255,
                  orient=HORIZONTAL, label='Red:')
redSlider.set(127)
redSlider.grid(column=0, row=1, sticky=W)

# A button to change to the new color
def update():
    ''' 
    An event handler for the update button
    '''
    # The following code creates a two-character hex string for red
    # Get an integer from an IntVar
    red_int = red_input.get()
    # Convert to hex
    red_hex = hex(red_int)
    # Drop the 0x at the beginning of the hex string
    red = red_hex[2:] 
    # Ensure two hex-digits:
    if len(red)==1:
        red = '0' + red 
    
    if len(circ)>0:
        canvas.itemconfig(circ[-1],fill='#' + red + '0000')

# Create the update button
update_button = Button(root, text='Update', command=update)
update_button.grid(column=0, row=2, sticky=W)

# A canvas for mouse events and image drawing
canvas = Canvas(root, height=600, width=600, relief=RAISED, bg='white')
canvas.grid(column=1, row=0, rowspan=4, sticky=W)

# Initialize an aggregator for circle items
circ=[]
#create variables for global use in handlers
centerx, centery = 0,0

def down(event):
    '''
    Handler for mouse left button down
    Collects information for later use creating a circle.
    '''
    global centerx, centery
    centerx=event.x
    centery=event.y

def up(event):
    '''
    Handler for mouse left button up
    '''
    global circ, centerx, centery
    # Use the Pythagoream th'm to calculate distance from down to up events
    r=(centerx-event.x)**2 + (centery-event.y)**2
    r=int(r**.5)
    
    # Create a new circle and add it to the global list
    circ += [canvas.create_oval(centerx-r, centery-r,centerx+r, centery+r,
                              outline='#000000')]
    
    # The following code creates a two-character hex string for red
    # Should be placed in a function for reuse.
    
    # Get an integer from an IntVar
    red_int = red_input.get()
    # Convert to hex
    red_hex = hex(red_int)
    # Drop the 0x at the beginning of the hex string
    red = red_hex[2:] 
    # Ensure two hex-digits:
    if len(red)==1:
        red = '0' + red 
       
    # Fill the circle with the user-defined color
    canvas.itemconfig(circ[-1], fill='#' + red + '0000')
    
# Bind the handlers to the canvas.
canvas.bind('<Button-1>', down)
canvas.bind('<ButtonRelease-1>', up)

# Enter event loop
root.mainloop() 