#save data in Excel file
#text_excel.py

import sys
import xlsxwriter

import functions as func


f = open('data.csv')
output = func.get_countries(f)

get_continent = sys.argv[1]
min_density = float(sys.argv[2])

#-------------------------------------------------------------

workbook = xlsxwriter.Workbook(get_continent+'countries.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_paper(9)  # A4
worksheet.center_horizontally()
worksheet.set_margins(left = 0.7, right = 0.7)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

title1 = get_continent + ' countries'
title2 = 'of population density not less than ' + str(min_density)

worksheet.write('B1', title1, bold)
worksheet.write('C1', title2, bold)
worksheet.write('B3', 'country', bold)
worksheet.write('C3', 'population', bold)
worksheet.write('D3', 'area in sq. km', bold)
worksheet.write('E3', 'pop. density', bold)


i = 2
col = 1

#-------------------------------------------------------------

for row in output:
    country = row[0]
    continent = row[1]
    population = row[2]
    area = row[3]
    density = round(float(population) / float(area), 1)
    if continent == get_continent and density >= min_density:
        print '%-30s %10s %10s %10s' %(country, population, area, density)
        i = i + 1
        worksheet.write(i, col,   country)
        worksheet.write(i, col+1, int(population))
        worksheet.write(i, col+2, int(area))
        worksheet.write(i, col+3, density)
        
workbook.close()  