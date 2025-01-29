def main():
    pace = get_pace(miles=26.2, minutes=180)
    print(f'Run each mile in {round(pace, 2)} minutes.')

def get_pace(miles, minutes):
    if not minutes > 0:
        raise ValueError('Invalid value for mins')
    
    return minutes / miles



main()