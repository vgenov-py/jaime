from flask import Blueprint
import sqlite3 
api = Blueprint("api", __name__)

@api.route("/<country>")
def t_home(country:str):
    con = sqlite3.connect("mes.db")
    def make_dicts(cursor, row):
        return dict((cursor.description[idx][0], value)
                    for idx, value in enumerate(row))

    con.row_factory = make_dicts
    cur = con.cursor()
    data = list(cur.execute(f"SELECT * FROM countries where country = ?", [country.title()]))
            
    return {"success":True, "data":data}