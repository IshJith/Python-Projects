import sys
import requests
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_name = QLabel("Enter City name: ",self)
        self.input_name = QLineEdit(self)
        self.input_get_weather = QPushButton("Get Weather", self)
        self.temp = QLabel(self)
        self.emoji = QLabel(self)
        self.weather = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        vbox = QVBoxLayout()   

        vbox.addWidget(self.city_name)
        vbox.addWidget(self.input_name)
        vbox.addWidget(self.input_get_weather)
        vbox.addWidget(self.temp)
        vbox.addWidget(self.emoji)
        vbox.addWidget(self.weather)

        self.setLayout(vbox)

        self.city_name.setAlignment(Qt.AlignCenter)
        self.input_name.setAlignment(Qt.AlignCenter)
        self.temp.setAlignment(Qt.AlignCenter)
        self.emoji.setAlignment(Qt.AlignCenter)
        self.weather.setAlignment(Qt.AlignCenter)

        self.city_name.setObjectName("city_name")
        self.input_name.setObjectName("input_name")
        self.input_get_weather.setObjectName("input_get_weather")
        self.temp.setObjectName("temp")
        self.emoji.setObjectName("emoji")
        self.weather.setObjectName("weather")

        self.setStyleSheet("""
            QLabel,QPushButton{
                font-family:calibri;
                font-size:40px;
            }
            QLabel#city_name{
                font-size: 40px;
                font-style: italic;

            }
            QLineEdit{
                font-size:40px;
            }
            QPushButton#input_get_weather{
                font-size:30px;
                font-weight:bold;
            }
            QLabel#emoji{
                font-size:100px;
                font-family:Segoe UI emoji;
            }
  
            
            """)
        
        self.input_get_weather.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "xxxx"
        city = self.input_name.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if data["cod"]==200:
                self.display_weather(data)
        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request \n Please Check your input")
                case 401:
                        self.display_error("Unauthorized \n Please Check your input")
                case 403:
                        self.display_error("Forbidden \n Please Check your input")
                case 404:
                        self.display_error("Not Found \n City not found")
                case 500:
                        self.display_error("Internal server error \n Try again later")
                case 502:
                        self.display_error("Bad Gateway \n Inavlid response in the server")
                case 503:
                        self.display_error("Server unavailable \n Server is down ")
                case 504:
                        self.display_error("Server unavailable \n Server is down ")
                case _:
                      self.display_error(f"HTTP Error occured \n{http_error}")
        except requests.exceptions.ConnectionError:
             print("Connection Error")
        except requests.exceptions.Timeout:
             print("Timout error \n We request timeout")
        except requests.TooManyRedirects:
             print("Too many redirects \n Check URL")
                
        except requests.exceptions.RequestException:
            print(f"Request Error:\n{req_error}")    

    def display_error(self,message):
        self.temp.setText(message)


    def display_weather(self,data):
        temp_k = data["main"]["temp"]
        temp_c = (temp_k-273)
        self.temp.setText(F"{temp_c:.1F}°C")
        weather_id = data["weather"][0]["id"]
        weath = data["weather"][0]["description"]
        self.weather.setText(weath)
        self.emoji.setText(self.get_weather_emoji(weather_id))

    @staticmethod
    def get_weather_emoji(weather_id):
       if 200<= weather_id<=232:
            return "⛈️"
       elif 300<= weather_id <=321:
            return "🌦️"
       elif 500<= weather_id <=531:
                   return "🌧️"
       elif 600<= weather_id <=622:
                   return "❄️"
       elif 701<= weather_id <=741:
                   return "🌫️"
       elif 762==weather_id:
                   return "🌋"
       elif weather_id==771:
                   return "💭"
       elif weather_id==721:
                   return "🌪️"
       elif weather_id==800:
                   return "☀️"
       elif 801<= weather_id <=804:
                   return "☁️"
       else:
              return ""
        

if __name__ == "__main__":
    app = QApplication(sys.argv)    
    weatherApp = WeatherApp()
    weatherApp.show()
    sys.exit(app.exec_())