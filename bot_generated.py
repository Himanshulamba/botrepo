Of course! Here are a few ways to write a Python function that prints the current time, from the most common and simple to slightly more customized versions.

### The Standard and Most Common Way

This is the recommended approach. It uses the built-in `datetime` module to get the current time and the `strftime` method to format it into a clean `HH:MM:SS` string.

```python
import datetime

def print_current_time():
  """
  Gets the current time and prints it in HH:MM:SS format.
  """
  # Get the current datetime object
  now = datetime.datetime.now()
  
  # Format the time into a string (24-hour format)
  current_time = now.strftime("%H:%M:%S")
  
  # Print the formatted time
  print("The current time is:", current_time)

# --- Example Usage ---
print_current_time() 
```

#### Code Breakdown:
1.  **`import datetime`**: This line imports Python's standard module for working with dates and times.
2.  **`now = datetime.datetime.now()`**: This calls the `now()` method to get a `datetime` object containing the current date, time (down to the microsecond), and timezone information (if available).
3.  **`now.strftime("%H:%M:%S")`**: This is the key formatting step.
    *   The `strftime` method formats a `datetime` object into a string.
    *   `%H`: Represents the hour (in 24-hour format, 00-23)
    *   `%M`: Represents the minute (00-59)
    *   `%S`: Represents the second (00-59)
4.  **`print(...)`**: This displays the final string.

---

### Variations and Other Options

Here are a few other ways you might want to print the time.

#### 1. With AM/PM (12-Hour Clock)

To use a 12-hour clock format, you just need to change the format codes.

```python
import datetime

def print_current_time_ampm():
  """
  Prints the current time in 12-hour format with AM/PM.
  """
  now = datetime.datetime.now()
  
  # Format with %I for 12-hour clock and %p for AM/PM
  current_time = now.strftime("%I:%M:%S %p") 
  
  print("The current time is:", current_time)

# --- Example Usage ---
print_current_time_ampm()
```
*   `%I`: Hour in 12-hour format (01-12)
*   `%p`: Locale’s equivalent of either AM or PM.

#### 2. Including the Date

If you also want to include the current date, you can add more format codes.

```python
import datetime

def print_current_datetime():
  """
  Prints the current date and time.
  """
  now = datetime.datetime.now()
  
  # Format with date and time codes
  # %Y: Year, %m: Month, %d: Day
  formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
  
  print("Current date and time:", formatted_datetime)

# --- Example Usage ---
print_current_datetime()
```

#### 3. Including Milliseconds

If you need more precision, you can use the `%f` code, which represents microseconds.

```python
import datetime

def print_time_with_milliseconds():
  """
  Prints the current time including milliseconds.
  """
  now = datetime.datetime.now()

  # %f gives microseconds (6 digits). We can slice it for milliseconds (3 digits).
  current_time = now.strftime("%H:%M:%S") + f".{now.microsecond // 1000:03d}"
  
  print("Current time with milliseconds:", current_time)

# --- Example Usage ---
print_time_with_milliseconds()
```