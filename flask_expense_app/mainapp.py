from flask import Flask, render_template, request, redirect
import csv
from collections import Counter

app = Flask(__name__)


def get_top_10_common_values(csv_file, field_name, how_many=15):
    with open(csv_file, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        values = [row[field_name] for row in reader]
        mostused_values = [i[0] for i in Counter(values).most_common(how_many)]
        return mostused_values


def load_data_from_csv(csv_file):
    data = []
    with open(csv_file, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return sorted(data, key=lambda x: x["DATE"], reverse=True)


def get_unique_values(csv_file, field_name):
    unique_values = set()
    with open(csv_file, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            unique_values.add(row[field_name])
    return sorted(list(unique_values))


def get_where_new(csv_file, field_name, how_many=15):
    sorted_list = get_unique_values(csv_file, field_name)
    most_used = get_top_10_common_values(csv_file, field_name, how_many)
    return most_used + sorted_list


@app.route("/")
def index():
    data = load_data_from_csv("data.csv")
    where_categories = get_where_new("data.csv", "WHERE")
    how_categories = get_top_10_common_values("data.csv", "HOW")
    return render_template(
        "index.html",
        data=data,
        where_categories=where_categories,
        how_categories=how_categories,
    )


@app.route("/add", methods=["POST"])
def add_expense():
    date = request.form["date"]
    where = request.form["where"]
    amount = request.form["amount"]
    tags = request.form["tags"]
    how = request.form["how"]

    new_expense = {
        "DATE": date,
        "WHERE": where,
        "AMOUNT": amount,
        "TAGS": tags,
        "HOW": how,
    }

    data = load_data_from_csv("data.csv")
    data.append(new_expense)
    save_data_to_csv("data.csv", data)

    return redirect("/")


def save_data_to_csv(csv_file, data):
    sorted_data = sorted(data, key=lambda x: x["DATE"], reverse=True)
    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=["DATE", "WHERE", "AMOUNT", "TAGS", "HOW"]
        )
        writer.writeheader()
        writer.writerows(sorted_data)


@app.route("/update", methods=["POST"])
def update_expense():
    date = request.form["date"]
    where = request.form["where"]
    amount = request.form["amount"]
    tags = request.form["tags"]
    how = request.form["how"]
    edit_id = request.form["edit_id"]

    data = load_data_from_csv("data.csv")
    for expense in data:
        comptext = "{0}-{1}-{2}".format(expense["DATE"], expense["WHERE"], expense["AMOUNT"])
        if comptext == edit_id:
            expense["WHERE"] = where
            expense["AMOUNT"] = amount
            expense["TAGS"] = tags
            expense["HOW"] = how
            break

    save_data_to_csv("data.csv", data)

    return redirect("/")



