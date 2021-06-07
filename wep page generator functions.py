def WPgen():
        f = open("WPgenPage.html", "w")
        f.write("<html>\n   <body>\n        <h1>\n  Stay tuned for our amazing summer sale!\n       </h1>\n </body>\n</html>")
        f.close()
        filename = 'WPgenPage.html'
        webbrowser.open_new_tab(filename)
    
    def WPgenEDIT():
        f = open("WPgenPage.html", "w")
        UserInput = self.UI.get()
        f.write("<html>\n<body>\n<h1>\n{}\n</h1>\n</body>\n</html>".format(UserInput))
        f.close()
        filename = 'WPgenPage.html'
        webbrowser.open_new_tab(filename)
