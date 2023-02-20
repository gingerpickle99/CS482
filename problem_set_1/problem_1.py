#Author: Lakshmi Nikhil Goduguluri
#Date: 02/19/2023
#Description: This program finds the maximum profit that can be earned by choosing a subset of shops such that the distance between any two shops is at least k

# This program uses dynamic programming to solve the problem
def maxprofit(d,p,k):
    arr=[0]*len(p)
    arr[0]=p[0]
    for i in range(1,len(p)):
        arr[i]=p[i]
        for j in range(0,i):
            if(d[i]-d[j]>=k):
                # if the distance between the current shop and the previous shop is greater than k, then we can choose the current shop
                arr[i]=max(arr[i],arr[j]+p[i])
                # combine the present shop with the shop that gives the maximum profit
            else:
                # no need to any further checks as the distance between the current shop and the previous shop is less than k
                break 
    print(arr)           
    return max(arr)


def fatoracle(d,p,k):
    # greedy algorithm
    
    list=[]
    # choose shop with maximum profit , add it to the list and remove all the shops that are within k distance from it. repeat the process until all the shops are visited
    while(len(d)>0):
        #print(d)
        # intisalise to minus infinity
        maxprofit=-float('inf')
        index=-float('inf')
        for i in range(len(d)):
            if(p[i]>=maxprofit):
                maxprofit=p[i]
                index=i
        list.append(p[index])
        remove=[]
        for i in range(len(d)):
            if(abs(d[index]-d[i])<k):
                remove.append(i)
        remove.sort(reverse=True)        
        for i in remove:
            d.pop(i)
            p.pop(i)        
    return sum(list)     


      



def main():

    d=[1,2,3,4,5,6,7,8,9,10]
    p=[1,2,3,4,5,6,7,8,9,10]
    k=3
    print('\nd=[1,2,3,4,5,6,7,8,9,10]')
    print('p=[1,2,3,4,5,6,7,8,9,10]')
    print('k=3')
    print(f"Testcase 1 dp_approach: {maxprofit(d,p,k)}")
    print(f"Testcase 1 fatoracle: {fatoracle(d,p,k)}")
 

    d=[1,2,3,4,5]
    p=[7,10,20,25,36]
    k=3
    print('\nd=[1,2,3,4,5]')
    print('p=[7,10,20,25,36]')
    print('k=3')
    print(f"Testcase 2 dp_approach: {maxprofit(d,p,k)}")
    print(f"Testcase 2 fatoracle: {fatoracle(d,p,k)}")


    d=[1,2,3]
    p=[10,15,9]
    k=4
    print('\nd=[1,2,3]')
    print('p=[10,15,9]')
    print('k=4')
    print(f"Testcase 3 dp_approach: {maxprofit(d,p,k)}")
    print(f"Testcase 3 fatoracle: {fatoracle(d,p,k)}")


    p=[10,12,11]
    d=[4,5,6]
    k=2
    print('\nd=[4,5,6]')
    print('p=[10,12,11]')
    print('k=2')
    print(f"Testcase 4 dp_approach: {maxprofit(d,p,k)}")
    print(f"Testcase 4 fatoracle: {fatoracle(d,p,k)}")
    print('Observation : The greedy algorithm does not work for this testcase')


    print('\nDo you want to enter your own testcases?  (y/n)')
    choice=input()
    if(choice=='y'):
        print('\nManual input')
        n=int(input('Enter the number of shops: '))
        d=[]
        p=[]
        print('\n')
        for i in range(n):
            d.append(int(input(f'Enter the distance of shop {i+1}: ')))
        print('\n')
        for i in range(n):
            p.append(int(input(f'Enter the profit of shop {i+1}: ')))    
        k=int(input('\nEnter the minimum distance between two shops: '))

        print(f"\nMaximum profit: {maxprofit(d,p,k)}")
        print(f"Maximum profit by fatoracle: {fatoracle(d,p,k)}")

        print('Exiting...\n')

    else:
        print('Exiting...')

if __name__=='__main__':
    main()





