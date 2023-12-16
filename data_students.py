"""Traccia
Un’applicazione scolastica richiede di rappresentare le informazioni sugli studenti
di un corso universitario.
Ogni studente ha un nome e una lista di voti.
Possiamo utilizzare questi elementi come attributi di una classe chiamata Student
Questa classe dovrà consentire all'utente di:
1. visualizzare il nome di uno studente
2. il voto per una data posizione (a partire da 1)
3. assegnare il voto a una data posizione
4. visualizzare il voto più alto
5. la media dei voti
6. ottenere una stringa di rappresentazione delle informazioni sullo
studente.
Quando viene creato un oggetto Student, l'utente fornisce il nome dello studente
e numero di voti. Ogni voto inizialmente è posto a zero."""
class Student:
    def __init__(self,name, grades):
        self.__name = name
        self.__grades =grades
    def get_name(self):
        return self.__name
    def get_grades(self):
        return self.__grades
    def set_name(self,nome):
        self.__name = nome
    def set_grades(self,voti):
        self.__grades = voti
    def set_grade(self, grade, index):
        self.__grades[index] = grade
    def __str__(self):
        return "studente: " + self.__name+\
               "\nvoti: \n" + str(self.__grades)
def load(students, n_grades):
    set_students = {}
    for i in range (students):
        list_grades = []
        ID = i+1 
        name = input("inserisci nome dello studente ")
        for j in range(n_grades):
            grade= int(input("inserisci voto posizione "+ str(j+1)+ " "))
            list_grades.append(grade)
        student = Student(name, list_grades)
        set_students[ID] = student
    print("lista studenti: ")
    for key in set_students:
        print(set_students[key])
    return set_students
#1. visualizzare il nome di uno studente
#2. il voto per una data posizione (a partire da 1)
def view(set_students, ID):
        pos= int(input("inserire posizione del voto da visualizzare "))
        print("len: ",len(set_students))
        print(ID)
        grades = set_students[ID].get_grades()
        print("voto ",pos,"= ", grades[pos-1])
# inserire voto in una data posizione
def update_grade(set_students, ID):
    print(set_students[ID])
    index= int(input("inserire posizione del voto da cambiare "))
    grade = int(input("inserire nuovo voto "))
    student = set_students[ID]
    student.set_grade(grade, index-1)
    print("voti aggiornati :",student.get_grades(), sep ="\n")
    return                         
#4. visualizzare il voto più alto        
def max_vote(set_students,ID):
    grades = set_students[ID].get_grades()
    # ricerca max
    max = grades[0]
    for i in range (len(grades)):
        if max < grades[i]:
            max = grades[i]
    print("il più alto voto di",ID, "è: ", max)
#5. la media dei voti
def mean(set_students,ID):
    grades = set_students[ID].get_grades()
    sum = 0
    for item in grades:
        sum += item
    mean = sum/len(grades)
    print("la media dei voti di :",ID,"è :\n", mean)
def info_students(set_students):
    for key in set_students:
        print(set_students[key])
def main():
    n_stu= int(input("inserire numero studenti "))
    n_grades= int(input("inserire numero di voti "))
    set_students = load(n_stu,n_grades)
    view(set_students, int(input("ID studente del quale si vuole visualizzare un voto ")))
    ID = int(input("ID studente al quale si vuole cambiare un voto "))
    update_grade(set_students, ID)
    max_vote(set_students,ID)
    mean(set_students,ID)
    info_students(set_students)
main()




    
