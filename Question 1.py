file_path = 'CountryData.csv'
file = open(file_path, 'r')

country_names = []
populations = []
literacy_rates = []
mobile_subscriptions = []
internet_users = []
electricity_production = []
electricity_consumption = []
country_index_dict = {}

lines = file.readlines()
 
# Iterate through each row in the CSV
for index, row in enumerate(lines[1:]):
    data = row.split(',')

    country = data[0]
    population = data[1]
    literacy_rate = int(data[2])
    mobile_subs = int(data[3])
    internet_users_count = int(data[4])
    elec_production = int(data[5])
    elec_consumption = int(data[6])

    # Storing data in lists
    country_names.append(country)
    populations.append(population)
    literacy_rates.append(literacy_rate)
    mobile_subscriptions.append(mobile_subs)
    internet_users.append(internet_users_count)
    electricity_production.append(elec_production)
    electricity_consumption.append(elec_consumption)

    # Storing country names in the dictionary with indices as values
    country_index_dict[country] = index

#close the file
file.close()

# Print the lists and dictionary 
print("Country Names:", country_names,"\n")
print("Populations:", populations,"\n")
print("Literacy Rates:", literacy_rates,"\n")
print("Mobile Subscriptions:", mobile_subscriptions,"\n")
print("Internet Users:", internet_users,"\n")
print("Electricity Production:", electricity_production,"\n")
print("Electricity Consumption:", electricity_consumption,"\n")
print("Country Index Dictionary:", country_index_dict,"\n")






