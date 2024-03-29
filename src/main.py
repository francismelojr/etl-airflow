from controller import get_current_weather

city = 'Paris'


def main(city: str):
    data = get_current_weather(city)
    return data

if __name__ == '__main__':
    main(city)
