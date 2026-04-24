import customtkinter as ctk
from tkinter import filedialog
from pathlib import Path
from engine import convert_pdf_to_md

class PDFConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PDF → Markdown Pro")
        self.geometry("520x350")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue") # Or "green"

        # Center Frame (The "Card")
        self.card = ctk.CTkFrame(self, corner_radius=20)
        self.card.pack(pady=30, padx=30, fill="both", expand=True)

        # UI Elements inside the card
        self.label = ctk.CTkLabel(self.card, text="PDF to Markdown", font=("Segoe UI", 24, "bold"))
        self.label.pack(pady=(30, 5))

        self.sub_label = ctk.CTkLabel(self.card, text="Optimized for AI & LLM training", font=("Segoe UI", 12), text_color="gray")
        self.sub_label.pack(pady=(0, 20))

        self.select_btn = ctk.CTkButton(
            self.card, 
            text="Choose PDF File", 
            command=self.process_file,
            font=("Segoe UI", 14, "bold"),
            height=45,
            corner_radius=10
        )
        self.select_btn.pack(pady=10)

        self.status_label = ctk.CTkLabel(self.card, text="Status: Ready", font=("Segoe UI", 12))
        self.status_label.pack(pady=(20, 10))

    def process_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.status_label.configure(text="⚙️ Processing... Please wait", text_color="#FFCC00")
            self.select_btn.configure(state="disabled") # Prevent double-clicking
            self.update_idletasks()
            
            # Use the engine
            result = convert_pdf_to_md(file_path, Path(file_path).parent)
            
            self.select_btn.configure(state="normal")
            
            if "Success" in result:
                self.status_label.configure(text="✅ Success! Check your Downloads folder", text_color="#2ECC71")
            else:
                self.status_label.configure(text=f"❌ {result}", text_color="#E74C3C")

if __name__ == "__main__":
    app = PDFConverterApp()
    app.mainloop()
