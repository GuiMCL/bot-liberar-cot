from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager   
from selenium.webdriver.chrome.service import Service
from time import sleep
from tkinter import *
from tkinter import ttk
from typing import Any
import threading
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import threading


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Guilherme Maciel\Desktop\bot cot\sla\assets\frame0")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_argument("--incognito")
#ChromeOptions.add_argument("--headless")
servico = Service(ChromeDriverManager().install())
Navegador = webdriver.Chrome(service=servico , options=ChromeOptions )


#-------------------------------------------------------------------------------------------------------#
#---------------------------------Codigo feito por guilherme maciel-------------------------------------#
#-------------------------------------------------------------------------------------------------------#

class Interface:
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    def execute(self):
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        window = Tk()
        window.geometry("600x400")
        window.configure(bg = "#252424")


        canvas = Canvas(
            window,
            bg = "#252424",
            height = 400,
            width = 600,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_text(
            120.0,
            61.0,
            anchor="nw",
            text="EMAIL",
            fill="#E1E1E6",
            font=("Inter SemiBold", 12 * -1)
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            303.0,
            102.5,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=126.0,
            y=87.0,
            width=354.0,
            height=30.0
        )

        canvas.create_text(
            120.0,
            163.0,
            anchor="nw",
            text="SENHA",
            fill="#E1E1E6",
            font=("Inter SemiBold", 12 * -1)
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            300.0,
            205.0,
            image=entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_2.place(
            x=126.0,
            y=183.0,
            width=348.0,
            height=42.0
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command= lambda:threading.Thread(target=self.get).start(),
            relief="flat"
        )
        button_1.place(
            x=111.0,
            y=272.0,
            width=386.0,
            height=65.0
        )
        window.resizable(False, False)
        window.mainloop()



    def get(self):
        Navegador.get("https://csc.princesadoscampos.wtmh.com.br/login")
        email2 = "{}".format(self.input_from.get())
        senha2= "{}".format(self.input_from_uf.get())
        email = email2
        senha = senha2

        campoemail = Navegador.find_element(By.CSS_SELECTOR , '#login_username')
        sleep(1)
        camposenha = Navegador.find_element(By.CSS_SELECTOR , '#login_password')
        sleep(1)
        botaoentrar = Navegador.find_element(By.XPATH , '//*[@id="form"]/div[3]/input')



        campoemail.send_keys(email)
        sleep(1)
        camposenha.send_keys(senha2)
        botaoentrar.click()
        sleep(10)
   



Interface().execute()





