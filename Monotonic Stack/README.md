|  Problem           |  Stack Type                  |  Operator in while loop |  Assignment Position  |
|--------------------|------------------------------|-------------------------|-----------------------|
|  next greater      |  decreasing (equal allowed)  |  stackTop < current     |  inside while loop    |
|  previous greater  |  decreasing (strict)         |  stackTop <= current    |  outside while loop   |
|  next smaller      |  increasing (equal allowed)  |  stackTop > current     |  inside while loop    |
|  previous smaller  |  increasing (strict)         |  stackTop >= current    |  outside while loop   |