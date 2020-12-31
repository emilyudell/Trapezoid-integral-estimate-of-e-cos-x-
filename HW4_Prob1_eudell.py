# HW4 Programming Problem 1
# File: hw4_prob1_eudell.py
# Date: 30 September 2020
# By: Emily Udell
# Login Id: eudell
#
#
# ELECTRONIC SIGNATURE
# Emily Udell
#
# The electronic signature above indicates that the program
# submitted for evaluation is my individual work. I have
# a general understanding of all aspects of its development
# and execution.
#
# This program calculates the trapezoid estimate of the integral of e^cos(x) 
#given the values of the upper and lower bounds as wlel as a convergence 
#criteria.
#

import math
#---------------------------------------------------
#  
#---------------------------------------------------
lowerA = float(input(" Enter the lower bound: "))
upperB = float(input(" Enter the upper bound: "))
converV = float(input(" Enter the convergence criterion value: "))

if lowerA>=upperB:
    print ("Error: lower bound greater than upper bound")
#check that lower bound is less than the upper bound
else: 
    if converV<=0.0:
        print("Error: convergence value less than zero")
#check that convergence value is greater than zero
    else: 
        
        exponentA = math.cos(lowerA)
        exponentB = math.cos(upperB)
        flowerA = math.exp(exponentA)
        fupperB = math.exp(exponentB)
        N=3 #N=3 will be the first variable term as newTerm and oldterm known
        xSubK= lowerA + (1 * ((upperB-lowerA)/2))
        newTerm= ((upperB-lowerA)/4)*(flowerA + 2*(math.exp(math.cos(xSubK)))
                                      + fupperB)
        oldTerm= (flowerA + fupperB) * ((upperB-lowerA)/2)
#---------------------------------------------------
#  Calculations
#---------------------------------------------------        
     
        while((abs(newTerm-oldTerm)) > converV): #checks for converV
           oldTerm = newTerm #old term gets replaced by new for check
           deltaX = (upperB-lowerA)/N
           fXCollector = 0
           for i in range (1, N): 
               xK = lowerA + (i * deltaX)
               fXK = math.exp(math.cos(xK))
               fXCollector = fXCollector + fXK #adds for loop values
           newTerm= deltaX/2 * (flowerA + (2*(fXCollector))+ fupperB)
           N = N+1
 #---------------------------------------------------
#  Outputs
#---------------------------------------------------       
finalAnswer = round(newTerm,6)
print("The integral is: ", finalAnswer)
            