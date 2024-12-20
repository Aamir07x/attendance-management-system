import tkinter as tk
from tkinter import messagebox, filedialog
import os
from utils.face_recognition import detect_face, mark_attendance
from utils.db_operations import initialize_db, fetch_attendance

DB_PATH = 'database/attendance.db'

class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI-Based Attendance System")
        self.root.geometry("800x600")

        # Title
        title = tk.Label(self.root, text="Attendance Management System", font=("Helvetica", 20, "bold"))
        title.pack(pady=20)

        # Upload Button
        upload_btn = tk.Button(self.root, text="Upload Image", command=self.upload_image, font=("Helvetica", 14))
        upload_btn.pack(pady=20)

        # Attendance Log Button
        log_btn = tk.Button(self.root, text="View Attendance Logs", command=self.view_logs, font=("Helvetica", 14))
        log_btn.pack(pady=20)

        # Display Area
        self.display_frame = tk.Frame(self.root)
        self.display_frame.pack(pady=20, fill="both", expand=True)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
        if file_path:
            name = detect_face(file_path)
            if name:
                mark_attendance(DB_PATH, name)
                messagebox.showinfo("Success", f"Attendance marked for {name}")
            else:
                messagebox.showerror("Error", "Face not recognized!")

    def view_logs(self):
        logs = fetch_attendance(DB_PATH)
        self.display_frame.destroy()
        self.display_frame = tk.Frame(self.root)
        self.display_frame.pack(pady=20, fill="both", expand=True)

        if logs:
            for i, (name, timestamp) in enumerate(logs, start=1):
                record = f"{i}. {name} - {timestamp}"
                tk.Label(self.display_frame, text=record, font=("Helvetica", 12)).pack(anchor="w")
        else:
            tk.Label(self.display_frame, text="No attendance records found.", font=("Helvetica", 12)).pack(anchor="w")


if __name__ == "__main__":
    initialize_db(DB_PATH)
    root = tk.Tk()
    app = AttendanceApp(root)
    root.mainloop()
