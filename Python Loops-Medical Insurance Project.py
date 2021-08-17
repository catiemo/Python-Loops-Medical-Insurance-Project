names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Add your code here
total_cost = 0
for item in actual_insurance_costs:
  total_cost += item
#print(total_cost)
average_cost = total_cost / len(actual_insurance_costs)
print("Average Insurance Cost:", average_cost, "dollars")

for i in range(0, len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print("The insurance cost for", name, "is", insurance_cost, "dollars")
  if insurance_cost > average_cost:
    print("The insurance cost for", name, "is above average")
  elif insurance_cost < average_cost:
    print("The insurance cost for", name, "is below average")
  else:
    print("The insurance cost for", name, "is equal to the average")

updated_estimated_costs = [each_entry * (11/10) for each_entry in estimated_insurance_costs]
print(updated_estimated_costs)

#Extra Practice
total_costs = 0
i = 0
while i < len(actual_insurance_costs):
  total_costs += actual_insurance_costs[i]
  i += 1
average__cost = total_costs / len(actual_insurance_costs)
print("Average Insurance Cost:", average__cost, "dollars")

for i in range(0, len(names)):
  name = names[i]
  estimated_insurance_cost = estimated_insurance_costs[i]
  print("The estimated insurance cost for", name, "is", estimated_insurance_cost, "dollars")
  if estimated_insurance_cost > average_cost:
    difference_from_average_cost = estimated_insurance_cost - average_cost
    print("The estimated insurance cost for", name, "is", difference_from_average_cost, "above average")
  elif estimated_insurance_cost < average_cost:
    difference_from_average_cost = average_cost - estimated_insurance_cost
    print("The estimated insurance cost for", name, "is", difference_from_average_cost, "below average")
  else:
    print("The estimated insurance cost for", name, "is equal to the average")
