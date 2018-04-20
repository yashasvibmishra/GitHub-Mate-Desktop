''' +-------------------------+
    | Authored by James George|  
    +-------------------------+ 
'''

from tkinter import *

class github_mate:

	  # Constructor which gets invoked automatically when the github_mate class is instantiated.	

	  def __init__(self, master):

	  	# Configuring the window 

	  	master.title("GitHub-Mate")

	  	master.geometry("500x500")

	  	master.resizable(False, False)

	  	# Setting up the UI widgets.

	  	self.caption = Label(text = "GitHub-Mate", font="algerian 30 bold underline", fg = "blue").grid(row = 0, column = 0, columnspan = 2)

	  	self.blank_label_one = Label(text = "").grid(row = 1, column = 0)

	  	self.username_label = Label(text = "Username:", font = "courier 20 bold").grid(row = 2, column = 0)

	  	self.username_field = Entry(font = "cursive 16 bold", bd = 6, relief = "groove").grid(row = 2, column = 1)
	  	
	  	self.blank_label_two = Label(text = "").grid(row = 3, column = 0)

	  	self.repositories_label = Label(text = "Repositories:", font = "courier 20 bold").grid(row = 4, column = 0)

	  	self.repositories_field = Entry(font = "cursive 16 bold", bd = 6, relief = "groove").grid(row = 4, column = 1)
	  	
	  	self.blank_label_three = Label(text = "").grid(row = 5, column = 0)

	  	self.followers_label = Label(text = "Followers:", font = "courier 20 bold").grid(row = 6, column = 0)

	  	self.followers_field = Entry(font = "cursive 16 bold", bd = 6, relief = "groove").grid(row = 6, column = 1)
	  	
	  	self.blank_label_four = Label(text = "").grid(row = 7, column = 0)

	  	self.following_label = Label(text = "Following:", font = "courier 20 bold").grid(row = 8, column = 0)

	  	self.following_field = Entry(font = "cursive 16 bold", bd = 6, relief = "groove").grid(row = 8, column = 1)

	  	self.blank_label_five = Label(text = "").grid(row = 9, column = 0)

	  	self.gists_label = Label(text = "Gists:", font = "courier 20 bold").grid(row = 10, column = 0)

	  	self.gists_field = Entry(font = "cursive 16 bold", bd = 6, relief = "groove").grid(row = 10, column = 1)
	  	
	  	self.blank_label_six = Label(text = "").grid(row = 10, column = 0)

	  	self.blank_label_seven = Label(text = "").grid(row = 11, column = 0)

	  	self.btn = Button(text = "Get", font="times 22 bold", fg = "red", bd = 2, relief = "raised").grid(row = 12, column = 0, columnspan = 2)
	  	

if __name__ == '__main__':

    root = Tk()
    app = github_mate(root)	  	