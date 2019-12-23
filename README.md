# Robot Tour Optimisation

## Description
This project consist in finding 3 different types of algorithm to resolve the problem of the traveling-salesman problem.

## Tech/Framework used
For this project we had to use Python 3.6 or less :
https://docs.python.org/3/library/math.html

The software we used to make this project are :
- Git : https://git-scm.com/downloads
- Visual Studio Code : https://code.visualstudio.com/
- Notable (Markdown) : https://github.com/notable/notable

## Code Style
We respect the PEP8 requirement :
http://pep8online.com/

## Solutions

### The nearest neighbor algorithm
This algorithm consist in finding the closest point of the current point. It's the fastest solution but not the best.

### The geat algorithm
This algorithm use the nearest neighbor algorithm as a model of solution and permute every point (except the first one) and verify if the solution is better than the model.
So this algorithm is better than the first one but still not the best one.

### The optimal algorithm
It generates every solution that we can find (even the worst one) by using the Tree structure and it return the best solution. So this one will find the best path but will be very slow.

## Installation
To use our program you will need `Visual Studio Code` and `Python`.

## Credit
We credit this project to Sophie SURMONT who helped us.

## Contact
If you need more informations you can contact us :
Audrey ALCARAZ :
dedealca@gmail.com 
Alexis SOK : r.alexis.sok@gmail.com
