
#      *
#     * *
#    * * * 
#   * * * *
#  * * * * *
# * * * * * *
#* * * * * * *

for i in range(1,8): #Rows
    for j in range(7-i): #Spacing
        print('', end=' ')  #Make sure only single space
        
    for k in range(i): #Printing
        print('*', end=' ')
        
    print()

#i=1, j=(6)
#i=2, j=(5)
#i=3, j=(4)
#i=4, j=(2)
#i=5, j=(2)
#i=6, j=(1)
#i=7, j=(0)
