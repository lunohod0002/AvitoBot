import openpyxl
book=openpyxl.open("Без названия 1.xlsx",read_only=False,)
sheet=book.active
for row in range(1,sheet.max_row+1):
    print("number="+str(sheet[row][0].value)+"salt="+str(sheet[row][1].value))
    sheet[row][0].value=f"Р23{row}АВ199"
book.save("Без названия 1.xlsx")
book.close()