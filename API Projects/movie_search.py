import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO

class OMBApp():
    #   Initialize user interface method
    def __init__(self, rootWindow):
        self.rootWindow = rootWindow
        self.omdbWindow = tk.Toplevel(rootWindow)
        self.omdbWindow.title("OMDB")
        self.omdbWindow.geometry("500x500")
        self.api_key = "YOUR_API"
        self.create_widgets()

    def create_widgets(self):
        #   Create UI elements
        self.label = tk.Label(self.root, text="Enter Movie Name:")
        self.entry = tk.Entry(self.root, width=20)
        self.search_button = tk.Button(self.root, text="Search", command=self.search_movie)
        self.result_text = tk.Text(self.root, width=40, height=20, wrap=tk.WORD)
        self.poster_label = tk.Label(self.root)

        #   Widget Layout
        self.label.grid(row=0, column=0, padx=10, pady=10)
        self.entry.grid(row=0, column=1, padx=10, pady=10)
        self.search_button.grid(row=0, column=2, padx=10, pady=10)
        self.result_text.grid(row=1, column=0, columnspan=1, padx=10, pady=10)
        self.poster_label.grid(row=1, column=2, columnspan=1, padx=10, pady=10)

    #   Function to handle API call and errors
    def search_movie(self):
        movie_name = self.entry.get()
        if not movie_name:
            messagebox.showerror("Error:", "Please enter a movie name.")
            return
        url = f"http://www.omdbapi.com/?apikey={self.api_key}&t={movie_name}"
        response = requests.get(url)
        if response.status_code != 200:
            messagebox.showerror("Error:", "Failed to retrieve data.")
            return
        data = response.json()
        if data.get("Response") == "False":
            messagebox.showerror("Error:", "Movie not found.")
            return
        self.display_result(data)

    #   Function to display movie results and poster
    def display_result(self, data):
        self.result_text.delete(1.0, tk.END)
        result = (f"Title: {data.get('Title')}\n"
                  f"Year: {data.get('Year')}\n"
                  f"Rated: {data.get('Rated')}\n"
                  f"Released: {data.get('Released')}\n"
                  f"Runtime: {data.get('Runtime')}\n"
                  f"Genre: {data.get('Genre')}\n"
                  f"Director: {data.get('Director')}\n"
                  f"Writer: {data.get('Writer')}\n"
                  f"Actors: {data.get('Actors')}\n"
                  f"Language: {data.get('Language')}\n"
                  f"Country: {data.get('Country')}\n"
                  f"Awards: {data.get('Awards')}\n"
                  f"IMDb Rating: {data.get('imdbRating')}\n")
        self.result_text.insert(tk.END, result)
        poster_url = data.get("Poster")
        if poster_url and poster_url == "N/A":
            response = requests.get(poster_url)
            if response.status_code == 200:
                image_data = response.content
                image = Image.open(BytesIO(image_data))
                image = image.resize((300, 450))
                photo = ImageTk.PhotoImage(image)
                self.poster_label.config(image=photo)
                self.poster_label.image = photo
            else:
                self.poster_label.config(image="", text="No poster available.")
        else:
            self.poster_label.config(image="", text="No poster available.")

#   Execute if script is ran directly
if __name__ == "__main__":
    root = tk.Tk()
    app = OMBApp(root)
    root.mainloop()