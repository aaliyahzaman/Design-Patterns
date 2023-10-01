#!/usr/bin/env python
# coding: utf-8

# 
# ## <font color="black">Design Patterns</font> ##
# ## <font color="black"> Aaliyah Zaman</font> ##
# 
# ## <font color="black"> 22044192</font> ##
# 
# 
# 
# 
# 

# ## <font color="red">Logbook Exercise 1</font> ##
# 
# Insert a 'code' cell below. In this do the following:
# 
# - line 1 - create a list named "shopping_list" with items: milk, eggs, bread, cheese, tea, coffee, rice, pasta, milk, tea (<font color="red">NOTE: the duplicate items are intentional</font>)
# - line 2 - print the list along with a message e.g. "This is my shopping list ..."
# - line 3 - create a tuple named "shopping_tuple" with the same items
# - line 4 - print the tuple with similar message e.g. "This is my shopping tuple ..."
# - line 5 - create a set named "shopping_set" from "shopping_list" by using the set() method
# - line 6 - print the set with appropriate message and check duplicate items have been removed
# - line 7 - make a dictionary "shopping_dict" - copy and paste the following items and prices: "milk": "£1.20", "eggs": "£0.87", "bread": "£0.64", "cheese": "£1.75", "tea": "£1.06", "coffee": "£2.15", "rice": "£1.60", "pasta": "£1.53".
# - line 8 - print the dictionary with an appropriate message 
# 
# An example of fully described printed output is presented below (some clues here also)
# Don't worry of your text output is different - it is the contents of the compund variables that matter
# 
# ```
# This is my shopping list ['milk', 'eggs', 'bread', 'cheese', 'tea', 'coffee', 'rice', 'pasta', 'milk', 'tea']
# This is my shopping tuple ('milk', 'eggs', 'bread', 'cheese', 'tea', 'coffee', 'rice', 'pasta', 'milk', 'tea')
# This is my Shopping_set with duplicates removes {'rice', 'milk', 'pasta', 'cheese', 'eggs', 'tea', 'bread', 'coffee'}
# This is my shopping_dict {'milk': '£1.20', 'eggs': '£0.87', 'bread': '£0.64', 'cheese': '£1.75', 'tea': '£1.06', 'coffee': '£2.15', 'rice': '£1.60', 'pasta': '£1.53'}
# ```

# #### Solution:-

# In[1]:


shopping_list = ["milk", "eggs", "bread", "cheese", "tea", "coffee", "rice", "pasta", "milk", "tea"]
print("This is my shopping list", shopping_list)

shopping_tuple = tuple(shopping_list)
print("This is my shopping tuple", shopping_tuple)

shopping_set = set(shopping_list)
print("This is my Shopping_set with duplicates removed", shopping_set)

shopping_dict = {
    "milk": "£1.20",
    "eggs": "£0.87",
    "bread": "£0.64",
    "cheese": "£1.75",
    "tea": "£1.06",
    "coffee": "£2.15",
    "rice": "£1.60",
    "pasta": "£1.53"
}
print("This is my shopping_dict", shopping_dict)


# ## <font color="red">Logbook Exercise 2</font> ##
# 
# Create a 'code' cell below. In this do the following:
# 
# - line 1 - Use a comment to title your exercise - e.g. "Unit 2 Exercise" 
# - line 2 - create a list ... li = ["USA","Mexico","Canada"]
# - line 3 - append "Greenland" to the list
# - l4 - print the list to de,monstrate that Greenland is attached
# - l5 - remove "Greenland"
# - l6 - print the list to de,monstrate that Greenland is removed
# - l7 - insert "Greenland" at the beginning of the list
# - l8 - print the resul of l7
# - l9 - shorthand slice the list to extract the first two items - simultaneausly print the output
# - l10 - use a negative index to extract the second to last item - simultaneausly print the output
# - l11 - use a splitting sequence to extract the middle two items - simultaneausly print the output
# 
# An example of fully described printed output is presented below (some clues here also)
# Don't worry of your text output is different - it is the contents of the list that matter
# 
# ```
# li.append('Greenland') gives ...  ['USA', 'Mexico', 'Canada', 'Greenland']
# li.remove('Greenland') gives ...  ['USA', 'Mexico', 'Canada']
# li.insert(0,'Greenland') gives ...  ['Greenland', 'USA', 'Mexico', 'Canada']
# li[:2] gives ...  ['Greenland', 'USA']
# li[-2] gives ...  Mexico
# li[1:3] gives ...  ['USA', 'Mexico']
# ```

# #### Solution:-

# In[2]:


li = ["USA", "Mexico", "Canada"]

li.append("Greenland")

print(li)

li.remove("Greenland")

print(li)

li.insert(0, "Greenland")

print(li)

print(li[:2])

print(li[-2])

print(li[1:-1])


# ## <font color="red">Logbook Exercise 3</font> ##
# 
# Create a 'code' cell below. In this do the following:
# - on the first line create the following set ... a=[0,1,2,3,4,5,6,7,8,9,10] 
# - on the second line create the following set ... b=[0,5,10,15,20,25]
# - on the third line create the following dictionary ... topscores={"Jo":999, "Sue":987, "Tara":960; "Mike":870}
# - use a combination of print() and type() methods to produce the following output
# 
# ```
# list a is ...  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list b is ...  [0, 5, 10, 15, 20, 25]
# The type of a is now ... <class 'list'>
# ```
# 
# - on the next 2 lines convert list a and b to sets using set()
# - on the following lines use a combination of print(), type() and set notaion (e.g. 'a & b', 'a | b', 'b-a') to obtain the following output
# 
# ```
# set a is ...  {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# set b is ...  {0, 5, 10, 15, 20, 25}
# The type of a is now ... <class 'set'>
# Intersect of a and b is [0, 10, 5]
# Union of a and b is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25]
# Items unique to set b are {25, 20, 15}
# ```
# 
# - on the next 2 lines use print(), '.keys()' and '.values()' methods to obtain the following output 
# 
# ```
# topscores dictionary keys are dict_keys(['Jo', 'Sue', 'Tara', 'Mike'])
# topscores dictionary values are dict_values([999, 987, 960, 870])
# ```

# #### Solution:-

# In[1]:


#1
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#2
b = [0, 5, 10, 15, 20, 25]

#3
topscores = {"Jo": 999, "Sue": 987, "Tara": 960, "Mike": 870}

#4
print("List a is ... ", a)
print("List b is ... ", b)
print("The type of a is now ...", type(a))

#5
a = set(a)
b = set(b)

#6
print("Set a is ... ", a)
print("Set b is ... ", b)
print("The type of a is now ...", type(a))

print("Intersect of a and b is", a & b)
print("Union of a and b is", a | b)
print("Items unique to set b are", b - a)

#7
print("Topscores dictionary keys are", topscores.keys())
print("Topscores dictionary values are", topscores.values())


# ### <font color="red">Logbook Exercise 4</font> ###
# 
# Create a 'code' cell below. In this do the following:
# - Given the following 4 lists of names, house number and street addresses, towns and postcodes ...  
# 
# ```
# ["T Cruise","D Francis","C White"]
# ["2 West St","65 Deadend Cls","15 Magdalen Rd"]
# ["Canterbury", "Reading", "Oxford"]
# ["CT8 23RD", "RG4 1FG", "OX4 3AS"]
# ```
# 
# - write a Custom 'address_machine' function that formats 'name', 'hs_number_street', 'town', 'postcode' with commas and spaces between items
# - create a 'newlist' that repeatedly calls 'address_machine' and 'zips' items from the 4 lists
# - write a 'for loop' that iterates over 'new list' and prints each name and address on a separate line
# - the output should appear as follows
# 
# ```
# T Cruise, 2 West St, Canterbury, CT8 23RD
# D Francis, 65 Deadend Cls, Reading, RG4 1FG
# C White, 15 Magdalen Rd, Oxford, OX4 3AS
# ```
# 
# - <font color="red">HINT:</font> look at "# CUSTOM FUNCTION WORKED EXAMPLES 3 & 4" above

# #### Solution:-

# In[2]:


#1
def address_machine(name, house_number_street, town, postcode):
    address = "{}, {}, {}, {}".format(name, house_number_street, town, postcode)
    return address

#2 : Given
names = ["T Cruise", "D Francis", "C White"]
house_number_street = ["2 West St", "65 Deadend Cls", "15 Magdalen Rd"]
towns = ["Canterbury", "Reading", "Oxford"]
postcodes = ["CT8 23RD", "RG4 1FG", "OX4 3AS"]

#3
newlist = [address_machine(name, house, town, postcode) for name, house, town, postcode in zip(names, house_number_street, towns, postcodes)]

#4
for address in newlist:
    print(address)


