"""
TODO: Paramaterise screen size.
Screen is assumed to be 1920 X 1080.

Things that are possible with this.
1 Place N visuals with X gaps between them.
2 Place a Card at Position X,Y with size W,H 
"""
import pyautogui as r


debug = False
safe = True
def function1(h=0,w=0,x=0,y=0,visual="card"): 

    if safe:r.alert("function1")
    r.doubleClick(77,195)
    r.click(1901,193)
    r.click(1671,307)
    r.click(1717,341)
    r.click(1901,193)

    height = str(h)
    width = str(w)
    horizontal = str(x)
    vertical = str(y)


    visual_menu_position = {"card":(1761,480) ,"bar": (1713,355)}
    r.click(visual_menu_position[visual][0],visual_menu_position[visual][1])

    r.click(1735,277)

    r.click(1735,413)

    r.click(1621,481)

    r.click(1639,619)
    r.hotkey('ctrl','a')
    r.hotkey('delete')
    r.write(height) 

    r.click(1643,697)
    r.hotkey('ctrl','a')
    r.hotkey('delete')
    r.write(width)

    r.click(1633,811)

    r.click(1647,891)
    r.hotkey('ctrl','a')
    r.hotkey('delete')
    r.write(horizontal)

    r.click(1639,969)
    r.hotkey('ctrl','a')
    r.hotkey('delete')
    r.write(vertical)



if __name__ == "__main__":
    x=20
    Y=100
    width=100
    height=100
    gap=10
    gaap=30

    #Card1
    print("Card placed at:",x,Y)
    function1(height,width,x,Y,"card")
    x+=width+gap
    #Card2
    print("Card placed at:",x,Y)
    function1(height,width,x,Y,"card")
    #Card3
    x+=width+gaap
    print("Card placed at:",x,Y)
    function1(height,width,x,Y,"card")
    #Card4
    x+=width+gap
    print("Card placed at:",x,Y)
    function1(height,width,x,Y,"card")