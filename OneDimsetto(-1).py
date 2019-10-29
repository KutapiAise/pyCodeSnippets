What does reshaping an array in Python with one dimension set to -1 do?
According to numpy docs -

Once the shape dimension can be -1, the value is offered from the length of the array and remaining dimension.

Let's see how the value of -1 is calculated.

Eg -

import numpy as np
z = np.array([
[1,2,3,4],
[5,6,7,8],
[9,10,11,12]])
 
z.shape=>(3,4)
z.size => 12 =>3*4
z.ndin=>2, z is 2d
Now if .

z.reshape(-1) 
[ 1  2  3  4  5  6  7  8  9 10 11 12]                                   
z.reshape(-1).ndim => 1
Comments - z has been reduced to 1d array which equals to size of original array z. So -1 == 12(size of original z).

Now if.

z.reshape((-1,1))
[[ 1]
 [ 2]                                                                 
[ 3]                                                                   
[ 4]                                                                    
[ 5]                                                                    
[ 6]                                                                    
[ 7]                                                                    
[ 8]                                                                    
[ 9]                                                                    
[10]                                                                    
[11]                                                                    
[12]]                        
Comments -

Now shape of z is (12,1).
Passed value (-1,1)
Calculation of -1 = size of z /column = 12/1 = 12
So shape is (12,1).
Now if.

z.reshape((-1,2))
[[ 1  2]
 [ 3  4]                                                            
[ 5  6]                                                               
[ 7  8]                                                                 
[ 9 10]                                                                 
[11 12]]           
Comments -

Now shape of z is (6,2).
Passed value(-1,2).
Calculation of -1 = size of z /column = 12/2 = 6.
So the shape is (6,2).
Now if.

z.reshape((3,-1))
[[ 1  2  3  4]
[ 5  6  7  8]                                                           
[ 9 10 11 12]]                
Comments -

Now shape of z is (3 ,4).
Passed size (3,-1)
Calculation of -1 = size of z /row= 12/3 =4.
So the shape is (3,4).
Now if.

z.reshape((-1,-1))                      
ValueError: can only specify one unknown dimension                      
Comments -

Value error.
Passed size (-1,-1).
Calculation of -1 = 12/12 = 1
Shape(1,1 ). A size 12 array cannot be reduced to shape (1,1). So we get the Error.
