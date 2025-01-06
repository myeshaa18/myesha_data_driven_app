from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import requests
import json
from io import BytesIO
import random

# Initialize the main window
root = Tk()
root.title("Juice World App")
root.geometry("600x700")
root.resizable(0, 0)

# Function to fetch random cocktail data
def get_random_cocktail():
    url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
    response = requests.get(url)
    data = response.json()

    drink_name = data["drinks"][0]["strDrink"]
    drink_id = data["drinks"][0]["idDrink"]
    cocktail_name_label.config(text=f"Name: {drink_name}\nID: {drink_id}")

    image_url = data["drinks"][0]["strDrinkThumb"]
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        image = Image.open(BytesIO(image_response.content))
        image = image.resize((200, 200))
        image = ImageTk.PhotoImage(image)
        cocktail_image_label.config(image=image)
        cocktail_image_label.image = image

# Function to fetch an alcoholic cocktail
def get_alcoholic_cocktail():
    url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Alcoholic"
    response = requests.get(url)
    data = response.json()

    drink = random.choice(data["drinks"])
    drink_name = drink["strDrink"]
    drink_id = drink["idDrink"]

    alcoholName.config(text=f"Name: {drink_name}\nID: {drink_id}")

    image_url = drink["strDrinkThumb"]
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        image = Image.open(BytesIO(image_response.content))
        image = image.resize((200, 200))
        image = ImageTk.PhotoImage(image)
        alcohol_image_label.config(image=image)
        alcohol_image_label.image = image
        
# Function to fetch a non-alcoholic cocktail
def get_non_alcoholic_cocktail():
    url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Non_Alcoholic"
    response = requests.get(url)
    data = response.json()

    drink = random.choice(data["drinks"])
    drink_name = drink["strDrink"]
    drink_id = drink["idDrink"]

    non_alcoholic_name.config(text=f"Name: {drink_name}\nID: {drink_id}")

    image_url = drink["strDrinkThumb"]
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        image = Image.open(BytesIO(image_response.content))
        image = image.resize((200, 200))
        image = ImageTk.PhotoImage(image)
        non_image_label1.config(image=image)
        non_image_label1.image = image

# Function to fetch ingredient details
def search_ingredient():
    ingredient = ingredient_entry.get().strip()
    if not ingredient:
        messagebox.showerror("Error", "Please enter an ingredient name.")
        return

    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?i={ingredient}"
    response = requests.get(url)
    data = response.json()

    ingredient_info.delete("1.0", END)  # Clear previous information

    if data["ingredients"]:
        ingredient_data = data["ingredients"][0]
        name = ingredient_data.get("strIngredient", "N/A")
        description = ingredient_data.get("strDescription", "No description available.")
        type_ = ingredient_data.get("strType", "N/A")
        alcoholic = ingredient_data.get("strAlcohol", "N/A")

        ingredient_info.insert(END, f"Name: {name}\n")
        ingredient_info.insert(END, f"Type: {type_}\n")
        ingredient_info.insert(END, f"Alcoholic: {alcoholic}\n")
        ingredient_info.insert(END, f"Description: {description}\n")
    else:
        ingredient_info.insert(END, "No ingredient found.")

# Function to switch frames
def show_frame(frame):
    frame.tkraise()

# Instructions popup
def show_instructions():
    instructions = "Welcome to the Cocktail App! Use the buttons to explore cocktails."
    messagebox.showinfo("Instructions", instructions)

# Frame 1: Welcome screen
frame1 = Frame(root, width=600, height=700)
image = Image.open("C:\\Users\\Ruzeynah kashif\\Desktop\\cocktail\\cockttt.jpg")
resize_image = image.resize((600, 700))
bg_img1 = ImageTk.PhotoImage(resize_image)
bg_image_label1 = Label(frame1, image=bg_img1)
bg_image_label1.place(x=0, y=0)

