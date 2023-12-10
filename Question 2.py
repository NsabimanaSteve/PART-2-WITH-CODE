def read_data(file_path):
    file = open(file_path, 'r')

    country_names = []
    populations = []
    literacy_rates = []
    mobile_subscriptions = []
    internet_users = []
    electricity_production = []
    electricity_consumption = []
    country_dict = {}

    
    lines = file.readlines()[1:]

 
    for index, row in enumerate(lines):
        data = row.strip().split(',')
        country = data[0]
        population = int(data[1])
        literacy_rate = int(data[2])
        mobile_subs = int(data[3])
        internet_users_count = int(data[4])
        elec_production = int(data[5])
        elec_consumption = int(data[6])

        country_names.append(country)
        populations.append(population)
        literacy_rates.append(literacy_rate)
        mobile_subscriptions.append(mobile_subs)
        internet_users.append(internet_users_count)
        electricity_production.append(elec_production)
        electricity_consumption.append(elec_consumption)

        country_dict[country] = index

    # Close the file
    file.close()

    return country_names, populations, literacy_rates, mobile_subscriptions, internet_users, electricity_production, electricity_consumption, country_dict

file_path = 'CountryData-1.csv'
countries, populations, literacy_rates, mobile_subscriptions, internet_users, electricity_production, electricity_consumption, country_dict = read_data(file_path)
country_name_input = input("Hello! What country would you like information on?: ")
index = country_dict.get(country_name_input)

if index is not None:
    print(f"{country_name_input} has a population of {populations[index]:,}, and a literacy rate of {literacy_rates[index]}%.")
    print(f"The estimate of the number of mobile subscriptions is {mobile_subscriptions[index]:,}, while that of internet users is {internet_users[index]:,}.")
    print(f"{country_name_input} produces {electricity_production[index]} billion KWh of electricity annually, while it consumes {electricity_consumption[index]} billion KWh of electricity.")
else:
    print(f"Country {country_name_input} not found in the data.")

