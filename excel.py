import openpyxl


def create_book(name,lis:list):
    filepath = name
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet["A1"].value="Машина"
    sheet["B1"].value="ФИО"
    sheet["C1"].value="Телефоны"
    for dic in lis:
        model =dic["model"]
        number =dic["number"]
        year =dic["year"]
        fio =dic["fio"]
        phone =dic["phone"]

        sheet.append((f"{number} {model} {year}",f"{fio}", phone))

    wb.save(filepath,)
a= [{
    "model":"Mazda c ",
    "year":2004,
    "phone": 89851611586,
    "fio":"George Zhironkin",
    "number":"T239AB199"

},
    {"model":"Benz c ",
    "year":2006,
    "phone": 89851611586,
    "fio":"Ivan Ivanov",
    "number":"T044AB199"

},
]
create_book(r'my_book4.xlsx', a)