appName = Label(frame1, text="Welcome to Cocktail App", bg="pink", fg="red", font=('Roboto', 30, 'bold'))
appName.place(x=60, y=100)


InstrButton = Button(frame1, text="Instructions", bg="pink", fg="red", font=('Roboto', 16, 'bold'), command=show_instructions)
InstrButton.place(x=50, y=600)

nextButton = Button(frame1, text="Go to App", bg="pink", fg="red", font=('Roboto', 16, 'bold'), command=lambda: show_frame(ButtonFrame))
nextButton.place(x=400, y=600)
frame1.place(x=0, y=0)

# Frame 2: Button options
ButtonFrame = Frame(root, width=600, height=700)
image = Image.open("C:\\Users\\Ruzeynah kashif\\Desktop\\cocktail\\image11.jpeg")
resize_image = image.resize((600, 700))
bg_img2 = ImageTk.PhotoImage(resize_image)
bg_image_label2 = Label(ButtonFrame, image=bg_img2)
bg_image_label2.place(x=0, y=0)

h1 = Label(ButtonFrame, text="Click the buttons below", bg="pink", fg="black", font=('Roboto', 18))
h1.place(x=180, y=100)

RandButton = Button(ButtonFrame, text="Random cocktail", bg="red", fg="white", font=('Roboto', 14, 'bold'), command=lambda: show_frame(Frame3))
RandButton.place(x=220, y=200)

alcoholicButton = Button(ButtonFrame, text="Alcoholics", bg="red", fg="white", font=('Roboto', 14, 'bold'), command=lambda: show_frame(Frame4))
alcoholicButton.place(x=220, y=300)

nonalcoholicsButton = Button(ButtonFrame, text="Non-Alcoholics", bg="red", fg="white", font=('Roboto', 14, 'bold'), command=lambda: show_frame(Frame5))
nonalcoholicsButton.place(x=220, y=400)

searchIngredientButton = Button(ButtonFrame, text="Search Ingredient", bg="red", fg="white", font=('Roboto', 14, 'bold'), command=lambda: show_frame(Frame6))
searchIngredientButton.place(x=220, y=500)

ButtonFrame.place(x=0, y=0)

# Frame 6: Ingredient Search
Frame6 = Frame(root, width=600, height=700)
image = Image.open("C:\\Users\\Ruzeynah kashif\\Downloads\\DALL·E 2025-01-06 06.54.42 - A visually appealing background image for a cocktail-themed application screen. The design features a vibrant mix of tropical fruits, cocktail glasses.webp")
resize_image = image.resize((600, 700))
bg_img6 = ImageTk.PhotoImage(resize_image)
bg_image_label6 = Label(Frame6, image=bg_img6)
bg_image_label6.place(x=0, y=0)

h1_ingredient = Label(Frame6, text="Search Ingredient", bg="pink", fg="red", font=('Roboto', 24, 'bold'))
h1_ingredient.place(x=180, y=50)

ingredient_entry = Entry(Frame6, width=30, font=('Roboto', 14))
ingredient_entry.place(x=150, y=150)

search_button_ingredient = Button(Frame6, text="Search", bg="red", fg="white", font=('Roboto', 15, 'bold'), command=search_ingredient)
search_button_ingredient.place(x=250, y=200)

ingredient_info = Text(Frame6, width=50, height=20, font=('Roboto', 12))
ingredient_info.place(x=50, y=250)

back_button_ingredient = Button(Frame6, text="Go Back", bg="red", fg="white", font=('Roboto', 15, 'bold'), command=lambda: show_frame(ButtonFrame))
back_button_ingredient.place(x=400, y=600)

Frame6.place(x=0, y=0)

# Frame 3: Random cocktail
Frame3 = Frame(root, width=600, height=700)
image = Image.open("C:\\Users\\Ruzeynah kashif\\Desktop\\cocktail\\coktt.jpg")
resize_image = image.resize((600, 700))
bg_img3 = ImageTk.PhotoImage(resize_image)
bg_image_label3 = Label(Frame3, image=bg_img3)
bg_image_label3.place(x=0, y=0)

