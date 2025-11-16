### Bending Moment Diagram Generator 
### ENCMP 100 Coding Contest 
### Author: Simon Wong 
### CCID: smw2

import numpy as np                   # Numpy library for matrices, trig functions, and pi constant. 
import matplotlib.pyplot as plt      # Pyplot library for creating lines and plotting points. 
import matplotlib.patches as patches # Patches library for compositing shapes for use in  figures. 

# Entire program is designed to be modular and easily reorganized. 
# Important and/or repeated actions are contained within functions. 
def main(): 

    # This function contains numeroous strings that serve as instructions for the user. 
    # Accepts an argument (step), representing the overall progress of the program. 
    # For each possible value of (step), there is an associated string, selected using 
    # a series a of if/elif statements. 
    # Specfically for the first "step" of the program, this function prompts the user
    # to input "units" if they wish to see detials regarding units and sign convention. 
    def instructions(step): 
        welcome = ("This is a bending moment diagram template generator. \n\n"
                   "It generates a figure representing support reactions, point loads, "
                   "\nand couple moments acting on a straight beam. \n\n" 
                   "While this program does not generate either shear force or bending moment diagrams as originally planned, " 
                   "it does produce a usable free body diagram (FBD). \n\n"
                   "Enjoy! \n\n"
                   "For details regarding units and sign convention, type 'units', otherwise press enter: ")     
        details = ("\n"
                   "This program uses the following units: \n"
                   "meter (m), Newton (N), Newton-meter (N⋅m). \n\n"
                   "Sign convention is as follows: \n"
                   "Positive in the horizontal direction means to the right (→). \n"
                   "Positive in the vertical direction means upwards (↑). \n"
                   "Positive bending/couple moment means a counterclockwise torque (↺). ") 
        one = "\nEnter the length of the beam. "
        two = ("\nEnter the total number of supports. "
               "A beam with a single support will have a fixed support. "
               "A beam with two supports will have one pinned and one roller support. ")
        three = "\nEnter the type of each support ('pinned', 'roller', or 'fixed'). "  
        four = "\nEnter the location of the each support staring from the left side. "
        five = "\nVerify figure. If something is wrong, enter 'back': "   
        six = "\nEnter the total number of point forces acting on the beam. "
        seven = "\nEnter the location of each point force.. "
        eight = "\nEnter the magnitude of each point force. "
        nine = ("\nEnter the angle of each point force. "
               "Use the angle in between the top of the beam and the force's arrow. ")
        ten = ("\nEnter the total number of couple moments acting on the beam. ")
        eleven = "\nEnter the location of each couple moment. "
        twelve = "\nEnter the magnitude of each couple moment. "
        thirteen = ("\nEnter the direction of each couple moment. "
                    "\n  Positive (↺) or negative (↻). ")
        fourteen = "\nEnter 'save' to save the final figure to disk. "
        
        if step == 0:                           # Long chain of if/efif statements allows function to 
            units = input(welcome).strip()      # display appropriate/correct functions for each invocation. 
            if units == "units": 
                print(details)
        elif step == 1: 
            print(one)
        elif step == 2: 
            print(two)
        elif step == 3: 
            print(three)
        elif step == 4: 
            print(four)
        elif step == 5: 
            print(five)
        elif step == 6: 
            print(six)
        elif step == 7: 
            print(seven)
        elif step == 8: 
            print(eight)
        elif step == 9: 
            print(nine)
        elif step ==10: 
            print(ten)
        elif step == 11: 
            print(eleven)
        elif step == 12: 
            print(twelve)
        elif step == 13: 
            print(thirteen)
        elif step == 14: 
            print(fourteen)
    
    # This function is the largest and most frequently invoked function in the program. 
    # Whenever user input is required, this function is called to clean up and format input,
    # as well as verify certain restrictions on input (must be integer, must be float, etc). 
    # Different rules are applied using a long series of if statements. 
    # This function takes three arguments (rule,i,extra). 
    # (rule) corresponds to the specific rules and restrictions that should be applied to a 
    # given user input. Everytime the check function is invoked, a unique string is passed 
    # representing the rule to be applied.
    # (i) passes the index of the invocation, if applicable. This allows user prompts to better
    # suit the context of the input. 
    # (extra) is an argument for passing additional information involved in the accurate cleaning 
    # and formatting of input. 
    # Function returns a single value, called (value). 
    def check(rule,i,extra):
        if rule == "Len1": # Length of beam. 
            valid = False
            while valid is False: 
                value = input("  Length of beam: ").strip()
                if value.replace(".","").isnumeric(): 
                    value = float(value)
                    valid = True
                else: 
                    print("\n  Enter a positive number with '.' as decimal point.")
        if rule == "Sup1": # Number of supports. 
            valid = False
            while valid is False: 
                value = input("  Number of supports: ").strip()
                if value.isnumeric(): 
                    if 1 <= float(value) <= 2: 
                        value = int(value)
                        valid = True 
                    else: 
                        print("  Enter either 1 or 2. ")
                else: 
                    print("  Enter either 1 or 2. ")          
        if rule == "Sup2": # Types of supports. 
            valid = False
            while valid is False: 
                if extra == 1: 
                    value = input("  Type of support #%s: " % str(i+1))
                    if value == "fixed": # Verifies that user input is "fixed". 
                        valid = True
                    else: 
                         print("  Only one support: must be 'fixed'. ")
                if extra == 2: 
                    value = input("  Type of support #%s: " % str(i+1))
                    if value in ["roller","pinned"]: # Verifies that user input is "roller" or "pinned".
                        valid = True 
                    else: 
                        print("  Two supports: one pinned and one roller. ")
        if rule == "Sup3": # Locations of supports. 
            valid = False 
            while valid is False: 
                value = input("  Location of support #%s: " % str(i+1)).strip()
                if value.replace(".","").isnumeric(): 
                    if 0 <= float(value) <= beamLength: 
                        value = float(value)
                        valid = True 
                    else: 
                         print("  Enter a positive number between zero and beam length. ")    
                else: 
                    print("  Enter a positive number between zero and beam length. ")
        if rule == "Points1": # Number of point forces. 
            valid = False 
            while valid is False: 
                value = input("  Number of point forces: ").strip()
                if value.isnumeric(): 
                    value = int(value)
                    valid = True 
                else: 
                    print("  Enter a positive whole number. ")
        if rule == "Points2": # Locations of point forces. 
            valid = False 
            while valid is False: 
                value = input("  Location of point force #%s: " % str(i+1)).strip()
                if value.replace(".","").isnumeric(): 
                    if 0 <= float(value) <= beamLength: 
                        value = float(value)
                        valid = True
                    else: 
                        print("  Enter a positive number between zero and beam length. ")
                else: 
                    print("  Enter a positive number between zero and beam length. ")        
        if rule == "Points3": # Magnitude of point forces. 
            valid = False 
            while valid is False: 
                value = input("  Magnitude of point force #%s: " % str(i+1)).strip()
                if value.replace(".","").isnumeric(): 
                    value = float(value)
                    valid = True
                else: 
                    print("  Enter a positive number. ")      
        if rule == "Points4": # Angle of point forces. 
            valid = False 
            while valid is False: 
                value = input("  Angle of point force #%s: " % str(i+1)).strip()
                if value.replace(".","").isnumeric(): # Verifies that user input is an angle (between 0 and 360). 
                    if 0 <= float(value) <= 360: 
                        value = float(value)
                        valid = True 
                    else: 
                        print("  Enter a positive number between 0 and 360. ")
                else: 
                    print("  Enter a positive number between 0 and 360. ")     
        if rule == "Couples1": # Number of couple moments. 
            valid = False 
            while valid is False: 
                value = input("  Number of couple moments: ").strip()
                if value.isnumeric(): 
                    value = int(value)
                    valid = True
                else: 
                    print("Enter a positive whole number. ")
        if rule == "Couples2": # Locations of couple moments. 
            valid = False 
            while valid is False: 
                value = input("  Location of couple moment #%s: " % str(i+1)).strip()
                if value.replace(".","").isnumeric(): 
                    if 0 <= float(value) <= beamLength: 
                        value = float(value)
                        valid = True
                    else: 
                        print("  Enter a positive number between zero and beam length. ")
                else: 
                    print("  Enter a positive number between zero and beam length. ")  
        if rule == "Couples3": # Magnitude of couples moments. 
            valid = False
            while valid is False: 
                value = input("  Magnitude of couple moment #%s: " % str(i+1)).strip()
                if value.replace(".","").isnumeric():
                    value = float(value)
                    valid = True 
                else: 
                    print("  Enter a positive number. ")
        if rule == "Couples4": # Direction of couple moments. 
            valid = False 
            while valid is False: 
                value = input("  Direction of couple moment #%s: " % str(i+1)).strip()
                if value in ["positive","negative"]: # Verifies that user input is either "positive" or "negative'. 
                    if value == "positive": 
                        value = +1
                    if value == "negative":
                        value = -1
                    value = int(value)
                    valid = True
                else: 
                    print("  Enter either 'positive' or 'negative' as the couple moment direction. ")
        return(value)
                
    # Obtains beam length from user by invoking instructions and check. 
    # Returns sing value (beamLength). 
    def length(): 
        instructions(1)                         # Step 1. 
        beamLength = check("Len1",0,0)
        return(beamLength)
    
    # Obtains support information from user by invoking instructions and check
    # functions multiple times. 
    # Makes use of two for loops to iterate for as many times as there are supports. 
    # Takes an argument (beamLength), which is subsequently passed to the check function. 
    # Returns two lists, containing the locations and types of supports
    def supports(beamLength): 
        instructions(2)                         # Step 2. 
        numSupports = check("Sup1",0,0)
        locations = []
        instructions(3)                         # Step 3. 
        for i in range(numSupports): 
            locations.append(check("Sup2",i,numSupports))
        types = []
        instructions(4)                         # Step 4. 
        for i in range(numSupports): 
            types.append(check("Sup3",i,0))          
        return(locations,types)
    
    # This functions takes previously obtained beam length and supports information as input. 
    # Creates a new figure using Pyplot, with invisible y-axis, and specifc scales and dimensions. 
    # The value of beam length is used to scale the x-axis using plt.xlim, 
    # (H) is a parameter controlling the vertical postion of all elements in the figure. 
    # as well as any plotted points (using a beam length as a scaling factor). 
    # Uses Patches to create a rectangle representing the beam.
    # Uses Patches to add either a triangle, square, or circle depending on the type of support. 
    # Annotates the figure with the type of support (fixed, pinned, or roller). 
    # Uses Pyplot to add vertical lines, which would make shear force and bending moment 
    # diagrams easier to draw. 
    # Adds title and x-axis title (incorporating value of beam length). 
    # Displays plotted figure to user. 
    def plot1(beamLength,supportData,H): 
        fig, ax = plt.subplots()
        ax.axes.get_yaxis().set_visible(False)
        if len(supportData[0]) == 1: 
            x = float(supportData[1][0])
            y = H-0.1
            ax.plot(x,y,marker="s",markeredgecolor="none",markerfacecolor="red",markersize=20) # Adds fixed support. 
        if len(supportData[0]) == 2: 
            x = float(supportData[1][0])
            y = H-0.1
            if supportData[0][0] == "roller": 
                mark = "o"
            else: 
                mark = "^"
            ax.plot(x,y,marker=mark,markeredgecolor="none",markerfacecolor="red",markersize=20) # Adds roller/pinned support. 
            x = float(supportData[1][1])
            y = H-0.1
            if supportData[0][1] == "roller": 
                mark = "o"
            else: 
                mark = "^"
            ax.plot(x,y,marker=mark,markeredgecolor="none",markerfacecolor="red",markersize=20) # Adds roller/pinned support. 
        for i in range(len(supportData[0])): 
            plt.annotate(supportData[0][i], (float(supportData[1][i])+5,H-0.125))
        plt.xlim((-0.1*beamLength,beamLength+0.1*beamLength)) # Sets x-axis bounds based on beam length. 
        plt.ylim((0,1))                                       # Sets y-axis bounds. 
        beam = patches.Rectangle((0,H-0.05),beamLength,0.1,linewidth=5,edgecolor='C0',facecolor='none') 
        ax.add_patch(beam) # Defines rectangle representing beam. 
        plt.title("Bending Moment Diagram Template")
        plt.xlabel("Length of the beam is %.2f m" % beamLength)
        plt.axvline(x=0, color="black", linestyle="dashed")
        for i in range(len(supportData[1])):
            plt.axvline(x=float(supportData[1][i]), color="black", linestyle="dashed") # Adds vertical liness. 
        plt.axvline(x=beamLength, color="black", linestyle="dashed")
        plt.show()
        return()
     
    # This function prompts the user to verify the generated figure. 
    # By entering "back", the user may reinput beam length and supports information. 
    # Returns a boolean value (good), determining whether the program should continue. 
    def confirm(): 
        instructions(5)                         # Step 5. 
        if input() == "back": 
            good = False
        else: 
            good = True
        return(good)
    
    # Obtains point forces information from user by invoking instructions and check functions. 
    # Makes use of three for loops to iterate for as many times as there are point forces. 
    # Takes an argument (beamLength), which is subsequently passed to the check function. 
    # Returns three lists, containg point force locations, magnitudes, and angles. 
    def pointForces(beamLength):
        instructions(6)                         # Step 6. 
        numPoints = check("Points1",0,0)
        instructions(7)                         # Step 7. 
        locations = []
        for i in range(numPoints): 
            locations.append(check("Points2",i,0))
        instructions(8)                         # Step 8. 
        magnitudes = []
        for i in range(numPoints):
            magnitudes.append(check("Points3",i,0))
        instructions(9)                         # Step 9. 
        angles = []
        for i in range(numPoints):
            angles.append(check("Points4",i,0))
        return(locations,magnitudes,angles)
    
    # Repeats everything done by plot1 function. 
    # Takes four arguments, which are used to position visual elements. 
    # Adds arrows and annotations representing point forces. 
    # Makues use of Numpy cos() and sin() functions to correctly orient arrows. 
    # Adds vertical lines at locations of point forces to facilitate diagram interpretation. 
    # Displays plotted figure to user. 
    def plot2(beamLength,pointData,supportData,H): 
        fig, ax = plt.subplots()
        ax.axes.get_yaxis().set_visible(False)
        if len(supportData[0]) == 1: 
            x = float(supportData[1][0])
            y = H-0.1
            ax.plot(x,y,marker="s",markeredgecolor="none",markerfacecolor="red",markersize=20)
        if len(supportData[0]) == 2: 
            x = float(supportData[1][0])
            y = H-0.1
            if supportData[0][0] == "roller": 
                mark = "o"
            else: 
                mark = "^"
            ax.plot(x,y,marker=mark,markeredgecolor="none",markerfacecolor="red",markersize=20)
            x = float(supportData[1][1])
            y = H-0.1
            if supportData[0][1] == "roller": 
                mark = "o"
            else: 
                mark = "^"
            ax.plot(x,y,marker=mark,markeredgecolor="none",markerfacecolor="red",markersize=20)
        for i in range(len(supportData[0])): 
            plt.annotate(supportData[0][i], (float(supportData[1][i])+5,H-0.125))
        plt.xlim((-0.1*beamLength,beamLength+0.1*beamLength))
        plt.ylim((0,1))
        beam = patches.Rectangle((0,H-0.05),beamLength,0.1,linewidth=5,edgecolor='C0',facecolor='none') 
        ax.add_patch(beam)
        plt.title("Bending Moment Diagram Template")
        plt.xlabel("Length of the beam is %.2f m" % beamLength)
        plt.axvline(x=0, color="black", linestyle="dashed")
        for i in range(len(supportData[1])):
            plt.axvline(x=float(supportData[1][i]), color="black", linestyle="dashed")
        plt.axvline(x=beamLength, color="black", linestyle="dashed")
        # End of plot1. 
        for i in range(len(pointData[0])): # Iterates for however many point forces there are. 
            plt.annotate(("" % pointData[1][i]), 
                         xytext = (pointData[0][i]+(0.25*beamLength*np.cos(pointData[2][i]*np.pi/180)),
                                   H+0.25*np.sin(pointData[2][i]*np.pi/180) ),
                         # Computes coordinates of arrow start and end using trigononmetry, beam length, 
                         # and point force location. 
                         xy = ( pointData[0][i] , H ), 
                         arrowprops = dict(arrowstyle='->', lw=3)) # Adds arrows with angles and annotations). 
        for i in range(len(pointData[0])): 
            plt.axvline(x=float(pointData[0][i]), color ="black",linestyle="dotted") # Adds vertical lines. 
            plt.annotate((str(pointData[1][i])+" N"), (float(pointData[0][i]),H-0.02)) 
        plt.show()
        return()

    # Obtains couple moments information from user by invoking instructions and check functions. 
    # Makes use of three for loops to iterate for as many times as there are couple moments. 
    # Takes an argument (beamLength), which is subsequently passed to the check function. 
    # Returns three lists, containg couple moment locations, magnitudes, and directions. 
    def coupleMoments(beamLength): 
        instructions(10)                         # Step 10. 
        numCouples = check("Couples1",0,0)
        instructions(11)                         # Step 11. 
        locations = []
        for i in range(numCouples): 
            locations.append(check("Couples2",i,0))
        instructions(12)                         # Step 12. 
        magnitudes = [] 
        for i in range(numCouples): 
            magnitudes.append(check("Couples3",i,0))
        instructions(13)                         # Step 13. 
        directions = [] 
        for i in range(numCouples): 
            directions.append(check("Couples4",i,0))
        values = []
        for i in range(numCouples):
            values.append(magnitudes[i]*directions[i])
        return(locations,values)
    
    # Repeats everything done by plot1 and plot2 functions. 
    # Takes five arguments, which are used to position visual elements. 
    # Uses Patches to draw circles and triangles representing couple moments. 
    # Annotates figure with magnitudes of each couple moment. 
    # Adds vertical lines at locations of couple moments to facilitate diagram interpretation. 
    # Displays plotted figure to user. 
    # At the end of this function as invoked by main(), the program has almost completed running. 
    # Prompts user to enter "save", if they wish to save an image (.png file) of the final figure. 
    def plot3(beamLength,supportData,pointData,coupleData,H):
        fig, ax = plt.subplots()
        ax.axes.get_yaxis().set_visible(False)
        if len(supportData[0]) == 1: 
            x = float(supportData[1][0])
            y = H-0.1
            ax.plot(x,y,marker="s",markeredgecolor="none",markerfacecolor="red",markersize=20)
        if len(supportData[0]) == 2: 
            x = float(supportData[1][0])
            y = H-0.1
            if supportData[0][0] == "roller": 
                mark = "o"
            else: 
                mark = "^"
            ax.plot(x,y,marker=mark,markeredgecolor="none",markerfacecolor="red",markersize=20)
            x = float(supportData[1][1])
            y = H-0.1
            if supportData[0][1] == "roller": 
                mark = "o"
            else: 
                mark = "^"
            ax.plot(x,y,marker=mark,markeredgecolor="none",markerfacecolor="red",markersize=20)
        for i in range(len(supportData[0])): 
            plt.annotate(supportData[0][i], (float(supportData[1][i])+5,H-0.125))
        plt.xlim((-0.1*beamLength,beamLength+0.1*beamLength))
        plt.ylim((0,1))
        beam = patches.Rectangle((0,H-0.05),beamLength,0.1,linewidth=5,edgecolor='C0',facecolor='none')
        ax.add_patch(beam)
        plt.title("Bending Moment Diagram Template")
        plt.xlabel("Length of the beam is %.2f m" % beamLength)
        plt.axvline(x=0, color="black", linestyle="dashed")
        for i in range(len(supportData[1])):
            plt.axvline(x=float(supportData[1][i]), color="black", linestyle="dashed")
        plt.axvline(x=beamLength, color="black", linestyle="dashed")
        # End of plot1. 
        for i in range(len(pointData[0])): 
            plt.annotate(("" % pointData[1][i]), 
                         xytext = (pointData[0][i]+(0.25*beamLength*np.cos(pointData[2][i]*np.pi/180)), 
                                   H+0.25*np.sin(pointData[2][i]*np.pi/180) ),
                         xy = ( pointData[0][i] , H ), 
                         arrowprops = dict(arrowstyle='->', lw=3))
        for i in range(len(pointData[0])): 
            plt.axvline(x=float(pointData[0][i]), color ="black",linestyle="dotted")
            plt.annotate((str(pointData[1][i])+" N"), (float(pointData[0][i]),H-0.02))
        # End of plot2. 
        for i in range(len(coupleData[0])): 
            ellipse = patches.Ellipse(xy=(coupleData[0][i],H),
                                      width=beamLength*0.15, height=0.19,
                                      edgecolor="black",facecolor="none",lw=2) # Defines ellipse representing torque of couple. 
            x = coupleData[0][i]
            if abs(coupleData[1][i])==(coupleData[1][i]): 
                triangle = patches.Polygon([[x-3,H+0.09],[x+3,H+0.12],[x+3,H+0.06]], # Defines triangle for positive couple. 
                                           closed=True,
                                           facecolor="black")
            if abs(coupleData[1][i])!=(coupleData[1][i]): 
                 triangle = patches.Polygon([[x+3,H+0.09],[x-3,H+0.12],[x-3,H+0.06]], # Defines triangle for negative couple. 
                                            closed=True, facecolor="black")   
            ax.add_patch(ellipse)
            ax.add_patch(triangle)
            for i in range(len(coupleData[0])): 
                plt.axvline(x=float(coupleData[0][i]), color ="black",linestyle="dotted")
                plt.annotate((str(coupleData[1][i])+" N⋅m"), (float(coupleData[0][i]),H+0.15))
        instructions(14)                         # Step 14. 
        if input().strip() == "save": 
            plt.savefig("BendingMomentDiagramTemplate.png") # Saves figure to working directory with specified filename. 
        plt.show()
      
    # The code below also part of main(), just as the above functions are. 
    # This is where all functions are invoked as subfunctions within main(). 
    HEIGHT = 0.5
    instructions(0)                         # Step 0. 
    good1 = good2 = good3 = False    
    while good1 is False: 
        beamLength = length()
        supportData = np.row_stack(supports(beamLength)) # Creates a 2 by n matrix using Numpy. 
        plot1(beamLength,supportData,HEIGHT) 
        good1 = confirm()                                # Confirms if user wants to continue. 
    while good2 is False: 
        pointData = np.row_stack(pointForces(beamLength)) # Creates a 3 by n matrix using Numpy. 
        plot2(beamLength,pointData,supportData,HEIGHT) 
        good2 = confirm()                                 # Confirms if user wants to continue. 
    while good3 is False:
        coupleData = np.row_stack(coupleMoments(beamLength)) # Creates a 3 by n matrix using Numpy. 
        plot3(beamLength,supportData,pointData,coupleData,HEIGHT)
        good3 = confirm()                                    # Confirms if user wants to continue. 
    
main() # Invokes all above code, running the program in its entirety. 
                