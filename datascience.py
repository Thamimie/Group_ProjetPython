import json
import os
import boto3

class Student:
    def __init__(self,kesyon1,kesyon2,kesyon3,kesyon4,kesyon5,kesyon6,kesyon7,kesyon8) :
        self.kesyon1 = kesyon1
        self.kesyon2 = kesyon2
        self.kesyon3 = kesyon3
        self.kesyon4 = kesyon4
        self.kesyon5 = kesyon5
        self.kesyon6 = kesyon6
        self.kesyon7 = kesyon7
        self.kesyon8 = kesyon8

    print(      )
    def poze_kesyon1(self):
        print("1-) Intention de quitter le pays:")
        print("Avez-vous l'intention de quitter le pays apres avoir terminer vos etudes universitaires?") 
        print("1-) Oui")
        print("2-) Non")
        print("3-) Incertain")
        self.kesyon1 = input("reponse_1:") 
        print("  ")
       

    def poze_kesyon2(self):
        print("2-) Tranche d'âge :")
        print("Quel est votre âge actuel?")
        print("1-) Moins de 20 ans")
        print("2-) 20-24 ans")
        print("3-) 25-29 ans")
        print("4-) 30-34 ans")
        print("5-) 35 ans et plus")
        self.kesyon2 = input("reponse)2:") 
        print("  ")

    def poze_kesyon3(self):
        print("3-) Niveau d'études:")
        print("A quel niveau d'études êtes-vous actuellement?")
        print("1-) Licence 1")
        print("2-) Licence 2")
        print("3-) Licence 3")
        print("4-) Licence 4")
        print("5-) DUT 1")
        print("6-) DUT 2")
        self.kesyon3 = input("reponse_3:")
        print("  ")

    def poze_kesyon4(self):
        print("4-) Pays visé:")
        print("Vers quel(s) pays envisagez-vous de vous rendre?")  
        print("1-) États-Unis")
        print("2-) Canada")
        print("3-) Royaume-Uni")
        print("4-) Australie")
        print("5-) France")
        print("6-) Autre (precisez):") 
        self.kesyon4 = input("reponse_4:")
        print("  ") 

    def poze_kesyon5(self):
        print("5-) Raison du départ :")       
        print("Pourquoi envisagez-vous de quitter le pays?") 
        print("1-) Opportunités professionnelles")
        print("2-) Recherche académique")
        print("3-) Qualité de Vie") 
        print("4-) Autre (precisez:)")
        self.kesyon5 = input("reponse_5:")
        print("  ") 

    def poze_kesyon6(self):
        print("6-)Objectif du départ:")
        print("Envisagez-vous de quitter le pays pour des études supplémentaires ou d'autres raisons?")
        print("1-) Études supplémentaires")
        print("2-) Raisons professionnelles")
        print("3-) Raisons personnelles")
        self.kesyon6 = input("reponse_6:") 
        print("  ")

    def poze_kesyon7(self):
        print("7-)Durée prévue à l'étranger :")
        print("Si vous envisagez un départ temporaire,quelle est la durée prévue de votre sejour?") 
        print("1-) Moins d'un an") 
        print("2-) 1-2 ans")
        print("3-) 3-5 ans")
        print("4-) Plus de 5 ans")
        self.kesyon7 = input("reponse_7:") 
        print("  ")

    def poze_kesyon8(self):
        print("8-) Intention de retour dans le pays d'origine :")  
        print("Avez-vous l'intention de retourner dans votre pays d'origine apres votre séjour à l'étranger? ") 
        print("1-) Oui")
        print("2-) Non")
        print("3-) Incertain")
        self.kesyon8 = input("reponse_8:")
        print("  ") 

student = Student("kesyon1","kesyon2","kesyon3","kesyon4","kesyon5","kesyon6","kesyon7","kesyon8")
student.poze_kesyon1()
student.poze_kesyon2()
student.poze_kesyon3()
student.poze_kesyon4()
student.poze_kesyon5()
student.poze_kesyon6()
student.poze_kesyon7()
student.poze_kesyon8()

name_file = 'student_donnee.json'

if not os.path.exists(name_file):
        data_exists = {}
else:
    with open('student_donnee.json','r') as file:
        data_exists = json.load(file)
        print(data_exists)    
        
new_data = {
    "kesyon1" : student.kesyon1,
    "kesyon2" : student.kesyon2,
    "kesyon3" : student.kesyon3,
    "kesyon4" : student.kesyon4,
    "kesyon5" : student.kesyon5,
    "kesyon6" : student.kesyon6,
    "kesyon7" : student.kesyon7,
    "kesyon8" : student.kesyon8
}

data_exists.update({len(data_exists) + 1: new_data})

with open('student_donnee.json','w') as file:
    json.dump(data_exists,file,indent=4)
    print("                                                    Questions ESIH Sondage :"        )
    print("                       *=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*          ")
    print(          )
    print(new_data)

#Konfigire kle AWS yo
aws_access_key_id = 'AKIAXMTC3T25WLCKRH2U'
aws_secret_access_key = '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'

#Configuration de boto3 pour utiliser les variables d'environnement AWS_ACCESS_KEY_ID et AWS_SECRET_ACCESS_KEY
s3 = boto3.client('s3', 
                    aws_access_key_id='AKIAXMTC3T25WLCKRH2U',
                    aws_secret_access_key='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',
                    region_name='us-east-2')

#Lyen kote fichye a ye sou AWS
bucket_name = 'thamprojetbucket'
object_key = 'FORMULAIRE/student_donnee.json'

#Lekti fichye a
try:
    response = s3.get_object(Bucket='thamprojetbucket', Key='FORMULAIRE/student_donnee.json') 
    file_content = response['Body'].read().decode('utf-8')
    print(file_content)
except Exception as e:
    print(f"Erreur lors de la lecture dans S3 : {str(e)}")

#Televèse konti nan yon fichye, (ekriti)
try:
    updated_content = "Nouvo_Konti"
    s3.put_object(Body=updated_content, Bucket='thamprojetbucket', Key='FORMULAIRE/student_donnee.json')
    print("Écriture réussie dans S3.")
except Exception as e:
    print(f"Erreur lors de l'écriture dans S3 : {str(e)}")
