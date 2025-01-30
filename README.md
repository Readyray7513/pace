### Main Function
The `main()` function calculates the pace per mile for a marathon (26.2 miles) assuming the total run time is 180 minutes (3 hours). 
It uses the `get_pace()` function to perform the calculation and then prints the result.

### Pace Calculation Function
The `get_pace()` function takes two parameters:
- `miles`: The total number of miles (26.2 for a marathon).
- `minutes`: The total time in minutes (180 minutes for 3 hours).

It checks if the `minutes` value is greater than 0, raising an error if not. 
Then, it calculates and returns the pace (time per mile) by dividing the total minutes by the number of miles.
