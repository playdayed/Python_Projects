# Sal's Shipping
# Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
# Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
# Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

# Start Code
weight = 80
ground_flat_rate = 20.00
premium_flat_rate = 125.00

# Ground Shipping + Drone Shipping
if weight <= 2:
  ground_cost = weight * 1.50 + ground_flat_rate 
  drone_cost = weight * 4.50  
elif weight <= 6:
  ground_cost = weight * 3.00 + ground_flat_rate
  drone_cost =  weight * 9.00
elif weight <= 10:
  ground_cost = weight * 4.00 + ground_flat_rate
  drone_cost = weight * 12.00
else:
  ground_cost = weight * 4.75 + ground_flat_rate
  drone_cost = weight * 14.25

print("Ground Shipping Price :", "$", ground_cost, "\nGround Shipping Premium Flat Price: ", "$", premium_flat_rate, "\nDrone Shipping Price :", "$", drone_cost)

# Recommend Shipping Method to customer
if ground_cost <= premium_flat_rate and ground_cost <= drone_cost:
  print("Recommend Regular Ground Shipping")
elif drone_cost <= premium_flat_rate and drone_cost <= ground_cost:
  print("Recommend Drone Shipping")
else:
  print("Recommend Premium Ground Shipping")