h1 = Label(Frame3, text="Random Alcohol", bg="pink", fg="red", font=('Roboto', 24, 'bold'))
h1.place(x=200, y=50)

cocktail_name_label = Label(Frame3, text="", bg="black", fg="white", font=('Roboto', 16))
cocktail_name_label.place(x=200, y=250)

cocktail_image_label = Label(Frame3, bg="black")
cocktail_image_label.place(x=200, y=300)

nextButton = Button(Frame3, text="Get Alcohol", bg="red", fg="white", font=('Roboto', 16, 'bold'), command=get_random_cocktail)
nextButton.place(x=230, y=150)

BackButton = Button(Frame3, text="Go Back", bg="red", fg="white", font=('Roboto', 16, 'bold'), command=lambda: show_frame(ButtonFrame))
BackButton.place(x=400, y=600)

Frame3.place(x=0, y=0)

# Frame 4: Alcoholic cocktails
Frame4 = Frame(root, width=600, height=700)
image = Image.open("C:\\Users\\Ruzeynah kashif\\Downloads\\DALL·E 2025-01-06 07.00.04 - A visually appealing background image for an alcoholic cocktail-themed application screen. The design features a variety of vibrant cocktails in elega.webp")
resize_image = image.resize((600, 700))
bg_img4 = ImageTk.PhotoImage(resize_image)
bg_image_label4 = Label(Frame4, image=bg_img4)
bg_image_label4.place(x=0, y=0)

h1 = Label(Frame4, text="Alcoholic Drinks", bg="pink", fg="red", font=('Roboto', 24, 'bold'))
h1.place(x=180, y=50)

alcoholName = Label(Frame4, text="", bg="white", fg="black", font=('Roboto', 16))
alcoholName.place(x=200, y=250)

nextButton = Button(Frame4, text="Get Drink", bg="pink", fg="red", font=('Roboto', 15, 'bold'), command=get_alcoholic_cocktail)
nextButton.place(x=230, y=150)

BackButton = Button(Frame4, text="Go Back", bg="pink", fg="red", font=('Roboto', 15, 'bold'), command=lambda: show_frame(ButtonFrame))
BackButton.place(x=400, y=600)

alcohol_image_label = Label(Frame4, bg="black")
alcohol_image_label.place(x=200, y=350)

Frame4.place(x=0, y=0)

# Frame 5: Non-alcoholic cocktails
Frame5 = Frame(root, width=600, height=700)
image = Image.open("C:\\Users\\Ruzeynah kashif\\Desktop\\cocktail\\cock4.jpeg")
resize_image = image.resize((600, 700))
bg_img5 = ImageTk.PhotoImage(resize_image)
bg_image_label5 = Label(Frame5, image=bg_img5)
bg_image_label5.place(x=0, y=0)

h1_non_alcoholic = Label(Frame5, text="Non-Alcoholic Drinks", bg="pink", fg="red", font=('Roboto', 24, 'bold'))
h1_non_alcoholic.place(x=180, y=50)

non_alcoholic_name = Label(Frame5, text="", bg="white", fg="black", font=('Roboto', 16))
non_alcoholic_name.place(x=200, y=250)

next_button_non = Button(Frame5, text="Get Drink", bg="red", fg="white", font=('Roboto', 15, 'bold'), command=get_non_alcoholic_cocktail)
next_button_non.place(x=230, y=150)

back_button_non = Button(Frame5, text="Go Back", bg="red", fg="white", font=('Roboto', 15, 'bold'), command=lambda: show_frame(ButtonFrame))
back_button_non.place(x=400, y=600)

non_image_label1 = Label(Frame5, bg="black")
non_image_label1.place(x=200, y=350)

Frame5.place(x=0, y=0)
# Set the initial visible frame
show_frame(frame1)

root.mainloop()