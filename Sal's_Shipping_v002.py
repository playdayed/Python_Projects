weight = 80

# Function to calculate ground shipping cost
def calculate_ground_shipping(weight):
    ground_flat_rate = 20.00
    if weight <= 2:
        return weight * 1.50 + ground_flat_rate
    elif weight <= 6:
        return weight * 3.00 + ground_flat_rate
    elif weight <= 10:
        return weight * 4.00 + ground_flat_rate
    else:
        return weight * 4.75 + ground_flat_rate

# Function to calculate drone shipping cost
def calculate_drone_shipping(weight):
    if weight <= 2:
        return weight * 4.50
    elif weight <= 6:
        return weight * 9.00
    elif weight <= 10:
        return weight * 12.00
    else:
        return weight * 14.25

# Function to recommend the best shipping method

    # Print shipping prices
    print(f"Ground Shipping Price: ${ground_cost:.2f}")
    print(f"Ground Shipping Premium Flat Price: ${premium_flat_rate:.2f}")
    print(f"Drone Shipping Price: ${drone_cost:.2f}")

    # Recommend the best option
    if ground_cost <= premium_flat_rate and ground_cost <= drone_cost:
        print("Recommend Regular Ground Shipping")
    elif drone_cost <= premium_flat_rate and drone_cost <= ground_cost:
        print("Recommend Drone Shipping")
    else:
        print("Recommend Premium Ground Shipping")

