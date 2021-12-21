So, you have a list of 12 elements. Merge sort works by splitting everything in half, then re-assembling in order.

## 1. Keep splitting the list in half until you are left with only lists with 1 element each.

[79, 43, 36, 60, 49, 96] 

[79, 43, 36] [60, 49, 96]

[79, 43] [36] [60, 49] [96]

[79] [43] [36] [60] [49] [96]

## 2. Start re-combining the lists from left to right and sorting them while you do so.

Parenthesis indicate the lists that are being combined. 

```
  a    b
([79] [43]) [36] [60] [49] [96]
```

Is `a > b`? Yes, but `b` first in the new list.


```
[43, 79] ([36] [60]) [49] [96]
```

Is 36 greater than 60? No, put 36 first, 

```
[43, 79] [36, 60] ([49] [96])
```

```
([43, 79] [36, 60]) [49, 96]
```

```
([36, 43, 60, 79] [49, 96])
```