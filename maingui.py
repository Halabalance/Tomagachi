#  _____                                                    _____
# ( ___ )                                                  ( ___ )
#  |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   |
#  |   |    ░█░█░█▀█░█░░░█▀█░█▀▄░█▀█░█░░░█▀█░█▀█░█▀▀░█▀▀    |   |
#  |   |    ░█▀█░█▀█░█░░░█▀█░█▀▄░█▀█░█░░░█▀█░█░█░█░░░█▀▀    |   |
#  |   |    ░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀░░▀░▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀▀    |   |
#  |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___|
# (_____)                                                  (_____)

from behaviour import UserTomogachi
import pickle
import atexit
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import threading
import time
import io
import sys

class TamagotchiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tamagotchi Game")
        self.root.geometry("600x1000")
        self.root.configure(bg="#2C3E50")
        self.data = self.load_game()
        self.running = True
        self.create_widgets()
        self.update_thread = threading.Thread(target=self.background_update, daemon=True)
        self.cooldown = False
        self.COOLDOWN_TIME = 300
        self.last_recorded_cooldown = time.time()
        self.update_thread.start()
        self.update_display()
        atexit.register(self.save_on_exit)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def load_game(self):
        try:
            with open("save.dat", "rb") as f:
                data = pickle.load(f)
                print("Game loaded successfully!")
                return data
        except FileNotFoundError:
            name = simpledialog.askstring("New Tamagotchi",
                                          "Enter your Tamagotchi's name:",
                                          parent=self.root)
            if not name:
                name = "Tomo"
            return UserTomogachi(name)

    def create_widgets(self):
        title_frame = tk.Frame(self.root, bg="#34495E", pady=20)
        title_frame.pack(fill=tk.X)

        title = tk.Label(title_frame, text="TAMAGOTCHI",
                         font=("Arial", 24, "bold"),
                         bg="#34495E", fg="#ECF0F1")
        title.pack()

        info_frame = tk.Frame(self.root, bg="#2C3E50", pady=10)
        info_frame.pack(fill=tk.X, padx=20)

        self.name_label = tk.Label(info_frame, text="",
                                   font=("Arial", 18, "bold"),
                                   bg="#2C3E50", fg="#ECF0F1")
        self.name_label.pack()

        self.stage_label = tk.Label(info_frame, text="",
                                    font=("Arial", 14),
                                    bg="#2C3E50", fg="#BDC3C7")
        self.stage_label.pack()

        self.age_label = tk.Label(info_frame, text="",
                                  font=("Arial", 12),
                                  bg="#2C3E50", fg="#BDC3C7")
        self.age_label.pack()

        display_frame = tk.Frame(self.root, bg="#34495E",
                                 relief=tk.RIDGE, borderwidth=3,
                                 width=400, height=200)
        display_frame.pack(pady=20, padx=20)
        display_frame.pack_propagate(False)

        self.pet_display = tk.Label(display_frame, text="🐣",
                                    font=("Arial", 80),
                                    bg="#34495E", fg="#ECF0F1")
        self.pet_display.pack(expand=True)

        self.speech_label = tk.Label(self.root, text="",
                                     font=("Arial", 11, "italic"),
                                     bg="#2C3E50", fg="#F39C12",
                                     wraplength=500)
        self.speech_label.pack(pady=10)

        stats_frame = tk.Frame(self.root, bg="#2C3E50", pady=10)
        stats_frame.pack(fill=tk.X, padx=40)

        hunger_frame = tk.Frame(stats_frame, bg="#2C3E50")
        hunger_frame.pack(fill=tk.X, pady=5)

        tk.Label(hunger_frame, text="Hunger:",
                 font=("Arial", 11, "bold"),
                 bg="#2C3E50", fg="#ECF0F1", width=12, anchor='w').pack(side=tk.LEFT)

        self.hunger_bar = ttk.Progressbar(hunger_frame, length=300,
                                          mode='determinate')
        self.hunger_bar.pack(side=tk.LEFT, padx=10)

        self.hunger_value = tk.Label(hunger_frame, text="100",
                                     font=("Arial", 11),
                                     bg="#2C3E50", fg="#ECF0F1", width=5)
        self.hunger_value.pack(side=tk.LEFT)

        happiness_frame = tk.Frame(stats_frame, bg="#2C3E50")
        happiness_frame.pack(fill=tk.X, pady=5)

        tk.Label(happiness_frame, text="Happiness:",
                 font=("Arial", 11, "bold"),
                 bg="#2C3E50", fg="#ECF0F1", width=12, anchor='w').pack(side=tk.LEFT)

        self.happiness_bar = ttk.Progressbar(happiness_frame, length=300,
                                             mode='determinate')
        self.happiness_bar.pack(side=tk.LEFT, padx=10)

        self.happiness_value = tk.Label(happiness_frame, text="100",
                                        font=("Arial", 11),
                                        bg="#2C3E50", fg="#ECF0F1", width=5)
        self.happiness_value.pack(side=tk.LEFT)

        # Energy
        energy_frame = tk.Frame(stats_frame, bg="#2C3E50")
        energy_frame.pack(fill=tk.X, pady=5)

        tk.Label(energy_frame, text="Energy:",
                 font=("Arial", 11, "bold"),
                 bg="#2C3E50", fg="#ECF0F1", width=12, anchor='w').pack(side=tk.LEFT)

        self.energy_bar = ttk.Progressbar(energy_frame, length=300,
                                          mode='determinate')
        self.energy_bar.pack(side=tk.LEFT, padx=10)

        self.energy_value = tk.Label(energy_frame, text="100",
                                     font=("Arial", 11),
                                     bg="#2C3E50", fg="#ECF0F1", width=5)
        self.energy_value.pack(side=tk.LEFT)

        # Action buttons frame
        buttons_frame = tk.Frame(self.root, bg="#2C3E50", pady=20)
        buttons_frame.pack()

        # Button style
        button_config = {
            'font': ("Arial", 12, "bold"),
            'width': 10,
            'height': 2,
            'relief': tk.RAISED,
            'borderwidth': 3
        }

        btn_feed = tk.Button(buttons_frame, text="Feed",
                             bg="#27AE60", fg="white",
                             command=self.feed_pet, **button_config)
        btn_feed.grid(row=0, column=0, padx=10, pady=5)

        btn_play = tk.Button(buttons_frame, text="Play",
                             bg="#3498DB", fg="white",
                             command=self.play_with_pet, **button_config)
        btn_play.grid(row=0, column=1, padx=10, pady=5)

        btn_sleep = tk.Button(buttons_frame, text="Sleep",
                              bg="#9B59B6", fg="white",
                              command=self.put_to_sleep, **button_config)
        btn_sleep.grid(row=1, column=0, padx=10, pady=5)

        btn_talk = tk.Button(buttons_frame, text="Talk",
                             bg="#E67E22", fg="white",
                             command=self.talk_to_pet, **button_config)
        btn_talk.grid(row=1, column=1, padx=10, pady=5)

        # Status label
        self.status_label = tk.Label(self.root, text="",
                                     font=("Arial", 10),
                                     bg="#2C3E50", fg="#95A5A6")
        self.status_label.pack(pady=10)

    def get_pet_emoji(self):
        stage = self.data.user_pet
        emoji_map = {
            "Baby": "🐣",
            "Child": "🐤",
            "Teen": "🐔",
            "Adult": "🦅"
        }
        return emoji_map.get(stage, "🐣")

    def update_display(self):
        if not self.running:
            return

        pet = self.data.user_pet

        self.name_label.config(text=pet.name)
        self.stage_label.config(text=f"Stage: {str(pet)}")
        self.age_label.config(text=f"Age: {pet.age} days")

        self.pet_display.config(text=self.get_pet_emoji())

        self.hunger_bar['value'] = pet.hunger
        self.hunger_value.config(text=str(int(pet.hunger)))

        self.happiness_bar['value'] = pet.happiness
        self.happiness_value.config(text=str(int(pet.happiness)))

        self.energy_bar['value'] = pet.energy
        self.energy_value.config(text=str(int(pet.energy)))

        if not pet.alive:
            self.pet_display.config(text="💀")
            self.status_label.config(text="Your Tamagotchi has passed away... 😢",
                                     fg="#E74C3C")
            messagebox.showinfo("Game Over",
                                f"{pet.name} has passed away at age of {pet.age}.\n\n"
                                "Take better care next time!")
            return

        status = self.get_status_message()
        self.status_label.config(text=status)

        self.root.after(500, self.update_display)

    def get_status_message(self):
        pet = self.data.user_pet

        if pet.hunger < 30:
            return "Your pet is very hungry!"
        elif pet.happiness < 30:
            return "Your pet is very sad!"
        elif pet.energy < 30:
            return "Your pet is exhausted!"
        elif pet.hunger < 50 or pet.happiness < 50 or pet.energy < 50:
            return "Your pet needs attention soon"
        else:
            return f"{pet.name} is doing great!"

    def feed_pet(self):
        if not self.data.user_pet.alive:
            return
        if self.cooldown:
            self.speech_label.config(text=f"Cannot feed: in cooldown")
            return
        self.data.user_pet.set_hunger(self.data.user_pet.hunger + 20)
        self.speech_label.config(text=f"fed {self.data.user_pet.name}")
        self.cooldown = True
        self.root.after(3000, lambda: self.speech_label.config(text=""))

    def play_with_pet(self):
        if not self.data.user_pet.alive:
            return

        if self.cooldown:
            self.speech_label.config(text=f"Cannot play: in cooldown")
            return

        self.data.user_pet.set_happiness(self.data.user_pet.happiness + 20)
        self.data.user_pet.set_energy(self.data.user_pet.energy -  self.data.user_pet.ENERGY_RATE) #playing is tiring!
        self.speech_label.config(text=f"played with {self.data.user_pet.name}")
        self.root.after(3000, lambda: self.speech_label.config(text=""))

    def put_to_sleep(self):
        if not self.data.user_pet.alive:
            return

        if self.cooldown:
            self.speech_label.config(text=f"Cannot sleep: in cooldown")
            return

        hours = simpledialog.askinteger("Sleep Time",
                                        "How many hours? (1-9):",
                                        minvalue=1, maxvalue=9,
                                        parent=self.root)
        if hours:
            try:
                self.data.user_pet.set_energy(self.data.user_pet.energy + 10 * hours )
                self.speech_label.config(text=f"Zzzzz... sleeping for {hours} hours 💤")
                self.root.after(3000, lambda: self.speech_label.config(text=""))
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def talk_to_pet(self):
        if not self.data.user_pet.alive:
            return

        # Capture the print output
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()

        self.data.user_pet.speak()

        output = buffer.getvalue()
        sys.stdout = old_stdout

        self.speech_label.config(text=output.strip())
        self.root.after(4000, lambda: self.speech_label.config(text=""))

    def background_update(self):
        while self.running:
            if self.data.user_pet.alive:
                self.data.entropify()
                self.data.age()
                if time.time() - self.last_recorded_cooldown > self.COOLDOWN_TIME:
                    self.cooldown = False
            time.sleep(0.5)

    def save_on_exit(self):
        print("\nSaving progress... Don't turn off your computer!")
        with open("save.dat", "wb") as f:
            pickle.dump(self.data, f)
        print("Save complete. Goodbye!")

    def on_closing(self):
        self.running = False
        self.save_on_exit()
        self.root.destroy()


def main():
    root = tk.Tk()
    app = TamagotchiGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()