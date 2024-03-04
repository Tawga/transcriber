from customtkinter import *
from customtkinter import filedialog
from transcriber import Transcriber
import threading



class Ui:
    def __init__(self, transcriber) -> None:
        
        self.audio_file_path:str = ""
        self.transcriber:Transcriber = transcriber
        
        self.root = CTk()
        self.root.title("Transcriber")
        self.root.configure(padx=20, pady=20)
        
        #SELECT FRAME
        self.select_frame = CTkFrame(self.root)
        self.select_frame.pack(expand=True, fill="x", padx= 10, pady=10)
        
        self.select_file_button = CTkButton(self.select_frame, text="Select file", command=self.get_filepath)
        self.select_file_button.grid(row=0, column=0, padx=10, pady=10)
        
        self.filepath_label = CTkLabel(self.select_frame, text="")
        self.filepath_label.grid(row=0, column=1, padx=10, pady=10)
        
        #Settings FRAME
        settings_frame = CTkFrame(self.root)
        settings_frame.pack(expand=True, fill="both", padx= 10, pady=10)
        
        select_model_label= CTkLabel(settings_frame, text="Select model:")
        select_model_label.grid(row=0, column=0, padx= 10, pady=10)
        
        self.model_dropdown = CTkComboBox(settings_frame, values=["tiny", "base", "small", "medium", "large"], width=400)
        self.model_dropdown.set("base")
        self.model_dropdown.grid(row=0, column=1, padx= 10, pady=10)
        
        self.translate_cb = CTkCheckBox(settings_frame, text="Translate to English", onvalue=True, offvalue=False)
        self.translate_cb.grid(row=1, column=0, padx=10, pady=10)
        
        self.trans_button = CTkButton(self.root, text="Transcribe audio", command=self.transcribe_callback)
        self.trans_button.pack(expand=True, fill="x", padx=10, pady=10)
        
        self.srt_button = CTkButton(self.root, text="Save as SRT", command=self.save_srt, state="disabled")
        self.srt_button.pack(expand=True, fill="x", padx=10, pady=10)
        
        #Translation frame
        self.translation_frame = CTkFrame(self.root)
        self.translation_label = CTkLabel(self.translation_frame, text="", wraplength=600)
        self.translation_label.pack(padx=10, pady=10)
        
        self.root.mainloop()
    
    def get_filepath(self):
        self.audio_file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav; *.mp3")])
        self.filepath_label.configure(text=self.audio_file_path)
    
    def save_srt(self):
        self.transcriber.save_srt()
    
    def transcribe_finished(self, result):
        self.trans_button.configure(state="normal", text="Transcribe audio")
        self.srt_button.configure(state="normal")
        self.translation_frame.pack(expand=True, fill="both", padx= 10, pady=10)
        self.translation_label.configure(text=result["text"])
        
    def transcribe_callback(self):
        if self.audio_file_path == "":
            self.filepath_label.configure(text='No file selected')
        else: 
            def transcribe_audio_async(model, audio_file, translate, callback):
                t = threading.Thread(target=self.transcriber.transcribe, args=(model, audio_file, translate, callback))
                t.start()
            self.trans_button.configure(state="disabled", text="Transcribing...")
            self.srt_button.configure(state="disabled")
            transcribe_audio_async(self.model_dropdown.get(), self.audio_file_path, self.translate_cb.get(), self.transcribe_finished) 
            


            