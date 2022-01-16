x = 200
y = 200
def setup():
    size(600,600)
    rectMode(CENTER)
def draw():
    background(255,255,255)
    fill(255,25,0)
    if mousePressed:
        if mouseX > (x-25) and mouseX < (x+25) and mouseY > (y-25) and mouseY < (y+25): 
            mouseDragged()
    rect(x,y,50,50)
def mouseDragged():
  global x , y
  x = mouseX
  y = mouseY  
  if x > width:
       x = width
  if x < 0:
      
    
    
    
    
    
    
    
    
    
    
    
