"""
TODO: Paramaterise screen size.
Screen is assumed to be 1920 X 1080.

Things that are possible with this.
1 Place N visuals with X gaps between them.
2 Place a Card at Position X,Y with size W,H 
"""
import pyautogui as r


debug = False

def function1(h=0,w=0,x=0,y=0,visual="card"): 
    if debug: r.alert("Start")
    r.doubleClick(77,195)
    r.click(1901,193)
    r.click(1671,307)
    r.click(1717,341)
    r.click(1901,193)

    height = str(h)
    width = str(w)
    horizontal = str(x)
    vertical = str(y)

    if debug : r.alert("Create Card?")
    visual_menu_position = {"card":(1761,480) ,"bar": (1713,355)}
    r.click(visual_menu_position[visual][0],visual_menu_position[visual][1])
    if debug : r.alert("Properties?")
    r.click(1735,277)
    if debug : r.alert("General?")
    r.click(1735,413)
    if debug : r.alert("Properties?")
    r.click(1621,481)
    if debug : r.alert("Height as:"+height)
    r.click(1639,619)
    r.hotkey('ctrl','a')
    r.hotkey('delete')
    r.write(height) 
    if debug : r.alert("Width as:"+width)
    r.click(1643,697)
    r.hotkey('ctrl','a')
    r.hotkey('delete')
    r.write(width)
    if debug : r.alert("Position")
    r.click(1633,811)
    if debug : r.alert("Horizontal as:"+horizontal)
    r.click(1647,891)
    r.hotkey('ctrl','a')
    r.hotkey('delete')
    r.write(horizontal)
    if debug : r.alert("Vertical as:"+vertical)
    r.click(1639,969)
    r.hotkey('ctrl','a')
    r.hotkey('delete')
    r.write(vertical)

r.alert("Start")
# function1(200,200,50,100,"bar")
function1(200,200,50,300,"card")