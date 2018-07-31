#!/usr/bin/python3
# -*-coding:Latin-1 -*
import sys
fname = str(sys.argv[1])
print ("File to treat :", fname, "\n")
with open(fname, 'rb') as f:
    content = f.readlines()
datas_tmp, datas = [], []
line_nr, ki, ks, kn, ksr, kp, taux_econo_total, wd_nr = 0, 0, 0, 0, 0, 0, 0, 0
for l2 in content :
    line_nr+=1
    try :
        l = l2.decode(encoding='UTF-8',errors='strict')
        if(l.startswith("===>")) : 
            nm = l[len("===> "):].strip()
            d = {};
            d["line_nr"] = line_nr
            d["name"] = nm
            d["wd"] = []
            datas_tmp.append(d);
        elif(l.startswith("=============")):
            break
        elif(l.startswith("   >")) :
            d[">"] = l[len("   >"):].strip()
        else :
            d["wd"].append(l.strip())
    except UnicodeDecodeError:
        continue
for i in range(1,len(datas_tmp)) :
    if datas_tmp[i]["name"] != datas_tmp[i-1]["name"]:
        datas.append(datas_tmp[i-1])
datas.append(datas_tmp[len(datas_tmp)-1])
for i in datas :
    kp = (len(i["name"])-len(i[">"]))
    ki+=len(i[">"])
    taux_econo_total+=kp
    kn+=len(i["name"])+1 # Une espace après chaque mot
    if kp != 0 : # Si le nbre de lettres économisées est différent de 0
        ks+=1 # Le mot a été prédit et il faut un clic pour saisir la prédiction
    if len(i["name"]) == len(i[">"]) and i != datas[-1] :
    # Si toutes les lettres à prédire ont été saisies
        ki+=1 # On compte l'espace automatique (sauf dernier mot)
    if kp != 0 and i != datas[-1] : # Si la prédiction a été utilisée
        taux_econo_total+=1 # On compte l'espace automatique (sauf dernier mot)
    wd_nr+=1 # Nbre de mots
    # ========== Affichage des résultats (par mot) ==========
    print(i["name"]+' > '+i[">"]) # Mot à prédire > lettre(s) saisie(s)
    if i != datas[-1] : # Tous les mots, sauf le dernier
        print("nbre de lettre(s) a predire :", len(i["name"])+1)
        if kp == 0 : # Le mot n'a pas été prédit
            print("nbre de lettre(s) saisie(s) :", len(i["name"])+1, "/ nbre de lettre(s) economisees :", kp, "\n")
        else : # Le mot a été prédit
            print("nbre de lettre(s) saisie(s) :", len(i[">"]), "/ nbre de lettre(s) economisees :", kp+1, "\n")
    else : # Le dernier mot (sans espace)
        print("nbre de lettre(s) a predire :", len(i["name"]))
        print("nbre de lettre(s) saisie(s) :", len(i[">"]), "/ nbre de lettre(s) economisees :", kp, "\n")
kn-=1 # Enlève l'espace en trop du dernier mot
ksr = (1-(ki+ks)/kn)*100 # Formule du KSR de Vescovi
hit_ratio = (ks/wd_nr)*100 # # Taux d'utilisation de la prédiction
print("========== \n")
print("ki :", ki) # Actual keystrokes
print("ks :", ks) # Keystrokes required to select suggestion
print("ksr :", ksr, "% \n")
print("nbre total de lettres economisees :", taux_econo_total)
# taux_econo_total = (1-(ki/kn))*100
print("taux d'economie de saisie :", (taux_econo_total/kn)*100, "% \n")print("kn :", kn) # Keystrokes required with no prediction enabled
print("nbre total de mots :", wd_nr)
print("hit ratio :", hit_ratio, "%")