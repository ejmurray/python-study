# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui

def draw(canvas):
    canvas.draw_circle([90,200],20,10,"green")
    canvas.draw_circle([210,200],20,10,"green")
    canvas.draw_line([50,180], [250,180], 40, "red")
    canvas.draw_line([55,170], [90,120], 5, "red")
    canvas.draw_line([90,120],[130,120], 5, "red")
    canvas.draw_line([180,108],[180,160], 140, "red")

    

f = simplegui.create_frame("Person",300,300)
f.set_draw_handler(draw)
f.start()
