# Author: Lakshmi Nikhil Goduguluri
# Date: 02/19/2023
# Description: This program finds the minimum number of stops required to cover a given distance with a given maximum distance that can be covered in a single stop

def min_stops(d,m):
    # greedy approach
    stops=0
    prev_stop=0
    i=0
    # check if there is a gap greater than m, as it is not possible to cover such a gap
    for i in range(1,len(d)):
        if(d[i]-d[i-1])>m:
            return -1
    i=0
    while(i<len(d)):
        if(d[i]-d[prev_stop]<=m): 
            # if the distance between the current stop and the previous stop is less than m, then we can continue
            i+=1   
        else:
            # if the distance between the current stop and the previous stop is greater than m, 
            # then we need to stop at the destination before the current stop
            stops+=1
            prev_stop=i-1
    return stops+1 # +1 because we need to stop at the last stop


def main():
    print('\nd=[0,2,3,4,5,6,7,8,9,10]')
    print('m=3')
    d=[0,2,3,4,5,6,7,8,9,10]
    m=3
    print(f"Testcase 1: {min_stops(d,m)}")

    print('\nd=[0,2,4,6,9]')
    print('m=2')
    d=[0,2,4,6,9]
    m=2
    print(f"Testcase 2: {min_stops(d,m)}")
    print('comment: This testcase should return -1 as it is not possible to reach the destination')

    print('\nd=[0,2,4,6,9]')
    print('m=5')
    d=[0,2,4,6,9]
    m=5
    print(f"Testcase 3: {min_stops(d,m)}")
    

    print('\nd=[0,3,4,7]')
    print('m=3')
    d=[0,3,4,7]
    m=3
    print(f"Testcase 4: {min_stops(d,m)}")

    print('\nDo you want to enter your own testcases?  (y/n)')
    choice=input()
    if(choice=='y'):

        # manual input
        print('\nManual input')
        print('\nNote: The initial distance is always 0')
        print('distances should be in increasing order i.e. (d[i]<d[i+1])')
        d=[]
        n=int(input('\nEnter the number of places (including initial and final destinations): '))

        
        for i in range(n):
            d.append(int(input(f'Enter the distance of stop {i+1}: ')))
        m=int(input('Enter the maximum distance that can be covered in a single stop: '))
        print("Answer : ",min_stops(d,m))

    else:
        print('Exiting the program')

if __name__ == "__main__":
    main()





