from flask import Blueprint, render_template, request
import csv
import json
web = Blueprint("web", __name__)

@web.route("/<country_a>")
def t_home(country_a):
    with open("MES_1223.csv") as file:
        data = csv.reader(file)
        headers = next(data)
        n_gas = []
        combustible_fuels = []
        months = []
        wind = []
        solar = []
        for row in data:
            country = row[0]
            product = row[-3]
            time = row[1]
            if country == country_a.title():
            # if country == country.capitalize():
                value = row[-2]
                if product == "Natural Gas":
                    n_gas.append(float(value))
                    months.append(time)
                elif product == "Total Combustible Fuels":
                    combustible_fuels.append(float(value))
                elif product == "Wind":
                    wind.append(float(value))
                elif product == "Solar":
                    solar.append(float(value))
                
        n_gas.reverse()
        months.reverse()
        combustible_fuels.reverse()
        wind.reverse()
        solar.reverse()
        months = json.dumps(months)
        n_gas = json.dumps(n_gas)
        combustible_fuels = json.dumps(combustible_fuels)
        wind = json.dumps(wind)
        solar = json.dumps(solar)
            
    return render_template("index.html", n_gas=n_gas, months=months, combustible_fuels=combustible_fuels, wind=wind, solar=solar, country_name=country_a)