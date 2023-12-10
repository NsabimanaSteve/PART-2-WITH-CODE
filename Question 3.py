def process_and_create_file(file_path, output_file_path):
    country_names = []
    populations = []
    mobile_subscriptions = []
    internet_users = []

    # Open the file for reading
    file = open(file_path, 'r')
    lines = file.readlines()[1:]

    # Iterate through each row in the CSV
    for index, row in enumerate(lines):
        data = row.split(',') 
        country = data[0]
        population = int(data[1])
        mobile_subs = int(data[3])
        internet_users_count = int(data[4])

        # Storing data in lists
        country_names.append(country)
        populations.append(population)
        mobile_subscriptions.append(mobile_subs)
        internet_users.append(internet_users_count)

    # Open the output file for writing
    output_file_path = 'ProcessedCountryData-1.csv'

    # Write data to the file
    output_file = open(output_file_path, 'w') 
    # Write header
    output_file.write("Country, Mobile Subs Per Capita, Internet Users Per Capita\n")

    # Iterate through each country and write data to the file
    for i in range(len(country_names)):
        #print(i)
        country = country_names[i]
        population = populations[i]
        mobile_subs_per_capita = mobile_subscriptions[i] / population
        internet_users_per_capita = internet_users[i] / population

          
        output_file.write(f"{country}, {mobile_subs_per_capita:.2f}, {internet_users_per_capita:.2f}\n")

    return output_file_path


file_path = 'CountryData-1.csv'
output_file_path = 'ProcessedCountryData-1.csv'
result = process_and_create_file(file_path, output_file_path)
print(result)
