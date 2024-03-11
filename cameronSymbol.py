from tkinter import*

root = Tk()
root.geometry('300x300')
root.title('Cameron')
c = Canvas(root, bg = 'hotpink', height = 300 , width = 300)
c.pack()
dubz = 7


#-----------------------------------------------------------
# Woodhandle
polygon_points = [(132, 105), (155, 100), (206, 180), (198, 205)]
woodHandle = c.create_polygon(polygon_points, fill = 'goldenrod', outline = 'black')

polygon_points = [(133, 105), (142, 100), (200, 185), (200, 205)]
woodHandleShadow = c.create_polygon(polygon_points, fill = 'darkgoldenrod', outline = 'darkgoldenrod')

polygon_points = [(218, 235), (233, 225), (251, 245), (255, 250), (251, 255), (250, 255), (245, 258), (233, 255)] 
axeButt = c.create_polygon(polygon_points, fill = 'goldenrod', outline = 'black')

polygon_points = [(220, 235), (222, 225), (245, 256), (235, 255)]
axeButtShadow = c.create_polygon(polygon_points, fill = 'darkgoldenrod', outline = 'darkgoldenrod')

# Main C
coord = 220, 38, 260, 125
blocks = c.create_rectangle(coord, fill = 'lemonchiffon', outline = 'lemonchiffon')

polygon_points = [(40, 75), (100, 38), (195, 38), (220, 50), (220, 115), (180, 80), (130, 80), (130, 175), (100, 250), (40, 215)]
topC = c.create_polygon(polygon_points, fill = 'lemonchiffon', outline = 'lemonchiffon')

polygon_points = [(130, 175), (150, 195), (185, 195), (220, 175), (220, 160), (260, 160), (260, 215), (195, 250), (100, 250)]
bottomC = c.create_polygon(polygon_points, fill = 'lemonchiffon', outline = 'lemonchiffon')

# Gold inside
polygon_points = [(195, 60), (240, 75), (240, 100)]
topGold = c.create_polygon(polygon_points, fill = 'gold', outline = 'gold')

polygon_points = [(60, 80), (110, 55), (110, 200), (140, 225), (100, 225), (60, 200)]
middleGold = c.create_polygon(polygon_points, fill = 'gold', outline = 'gold')

polygon_points = [(195, 215), (235, 190), (235, 175), (240, 175), (240, 195)]
bottomGold = c.create_polygon(polygon_points, fill = 'gold', outline = 'gold')


# Blackoutline
coord = 38, 75, 100, 38
blackOutline = c.create_line(coord, fill = 'black', width = dubz)

coord = 40, 73, 40, 218
blackOutline1 = c.create_line(coord, fill = 'black', width = dubz)

coord = 40, 215, 100, 250
blackOutline2 = c.create_line(coord, fill = 'black', width = dubz)

coord = 98, 250, 195, 250
blackOutline3 = c.create_line(coord, fill = 'black', width = dubz)

coord = 193, 250, 260, 215
blackOutline4 = c.create_line(coord, fill = 'black', width = dubz)

coord = 260, 218, 260, 160
blackOutline5 = c.create_line(coord, fill = 'black', width = dubz)

coord = 263, 160, 220, 160
blackOutline6 = c.create_line(coord, fill = 'black', width = dubz)

coord = 220, 157 , 220, 175
blackOutline7 = c.create_line(coord, fill = 'black', width = dubz)

coord = 223, 175, 180, 195
blackOutline8 = c.create_line(coord, fill = 'black', width = dubz)

coord = 182, 195, 150, 195
blackOutline9 = c.create_line(coord, fill = 'black', width = dubz)

coord = 152, 195, 130, 175
blackOutline10 = c.create_line(coord, fill = 'black', width = dubz)

coord = 130, 177, 130, 80
blackOutline11 = c.create_line(coord, fill = 'black', width = dubz)

coord = 127, 80, 180, 80
blackOutline12 = c.create_line(coord, fill = 'black', width = dubz)

coord = 182, 195, 150, 195
blackOutline13 = c.create_line(coord, fill = 'black', width = dubz)

coord = 178, 78, 219, 115
blackOutline14 = c.create_line(coord, fill = 'black', width = dubz)

coord = 219, 112, 219, 128
blackOutline15 = c.create_line(coord, fill = 'black', width = dubz)

coord = 216, 128, 260, 128
blackOutline16 = c.create_line(coord, fill = 'black', width = dubz)

coord = 260, 131, 260, 38
blackOutline17 = c.create_line(coord, fill = 'black', width = dubz)

coord = 263, 38, 218, 38
blackOutline18 = c.create_line(coord, fill = 'black', width = dubz)

coord = 218, 35, 218, 50
blackOutline19 = c.create_line(coord, fill = 'black', width = dubz)

coord = 221, 50, 190, 38
blackOutline20 = c.create_line(coord, fill = 'black', width = dubz)

coord = 191, 38, 99, 38
blackOutline21 = c.create_line(coord, fill = 'black', width = dubz)

# Axe
polygon_points = [(60, 200), (70, 165), (115, 85), (130, 90), (65, 205)]
axeHandleLeft = c.create_polygon(polygon_points, fill = 'white', outline = 'black')

polygon_points = [(130, 75), (215, 35), (220, 40), (135, 92)]
axeHandleRight = c.create_polygon(polygon_points, fill = 'white', outline = 'black')

polygon_points = [(105, 80), (135, 65), (145, 65), (155, 100), (135, 110)]
axeHandleMiddle = c.create_polygon(polygon_points, fill = 'black')

coord = 138, 115, 155, 80
whiteInMiddle = c.create_arc(coord, start = 110, extent = 90, fill = 'white', outline = 'white')

coord = 115, 80, 125, 80
grey1 = c.create_line(coord, fill = 'grey', width = 2)

coord = 125, 80, 145, 69
grey2 = c.create_line(coord, fill = 'grey', width = 2)

coord = 65, 205, 130, 90
blackUnderLeft = c.create_line(coord, fill = 'black', width = dubz)

coord = 150, 85, 220, 40
blackUnderRight = c.create_line(coord, fill = 'black', width = dubz)





















