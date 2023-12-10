def analyse_africa_countries(data):
    country_names = []
    populations = []
    literacy_rates = []
    mobile_subscriptions = []
    internet_users = []
    electricity_production = []
    electricity_consumption = []

    for index, line in enumerate(data):
        # Extracting data from the split line
        country = line[0]
        population = int(line[1])
        literacy_rate = int(line[2])
        mobile_subs = int(line[3])
        internet_users_count = int(line[4])
        elec_production = int(line[5])
        elec_consumption = int(line[6])

        # Storing data in lists
        country_names.append(country)
        populations.append(population)
        literacy_rates.append(literacy_rate)
        mobile_subscriptions.append(mobile_subs)
        internet_users.append(internet_users_count)
        electricity_production.append(elec_production)
        electricity_consumption.append(elec_consumption)

    # Compute required information using the lists
    total_population_africa = sum(populations)
    most_populous_country = country_names[populations.index(max(populations))]
    least_populous_country = country_names[populations.index(min(populations))]
    highest_literacy_country = country_names[literacy_rates.index(max(literacy_rates))]
    lowest_literacy_country = country_names[literacy_rates.index(min(literacy_rates))]
    Country_weighted_literacy_rate =[]
    
    for literacy_rate, population in zip(literacy_rates, populations):
    
        Country_weighted_literacy_rate.append(literacy_rate * population) 
    
        average_african_literacy_rate = sum(Country_weighted_literacy_rate) / total_population_africa 

    mobileCapita = []
   
    for subs, population in zip(mobile_subscriptions, populations):
        
        mobileCapita.append(subs/population)
       
    internetCapita =[]
    
    for users, population in zip(internet_users, populations):
        internetCapita.append(users/population)

    highest_mobile_subs_per_capita = country_names[mobileCapita.index(max(mobileCapita))]
    lowest_mobile_subs_per_capita = country_names[mobileCapita.index(min(mobileCapita))]
    highest_internet_users_per_capita = country_names[internetCapita.index(max(internetCapita))]
    lowest_internet_users_per_capita = country_names[internetCapita.index(min(internetCapita))]

    def high_production_elect_than_consumption_elect(electricity_production, electricity_consumption):
        countries_that_produce_more_elect_than_consumption = []
        for i in range(len(electricity_production)):
            if electricity_production[i] > electricity_consumption[i]:
                countries_that_produce_more_elect_than_consumption.append(country_names[i])
        return countries_that_produce_more_elect_than_consumption
    
    result_elect_production = high_production_elect_than_consumption_elect(electricity_production, electricity_consumption)

        
    def high_consumption_elect_than_production_elect(electricity_consumption, electricity_production):
        
        countries_that_consume_more_elect_than_production = []
        for i in range(len(electricity_consumption)):
            if electricity_consumption[i] > electricity_production[i]:
                countries_that_consume_more_elect_than_production.append(country_names[i])
                
        return countries_that_consume_more_elect_than_production
    
    result_elect_consumption = high_consumption_elect_than_production_elect(electricity_consumption, electricity_production)

    # Print or return the results as needed
    print(f'Total population of Africa: {total_population_africa:,}\n')
    print(f'Most populous country: {most_populous_country}\n')
    print(f'Least populous country: {least_populous_country}\n')
    print(f'Highest literacy rate country: {highest_literacy_country}\n')
    print(f'Lowest literacy rate country: {lowest_literacy_country}\n')
    print(f'The “average” literacy rate in Africa: {average_african_literacy_rate}\n')
    print(f'The countries with the highest number of mobile subscriptions per capita: {highest_mobile_subs_per_capita}\n')
    print(f'The countries with the lowest number of mobile subscriptions per capita: {lowest_mobile_subs_per_capita}\n')
    print(f'The countries with the highest number of internet users per capita: {highest_internet_users_per_capita}\n')
    print(f'The countries with the lowest number of internet users per capita: {lowest_internet_users_per_capita}\n')
    print(f'The countries that produce more electricity than they consume (electricity exporters): {result_elect_production}\n')
    print(f'The countries that consume more electricity than they produce (electricity importers): {result_elect_consumption}\n')



file_path = 'CountryData-1.csv'
with open(file_path, 'r') as file:
    # if the first line contains column names, skipping it
    lines = [line.strip().split(',') for line in file.readlines()[1:]]

    # Analyze the data
    analyse_africa_countries(lines)