# ## <font color="red">Logbook Exercise 5</font> ##
# 
# Create a 'code' cell below. In this do the following:
# - Create a super class "Person" that takes three string and one integer parameters for first and second name, UK Postcode and age in years.
# - Give "Person" a method "greeting" that prints a statement along the lines "Hello, my name is Freddy Jones. I am 22 years old and my postcode is HP6 7AJ"
# - Create a "Student" class that extends/inherits "Person" and takes additional parameters for degree_subject and student_ID.
# - give "Student" a "studentGreeting" method that prints a statement along the lines "My student ID is SN123456 and I am reading Computer Science"
# - Use either Python {} format or C-type %s/%d notation to format output strings
# - Create 3 student objects and persist these in a list
# - Iterate over the three objects and call their "greeting" and "studentGreeting" methods
# - Output should be along the lines of the following
# 
# ```
# Hello, my name is Dick Turpin. I am 32 years old and my postcode is HP11 2JZ
# My student ID is DT123456 and I am reading Highway Robbery
#  
# Hello, my name is Dorothy Turpin. I am 32 years old and my postcode is SO14 7AA
# My student ID is DT123457 and I am reading Law
#  
# Hello, my name is Oliver Cromwell. I am 32 years old and my postcode is OX35 14RE
# My student ID is OC123456 and I am reading History
# ```

# #### Solution:-

# In[3]:


#1
class Person:
    def __init__(self, first_name, last_name, postcode, age):
        self.first_name = first_name
        self.last_name = last_name
        self.postcode = postcode
        self.age = age
#2
    def greeting(self):
        print("Hello, my name is {0} {1}. I am {2} years old and my postcode is {3}".format(self.first_name, self.last_name, self.age, self.postcode))
        
#3
class Student(Person):
    def __init__(self, first_name, last_name, postcode, age, degree_subject, student_id):
        super().__init__(first_name, last_name, postcode, age)
        self.degree_subject = degree_subject
        self.student_id = student_id
#4
    def student_greeting(self):
        print("My student ID is {0} and I am reading {1}".format(self.student_id, self.degree_subject))
        
#5
students = [
    Student("Dick", "Turpin", "HP11 2JZ", 32, "Highway Robbery", "DT123456"),
    Student("Dorothy", "Turpin", "SO14 7AA", 32, "Law", "DT123457"),
    Student("Oliver", "Cromwell", "OX35 14RE", 32, "History", "OC123456")
]

#6
for student in students:
    student.greeting()
    student.student_greeting()
   
    print()
    
        


# ## <font color="red">Logbook Exercise 6</font> ##
# 
# 
# 
# 
# - The end result should be capable of creating the output below
# - Clearly ***comment your code*** to highlight the insertions you have made
# - Note: if you don't see the GUI immediately look for the icon Jupyter icon in your task bar (also higlighted below)

# ### Examine Steve Lipton's "simplest ever" version for the MVC 
# 
# #### Solution:-

# let's break it down into its components: 
# 
#    1. Model (MyModel Class)
#         
#         * Attrributes :
#             - myList
#                 which is initialized with a list containing three elements: 'duck', 'duck', and 'goose'.
#         * Methods :
#             - getList()
#                 Returns the current list stored in myList.
#             - initListWithList(aList)
#                 Initializes the myList with the given aList.
#             - addToList(item)
#                 Adds the item to the myList,
#                 updates the internal list,
#                 and calls the listChanged() method,
#                 which is the delegate to notify the controller of the change.
#                 
#    2. View (MyView Class)
#    
#        * This class represents the user interface elements.
#        * Initializes a Tkinter frame (self.frame) and sets up a basic GUI with buttons and labels.
#        * Getters and Setters Methods :
#            - getEntry_text()
#                + Returns the text entered in the entry field.
#            - setEntry_text(text)
#                + Sets the text of the entry field with the given text.
#            - getLabel_text():
#                + Returns the text displayed in the label.
#            - setLabel_text(text)
#                + Sets the text of the label with the given text.
#        * The view also creates buttons for "Quit" and "Add", an entry field, and a label.
#        
#    3. Controller (MyController Class)
#     
#         * The MyController class combines together the model and view.
#         * Initializes instances of both the model (MyModel) and view (MyView).
#         * Event Handlers for the buttons:
#             * quitButtonPressed()
#                 + Calling :
#                     - when the "Quit" button is pressed. 
#                 + Actions :
#                     - It terminat the application.
#             * addButtonPressed(): 
#                 + Calling :
#                     - when the "Add" button is pressed.
#                 + Actions :
#                     - It updates the label text with the text from the entry field
#                       and adds the text to the model's list using addToList().
#             * listChangedDelegate():
#                 + A delegate that is called by the model 
#                   when the list is internally changed. 
#                   It is responsible for updating the view with the new data.
# 

# ### Note how when the MyController object is initialised it:
#   * passes a reference to itself to the MyModel and MyView objects it creates
#   
#   * Thereby allowing MyModel and MyView to create 'delegate' vc (virtual control) aliases to call back the MyController object
#   
#   #### Solution:-

# When the MyController object is initialized, it establishes a two-way communication link between itself (MyController) and two objects (Mymodel and MyView ) it creates.
# 
# The communication is established as:
# 
# 1. MyController Initialization
#     
#     ```python
#     #Initializes the model and passes a reference to itself
#     self.model = MyModel(self)
#     #Initializes the view and passes a reference to itself.
#     self.view = MyView(self)
#     ```
#     
# 2. MyModel Initialization
# 
#     It receives the reference to the MyController instance (vc) as an argument
#     ```python
#     class MyModel():
#         def __init__(self, vc):
#             self.vc = vc
#     ```
# 
# 3. MyView Initialization
# 
#     It also receives the reference to the MyController instance (vc) as an argument
#     ```python
#     class MyView(Frame):
#         def __init__(self, vc):
#             self.vc = vc
#     ```
# 
# 4. Creating Delegates (Virtual Controllers)
#     * After MyModel and MyView have received the reference to the MyController instance (vc),
#       they can create delegates that allow them to call back methods on the MyController object.
#       
#       ```python
#         class MyModel():
#             def listChangedDelegate(self):
#                 print(self.model.getList())
#                 self.vc.listChangedDelegate()
#        ```

# 
# #### Solution:-

# In[ ]:


#MVC_Template_01
#2014 May 23  by Steven Lipton http://makeAppPie.com
#Controller initializing MVC -- simplest version possible.
#Additional annotations by R Mather - Oct 2018

# MVC EXTENDED WITH DELETE BUTTON

# Tkinter is a Python binding to the Tk GUI toolkit/library - RM
from tkinter import *
 
# A Model-View-Controller framework for TKinter.
# Model: Data Structure. Controller can send messages to it, and model can respond to message.
# View : User interface elements. Controller can send messages to it. View can call methods from Controller when an event happens.
# Controller: Ties View and Model together. turns UI responses into chages in data.
 


#Controller: Ties View and Model together.
#       --Performs actions based on View events.
#       --Sends messages to Model and View and gets responses
#       --Has Delegates - RM NOTE: essential for communications between view and model via control
 
class MyController():
    def __init__(self,parent):
        self.parent = parent
        # CRITICAL PART OF THE MVC 
        # RM NOTES:
        # MyController passes a reference to itself (self) when it creates MyModel and MyView objects
        # This allows the MyModel and MyView objects to create 'delegates' (see 'vc' = virtual controller?)
        # The vc objects can then call methods on the MyControl object, thereby allowing the View to update the Model via the Controller 
        self.model = MyModel(self)    # initializes the model
        self.view = MyView(self)  #initializes the view
        # Initialize objects in view
        self.view.setEntry_text('Add to Label') # a non cheat way to do MVC with tkinter control variables
        self.view.setLabel_text('Ready')
    
    #event handlers
    def quitButtonPressed(self):
        self.parent.destroy()
    def addButtonPressed(self):
        self.view.setLabel_text(self.view.entry_text.get())
        # CRITICAL PART OF THE MVC 
        # RM NOTES - In one operation:
        #[1] Get the text from the VIEW;
        #[2] Add it to the MODEL by appending it to the list
        self.model.addToList(self.view.entry_text.get())
    
    ##########################################################################################################
    # New code to create event handler 'removeButtonPressed' in MyController, which removes the last item from the list in MyModel.
    
    def removeButtonPressed(self):
        if self.model.getList():
            self.model.removeLastItem()
            self.view.setLabel_text("Last item removed")
        else:
            self.view.setLabel_text("List is empty")
    ##########################################################################################################
        
    
    def listChangedDelegate(self):
        #model internally changes and needs to signal a change
        print(self.model.getList())
 
#View : User interface elements.
#       --Controller can send messages to it.
#       --View can call methods from Controller vc when an event happens.
#       --NEVER communicates with Model.
#       --Has setters and getters to communicate with controller
 
