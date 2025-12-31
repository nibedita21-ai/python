def calculate_rectangle_area(length, width):
  """
  Calculates the area of a rectangle.

  Args:
    length: The length of the rectangle.
    width: The width of the rectangle.

  Returns:
    The area of the rectangle.
  """
  area = length * width
  return area

# Get input from the user
try:
  rectangle_length = float(input("Enter the length of the rectangle: "))
  rectangle_width = float(input("Enter the width of the rectangle: "))

  # Calculate the area
  result_area = calculate_rectangle_area(rectangle_length, rectangle_width)

  # Display the result
  print(f"The area of the rectangle with length {rectangle_length} and width {rectangle_width} is: {result_area}")

except ValueError:
  print("Invalid input. Please enter numerical values for length and width.")