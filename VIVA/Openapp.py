import os
import webbrowser

def Open(prompt):
    if "chrome" in prompt:
        response_str = "Opening Google Chrome"
        os.startfile(r"C:\Users\goran\OneDrive\Desktop\Gorantla (Manoj) - Chrome.lnk")
    elif "vs code" in prompt:
        response_str = "Opening Visual Studio Code"
        os.startfile(r"C:\Users\goran\OneDrive\Desktop\Visual Studio Code.lnk")
    elif "youtube" in prompt:
        response_str = "Opening Youtube"
        webbrowser.open("https://youtube.com/")
    elif "google" in prompt:
        response_str = "Opening Google"
        webbrowser.open("https://google.com/")
    elif "stackoverflow" in prompt:
        response_str = "Opening StackOverflow"
        webbrowser.open("https://stackoverflow.com/")
    else:
        response_str = "Application not available"

    return response_str