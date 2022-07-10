arr = []

with open('nyc_weather.csv', 'r') as f:
    for line in f:
        tokens = line.split(',')
        temperature = int(tokens[1])
        arr.append(temperature)
    print(line)
