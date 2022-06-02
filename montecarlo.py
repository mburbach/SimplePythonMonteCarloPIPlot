import sys
import random as r
import math as m
import matplotlib.pyplot as plot
import numpy as np

# creates plot and save it to the given imagePath as montecarlo.png
def makePlot( xArray, yArray, imagePath ):
    xPi = np.linspace( 3.14159265359, 3.14159265359 )
    yPi = np.linspace( 10, total )
    fig, ax = plot.subplots()
    ax.scatter( xArray, yArray, s=10,label="Iteration Result", color='tab:green' )
    ax.plot( xPi, yPi, label="PI Line", color='tab:red' )
    ax.set_ylabel( 'Iteration', loc='top')
    ax.set_xlabel('result of iteration')
    ax.set_title('Monte Carlo Plot')
    ax.legend()
    ax.set_facecolor('black')
    ax.grid()
    fig.savefig( imageName )
    plot.show()

def main():
    inside = 0
    xArray = []
    yArray = []
    #print( "3.14159265359" )
    for i in range(1, total+1):
        x2 = r.random()**2
        y2 = r.random()**2
        if(  m.sqrt(x2 + y2) < 1.0) :
            inside += 1

        if( ( i % dotPointsAt ) == 0 ):
            yArray.append( i )
            pi = (float(inside) / i ) * 4
            xArray.append( pi ) 
# comment out if you want to see the values of each dot
#            print( "i = " + str( i)  )
#            print( "pi = "+ str( pi ) )


    makePlot( xArray, yArray, '' )


if __name__ == '__main__':
    total = 100000
    dotPointsAt = 2000


    imagePath = ''
    imageName = 'montecarlo.png'
    try: 
        total = int( sys.argv[1] )
        dotPointsAt = int( sys.argv[2] )
    except IndexError:
        print( 'Usage: montecarlo.py <total value of y> <every given value a dot>' )
        print( 'Example: montecarlo.py 100000 2000 ' )
        print( 'Now working with default values.' )
        
    main()

    print( "Done. You would find your image as montecarlo.png" )
