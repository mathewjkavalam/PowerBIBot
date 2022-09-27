"""
offsetHeight,offsetWidth,offsetLeft,offsetTop are the css properties to be extracted.
Use browser dev tools to get theses properties of each div
"""
import re

css = """
offsetHeight
: 
229
offsetLeft
: 
18
offsetParent
: 
body
offsetTop
: 
306
offsetWidth
: 
331
"""
res = re.findall(r"\d+",css)
h,w,x,y = res[0],res[-1],res[1],res[2]
print("CDX "+h+","+w+","+x+","+y)