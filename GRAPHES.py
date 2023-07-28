from numpy import*
import matplotlib.pyplot as plt
from xlsxwriter import*
from scipy.stats import gamma
from time import*

t = linspace(0,1439,1440)

def data_beat () :
    #matrice données
    bpm = []
    #paramètres de la loi de probabilité
    mu_initial = 78
    sigma_initial = 0.4

    mu_variable = mu_initial
    sigma_variable = sigma_initial

    for i in range(len(t)) :
        if (70 <= mu_variable <= 140):
            valeur_bpm = (random.randn(1)*sigma_variable + mu_variable)
            mu_variable = float(valeur_bpm)
            sigma_variable = sigma_initial
            bpm.append(round((float(valeur_bpm)),2))
        elif (70 >= mu_variable) :
            valeur_bpm = (random.randn(1) * sigma_variable + 70)
            mu_variable = float(valeur_bpm)
            bpm.append(round((float(valeur_bpm)), 2))
        elif (140 <= mu_variable) :
            valeur_bpm = (random.randn(1) * sigma_variable + 140)
            mu_variable = float(valeur_bpm)
            bpm.append(round((float(valeur_bpm)), 2))
            
    print(bpm)


    #excel and txt opening
    f = open("bpm.txt", "w")
    workbook = Workbook('datasbpm.xlsx')
    worksheet = workbook.add_worksheet()

    #excel writting :
    for i in range(0,1440) :
        worksheet.write(i,0,t[i])
        worksheet.write(i,1,bpm[i])
    workbook.close()

    #txt writting :
    heure=0
    for i in range(0,1440) :
        ### mise en forme string m
        if ((len(str(i%60)) == 1)) :
            m = '0' + str(i%60)
        else :
            m =  str(i%60)
        ### mise en forme string h
        if (len(str(heure))==1) :
            h  = '0'+str(heure)+':'
        else :
            h= str(heure)+':'
        f.write("INSERT INTO `donnees` (`id_data`, `temps_donnee`, `valeur_donnee`, `id_capteur`) VALUES (NULL, '2023-01-07 " + h + m + ":00.000000', '" + str(bpm[i]) + "', '2'); \n")
        if (i%60 == 59) :
            heure = heure + 1
    f.close()

    ###ploting
    plt.plot(t, bpm)
    plt.title("BPM en fonction du temps")
    plt.xlabel("Temps en minutes")
    plt.ylabel("BPM enregistrés")
    plt.show()
    return bpm

def data_temperature () :
    #matrice données
    temp = []
    #paramètres de la loi de probabilité
    mu_initial = 37.55
    sigma_initial = 0.005

    mu_variable = mu_initial
    sigma_variable = sigma_initial


    for i in range(len(t)):
        if (34 <= mu_variable <= 42):
            valeur_temperature = (random.randn(1)*sigma_variable + mu_variable)
            mu_variable = float(valeur_temperature)
            sigma_variable = sigma_initial
            temp.append(round((float(valeur_temperature)),4))
        elif (34 >= mu_variable) :
            valeur_temperature = (random.randn(1) * sigma_variable + 34)
            mu_variable = float(valeur_temperature)
            temp.append(round((float(valeur_temperature)), 4))
        elif (42 <= mu_variable) :
            valeur_temperature = (random.randn(1) * sigma_variable + 42)
            mu_variable = float(valeur_temperature)
            temp.append(round((float(valeur_temperature)), 4))

        # excel and txt opening
    f = open("temp.txt", "w")
    workbook = Workbook('datastemp.xlsx')
    worksheet = workbook.add_worksheet()

    # excel writting :
    for i in range(0, 1440):
        worksheet.write(i, 0, t[i])
        worksheet.write(i, 1, temp[i])
    workbook.close()

    # txt writting :
    heure = 0
    for i in range(0, 1440):
        ### mise en forme string m
        if ((len(str(i % 60)) == 1)):
            m = '0' + str(i % 60)
        else:
            m = str(i % 60)
        ### mise en forme string h
        if (len(str(heure)) == 1):
            h = '0' + str(heure) + ':'
        else:
            h = str(heure) + ':'
        f.write(("INSERT INTO `donnees` (`id_data`, `temps_donnee`, `valeur_donnee`, `id_capteur`) VALUES (NULL, '2023-01-07 " + h + m + ":00.000000', '" + str(temp[i]) + "', '2'); \n"))

        if (i % 60 == 59):
            heure = heure + 1
    f.close()



    ###ploting
    plt.plot(t, temp)
    plt.title("Température en fonction du temps")
    plt.xlabel("Temps en minutes")
    plt.ylabel("Température enregistrée")
    plt.show()
    return temp

def data_air_quality () :
    #matrice données
    quality = []
    #paramètres de la loi de probabilité
    k_initial = 1
    theta_initial = 2
    #entre 18 et 26
    k_variable = k_initial
    theta_variable = theta_initial

    for i in range(len(t)) :
        valeur_qualite = ((random.gamma(shape=k_variable, scale=theta_variable)/10))+19
        k_variable = float((valeur_qualite)-16)
        theta_variable = theta_initial
        quality.append(float(valeur_qualite))

        # excel and txt opening
    f = open("quality.txt", "w")
    workbook = Workbook('datasquality.xlsx')
    worksheet = workbook.add_worksheet()

    # excel writting :
    for i in range(0, 1440):
        worksheet.write(i, 0, t[i])
        worksheet.write(i, 1, quality[i])
    workbook.close()

    # txt writting :
    f = open("quality.txt", "w")
    heure = 0
    for i in range(0, 1440):
        ### mise en forme string m
        if ((len(str(i % 60)) == 1)):
            m = '0' + str(i % 60)
        else:
            m = str(i % 60)
        ### mise en forme string h
        if (len(str(heure)) == 1):
            h = '0' + str(heure) + ':'
        else:
            h = str(heure) + ':'
        f.write(
            "INSERT INTO `donnees` (`id_data`, `temps_donnee`, `valeur_donnee`, `id_capteur`) VALUES (NULL, '2023-01-07 " + h + m + ":00.000000', '" + str(quality[i]) + "', '2'); \n")
        if (i % 60 == 59):
            heure = heure + 1
    f.close()

    ###ploting
    plt.plot(t, quality)
    plt.title("Concentration de PM10 en fonction du temps")
    plt.xlabel("Temps en minutes")
    plt.ylabel("Concentration en PM10 en µg/m³")
    plt.show()
    return quality

def sql_queries() :

    bpm = data_beat()
    temp = data_temperature()
    quality = data_air_quality()

    # txt writting :
    f = open("sqlqueries.txt", "w")
    heure = 0
    for i in range(0, 1440):
        ### mise en forme string m
        if ((len(str(i % 60)) == 1)):
            m = '0' + str(i % 60)
        else:
            m = str(i % 60)
        ### mise en forme string h
        if (len(str(heure)) == 1):
            h = '0' + str(heure) + ':'
        else:
            h = str(heure) + ':'
        f.write("INSERT INTO `donnees` (`id_data`, `temps_donnee`, `valeur_bpm`, `valeur_temperature`, `valeur_airquality`, `id_capteur`) VALUES (NULL, '2023-01-07 " + h + m + ":00.000000' , '"+str(bpm[i])+"' , '"+ str(temp[i])+"' , '"+str(quality[i])+"', '1'); \n")
        if (i % 60 == 59):
            heure = heure + 1
    f.close()



sql_queries()