class MyView(Frame):
    
    def __init__(self,vc):
        self.frame=Frame()
        self.frame.grid(row = 0,column=0)
        self.vc = vc
        self.entry_text = StringVar()
        self.entry_text.set('nil')
        self.label_text = StringVar()
        self.label_text.set('nil')
        self.loadView()

    def loadView(self):
        quitButton = Button(self.frame,text = 'Quit', command= self.vc.quitButtonPressed).grid(row = 0,column = 0)
        addButton = Button(self.frame,text = "Add", command = self.vc.addButtonPressed).grid(row = 0, column = 1)
        
        ##########################################################################################################
        # New code to create Remove button that is binded with event handler 'removeButtonPressed' in MyController.
        removeButton = Button(self.frame, text="Remove", command=self.vc.removeButtonPressed).grid(row=0, column=2)
        
        ##########################################################################################################
        
        entry = Entry(self.frame,textvariable = self.entry_text).grid(row = 1, column = 0, columnspan = 3, sticky = EW)
        label = Label(self.frame,textvariable = self.label_text).grid(row = 2, column = 0, columnspan = 3, sticky = EW)

    def getEntry_text(self):
    #returns a string of the entry text
        return self.entry_text.get()
    def setEntry_text(self,text):
    #sets the entry text given a string
        self.entry_text.set(text)
    def getLabel_text(self):
    #returns a string of the Label text
        return self.label_text.get()
    def setLabel_text(self,text):
    #sets the label text given a string
        self.label_text.set(text)
 
#Model: Data Structure.
#   --Controller can send messages to it, and model can respond to message.
#   --Uses delegates from vc to send messages to the Control of internal change
#   --NEVER communicates with View
#   --Has setters and getters to communicate with Controller
 
class MyModel():
    def __init__(self,vc):
        self.vc = vc
        self.myList = ['duck','duck','goose']
        self.count = 0
#Delegates-- Model would call this on internal change
    def listChanged(self):
        self.vc.listChangedDelegate()
#setters and getters
    def getList(self):
        return self.myList
    def initListWithList(self, aList):
        self.myList = aList
    def addToList(self,item):
        print("returned")
        myList = self.myList
        myList.append(item)
        self.myList=myList
        self.listChanged()
    ##########################################################################################################
    # New code of method which removes the last item from the list.
    
    def removeLastItem(self):
        print("returned")
        if self.myList:
            self.myList.pop()
            self.listChanged()
        
    ##########################################################################################################
       
 
def main():
    # Creates a root window from the Tk GUI class
    root = Tk()
    frame = Frame(root )
    root.title('Hello TEST')
    app = MyController(root)
    root.mainloop()
 
if __name__ == '__main__':
    main()  


# ## <font color="red">Logbook Exercise 7</font> ##
# 
# - Your task is to extend the Observer example below with a pie-chart view of model data and to copy this cell and the solution to your logbook
# - The bar chart provides a useful example of structure
# - Partial code is provided below for insertion, completion (note '####' requires appropriate replacement) and implementation
# - you will also need to create an 'observer' object from the PieView class and attach it to the first 'model'
# 
# ```
# # Pie chart viewer/ConcreteObserver - overrides the update() method
# class PieView(####):
# 
#     def update(####, ####): #Alert method that is invoked when the notify() method in a concrete subject is invoked
#         # Pie chart, where the slices will be ordered and plotted counter-clockwise:
#         labels = ####
#         sizes = ####
#         explode = (0.1, 0, 0, 0, 0, 0)  # only "explode" the 1st slice
#         fig1, ax1 = plt.subplots()
#         ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
#         ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#         plt.####()
# 
# ```
# 
# 

# #### Solution:-

# In[3]:


import matplotlib.pyplot as plt
import numpy as np


# Nicely abstracted structure by which any model can notify any observer (view) of changes in the model
class Subject(object): #Represents what is being 'observed'

    def __init__(self):
        self._observers = [] # This where references to all the observers are being kept
                             # Note that this is a one-to-many relationship: there will be one subject to be observed by multiple _observers

    def attach(self, observer):
        if observer not in self._observers: #If the observer is not already in the observers list
            self._observers.append(observer) # append the observer to the list

    def detach(self, observer): #Simply remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers: # For all the observers in the list
            if modifier != observer: # Don't notify the observer who is actually doing the updating 
                observer.update(self) # Alert the observers
                
# Represents the 'data' for which changes will produce notifications to any registered view/observer objects 
class Model(Subject): # Extends the Subject class

    def __init__(self, name):
        Subject.__init__(self)
        self._name = name # Set the name of the model
        self._labels = ['Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp']
        self._data = [10,8,6,4,2,1]

    @property #Getter that gets the labels
    def labels(self):
        return self._labels

    @labels.setter #Setter that sets the labels
    def labels(self, labels):
        self._labels = labels
        self.notify() # Notify the observers whenever somebody changes the labels
        
    @property #Getter that gets the data
    def data(self):
        return self._data

    @data.setter #Setter that sets the labels
    def data(self, data):
        self._data = data
        self.notify() # Notify the observers whenever somebody changes the data
        

# This is the 'standard' view/observer which also acts as an 'abstract' class whereby deriving Bar/Chart/Table views override the update() method
# This 'abstracted' layer is always shown in examples but is important to demonstrate potential polymorphic behaviour of update()
class View():
    
    def __init__(self, name=""):
         self._name = name #Set the name of the Viewer

    def update(self, subject): #Alert method that is invoked when the notify() method in a concrete subject is invoked
        print("Generalised Viewer '{}' has: \nName = {}; \nLabels = {}; \nData = {}".format(self._name, subject._name, subject._labels, subject._data))

# Table 'chart' viewer/ConcreteObserver - overrides the update() method
class TableView(View):
    
    def update(self, subject): #Alert method that is invoked when the notify() method in a concrete subject is invoked
        fig = plt.figure(dpi=80)
        ax = fig.add_subplot(1,1,1)
        table_data = list(map(list,zip(subject._labels, subject._data)))
        table = ax.table(cellText=table_data, loc='center')
        table.set_fontsize(14)
        table.scale(1,4)
        ax.axis('off')
        plt.show()

# Bar chart viewer/ConcreteObserver - overrides the update() method
class BarView(View):
        
    def update(self, subject): #Alert method that is invoked when the notify() method in a concrete subject is invoked
        objects = subject._labels
        y_pos = np.arange(len(objects))
        performance = subject._data
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Usage')
        plt.title('Programming language usage')
        plt.show()

# Pie chart viewer/ConcreteObserver - overrides the update() method
class PieView(View):

    def update(self, subject): #Alert method is invoked when the notify() method in a concrete subject is invoked
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = subject._labels
        sizes = subject._data
        explode = (0.1, 0, 0, 0, 0, 0)  # only "explode" the 1st slice
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

#Let's create our subjects
m1 = Model("Model 1")
m2 = Model("Model 2") # This is not used!

# Create observers
v1 = View("1: standard text viewer")
v2 = TableView("2: table viewer")
v3 = BarView("3: bar chart viewer")
v4 = PieView("4: pie chart viewer")
####

# Attaches the observers to the first model
m1.attach(v1)
m1.attach(v2)
m1.attach(v3)
m1.attach(v4)
####

# Calls the notify() method to see all the charts in their unchanged state
m1.notify()

# Change the properties of our first model
# Change 1 triggers all 4 views and updates their labels
m1.labels = ['C#','PHP','JavaScript','ASP','Python','Smalltalk']
# Change 2 triggers all 4 views and updates their data
m1.data = [1,18,8,60,3,1]

# Reference (Plot Types, n,d) 


# ## <font color="red">Logbook Exercise 8</font> ##
# 
# - Your task is to extend the modified version of Burkhard Meier's button factory (below) to create a text field factory
# - In tkinter textfields are 'Entry' widgets
# - similary to the button factory structure you will need:
#  - a concrete Entry widget factory class - name it TextFactory()
#  - the TextFactory's Factory Method - name it createText(...)
#  - an abstract product - name it TextBase() and give it default attributes 'textvariable' and 'background'
#  - a getTextConfig(...) method
#  - 3x concrete text products - name these Text_1/2/3 
#  - ... and assign them textvariable values of " red/blue/green type" respectively
#  - ... and assign them background values of 'red/blue/green' respectively
#  - to extend the OOP class with a createTextFields() method
#  - ... that creates a factory object
#  - and the Entry fields ... the code for the first Entry Field is as follows
#  ```
#         # Entry field 1
#         sv=tk.StringVar()
#         tx = factory.createText(0).getTextConfig()[0]
#         sv.set(tx)
#         bg  = factory.createText(0).getTextConfig()[1]
#         action = tk.Entry(self.widgetFactory, textvariable=sv, background=bg, foreground="white")   
#         action.grid(column=1, row=1)  
#  ```

# #### Solution:-

# Below is the extended version of Burkhard Meier's button factory.
# 
# 1. Changes that are made:
# 
# * TextFactory() is a factory class created to create concrete Entry widgets.
# * The Factory Method createText(...) is implemented within TextFactory.
# * TextBase() is an abstract product that has default properties like "textvariable" and "background."
# * A new function getTextConfig(...) is introduced to improve configurability.
# * Text_1, Text_2, and Text_3 are three unique concrete text products that are instantiated. The textvariable values "red," "blue," and "green," as well as the associated backdrop values, are all present in them.
# * A createTextFields() function is added as part of additional OOP extension to produce the factory object and Entry fields.
# 
# 2. Reason for changes:
# 
# These changes adhere to the principles of the Factory Method pattern, emphasising the separation of product creation from usage. By implementing these changes:
# New products (concrete classes) can be added or existing ones can be changed without requiring changes to the client code that utilises these products.
# The codebase becomes more maintainable and supports code reuse, making it easier to extend or adapt as requirements evolve.
# 

