* A trivial bounded knapsack instance, where all available quantities of the item times can immediately fit in the knapsack
  without filling it up, seems to cause SEGFAULTs.

```python3
capacity = 7999
sizes = [109, 225, 462]
available_quantities = [1] * len(sizes)
_, solution = bouknap.solve(
    values=sizes,
    weights=sizes,
    available_quantities=available_quantities,
    capacity=capacity
)
```


* Going too large with the capacities and/or weights and/or values seems to introduce unknown errors.

```python3
capacity = 7999000
sizes = [108837, 224227, 461535]
available_quantities = [
    (capacity // byte_size) + 1
    for byte_size in sizes
]
_, solution = bouknap.solve(
    values=sizes,
    weights=sizes,
    available_quantities=available_quantities,
    capacity=capacity
)
```

* Work with floating-point values for weights, values, and knapsack capacity.