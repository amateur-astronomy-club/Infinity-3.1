import pygame
import requests

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def prin(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10
    

pygame.init()
 
# Set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()
    
# Get ready to print
textPrint = TextPrint()

e=0

Axis=[]
if __name__ == '__main__':

    # -------- Main Program Loop -----------
    while done==False:
        
        # EVENT PROCESSING STEP
        for event in pygame.event.get(): # User did something
            e=e+1
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            
            # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
            if event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")
            #if event.type == pygame.JOYAXISMOTION:
    #            print("Joystick axis moved")     
        # DRAWING STEP
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)
        textPrint.reset()

        # Get count of joysticks
        joystick_count = pygame.joystick.get_count()

        textPrint.prin(screen, "Number of joysticks: {}".format(joystick_count) )
        textPrint.indent()
        
        # For each joystick:
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
        
            textPrint.prin(screen, "Joystick {}".format(i) )
            textPrint.indent()
        
            # Get the name from the OS for the controller/joystick
            name = joystick.get_name()
            textPrint.prin(screen, "Joystick name: {}".format(name) )
            
            # Usually axis run in pairs, up/down for one, and left/right for
            # the other.
            axes = joystick.get_numaxes()
            textPrint.prin(screen, "Number of axes: {}".format(axes) )
            textPrint.indent()
            
            
            A=[]
            for i in range( axes ):
                axis = joystick.get_axis( i )
                textPrint.prin(screen, "Axis {} value: {:>6.3f}".format(i, axis) )
                A.append(axis)
            textPrint.unindent()
            A = ["%6.3f" % mem for mem in A]
            A = [float(j) for j in A]
            #print A
            Axis.append(A)


            #FOR JOYSTICK: 
            #Axis1: Moving front and back
            #Axis3: Moving left and right
            #Axis2: Controlling the speed
            #For the gamepad axis 0 is left right and axis 1 is front and back
            if(A[2]<0):
                A[2]=A[2]*(-1)

            
            if A[3] < 0:
                url='http://192.168.43.110:8002/left/%s' %(A[2])
                r = requests.get(url)
                print(r,"Left movement")
                
            elif A[3] > 0:
                url='http://192.168.43.110:8002/right/%s' %(A[2])
                r = requests.get(url)
                print(r,"Right Movement")

            elif A[1] < 0:     
                url='http://192.168.43.110:8002/forward/%s' %(A[2])
                r = requests.get(url)
                print(r,"Foward Movement")
                
            elif A[1] > 0:
                url='http://192.168.43.110:8002/backward/%s' %(A[2])
                r = requests.get(url)
                print(r,"Backward Movement")
                
                
            else:
                r = requests.get('http://192.168.43.110:8002/stop')
                print(r,"Stop the motors")


            buttons = joystick.get_numbuttons()
            textPrint.prin(screen, "Number of buttons: {}".format(buttons) )
            textPrint.indent()

            for i in range( buttons ):
                button = joystick.get_button( i )
                textPrint.prin(screen, "Button {:>2} value: {}".format(i,button) )
            textPrint.unindent()
                
            # Hat switch. All or nothing for direction, not like joysticks.
            # Value comes back in array.
            hats = joystick.get_numhats()
            textPrint.prin(screen, "Number of hats: {}".format(hats) )
            textPrint.indent()

            for i in range( hats ):
                hat = joystick.get_hat( i )
                textPrint.prin(screen, "Hat {} value: {}".format(i, str(hat)) )
            textPrint.unindent()
            
            textPrint.unindent()

    
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 20 frames per second
        clock.tick(20)
        
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit ()
