
import webbrowser
def WPgen():
    f = open("WPgenPage.html", "w")
    f.write("<html>\n   <body>\n        <h1>\n  Stay tuned for our amazing summer sale!\n       </h1>\n </body>\n</html>")
    f.close()

url = 'D:/Watson Tech Academy repositories/Python_Projects/WPgen.html'
webbrowser.open(url, new=2)  # open in new tab


    



if __name__ == "__main__":
    WPgen() 
