def estimate_shirt_size(chest_circumference, neck_circumference):


  # Define size ranges based on circumference measurements (adjust as needed)
  size_ranges = {
      "XS": (chest_circumference <= 81, neck_circumference <= 36),
      "S": (81 < chest_circumference <= 89, 36 < neck_circumference <= 38),
      "M": (89 < chest_circumference <= 97, 38 < neck_circumference <= 40),
      "L": (97 < chest_circumference <= 105, 40 < neck_circumference <= 42),
      "XL": (105 < chest_circumference <= 113, 42 < neck_circumference <= 44),
      "XXL": (chest_circumference > 113, neck_circumference > 44)
  }

  for size, (chest_range, neck_range) in size_ranges.items():
    if chest_range and neck_range:
      return size

  return "Not Found"

chest_cm = int(input("enter chest size"))
neck_cm = int(input("enter neck size"))
estimated_size = estimate_shirt_size(chest_cm, neck_cm)
print(f"Estimated shirt size: {estimated_size}")