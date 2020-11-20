import csv

option = 5
while(option != 0):
    option = input('Wybierz opcje, ktora chcesz wykonac:\n1-wyswietl zawartosc pliku csv\n2-dodaj krotke\n3-usun krotke\n0-zakoncz program\n')

    if(option=='1'):
        csvfile=open('CSV.csv','r', newline='')
        obj=csv.reader(csvfile)
        for row in obj:
            print(row)

    if(option=='2'):
        author, title, type, year = input('Podaj autora ksiazki, tytul, rodzaj oraz rok wydania:\n').split()
        tuple = []
        tuple.append((author, title, type, year))
        csvfile=open('CSV.csv','w', newline='')
        obj=csv.writer(csvfile)
        obj.writerow(tuple)
        #obj.close()

    if(option=='3'):
        row_no = input('Podnaj numer krotki, ktora chcesz usunac')
#        csvfile=open('CSV.csv','w', newline='')
#        obj=csv.writer(csvfile)
#        for row in obj:
#            if(row == row_no):
                 
        imp = open('mycsv.csv' , 'rb')
        out = open('mycsv.csv' , 'wb')
        writer = csv.writer(out)
        for row in csv.reader(imp):
            if row == row_no:
                writer.writerow(row)
        imp.close()
        out.close()

    if(option=='0'):
        break