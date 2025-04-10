from tkinter import *
from tkinter import ttk
from game import PrisonersDilemma
import configLoader
from PlayersLoader import loadPlayerClass
from Player import Player

class GUI:
    def __init__(self, root):

        self.root = root
        self.root.title("Prisoner's Dilemma")
        self.root.geometry("700x700")

        self.config = configLoader.load_config()

        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.pack(fill=BOTH, expand="10")

        self.label_title = ttk.Label(root, text="Simulation Prisonner's dilemma", font=("Arial", 16))
        self.label_title.pack()

        self.algoClasses = loadPlayerClass()

        # Choix de l'algorithme pour le joueur 1
        ttk.Label(self.main_frame, text="Joueur 1 :").grid(column=0, row=1, sticky=W)
        self.algo0val = StringVar()
        self.algo0 = ttk.Combobox(self.main_frame, textvariable=self.algo0val, state="readonly")
        self.algo0["values"] = list(self.algoClasses.keys()) #self.config["players"]
        self.algo0.grid(column=1, row=1, padx=5, pady=5)
        self.algo0.current(0)  # Sélection par défaut

        # Choix de l'algorithme pour le joueur 2
        ttk.Label(self.main_frame, text="Joueur 2 :").grid(column=2, row=1, sticky=W)
        self.algo1val = StringVar()
        self.algo1 = ttk.Combobox(self.main_frame, textvariable=self.algo1val, state="readonly")
        self.algo1["values"] = list(self.algoClasses.keys()) #self.config["players"]
        self.algo1.grid(column=3, row=1, padx=5, pady=5)
        self.algo1.current(1)

        # Add noise
        ttk.Label(self.main_frame, text="Add noise").grid(column=0, row=2, sticky=W)
        self.spinval = StringVar()
        self.spinboxnoise = ttk.Spinbox(self.main_frame, from_=1.0, to=100.0, textvariable=self.spinval)
        self.spinboxnoise.grid(column=1, row=2, padx=4, pady=3)
        self.spinval.set(10)

        #change number of round
        ttk.Label(self.main_frame, text="Number of round").grid(column=2, row=2, sticky=W)
        self.spinval1 = StringVar()
        self.spinboxround1 = ttk.Spinbox(self.main_frame, from_=1.0, to=1000.0, textvariable=self.spinval1)
        self.spinboxround1.grid(column=3, row=2, padx=4, pady=3)
        self.spinval1.set(200)

        self.start_button = ttk.Button(self.main_frame, text="Lancer la simulation", command=self.start_simulation)
        self.start_button.grid(column=0, row=4, columnspan=2, pady=10)

        # Zone d'affichage des résultats
        self.result_label = ttk.Label(self.main_frame, text="Resultat", font=("Arial", 12))
        self.result_label.grid(column=0, row=5, columnspan=2, pady=10)
        self.result_label2 = ttk.Label(self.main_frame, text="", font=("Arial", 12))
        self.result_label2.grid(column=0, row=7, columnspan=2, pady=10)
        self.state = ttk.Label(self.main_frame, text="Both cooperated")
        self.state.grid(column=0, row=9)
        self.state2 = ttk.Label(self.main_frame, text="One cooperated")
        self.state2.grid(column=0, row=10)
        self.state3 = ttk.Label(self.main_frame, text="One cooperated")
        self.state3.grid(column=0, row=11)
        self.state4 = ttk.Label(self.main_frame, text="None cooperated")
        self.state4.grid(column=0, row=12)
        self.displayState = ttk.Label(self.main_frame, text="", font=("Arial", 12))
        self.displayState.grid(column=1, row=9, columnspan=2, pady=10)
        self.displayState1 = ttk.Label(self.main_frame, text="", font=("Arial", 12))
        self.displayState1.grid(column=1, row=10, columnspan=2, pady=10)
        self.displayState2 = ttk.Label(self.main_frame, text="", font=("Arial", 12))
        self.displayState2.grid(column=1, row=11, columnspan=2, pady=10)
        self.displayState3 = ttk.Label(self.main_frame, text="", font=("Arial", 12))
        self.displayState3.grid(column=1, row=12, columnspan=2, pady=10)

    def start_simulation(self):
        algo1name = self.algo0val.get()
        algo1= self.algoClasses[algo1name]()
        algo2name = self.algo1val.get()
        algo2 = self.algoClasses[algo2name]()
        proba = int(self.spinboxnoise.get())
        nbround = int(self.spinboxround1.get())

        self.result_label.config(text=f"Simulation entre {algo1name} et {algo2name}")
        self.state2.config(text=f"{algo1name} cooperated")
        self.state3.config(text=f"{algo2name} cooperated")
        self.game = PrisonersDilemma(algo1, algo2, nbround, proba)
        self.game.launch()
        self.result_label2.config(text=(self.game.player0.printPoint() + " "+ self.game.player1.printPoint()))
        self.displayState.config(text= f"{self.game.gameState[0]}")
        self.displayState1.config(text= f"{self.game.gameState[1]}")
        self.displayState2.config(text= f"{self.game.gameState[2]}")
        self.displayState3.config(text= f"{self.game.gameState[3]}")

root = Tk()
app = GUI(root)

root.mainloop()