from tkinter import *
from tkinter import ttk
from game import PrisonersDilemma
import configLoader
from PlayersLoader import loadPlayerClass

class GUI:
    def __init__(self, root):

        self.root = root
        self.root.title("Prisoner's Dilemma")
        self.root.geometry("400x300")

        self.config = configLoader.load_config()

        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.pack(fill=BOTH, expand="10")

        self.label_title = ttk.Label(root, text="Simulation du Dilemme du Prisonnier", font=("Arial", 16))
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
        ttk.Label(self.main_frame, text="Joueur 2 :").grid(column=0, row=2, sticky=W)
        self.algo1val = StringVar()
        self.algo1 = ttk.Combobox(self.main_frame, textvariable=self.algo1val, state="readonly")
        self.algo1["values"] = list(self.algoClasses.keys()) #self.config["players"]
        self.algo1.grid(column=1, row=2, padx=5, pady=5)
        self.algo1.current(1)

        # Add noise
        ttk.Label(self.main_frame, text="Add noise").grid(column=0, row=3, sticky=W)
        self.spinval = StringVar()
        self.spinboxnoise = ttk.Spinbox(self.main_frame, from_=1.0, to=100.0, textvariable=self.spinval)
        self.spinboxnoise.grid(column=1, row=3, padx=4, pady=3)

        self.start_button = ttk.Button(self.main_frame, text="Lancer la simulation", command=self.start_simulation)
        self.start_button.grid(column=0, row=4, columnspan=2, pady=10)

        # Zone d'affichage des résultats
        self.result_label = ttk.Label(self.main_frame, text="", font=("Arial", 12))
        self.result_label.grid(column=0, row=4, columnspan=2, pady=10)
        self.result_label2 = ttk.Label(self.main_frame, text="", font=("Arial", 12))
        self.result_label2.grid(column=0, row=5, columnspan=2, pady=10)

    def start_simulation(self):
        algo1name = self.algo0val.get()
        algo1 = self.algoClasses[algo1name]
        algo2name = self.algo1val.get()
        algo2 = self.algoClasses[algo2name]
        proba = self.spinboxnoise.get()
        

        self.result_label.config(text=f"Simulation entre {algo1name} et {algo2name}")
        self.game = PrisonersDilemma(algo1, algo2, self.config["nb_rounds"], proba)
        self.game.launch()
        self.result_label2.config(text=(self.game.player0.printPoint() + " "+ self.game.player1.printPoint()))

root = Tk()
app = GUI(root)

root.mainloop()