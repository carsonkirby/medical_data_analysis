# Computational Thinking - Lab Activity 3
# Heart Attack Analysis
# Carson Kirby

import utilities as ut

def main():
    print("\nHeart Attack Analysis")
    print("\nThese are the factors related to heart attacks that are considered in this data: ")
    print("\t1. Heart Attack Percentage is calculated based on all data to see if the data is skewed.")
    print("\t2. Gender Percent is used to distinguish between the heart attack rates in men and women.")
    print("\t3. EKG is considered, as it detects heart problems that can forcast chance of future heart attacks.")
    print("\t4. Exercise is considered to see if likelihood of heart attack increases when physically active.")
    
    #Heart
    ut.getHeart()
    
    #Gender
    ut.getGender()
    
    #EKG
    ut.getEKG()
    
    # Perform Exercise Analysis
    ut.getExercise()
    
if __name__== "__main__":
    main()

