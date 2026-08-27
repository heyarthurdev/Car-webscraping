import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt
from pathlib import Path

def scraper(pagina):
    if pagina in range(1, 18):

        assinaturas = {"User-Agent" : "Mozilla/5.0"}
        link = f"https://webscraper.io/test-sites/pagination?page={pagina}"
        request = requests.get(link, headers=assinaturas)

        # print(request)

        soup = BeautifulSoup(request.text, "html.parser")
        cards = soup.find_all("div", class_= "card")

        with open(Path(__file__).parent / f"carros_pagina{pagina}.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Nome" , "Descricao" , "Ano" , "Disponibilidade"])

            for car in cards:
                nome = car.find("h3" , class_="card-title")["title"]
                descricao = car.find("p" , class_= "description").text
                ano_do_carro = car.find("p" , class_="card-text").text
                disponivel = car.find("div", class_="badge").text
                print(f"{nome} -- {descricao} -- {ano_do_carro} -- {disponivel}")

                writer.writerow([nome , descricao , ano_do_carro , disponivel])

            


    else:
        print("Está página não existe!")