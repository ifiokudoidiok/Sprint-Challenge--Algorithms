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


