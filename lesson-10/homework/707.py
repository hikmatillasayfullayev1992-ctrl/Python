## Homework 1. ToDo List Application

#Define Task Class:
#Create a Task class with attributes such as task title, description, due date, and status.
#Define ToDoList Class:
#Create a ToDoList class that manages a list of tasks.
#Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.
#Create Main Program:
#Develop a simple CLI to interact with the ToDoList.
#Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.
#Test the Application:
#Create instances of tasks and test the functionality of your ToDoList
class Task:
    def __init__(self,title,description,due_date,status):
        self.title=title
        self.descriptiion=description
        self.due_date=due_date
        self.status=status
class ToDoList():
    def add_task():       
        task.title=input("Vazifa nomini kiriting: ")
        task.description=input("Vazifa izohi: ")
        task.due_date=input("Vazifa qachon bajariladi: ")
        task.status='Bajarilmagan'
        lst_task[task.title]=[task.description,task.due_date,task.status]
        print(task.description,"Vazifa qo`shildi!\n")
        main()
    def mark_task(ish):
        task_status=input("Bajarilgan bo`lsa '1', bajarilmagan bo`lsa '0' yozing: \n")
        if task_status=='0':
            lst_task[ish][2]='Bajarilmagan'
        else:
            lst_task[ish][2]='Bajarilgan'
        print("Vazifa holati belgilandi!\n")
        main()
    def list_all_task():
        for v in lst_task:
            print(f'Nomi-{v}\nIzoh-{lst_task[v][0]}\nBajarish vaqti-{lst_task[v][1]}\nHolati-{lst_task[v][2]}\n')
        main()
    def incomp_tasks():
        dic_madi=dict(filter(lambda item: 'Bajarilmagan' in item[1], lst_task.items()))
        for m in dic_madi.items():
            print(
                f'Ish nomi: {m[0]}\n'
                f'Izohi: {m[1][0]}\n'
                f'Bajarish vaqti: {m[1][1]}\n'
            )
        main()
def main():
    mainprog=input(
        " Vazifa qo`shish uchun - add\n"
        " Bajarilgan qilib belgilash uchun -mark\n"
        " Barcha vazifalarni chiqarish uchun - list\n"
        " Bajarilmagan vazifalarni chiqarish uchun - incomp yozing\n"
        )
    if mainprog=='add':
        todo.add_task()
    if mainprog=='mark':
        for i in lst_task:
            print(i)
        ish=input('Qaysi isni tanlamoqchisiz? ')
        todo.mark_task(ish)
    if mainprog=='list':
        todo.list_all_task()
    if mainprog=='incomp':
        todo.incomp_tasks()
    else:
        print('Notog`ri buyruq kiritdingiz! Qaytqdqn kiriting')
        main()
lst_task={}
task = Task('','','','')
todo=ToDoList
main()
