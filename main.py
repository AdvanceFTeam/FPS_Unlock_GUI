import tkinter as tk
from tkinter import ttk
import os
import json
from ttkthemes import ThemedStyle

class FPSBoosterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FPS Booster GUI")

        bg_color = "#1E1E1E"
        top_bar_color = "#2A2A2A"

        self.root.configure(bg=bg_color)
        self.root.tk_setPalette(background=top_bar_color)

        roblox_version_folder = self.get_roblox_version_folder()
        self.client_settings_path = os.path.join(roblox_version_folder, "ClientSettings")

        if not os.path.exists(self.client_settings_path):
            os.makedirs(self.client_settings_path)

        self.notebook = ttk.Notebook(root)
        self.notebook.grid(row=0, column=0, columnspan=2, sticky="nsew")

        fps_booster_frame = ttk.Frame(self.notebook, style='Dark.TFrame')
        self.notebook.add(fps_booster_frame, text='FPS Booster')
        self.create_fps_booster_page(fps_booster_frame)

        new_page_frame = ttk.Frame(self.notebook, style='Dark.TFrame')
        self.notebook.add(new_page_frame, text='Credits')
        self.create_new_page(new_page_frame)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        fps_booster_frame.columnconfigure(1, weight=1)

        self.root.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        self.root.update_idletasks()

    def create_fps_booster_page(self, frame):
        self.toggle_var1 = tk.BooleanVar(value=True)
        self.toggle_var2 = tk.BooleanVar(value=True)
        self.toggle_var3 = tk.BooleanVar(value=True)
        self.toggle_var4 = tk.BooleanVar(value=True)
        self.fps_var = tk.StringVar(value="999")

        ttk.Entry(frame, textvariable=self.fps_var, style='Dark.TEntry').grid(row=0, column=1, pady=5, padx=5, sticky="ew")
        ttk.Checkbutton(frame, text="DFFlagDebugVisualizationImprovements", variable=self.toggle_var1, style='Dark.TCheckbutton').grid(row=1, column=1, pady=5, padx=5, sticky="w")
        ttk.Checkbutton(frame, text="DFFlagDebugVisualizeAllPropertyChanges", variable=self.toggle_var2, style='Dark.TCheckbutton').grid(row=2, column=1, pady=5, padx=5, sticky="w")
        ttk.Checkbutton(frame, text="DFFlagDebugVisualizerTrackRotationPredictions", variable=self.toggle_var3, style='Dark.TCheckbutton').grid(row=3, column=1, pady=5, padx=5, sticky="w")
        ttk.Checkbutton(frame, text="DFFlagDebugEnableInterpolationVisualizer", variable=self.toggle_var4, style='Dark.TCheckbutton').grid(row=4, column=1, pady=5, padx=5, sticky="w")

        ttk.Button(frame, text="Apply Changes", command=self.apply_changes, style='Dark.TButton').grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")
        ttk.Button(frame, text="Edit ClientAppSettings.json", command=self.edit_client_settings, style='Dark.TButton').grid(row=6, column=0, columnspan=2, pady=10, sticky="ew")
        ttk.Button(frame, text="Reset to Default", command=self.reset_to_default, style='Dark.TButton').grid(row=7, column=0, columnspan=2, pady=10, sticky="ew")

    def create_new_page(self, frame):
        ttk.Label(frame, text="Credits", font=("Helvetica", 16, "bold"), foreground="#FFD700").grid(row=0, column=0, pady=20, padx=10)

        credits_frame = ttk.Frame(frame, style='Light.TFrame')
        credits_frame.grid(row=1, column=0, pady=10, padx=10, sticky="w")

        ttk.Label(credits_frame, text="Credits:", font=("Arial", 12, "underline"), foreground="#00FF00").grid(row=0, column=0, pady=5, padx=5, sticky="w")
        ttk.Label(credits_frame, text="Developed by AdvanceFalling Team", font=("Arial", 10), foreground="#FFFFFF").grid(row=1, column=0, pady=5, padx=5, sticky="w")
        ttk.Label(credits_frame, text="Version 1.0", font=("Arial", 10), foreground="#FFFFFF").grid(row=2, column=0, pady=5, padx=5, sticky="w")
        ttk.Label(credits_frame, text="Date: February 14, 2024", font=("Arial", 10), foreground="#FFFFFF").grid(row=3, column=0, pady=5, padx=5, sticky="w")

        style.configure('Light.TFrame', background='#2A2A2A')



    def get_roblox_version_folder(self):
        versions_folder = r"C:\Users\ksorj\AppData\Local\Roblox\Versions"
        latest_version_folder = max(os.listdir(versions_folder), key=lambda f: os.path.getctime(os.path.join(versions_folder, f)))
        return os.path.join(versions_folder, latest_version_folder)

    def apply_changes(self):
        config = {
            "DFIntTaskSchedulerTargetFps": self.fps_var.get(),
            "DFFlagDebugVisualizationImprovements": str(self.toggle_var1.get()),
            "DFFlagDebugVisualizeAllPropertyChanges": str(self.toggle_var2.get()),
            "DFFlagDebugVisualizerTrackRotationPredictions": str(self.toggle_var3.get()),
            "DFFlagDebugEnableInterpolationVisualizer": str(self.toggle_var4.get())
        }

        settings_file_path = os.path.join(self.client_settings_path, "ClientAppSettings.json")
        with open(settings_file_path, 'w') as file:
            json.dump(config, file, indent=2)

        self.root.update_idletasks()

    def edit_client_settings(self):
        settings_file_path = os.path.join(self.client_settings_path, "ClientAppSettings.json")
        os.system(settings_file_path)

    def reset_to_default(self):
        self.fps_var.set("999")
        self.toggle_var1.set(True)
        self.toggle_var2.set(True)
        self.toggle_var3.set(True)
        self.toggle_var4.set(True)

if __name__ == "__main__":
    root = tk.Tk()

    style = ThemedStyle(root)
    style.set_theme("equilux")

    style.configure('Dark.TFrame', background='#1E1E1E')
    style.configure('Dark.TEntry', fieldbackground='#1E1E1E', foreground='#FFFFFF')
    style.configure('Dark.TCheckbutton', background='#1E1E1E', foreground='#FFFFFF')
    style.configure('Dark.TButton', background='#1E1E1E', foreground='#FFFFFF')

    app = FPSBoosterGUI(root)
    root.mainloop()
