import requests
import tkinter as tk
from tkinter import messagebox

# Vlož svůj API klíč sem
API_KEY = "6e8ba65dc98c3d2b7742c46ef361c858"

# Funkce pro získání dat z API
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=cz"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            "city": data["name"],
            "weather": data["weather"][0]["description"],
            "temp": data["main"]["temp"],
            "wind": data["wind"]["speed"]
        }
    except requests.exceptions.HTTPError as e:
        raise ValueError("Město nenalezeno nebo chyba v dotazu.") from e
    except requests.exceptions.RequestException as e:
        raise ValueError("Problém se sítí, zkontroluj připojení.") from e

# GUI aplikace
class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Počasí v tvém městě")
        self.root.geometry("350x200")

        # GUI komponenty
        self.label = tk.Label(root, text="Zadej název města:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.city_entry = tk.Entry(root, font=("Arial", 12), justify="center")
        self.city_entry.pack()

        self.get_weather_btn = tk.Button(root, text="Získat počasí", command=self.display_weather)
        self.get_weather_btn.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def display_weather(self):
        city = self.city_entry.get().strip()
        if not city:
            messagebox.showerror("Chyba", "Prosím, zadej název města!")
            return

        try:
            weather = get_weather(city)
            result = (f"📍 {weather['city']}\n"
                      f"🌡️ Teplota: {weather['temp']} °C\n"
                      f"☁️ Počasí: {weather['weather'].capitalize()}\n"
                      f"💨 Vítr: {weather['wind']} m/s")
            self.result_label.config(text=result, fg="green")
        except ValueError as e:
            messagebox.showerror("Chyba", str(e))
            self.result_label.config(text="", fg="red")

# Hlavní spuštění
if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
