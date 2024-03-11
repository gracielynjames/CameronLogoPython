from tkinter import*
from points import*

root = Tk()
root.geometry('300x300')
root.title('Cameron')
c = Canvas(root, bg = 'hotpink', height = 300 , width = 300)
c.pack()
dubz = 7


#-----------------------------------------------------------
# Woodhandle
woodHandle = c.create_polygon(a, fill = 'goldenrod', outline = 'black')

woodHandleShadow = c.create_polygon(b, fill = 'darkgoldenrod', outline = 'darkgoldenrod')
 
axeButt = c.create_polygon(s, fill = 'goldenrod', outline = 'black')

axeButtShadow = c.create_polygon(d, fill = 'darkgoldenrod', outline = 'darkgoldenrod')

# Main C
blocks = c.create_rectangle(e, fill = 'lemonchiffon', outline = 'lemonchiffon')

topC = c.create_polygon(f, fill = 'lemonchiffon', outline = 'lemonchiffon')

bottomC = c.create_polygon(g, fill = 'lemonchiffon', outline = 'lemonchiffon')

# Gold inside
topGold = c.create_polygon(h, fill = 'gold', outline = 'gold')

middleGold = c.create_polygon(i, fill = 'gold', outline = 'gold')

bottomGold = c.create_polygon(j, fill = 'gold', outline = 'gold')


# Blackoutline

# Axe
axeHandleLeft = c.create_polygon(k, fill = 'white', outline = 'black')

axeHandleRight = c.create_polygon(l, fill = 'white', outline = 'black')

axeHandleMiddle = c.create_polygon(m, fill = 'black')

whiteInMiddle = c.create_arc(n, start = 110, extent = 90, fill = 'white', outline = 'white')

grey1 = c.create_line(o, fill = 'grey', width = 2)

grey2 = c.create_line(p, fill = 'grey', width = 2)

blackUnderLeft = c.create_line(q, fill = 'black', width = dubz)

blackUnderRight = c.create_line(r, fill = 'black', width = dubz)

root.mainloop()
