# In[1]:


import tkinter as tk
from tkinter import ttk
from tkinter import Menu


class ButtonFactory():
    def createButton(self, type_):
        return buttonTypes[type_]()
            
class ButtonBase():     
    relief     ='flat'
    foreground ='white'
    def getButtonConfig(self):
        return self.relief, self.foreground
    
class ButtonRidge(ButtonBase):
    relief     ='ridge'
    foreground ='red'        
    
class ButtonSunken(ButtonBase):
    relief     ='sunken'
    foreground ='blue'        

class ButtonGroove(ButtonBase):
    relief     ='groove'
    foreground ='green'        

buttonTypes = [ButtonRidge, ButtonSunken, ButtonGroove]
class TextFactory():
    def createText(self, type_):
        return textTypes[type_]()
            

class TextBase():     
    textvariable = ''
    background = ''
    
    def getTextConfig(self):
        return self.textvariable, self.background


class Text_1(TextBase):
    textvariable = " red type"
    background = "red"
    
    
class Text_2(TextBase):
    textvariable = " blue type"
    background = "blue"
    
    
class Text_3(TextBase):
    textvariable = " green type"
    background = "green"
    

textTypes = [Text_1, Text_2, Text_3]
     
     
    
class OOP():
    def __init__(self): 
        self.win = tk.Tk()         
        self.win.title("Python GUI")      
        self.createWidgets()

    def createWidgets(self):    
        self.widgetFactory = ttk.LabelFrame(text=' Button Factory ')
        self.widgetFactory.grid(column=0, row=0, padx=8, pady=4)        

        self.createButtons()
        self.createTextFields()
         

    def createButtons(self):
            
        factory = ButtonFactory()

        # Button 1
        rel = factory.createButton(0).getButtonConfig()[0]
        fg  = factory.createButton(0).getButtonConfig()[1]
        action = tk.Button(self.widgetFactory, text="Button "+str(0+1), relief=rel, foreground=fg)   
        action.grid(column=0, row=1)  

        # Button 2
        rel = factory.createButton(1).getButtonConfig()[0]
        fg  = factory.createButton(1).getButtonConfig()[1]
        action = tk.Button(self.widgetFactory, text="Button "+str(1+1), relief=rel, foreground=fg)   
        action.grid(column=0, row=2)  
        
        # Button 3
        rel = factory.createButton(2).getButtonConfig()[0]
        fg  = factory.createButton(2).getButtonConfig()[1]
        action = tk.Button(self.widgetFactory, text="Button "+str(2+1), relief=rel, foreground=fg)   
        action.grid(column=0, row=3)
    
    def createTextFields(self):        
        factory = TextFactory()

        # Entry field 1
        sv = tk.StringVar()
        tx = factory.createText(0).getTextConfig()[0]
        sv.set(tx)
        bg = factory.createText(0).getTextConfig()[1]
        action = tk.Entry(self.widgetFactory, textvariable=sv, background=bg, foreground="white")   
        action.grid(column=1, row=1)  

        # Entry field 2
        sv = tk.StringVar()
        tx = factory.createText(1).getTextConfig()[0]
        sv.set(tx)
        bg = factory.createText(1).getTextConfig()[1]
        action = tk.Entry(self.widgetFactory, textvariable=sv, background=bg, foreground="white")   
        action.grid(column=1, row=2)  

        # Entry field 3
        sv = tk.StringVar()
        tx = factory.createText(2).getTextConfig()[0]
        sv.set(tx)
        bg = factory.createText(2).getTextConfig()[1]
        action = tk.Entry(self.widgetFactory, textvariable=sv, background=bg, foreground="white")   
        action.grid(column=1, row=3)  
     
#==========================
oop = OOP()
oop.win.mainloop()


# ## <font color="red">Logbook Exercise 9</font> ##
# 
# - Extend the Jungwoo Ryoo's Abstract Factory below to mirror the structure used by a statically typed languages by:
#  - adding a 'CatFactory' and a 'Cat' class with methods that are compatible with 'DogFactory' and 'Dog' respectively
#  - providing an Abstract Factory class/interface named 'AnimalFactory' and make both the Dog and Cat factories implement this
#  - providing an AbstractProduct (name this 'Animal') and make both Dog and cat classes implement this
# - Use in-code comments (#) to identify the abstract and concrete entities present in Gamma et al. (1995)
#  - comments should include: "# Abstract Factory #"; "# Concrete Factory #"; "# Abstract Product #"; "# Concrete Product #"; and "# The Client #"
# - Implement the CatFactory ... the end output should look something like this ...
# 
# ```
# Our pet is 'Dog'!
# Our pet says hello by 'Woof'!
# Its food is 'Dog Food'!
# 
# Our pet is 'Cat'!
# Our pet says hello by 'Meeoowww'!
# Its food is 'Cat Food'!
# ```
# 

# #### Solution:-

# Below is provide the extended version of Jungwoo Ryoo's Abstract Factory
# 
# 1. Changes that are made:
# 
#     The extension of Jungwoo Ryoo's Abstract Factory involves several key components:
# 
# * Introducing the 'CatFactory' and 'Cat' classes. These upgrades are made to work seamlessly with the 'DogFactory' and 'Dog' classes that are already in use.
# * Establishing an 'AnimalFactory'-named abstract class or interface. This interface will be implemented by both the existing 'DogFactory' and the newly introduced 'CatFactory,' ensuring a uniform approach to factory building.
# * Creating a class of abstract goods called 'Animal.' The 'Dog' and 'Cat' classes will both use this common basis, encouraging uniform behaviour within the framework.
# 
# 2. Reason for changes:
# 
#     These modifications improve the Abstract Factory design by making it more flexible to future modifications and additions. It promotes code reusability, maintainability, and a clear separation of concerns, which are crucial principles in software design and architecture.
# 

# In[1]:


# Abstract Product
class Animal:
    """One of the objects to be returned"""
    def speak(self):
        pass
    def __str__(self):
        pass


# Concrete Product
class Dog(Animal):
    def speak(self):
        return "Woof!"
    def __str__(self):
        return "Dog"


# Concrete Product
class Cat(Animal):
    def speak(self):
        return "Meeoowww!"
    def __str__(self):
        return "Cat"


# Abstract Factory
class AnimalFactory:
    """Abstract Factory"""
    def get_pet(self):
        pass
    def get_food(self):
        pass


# Concrete Factory
class DogFactory(AnimalFactory):
    """Concrete Factory"""
    def get_pet(self):
        """Returns a Dog object"""
        return Dog()
    def get_food(self):
        """Returns a Dog Food object"""
        return "Dog Food!"


# Concrete Factory
class CatFactory(AnimalFactory):
    """Concrete Factory"""
    def get_pet(self):
        """Returns a Cat object"""
        return Cat()
    def get_food(self):
        """Returns a Cat Food object"""
        return "Cat Food!"


