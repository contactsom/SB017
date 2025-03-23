'''
         *
        * *
       * * *
      * * * *
     * * * * *
    *     *
   * *    * *
  * * *   * * *
 * * * *  * * * *
* * * * * * * * * *
'''

num=int(input("Enter a number"))
for i in range(1,num+1):
    print(" "*(2*num-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print(" "*(num-i),end="")
    for k in range(1,i+1):
        print("*",end=" ")
    print()