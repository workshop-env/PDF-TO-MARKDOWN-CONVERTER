import customtkinter as ctk
from tkinter import filedialog
from pathlib import Path
from engine import convert_pdf_to_md

class PDFConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PDF → Markdown Pro")
        self.geometry("520x400") # Increased height slightly for the progress bar
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Center Frame (The "Card")
        self.card = ctk.CTkFrame(self, corner_radius=20)
        self.card.pack(pady=30, padx=30, fill="both", expand=True)

        # UI Elements
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

        # --- Progress Bar Addition ---
        self.progress_bar = ctk.CTkProgressBar(self.card, orientation="horizontal", width=300)
        self.progress_bar.set(0) # Start at 0%
        self.progress_bar.pack(pady=(20, 0))
        # -----------------------------

        self.status_label = ctk.CTkLabel(self.card, text="Status: Ready", font=("Segoe UI", 12))
        self.status_label.pack(pady=(10, 10))

    def process_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            # UI Feedback: Start
            self.status_label.configure(text="⚙️ Processing... Please wait", text_color="#FFCC00")
            self.select_btn.configure(state="disabled")
            
            # Start progress bar animation
            self.progress_bar.set(0)
            self.progress_bar.configure(mode="indeterminate")
            self.progress_bar.start()
            
            self.update_idletasks()
            
            # Use the engine
            result = convert_pdf_to_md(file_path, Path(file_path).parent)
            
            # Stop progress bar and set to full
            self.progress_bar.stop()
            self.progress_bar.configure(mode="determinate")
            
            self.select_btn.configure(state="normal")
            
            if "Success" in result:
                self.progress_bar.set(1) # Fill the bar
                self.status_label.configure(text="✅ Success! Check your folder", text_color="#2ECC71")
            else:
                self.progress_bar.set(0) # Empty the bar on error
                self.status_label.configure(text=f"❌ Error", text_color="#E74C3C")

if __name__ == "__main__":
    app = PDFConverterApp()
    app.mainloop()
