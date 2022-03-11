
from this import d
from turtle import ht
from Cerbere import *
def main(port=8080):
    try:
        s = SimpleServer("127.0.0.1",port, verbose=True)

        s.AddHeaders("server: Cerbere Secure Server")

        s.AutorizeFile("css/home.css")
        s.AutorizeFile("css/main.css")

        def main(data):
            html = open("index.html", "r").read()
            print(data)
            if("/Home" in data):
                home_html = open("Home.template", "r").read()
                html = html.replace("%%template%%", home_html)
            return html

        s.AddRoot("/", main)
        s.AddRoot("/Home", main)
        s.AddRoot("/News", main)
        s.run()
    except KeyboardInterrupt:
        exit()
    except:
        main(port+1)
    

        
if __name__ == "__main__":
    main()