# The Client
class PetStore:
    """PetStore houses our Abstract Factory"""
    def __init__(self, pet_factory=None):
        """pet_factory is our Abstract Factory"""
        self._pet_factory = pet_factory
    def show_pet(self):
        """Utility method displays details of objects returned by DogFactory"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'!".format(pet_food))


# Create a Concrete Factory (Dog Factory)
factory = DogFactory()
# Create a pet store housing our Abstract Factory (Dog Factory)
shop = PetStore(factory)
# Invoke the utility method to show the details of our pet (Dog)
shop.show_pet()

# Create a Concrete Factory (Cat Factory)
factory = CatFactory()
# Create a pet store housing our Abstract Factory (Cat Factory)
shop = PetStore(factory)
# Invoke the utility method to show the details of our pet (Cat)
shop.show_pet()


# ## <font color="red">Logbook Exercise 10</font> ##
# 
# - Modify Jungwoo Ryoo's Strategy Pattern to showcase ***OpenCV*** capabilities with different image processing strategies
# - We will use the ***OpenCV*** (Open Computer Vision) library which has been reproduced with Python bindings
# - OpenCV has many standard computer science image-processing filters and includes powerful AI machine learning algorithms
# - The following resources provide more information on OpenCv with Python ...
#  - Beyeler, M. (2015). OpenCV with Python blueprints. Packt Publishing Ltd.
#  - Joshi, P. (2015). OpenCV with Python by example. Packt Publishing Ltd.
#  - The cartoon effect is from http://www.askaswiss.com/2016/01/how-to-create-cartoon-effect-opencv-python.html and https://www.tutorialspoint.com/cartooning-an-image-using-opencv-in-python
# 
# ### Development stages ###
# - Install the OpenCV package - we have to do this manually ...
#  - Start Anaconda Navigator
#  - From Anaconda run the CMD.exe terminal
#  - At the prompt type ... ``` conda install opencv-python ```
#  - The process may pause with a prompt ... ```Proceed ([y]/n)?``` ... just accept this ... ```y```
# - Copy Jungwoo Ryoo's code to a code cell below this one
# - As well as the ***types*** module you will need to provide access to OpenCV and numpy as follows
# ```
#     # Import OpenCV
#     import cv2
#     import numpy as np
# ```
# - Please place a copy of clouds.jpg in the same directory as your Jupyter logbook 
# - The code for each strategy and some notes on implementing these are below ...
# - The output should look something like this ... but if you wish feel free to experiment with something else ... cats etc.!
# 
# ### Implementing image processing strategies ###
# 
# - There will be six strategy objects s0-s5, where s0 is the default strategy of the **Strategy** class
# - Instead of assigning a name to each strategy object, you will need to reference the image to be processed - 'clouds.jpg'
#  - i.e. s0.image = "clouds.jpg"
# - The *body* code for each strategy is below, you will need to provide the method signatures and their executions
# 
# 
# #### strategy s0 ####
# 
# The default ***execute()*** method that simply displays the image sent to it 
# 
# ```
#         print("The image {} is used to execute Strategy 0 - Display image".format(self.image))
#         img_rgb = cv2.imread(self.image)
#         cv2.imshow('Image', img_rgb)
# ```
# 
# #### strategy s1 ####
# 
# This converts a colour image into a mononochrome one - suggested strategy method name is ***strategy_greyscale***
# 
# ```
#     img_rgb = cv2.imread(self.image)
#     img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
#     cv2.imshow('Greyscale image', img_gray)
#     
# ```
# 
# #### strategy s2 ####
# 
# This applies a blur filter to an image - suggested strategy method name is ***strategy_blur***
# 
# ```
#     img_rgb = cv2.imread(self.image)
#     img_blur = cv2.medianBlur(img_rgb, 7)
#     cv2.imshow('Blurred image', img_blur)
# 
# ```
# 
# #### strategy s3 ####
# 
# This produces a colour negative image from a colour one - suggested strategy method name is ***strategy_colNegative***
# 
# ```
#   img_rgb = cv2.imread(self.image)
#     for x in np.nditer(img_rgb, op_flags=['readwrite']):
#         x[...] = (255 - x)
#     cv2.imshow('Colour negative', img_rgb)
# 
# ```
# 
# #### strategy s4 ####
# 
# This produces a monochrome negative image from a colour one - suggested strategy method name is ***strategy_greyNegative***
# 
# ```
#     img_rgb = cv2.imread(self.image)
#     img_grey = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
#     for x in np.nditer(img_grey, op_flags=['readwrite']):
#         x[...] = (255 - x)
#     cv2.imshow('Monochrome negative', img_grey)
# ```
# 
# #### strategy s5 ####
# 
# This produces a cartoon-like effect - suggested strategy method name is ***strategy_cartoon***
# 
# ```
#     #Use bilateral filter for edge smoothing.
#     num_down = 2 # number of downsampling steps
#     num_bilateral = 7 # number of bilateral filtering steps
#     img_rgb = cv2.imread(self.image)
#     # downsample image using Gaussian pyramid
#     img_color = img_rgb
#     for _ in range(num_down):
#         img_color = cv2.pyrDown(img_color)
#     # repeatedly apply small bilateral filter instead of applying one large filter
#     for _ in range(num_bilateral):
#         img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=9, sigmaSpace=7)
#     # upsample image to original size
#     for _ in range(num_down):
#         img_color = cv2.pyrUp(img_color)
#     #Use median filter to reduce noise convert to grayscale and apply median blur
#     img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
#     img_blur = cv2.medianBlur(img_gray, 7)
#     #Use adaptive thresholding to create an edge mask detect and enhance edges
#     img_edge = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=2)
#     # Combine color image with edge mask & display picture, convert back to color, bit-AND with color image
#     img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
#     img_cartoon = cv2.bitwise_and(img_color, img_edge)
#     # display
#     cv2.imshow("Cartoon-ised image", img_cartoon); cv2.waitKey(0); cv2.destroyAllWindows()
# 
# ```

# #### Solution:-

# Below is the modified version of Jungwoo Ryoo's Abstract Factory to showcase OpennCV capabilities with different image processing strategies.
# 
# 1. Modifications that are made:
# 
#         Using the Python-bound version of the OpenCV (Open Computer Vision) package, we will modify. OpenCV features numerous common image-processing filters from computer science as well as potent AI machine learning algorithms.
# 
#         For the implementation, we use 6 image processing strategies which are
#     * GreyScale: 
#     This changes a colour of an image into one that is monochromatic.
#     * Blur:
#     An image is given a blur filter in this way.
#     * ColNegitive :
#     It turns a coloured image into a negative colour in the process.
#     * GreyNagitive:
#     Using a coloured image as a source, this creates a monochrome negative image.
#     * Cartoon:
#     This produces a cartoon-like effect of the given image.
#     
# 
# 2. Reason for Modifications:
# 
#         The changes implemented to Jungwoo Ryoo's Abstract Factory in a better way by the different representational view of the image using strategies pattern.
# 
# 3. Better under the circumstances:
# 
#         Under the circumstances, this Modified Pattern is better due to its exceptional capacity to convey complicated information both swiftly and thoroughly, visual representations have repeatedly shown to be superior to other modes of communication for humans. The way the human brain is built makes it capable of processing visual information quickly and efficiently.
# 

# In[3]:


# Example from Jungwoo Ryoo (2015)

# The 'types' module is needed to support dynamic creation of new types. In this case we dynamically create 
# ... a new method type
import types #Import the types module

##########################################################################################################
#import OpenCV
import cv2
import numpy as np
        
##########################################################################################################

# plot_image will display the image inside Jupyter notebook in the output cell

def plot_image(title, image):
    plt.title(title)
    #  OpenCV uses BGR (Blue-Green-Red) color channel order by default, whereas matplotlib uses RGB (Red-Green-Blue) order.
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Turn off axis labels and ticks
    plt.show()

# Although 'concrete' this performs the role of the Strategy interface in the GoF example 
class Strategy:
    """The Strategy Pattern class"""    
    def __init__(self, image):
        self.name = "Default Strategy"
        ##################################################################################################
        self.image = image
        ##################################################################################################
            
    # Although 'concrete' this performs an equivalent role to the GoF "AlgorithmInterface()"
    def execute(self): #This gets replaced by another version if another strategy is provided.
        """The defaut method that prints the name of the strategy being used"""

##################################################################################################
        print("The image {} is used to execute Strategy 0 - Display image".format(self.image))
        img_rgb = cv2.imread(self.image)
        cv2.imshow('Image', img_rgb)
        
# Replacement method 1 - this is a concrete implementation of 'AlgorithmInterface'
def strategy_greyscale(self):
    """This converts a colour image into a mononochrome one"""
    print("The image {} is used to execute Strategy 1 (Greyscale image)".format(self.image))
    img_rgb = cv2.imread(self.image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    #cv2.imshow('Greyscale image', img_gray)
    plot_image('Greyscale image', img_gray)

# Replacement method 2 - this is a concrete implementation of 'AlgorithmInterface'
def strategy_blur(self):
    """Applies a blur filter to an image"""
    print("The image {} is used to execute Strategy 2 (Blurred image)".format(self.image))
    img_rgb = cv2.imread(self.image)
    img_blur = cv2.medianBlur(img_rgb, 7)
    #cv2.imshow('Blurred image', img_blur)
    plot_image('Blurred image', img_blur)
    
def strategy_colNegative(self):
    """Produces a colour negative image from a colour one"""
    print("The image {} is used to execute Strategy 3 (Colour negative)".format(self.image))
    img_rgb = cv2.imread(self.image)
    for x in np.nditer(img_rgb, op_flags=['readwrite']):
        x[...] = (255 - x)
    #cv2.imshow('Colour negative', img_rgb)
    plot_image('Colour negative', img_rgb)

def strategy_greyNegative(self):
    """Produces a monochrome negative image from a colour one"""
    print("The image {} is used to execute Strategy 4 (Monochrome negative)".format(self.image))
    img_rgb = cv2.imread(self.image)
    img_grey = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    for x in np.nditer(img_grey, op_flags=['readwrite']):
        x[...] = (255 - x)
    #cv2.imshow('Monochrome negative', img_grey)
    plot_image('Monochrome negative', img_grey)

    
def strategy_cartoon(self):
    """Produces a cartoon-like effect"""
    print("The image {} is used to execute Strategy 5 (Cartoon-ised image)".format(self.image))
    num_down = 2 # number of downsampling steps
    num_bilateral = 7 # number of bilateral filtering steps
    img_rgb = cv2.imread(self.image)
    # downsample image using Gaussian pyramid
    img_color = img_rgb
    for _ in range(num_down):
        img_color = cv2.pyrDown(img_color)
    # repeatedly apply small bilateral filter instead of applying one large filter
    for _ in range(num_bilateral):
        img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=9, sigmaSpace=7)
    # upsample image to original size
    for _ in range(num_down):
        img_color = cv2.pyrUp(img_color)
    #Use median filter to reduce noise convert to grayscale and apply median blur
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.medianBlur(img_gray, 7)
    #Use adaptive thresholding to create an edge mask detect and enhance edges
    img_edge = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=2)
    # Combine color image with edge mask & display picture, convert back to color, bit-AND with color image
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
    # Resize img_edge to match the dimensions of img_color
    img_edge = cv2.resize(img_edge, (img_color.shape[1], img_color.shape[0]))
    
    img_cartoon = cv2.bitwise_and(img_color, img_edge)
    # display
    #cv2.imshow("Cartoon-ised image", img_cartoon); cv2.waitKey(0); cv2.destroyAllWindows()
    plot_image("Cartoon-ised image", img_cartoon);
    
image_path = "clouds.jpg"

# Let's create our default strategy
s0 = Strategy(image_path)
# Let's execute our default strategy
s0.execute()


# strategy s1
s1 = Strategy(image_path)
s1.execute = types.MethodType(strategy_greyscale, s1)  
s1.execute()

# strategy s2
s2 = Strategy(image_path)
s2.execute = types.MethodType(strategy_blur, s2)
s2.execute()

# strategy s3
s3 = Strategy(image_path)
s3.execute = types.MethodType(strategy_colNegative, s3)
s3.execute()

# strategy s4
s4 = Strategy(image_path)
s4.execute = types.MethodType(strategy_greyNegative, s4)
s4.execute()

# strategy s5
s5 = Strategy(image_path)
s5.execute = types.MethodType(strategy_cartoon, s5)
s5.execute()

# (Team, 2021)
# (Open Cv, n.d)
# (Soothing Imaage, n.d)
##################################################################################################


# ## <font color="red">Logbook Exercise 11</font> ##
# 
# - Demonstrate the use of ```__iter__()```, ```__next()__``` and ```StopIteration``` using ...
# - ... the <font color="red">first four items from the top10books list</font> (see above) ... 
# - ... and the following structure
# 
# ```
# mylist = ['item1', 'item2', 'item3'] 
# 
# iter_mylist = iter(mylist) 
# 
# try: 
#     print( next(iter_mylist))  
#     print( next(iter_mylist))  
#     print( next(iter_mylist))
#     # Exceeds numbe of items so should raise StopIteration exception
#     print( next(iter_mylist)) 
# except Exception as e:
#     print(e)
#     print(sys.exc_info())
# 
# ```

# #### Solution:-

# In[4]:


import sys

class BookIterator:
    def __init__(self, collection, number_items):
        self.collection = collection
        self.number_items = number_items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.number_items:
            book = self.collection[self.index]
            self.index += 1
            return book
        raise StopIteration

top10books = [
    "Anna Karenina by Leo Tolstoy",
    "Madame Bovary by Gustave Flaubert",
    "War and Peace by Leo Tolstoy",
    "Lolita by Vladimir Nabokov",
    "The Adventures of Huckleberry Finn by Mark Twain",
    "Hamlet by William Shakespeare",
    "The Great Gatsby by F. Scott Fitzgerald",
    "In Search of Lost Time by Marcel Proust",
    "The Stories of Anton Chekhov by Anton Chekhov",
    "Middlemarch by George Eliot",
]


book_iterator = BookIterator(top10books, number_items=4)

try:
    print(next(book_iterator))
    print(next(book_iterator))
    print(next(book_iterator))
    print(next(book_iterator))
    print(next(book_iterator))  # Exceeds the number of items, should raise StopIteration
except Exception as e:
    print(e)
    print(sys.exc_info())


# ## <font color="red">Logbook Exercise 12 - The Adapter DP</font> ##
# 
# - Modify Jungwoo Ryoo's Adapter Pattern example (the one with 'country' classes that 'speak' greetings) to showcase:
#  - the ***polymorphic*** capability of the Adpater DP 
#  - the geo-data capabilities of ***matplotlib geographical projections*** ...
#  - in combination with ***Cartopy geospatial data processing*** package to ***produce maps and other geospatial data analyses***.
# - A frequent problem in handling geospatial data is that the user often needs to convert it from one form of map projection (essentially a formula to convert the globe into a plane for map-representation) to another map projection
# 
# 
# - Fortunately other clever people have written the algorithms we need
# - Less fortunately, the interfaces of all the classes that return projections are different
# 
# ##  Development Stages ##
# - We need ...
#  - first, to install the Python cartographic ***Cartopy*** package. In Anaconda launch a CMD.exe terminal and enter the following ...
#  ```
#      conda install -c conda-forge cartopy
#  ```
#  - to insert a code cell below this one ... and copy the extended example of Ryoo's Adapter above (with 'speak' methods in Korean, British and German) in this ...
#  - an ***Adapter*** - Ryoo's adapter is already a well-engineered solution that requires no modification
#  - then to import some essential packages 
#  ```
#      import cartopy.crs as ccrs
#      import matplotlib.pyplot as plt
#  ```
#  - then add the 'adaptee' classes - here represented by the plot axes and their map projections
#  ```
#     class PlateCarree: 
#         def __init__(self):
#             self.name = "PlateCarree"
#         def project_PlateCarree(self):
#             ax = plt.axes(projection=ccrs.PlateCarree())
#             return ax
#     
#     class InterruptedGoodeHomolosine:
#         def __init__(self):
#             self.name = "InterruptedGoodeHomolosine"    
#         def project_InterruptedGoodeHomolosine(self):
#             ax = plt.axes(projection=ccrs.InterruptedGoodeHomolosine())
#             return ax
# 
#     class AlbersEqualArea:
#         def __init__(self):
#             self.name = "AlbersEqualArea"    
#         def project_AlbersEqualArea(self):
#             ax = plt.axes(projection=ccrs.AlbersEqualArea())
#             return ax   
# 
#     class Mollweide:
#         def __init__(self):
#             self.name = "Mollweide"    
#         def project_Mollweide(self):
#             ax = plt.axes(projection=ccrs.Mollweide())
#             return ax
#  ```
#  - similarly to Ryoo's example you will need a collection to store projection objects
#  - again, simlarly to Ryoo, to create all the projection objects (e.g. ```plateCarree =PlateCarree()``` )
#  - again, similarly to Ryoo, to append to the collection key-value pairs for each projection and its projection method
#  - finally to traverse the list of objects to:
#  
#  ```
#     # Create an axes with the specified projection  
#     ax = obj.project()
#     # Attach Cartopy's default geospatially registered map/image of the world 
#     ax.stock_img()
#     # Add the coastlines - highlight these with a black vector 
#     ax.coastlines()
#     # Print the name of the object/projection
#     print(obj.name)
#     # Plot the axes, projection and render the map-image to the projection
#     plt.show()
# 
#  ```
# 
# 
#  

# #### Solution:-

# Below is the modified version of Jungwoo Ryoo's Abstract Factory to showcase the polymorphic capability of the Adpater DP
# 
# 1. Modifications that are Made:
# 
#     The polymorphic capability of the Adapter Design Pattern (DP) offers a versatile solution for software design. The geo-data capabilities of matplotlib geographical projections empower data visualization with a geographic context. Matplotlib's geographical projections enable the creation of maps that accurately represent spatial relationships and distributions
# 
#     So, here represented by the plot axes and their map projections
#     ```
#         class PlateCarree: 
#             def __init__(self):
#                 self.name = "PlateCarree"
#             def project_PlateCarree(self):
#                 ax = plt.axes(projection=ccrs.PlateCarree())
#                 return ax
#         
#         class InterruptedGoodeHomolosine:
#             def __init__(self):
#                 self.name = "InterruptedGoodeHomolosine"    
#             def project_InterruptedGoodeHomolosine(self):
#                 ax = plt.axes(projection=ccrs.InterruptedGoodeHomolosine())
#                 return ax
# 
#         class AlbersEqualArea:
#             def __init__(self):
#                 self.name = "AlbersEqualArea"    
#             def project_AlbersEqualArea(self):
#                 ax = plt.axes(projection=ccrs.AlbersEqualArea())
#                 return ax   
# 
#         class Mollweide:
#             def __init__(self):
#                 self.name = "Mollweide"    
#             def project_Mollweide(self):
#                 ax = plt.axes(projection=ccrs.Mollweide())
#                 return ax
#     ````
# 
# 2. Reason for Modifications:
# 
#     This modification is because the capabilities of matplotlib's geographical projections are greatly enhanced when used in conjunction with the Cartopy geospatial data processing package, the capabilities of matplotlib's geographical projections are greatly enhanced. Cartopy provides a suite of tools for handling and analysing geospatial data. This combination allows for the creation of comprehensive maps and other geospatial data analyses.
# 
# 3. Modified Version
# 

# In[2]:


import cartopy.crs as ccrs
import matplotlib.pyplot as plt

class PlateCarree: 
        def __init__(self):
            self.name = "PlateCarree"
        def project(self):
            ax = plt.axes(projection=ccrs.PlateCarree())
            return ax
    
class InterruptedGoodeHomolosine:
        def __init__(self):
            self.name = "InterruptedGoodeHomolosine"    
        def project(self):
            ax = plt.axes(projection=ccrs.InterruptedGoodeHomolosine())
            return ax

class AlbersEqualArea:
        def __init__(self):
            self.name = "AlbersEqualArea"    
        def project(self):
            ax = plt.axes(projection=ccrs.AlbersEqualArea())
            return ax   

class Mollweide:
        def __init__(self):
            self.name = "Mollweide"    
        def project(self):
            ax = plt.axes(projection=ccrs.Mollweide())
            return ax\
        
projection_objects = [
    PlateCarree(),
    InterruptedGoodeHomolosine(),
    AlbersEqualArea(),
    Mollweide()
]

for obj in projection_objects:
    # Create an axes with the specified projection  
    ax = obj.project()
    # Attach Cartopy's default geospatially registered map/image of the world 
    ax.stock_img()
    # Add the coastlines - highlight these with a black vector 
    ax.coastlines()
    # Print the name of the object/projection
    print(obj.name)
    # Plot the axes, projection and render the map-image to the projection
    plt.show()
# (Cartopy.crs.CRS#, nd)
# (Coordinate reference systems in cartopy¶, n.d)


# 4. Evaluation
# 
#     The polymorphic nature of the Adapter DP promotes flexible software design, matplotlib geographical projections enhance the visualization of geographic data, and the integration of Cartopy geospatial data processing with matplotlib enables the creation of sophisticated maps and geospatial analyses. This powerful combination empowers developers and researchers to effectively work with diverse data sources and create insightful geospatial visualizations.

# ## <font color="red">Logbook Exercise 13 - The Decorator DP</font> ##
# 
# - Repair the code below so that the decorator reveals the name and docstring of aTestMethod()
# - Note ... the @wrap decorator is NOT needed here
# 
# ```
#     <<< Name of the 'decorated' function ...  aTestMethod  >>> 
#     <<< Docstring for the 'decorated' function is ...  This is a method to test the docStringDecorator  >>>
#     What is your name? ... Buggy Code
#     Hello ... Buggy Code
# ```

# #### Solution:-

# In[1]:


def docStringDecorator(f):
    '''Decorator that automatically reports name and docstring for a decorated function'''
    def decorator(*args, **kwargs):
        print("<<< Name of the 'decorated' function ... ",f.__name__," >>> ")
        print("<<< Docstring for the 'decorated' function is ... ",f.__doc__," >>>")
        return f(*args, **kwargs)
    return decorator


@docStringDecorator
def aTestMethod():
    '''This is a method to test the docStringDecorator'''
    nm = input("What is your name? ... ")
    msg = "Hello ... " + nm
    return msg

print(aTestMethod())


# ## <font color="red">Logbook Exercise 14 - The 'conventional' Singleton DP</font> ##
# 
# - Insert a code cell below here
# - Copy the code from Dusty Philips' singleton
# - Create two objects
# - Test output using ```print( ... )``` and ```repr( ... )``` as well as the ```==``` operator to determine whether or not the two objects are the same and occupy the same memory addresses
# - Make a note below of your findings
# 

# #### Solution:-

# In[2]:


## SINGLETON - Extended from Dusty Philips (2015) ##

class OneOnly:
    _singleton =  None
    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(OneOnly, cls).__new__(cls, *args, **kwargs)
        return cls._singleton
    
# Creating two objects
p1 = OneOnly()
p2 = OneOnly()

# Testing output using print
print("p1 = ", p1)
print("p2 = ", p2)

# Testing output using repr
print("repr(p1) = ", repr(p1))
print("repr(p2) = ", repr(p2))

# Testing if the two objects are same and occupy the same addresses
print("p1 == p2:", p1 == p2)
print("Memory address of p1:", id(p1))
print("Memory address of p2:", id(p2))



# ### My observations having tested the two objects are ... ###
# 
# * The print(...) statement will display the memory address where the object p1 and p2 are stored.
# * The repr(...) statements will display the memory adresses but in a more formal representation.
# * The == operator will compare the two objects, and since the singleton design pattern ensures there's only one instance p1 and p2 should be the same object and hence p1 and p2 should return True. 
# * The code demonstrates the Singleton pattern. Both p1 and p2 are the same instance and they have the same memory address expected for a Singleton.

# ## <font color="red">Logbook Exercise 15 - The 'Borg' Singleton DP</font> ##
# 
# - Repeat the exercise above ...
# - Insert a code cell below here
# - Copy the code from Alex Martelli's 'Borg' singleton
# - Create THREE objects ... ***NOTE***: pass a name for the object when you call the constructor
# - Test output using ```print( ... )``` and ```repr( ... )``` as well as the ```==``` operator to determine whether or not the objects are the same and occupy the same memory addresses
# - ***Also*** can you use ```print( ... )``` to test the assertion in the notes above that ... "- ```_shared_state``` is effectively static and is only created once, when the first singleton is instantiated "
# - Make a note below of your findings
# 

# #### Solution:-

# In[2]:


# Singleton/BorgSingleton.py
# Alex Martelli's 'Borg'

class Borg:
    _shared_state = {}
    
    def __init__(self):
        self.__dict__ = self._shared_state
        print("Value of self._shared_state is ..."+str(self._shared_state))

class Singleton(Borg):
    def __init__(self, arg):
        # Here the 'static' Borg class is updated with the state of the new singleton object 
        Borg.__init__(self)
        self.val = arg
    def __str__(self): 
        return self.val
    
## CODE TO BE IMPLEMENTED FOR LOGBOOK EX 15 BELOW HERE ##

s1 = Singleton("s1")
s2 = Singleton("s2")
s3 = Singleton("s3")

# Testing output using print(...)
print("Testing output using print(...)")
print("s1 : ", s1)
print("s2 : ", s2)
print("s3 : ", s3)

# Testing output using repr(...)
print("Testing output using repr(...)")
print("repr(s1) : ", repr(s1))
print("repr(s2) : ", repr(s2))
print("repr(s3) : ", repr(s3))

# Testing if the three objects are the same and occupy the same memory addresses
print("Testing if the three objects are the same and occupy the same memory addresses")
if(s1 == s2): print("s1 == s2 ==> Same object")
else: print("s1 == s2 ==> Different object")

if(s1 == s2): print("s1 == s2 ==> Same object")
else: print("s1 == s2 ==> Different object")

if(s1 == s2): print("s1 == s2 ==> Same object")
else: print("s1 == s2 ==> Different object")

# Checking if _shared_state is effectively static and is only created once when the first singleton is instantiated
print("Checking if _shared_state is effectively static and is only created once when the first singleton is instantiated")
print("Value of s1._shared_state is..." + str(s1._shared_state))
print("Value of s2._shared_state is..." + str(s2._shared_state))
print("Value of s3._shared_state is..." + str(s3._shared_state))

# (Python repr() method (with examples), n.d)


# ### My observations having tested the three objects are ... ###
# 
# * The print(...) statements display the memory address where the objects s1, s2, and s3 are stored.
# * The repr(...) statements also display the memory address, but in a more formal representation.
# * The == operator compares the objects, and since the 'Borg' Singleton design pattern allows multiple instances with shared state, the three objects will not be the same, and the == comparison will return False for all pairs (s1 == s2, s1 == s3, s2 == s3).
# * The _shared_state attribute is effectively static and shared among all instances of the Singleton class. This is evident from the output, which shows that all three objects have the same value for _shared_state.

# ## <font color="red">Logbook Exercises 16 and 17</font> ##
# 
# - Per the assignment brief, for the third and final part of your assignment (copied below), note that it is necessary to write about <font color="red">TWO</font> additional Design Patterns ...
#   - *In you logbooks draw on a selection of Two Design Patterns, and document these using the following headings: 1 intent; 2 motivation; 3 structure (embed UML diagrams if applicable); 4 implementation; 5 sample code (your working example); 6 evaluation – raise any key points concerning programming language idioms, consequences of using the pattern, examples of appropriate uses with respect to application, architecture and implementation requirements* [40 marks]
# 
#  - Clearly it will be necessary to insert both markdown and code cells. 
#  - Please make sure that all cells are properly titled with the excercise they represent 
#  - Use and embed any screen capture that supports your assignment responses
# 
# - Suitable task subjects include:
#  - Demonstrating a new pattern (one which we haven't encountered)
#  - Presenting a pattern that we have addressed in a new/alternative/re-engineered format
#  - Converting a pattern to another programming language
#  - Identifying patterns in well known frameworks (e.g. for Python web development you might examine Django, Flask and/or Jinja2)
# 

# #### Solution :-

# ## The State Design Pattern ##
# 
# ### Intent: ### 
# The State Design Pattern allows an object to change its behavior when its internal state changes. By separating each state into distinct classes and assigning behavior to the current state, it helps in the management of complex conditional logic. The pattern encourages the Open/Closed Principle because it makes it simpler to add new states without changing the existing code.
# 
# ### Motivation: ###
# 1. Simplified Conditional Logic :- 
# The State Pattern replaces multiple conditional statements with individual state classes, making the code more maintainable and readable.
# 2. Encapsulation :-
# Each state class encapsulates behavior related to a specific state, making the code easier to understand and modify.
# 3. Extensibility :-
# It allows for easy addition of new states without modifying the existing code.
# 3. Clear Separation of Concerns :-
# The pattern separates the state-specific behavior from the main context object, reducing complexity.
# 
# 
# ### Structure ###
# 
# Typically, the State Pattern includes the following elements:
# 
# Context: The main object that maintains a reference to the current state and delegates behavior to the state objects.
# 
# State: The interface or abstract class that defines a common interface for all concrete states.
# 
# ConcreteState: The specific state classes that implement the behavior for a particular state.
# 
# ![state_obj_DP.png](attachment:state_obj_DP.png)
# 
# ### Implementation ###
# 
# In this implementation, a Context class that keeps track of the current state has been developed. The interface for all concrete states is represented by the abstract class known as "State." ConcreteStateA and ConcreteStateB, two concrete states, carry out their particular behavior. Each concrete state's handle() method carries out operations in accordance with its unique state.
# 
# We create ConcreteStateA and ConcreteStateB instances in the client code. Next, a Context object is created and its initial state is set to ConcreteStateA. In order to support state transitions, we also set the context for each concrete state.
# 
# The Context class's request() method passes the request on to the current state, which then takes the appropriate action in accordance with the current state.
# 

# ### Sample Example Code ###

# In[3]:


from abc import ABC, abstractmethod

class Context:
    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        self._state = state

    def request(self):
        self._state.handle()

# State (Abstract State)
class State(ABC):
    @abstractmethod
    def handle(self):
        pass

# ConcreteState A
class ConcreteStateA(State):
    def handle(self):
        print("State A: Performing action based on State A")
        self.context.set_state(ConcreteStateB())

# ConcreteState B
class ConcreteStateB(State):
    def handle(self):
        print("State B: Performing action based on State B")
        # State transitions (optional)
        self.context.set_state(ConcreteStateA())

if __name__ == "__main__":
    state_a = ConcreteStateA()
    state_b = ConcreteStateB()

    context = Context(state_a)
    state_a.context = context
    state_b.context = context

    context.request()

    context.set_state(state_b)
    context.request()
    
    # (State design patter, 2023)
    # (Design patterns and refactoring, n.d)
    # (Pankaj, 2022)
    # (Design patterns tutorial, n.d)


# ### Evaluation ###
# 
# The State Pattern is helpful in situations where the behavior of an object depends on its internal state and where various states call for various behaviors.
# The code is made simpler to understand, modify, and extend because it encourages a clear separation of concerns.
# When working with complex state transitions and conditional logic, the pattern becomes especially useful.
# 
# The State Pattern has many uses, including creating state machines, creating games, managing user interfaces, and managing workflows.
# 
# To prevent problems like cyclic state changes or undesirable side effects, it becomes essential to manage state transitions carefully.
# 
# To ensure flexibility and maintainability of the code, careful state interface and state-specific behavior design is essential.
# 
# 

# ## The Interpreter Design Pattern ##
# 
# ### Intent: ### 
# 
# The Interpreter Pattern is a behavioral pattern that is used for interpreting expressions or sentences in a language. It establishes a grammar for the language and offers an interpreter that applies the grammar to sentences or expressions. Domain-specific languages are typically parsed and understood using this technique.
# 
# ### Motivation: ###
# 
# 1. Language Interpretation: 
# The pattern allows parsing and interpreting expressions in a language using a predefined grammar.
# 2. Simplified Grammar: 
# It breaks down complex language grammar into smaller, manageable classes, reducing complexity in parsing.
# 3. Extensibility: 
# It allows for the addition of new language elements by defining new classes for the grammar rules.
# 
# 
# 
# ### Structure ###
# 
# The following elements make up the Interpreter Pattern's UML diagram:
# 
# * An abstract class called AbstractExpression defines the method that is used to interpret expressions.
# * A concrete class that implements the AbstractExpression interface is called TerminalExpression. It stands in for the grammar's terminal expressions.
# * A concrete class that implements the AbstractExpression interface is called NonTerminalExpression. It stands in for the grammar's non-terminal expressions.
# * A class called "context" contains data about the environment in which interpretation is to take place.
# 
# ![Interpreter_obj_DP.png](attachment:Interpreter_obj_DP.png)
# 
# ### Implementation ###
# 
# A basic arithmetic expression evaluator using the Interpreter Pattern is implemented below. We have four classes: Expression, NumberExpression, AddExpression, and SubtractExpression.
# 
# Expression is an abstract class representing the AbstractExpression interface. It has an interpret method that will be implemented by its concrete subclasses.
# 
# NumberExpression is a terminal expression that represents a number in the expression.
# 
# AddExpression and SubtractExpression are non-terminal expressions representing addition and subtraction, respectively. They hold references to other expressions (either terminal or non-terminal) and implement the interpret method to perform the corresponding operation.
# 
# The Context class is an empty class used to hold any contextual information required during interpretation (not used in this example).
# 

# ### Sample Example Code ###

# In[4]:


# Abstract Expression
class Expression:
    def interpret(self, context):
        pass

# Terminal Expression
class NumberExpression(Expression):
    def __init__(self, number):
        self.number = number

    def interpret(self, context):
        return self.number

# Non-Terminal Expression
class AddExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)

class SubtractExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) - self.right.interpret(context)

# Context
class Context:
    pass


if __name__ == "__main__":
    # Expression: 2 + 3 - 1
    context = Context()
    expression = SubtractExpression(AddExpression(NumberExpression(2), NumberExpression(3)), NumberExpression(1))

    result = expression.interpret(context)
    print("Solution of Expresion = ",result)
    
# (Interpreter design pattern, 2018)
# (Design patterns and refactoring, n.d)
# (C# interpreter, n.d)
# (Rajeshvelmani, 2023)


# ### Evaluation ###
# 
# The Interpreter Pattern is useful when working with languages or grammars that need to be evaluated or interpreted.
# By dividing complex expressions into smaller expressions and interpreting each one one at a time, it offers a sophisticated method for evaluating complex expressions.
# The process of adding new concrete expressions and updating the interpreter makes it simple to change the grammar or add new expressions.
# When working with a large number of expressions or a highly complex grammar, the pattern can, however, become complex.
# Applications like query languages, rule engines, and calculators that interpret or evaluate user-defined rules or expressions are suitable choices for the Interpreter Pattern.
# 
# 
# 

# 
# 
# References
# 
# Plot types# (no date) Plot types - Matplotlib 3.8.0 documentation. Available at: https://matplotlib.org/stable/plot_types/index.html
# Team, D. (2021) Cartoonify an image with opencv in python, DataFlair. Available at: https://data-flair.training/blogs/cartoonify-image-opencv-python/ 
# OpenCV image filters - javatpoint (no date) www.javatpoint.com. Available at: https://www.javatpoint.com/opencv-image-filters
# Smoothing images (no date) OpenCV. Available at: https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html 
# Coordinate reference systems in cartopy¶ (no date) Coordinate reference systems in Cartopy - cartopy 0.9.0 documentation. Available at: https://pelson.github.io/cartopy/crs/index.html 
# Cartopy.crs.CRS# (no date) cartopy.crs.CRS - cartopy 0.22.0 documentation. Available at: https://scitools.org.uk/cartopy/docs/latest/reference/generated/cartopy.crs.CRS.html
# Python repr() method (with examples) (no date) (With Examples). Available at: https://www.tutorialsteacher.com/python/repr-method 
# State design pattern (2023) GeeksforGeeks. Available at: https://www.geeksforgeeks.org/state-design-pattern/ 
# Design patterns and refactoring (no date) SourceMaking. Available at: https://sourcemaking.com/design_patterns/state 
# Design patterns tutorial (no date) Scaler Topics. Available at: https://www.scaler.com/topics/design-patterns/ 
# Pankaj (2022) State design pattern in Java, DigitalOcean. Available at: https://www.digitalocean.com/community/tutorials/state-design-pattern-java 
# Interpreter design pattern (2018) GeeksforGeeks. Available at: https://www.geeksforgeeks.org/interpreter-design-pattern/ 
# C# interpreter (no date) Dofactory. Available at: https://www.dofactory.com/net/interpreter-design-pattern 
# Rajeshvelmani (2023) Understanding language interpretation with the interpreter design pattern in Java, Medium. Available at: https://medium.com/@rajeshvelmani/understanding-language-interpretation-with-the-interpreter-design-pattern-in-java-b2a3969eaf9  
# 
# 
