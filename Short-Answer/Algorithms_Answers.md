#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
    Explanation:
    a = 0 #O(1)
   ```python
a)  a = 0 #O(1)
    while (a < n * n * n): #O(n) + O(1)
      a = a + n * n # O(1)
    #O(1) + O(n) + O(1)
    # O(2) + O(n)
    #O(n)
```
 

b) O(n^2)
    Explanation:

```python
b)  sum = 0 #O(1)
    for i in range(n): #O(n) + #O(1)
      j = 1 #O(1)
      while j < n: #O(n) + #O(1) + #O(1)
        j *= 2  #O(1)
        sum += 1 #O(1)
        #(O(1) + #O(n) + #O(1)) * (#O(n) + #O(1) + #O(1))
        #O(2) + #O(n) * #O(2) + #O(n)
        # O(n) * O(n)
        # O(n^2)
```


c) O(n)
Explanation:
```python
c)  def bunnyEars(bunnies): #O(n)
      if bunnies == 0: #O(1)
        return 0 #O(1)

      return 2 + bunnyEars(bunnies-1) #O(n)
      #O(n^2)
```

## Exercise II

-find the middle floor in the building and drop an egg from there. 
-if the egg breaks then we determine that the bottom half contains floor f and we could go ahead and find the middle floor of the bottom half of the building.
-We continue in the same manner until we find the floor that is one floor lower than floor f at which point the egg doesn't break.
-If the egg doesn't break at the first half of the building, the we do the same with the floors on the higher half until we find floor f.
So since binary search has a runtime complexity of O(log n), i assume this algorithm would have a runtime complexity of O(log n)

