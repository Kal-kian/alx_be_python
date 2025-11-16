def get_weather_advice(weather):
    weather = weather.lower()

    if weather == "sunny":
        return "Wear a t-shirt and sunglasses."
    elif weather == "rainy":
        return "Don't forget your umbrella and a raincoat."
    elif weather == "cold":
        return "Make sure to wear a warm coat and a scarf."
    elif weather == "windy":
        return "Wear a windbreaker jacket."
    elif weather == "cloudy":
        return "It might be chilly — take a light jacket."
    elif weather == "snowy":
        return "Wear a heavy coat, gloves, and boots."
    else:
        return "Sorry, I don't have recommendations for this weather."


def main():
    while True:
        weather = input("What's the weather like today? (sunny/rainy/cold/windy/cloudy/snowy): ")

        if not weather.strip():
            print("Please enter a valid weather condition.")
            continue

        advice = get_weather_advice(weather)
        print(advice)

        again = input("Check another weather? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
