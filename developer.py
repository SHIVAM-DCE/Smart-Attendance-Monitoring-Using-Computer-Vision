"""
Developer Info Dashboard
Face Recognition System | Final Year Project
"""

import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

DARK_BG = '#0D1117'
PANEL_BG = '#161B22'
CARD_BG = '#1A2230'
ACCENT = '#2563EB'
ACCENT2 = '#10B981'
TEXT_PRI = '#F0F6FC'
TEXT_SEC = '#8B949E'
BORDER = '#30363D'

DEVELOPERS = [
    {
        'name': 'Shivam Kumar',
        'initials': 'SK',
        'role': 'Lead Developer',
        'desc': 'Responsible for the core ML pipeline, face detection algorithm, and overall system architecture.',
        'skills': ['Python', 'OpenCV', 'ML', 'System Design'],
        'color': '#2563EB'
    },
    {
        'name': 'Abhishek Kumar',
        'initials': 'AK',
        'role': 'Backend Developer',
        'desc': 'Handles database design, student record management, attendance logic, and system integration.',
        'skills': ['MySQL', 'FastAPI', 'Security', 'Docker'],
        'color': '#10B981'
    },
    {
        'name': 'Aatish Raj',
        'initials': 'AR',
        'role': 'UI/UX Developer',
        'desc': 'Designed the full interface, user experience flows, and helped ensure polished usability.',
        'skills': ['Tkinter', 'CustomTkinter', 'Figma', 'Testing'],
        'color': '#F59E0B'
    },
]

TECHS = [
    ('Python 3', '#2563EB'),
    ('OpenCV', '#10B981'),
    ('MySQL', '#F59E0B'),
    ('Tkinter', '#8B5CF6'),
    ('Pillow', '#EC4899'),
    ('CustomTkinter', '#F472B6')
]

QUOTE = 'Great things in technology are never done by one person - they are done by a team.'


class DeveloperCard(ctk.CTkFrame):
    def __init__(self, parent, dev, index):
        super().__init__(parent, fg_color=CARD_BG, corner_radius=20, border_width=1, border_color=BORDER)
        self.dev = dev
        self.index = index
        self.build_card()

    def build_card(self):
        accent = self.dev['color']
        top_bar = ctk.CTkFrame(self, fg_color=accent, height=8, corner_radius=4)
        top_bar.pack(fill='x', side='top')

        body = ctk.CTkFrame(self, fg_color=CARD_BG, corner_radius=0)
        body.pack(fill='both', expand=True, padx=16, pady=16)

        avatar = ctk.CTkLabel(body, text=self.dev['initials'], width=90, height=90,
                              fg_color=accent, text_color='white', corner_radius=45,
                              font=('Helvetica', 24, 'bold'))
        avatar.pack(pady=(0, 14))

        ctk.CTkLabel(body, text=self.dev['name'], text_color=TEXT_PRI,
                     font=('Helvetica', 17, 'bold')).pack(pady=(0, 6))

        ctk.CTkLabel(body, text=self.dev['role'], fg_color=accent,
                     text_color='white', corner_radius=12,
                     font=('Helvetica', 11, 'bold'), width=210).pack(pady=(0, 14))

        ctk.CTkLabel(body, text=self.dev['desc'], text_color=TEXT_SEC,
                     font=('Helvetica', 11), wraplength=260, justify='center').pack(pady=(0, 18))

        skills_frame = ctk.CTkFrame(body, fg_color='#101624', corner_radius=16)
        skills_frame.pack(fill='x', pady=(0, 18))
        skills_frame.grid_columnconfigure((0, 1, 2), weight=1)
        for idx, skill in enumerate(self.dev['skills']):
            badge = ctk.CTkLabel(skills_frame, text=skill, fg_color='#19242F',
                                 text_color=TEXT_SEC, font=('Helvetica', 10, 'bold'), corner_radius=10)
            badge.grid(row=idx//3, column=idx%3, padx=4, pady=8, sticky='ew')

        ctk.CTkButton(body, text='View Profile', fg_color=accent,
                      hover_color='#1D4ED8', text_color='white', corner_radius=14,
                      command=self.show_details).pack(fill='x')

    def show_details(self):
        messagebox.showinfo(self.dev['name'],
                            f"{self.dev['role']}\n\n{self.dev['desc']}\n\nSkills: {', '.join(self.dev['skills'])}")


class DeveloperDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Face Recognition System - Developer Info')
        self.geometry('1260x780')
        self.minsize(1080, 700)
        self.configure(fg_color=DARK_BG)
        self.build_ui()

    def build_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        header = ctk.CTkFrame(self, fg_color='#090B10', height=70)
        header.grid(row=0, column=0, sticky='nsew')
        header.grid_propagate(False)

        ctk.CTkLabel(header, text='FACE RECOGNITION SYSTEM', text_color=ACCENT,
                     font=('Helvetica', 18, 'bold')).place(relx=0.03, rely=0.5, anchor='w')
        ctk.CTkLabel(header, text='SYSTEM ONLINE', text_color=ACCENT2,
                     font=('Helvetica', 11, 'bold')).place(relx=0.97, rely=0.5, anchor='e')

        main = ctk.CTkFrame(self, fg_color=DARK_BG)
        main.grid(row=1, column=0, sticky='nsew', padx=18, pady=18)
        main.grid_columnconfigure(0, weight=1)
        main.grid_columnconfigure(1, weight=1)
        main.grid_rowconfigure(0, weight=1)
        main.grid_rowconfigure(1, weight=1)

        summary = ctk.CTkFrame(main, fg_color=PANEL_BG, corner_radius=22,
                                border_width=1, border_color=BORDER)
        summary.grid(row=0, column=0, sticky='nsew', padx=(0, 12), pady=0)
        summary.grid_columnconfigure(0, weight=1)

        cards = ctk.CTkFrame(main, fg_color=PANEL_BG, corner_radius=22,
                              border_width=1, border_color=BORDER)
        cards.grid(row=0, column=1, sticky='nsew', padx=(12, 0), pady=0)
        cards.grid_columnconfigure((0, 1, 2), weight=1)
        cards.grid_rowconfigure((0, 1), weight=1)

        self.summary = summary
        self.cards = cards
        self.main = main
        self.card_frames = []

        section_title = ctk.CTkLabel(summary, text='Project Overview', text_color=TEXT_PRI,
                                     font=('Helvetica', 22, 'bold'))
        section_title.grid(row=0, column=0, sticky='w', padx=24, pady=(24, 8))

        section_subtitle = ctk.CTkLabel(summary, text='Final year attendance solution built with face recognition.',
                                        text_color=TEXT_SEC, font=('Helvetica', 12))
        section_subtitle.grid(row=1, column=0, sticky='w', padx=24)

        summary_text = (
            'A smart attendance system using webcam-based face recognition. '
            'It captures student attendance with OpenCV, verifies identities, '
            'and stores records securely in MySQL. '
            'This dashboard highlights the team, their roles, and the core technologies.'
        )
        tk.Label(summary, text=summary_text, justify='left', bg=PANEL_BG,
                 fg=TEXT_SEC, font=('Helvetica', 11), wraplength=400).grid(row=2, column=0, sticky='w', padx=24, pady=(10, 0))

        quote_label = ctk.CTkLabel(summary, text='Team Quote', text_color=TEXT_PRI,
                                   font=('Helvetica', 18, 'bold'))
        quote_label.grid(row=3, column=0, sticky='w', padx=24, pady=(24, 8))

        tk.Label(summary, text='"' + QUOTE + '"', justify='left', bg=PANEL_BG,
                 fg=ACCENT2, font=('Helvetica', 12, 'italic'), wraplength=400).grid(row=4, column=0, sticky='w', padx=24)

        tech_frame = ctk.CTkFrame(summary, fg_color=DARK_BG, corner_radius=16)
        tech_frame.grid(row=5, column=0, sticky='ew', padx=24, pady=(24, 24))
        tech_frame.grid_columnconfigure((0, 1), weight=1)

        title_badges = ctk.CTkLabel(tech_frame, text='Key Technologies', text_color=TEXT_PRI,
                                     font=('Helvetica', 14, 'bold'))
        title_badges.grid(row=0, column=0, columnspan=2, sticky='w', padx=18, pady=(16, 10))

        for idx, (tech, color) in enumerate(TECHS):
            badge = ctk.CTkLabel(tech_frame, text=tech, fg_color=color,
                                  text_color='white', font=('Helvetica', 11, 'bold'), corner_radius=12)
            badge.grid(row=1 + idx // 2, column=idx % 2, sticky='ew', padx=14, pady=8)

        for idx, dev in enumerate(DEVELOPERS):
            card = DeveloperCard(cards, dev, idx)
            card.grid(row=0, column=idx, padx=10, pady=24, sticky='nsew')
            cards.grid_columnconfigure(idx, weight=1)
            self.card_frames.append(card)

        self.bind('<Configure>', self.on_resize)
        self.after(100, self.adjust_layout)

        footer = ctk.CTkFrame(self, fg_color='#090B10', height=44)
        footer.grid(row=2, column=0, sticky='nsew')
        footer.grid_propagate(False)
        ctk.CTkLabel(footer, text='Face Recognition System - Final Year Project 2025-26 - Developed by Shivam Kumar, Abhishek Kumar & Aatish Raj',
                     text_color=TEXT_SEC, font=('Helvetica', 10)).place(relx=0.5, rely=0.5, anchor='center')

    def on_resize(self, event):
        if event.widget == self:
            self.adjust_layout()

    def adjust_layout(self):
        width = self.winfo_width()
        if width <= 0:
            return

        if width < 1080:
            self.main.grid_rowconfigure(0, weight=0)
            self.main.grid_rowconfigure(1, weight=1)
            self.summary.grid(row=0, column=0, sticky='nsew', padx=(0, 0), pady=(0, 12))
            self.cards.grid(row=1, column=0, sticky='nsew', padx=(0, 0), pady=(0, 0))
        else:
            self.main.grid_rowconfigure(0, weight=1)
            self.main.grid_rowconfigure(1, weight=0)
            self.summary.grid(row=0, column=0, sticky='nsew', padx=(0, 12), pady=0)
            self.cards.grid(row=0, column=1, sticky='nsew', padx=(12, 0), pady=0)

        if width < 900:
            cols = 1
        elif width < 1240:
            cols = 2
        else:
            cols = 3

        for col in range(3):
            self.cards.grid_columnconfigure(col, weight=1 if col < cols else 0)

        for idx, card in enumerate(self.card_frames):
            card.grid_forget()
            row = idx // cols
            col = idx % cols
            card.grid(row=row, column=col, padx=10, pady=12, sticky='nsew')
            self.cards.grid_rowconfigure(row, weight=0)


class Developer(ctk.CTkToplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            self.transient(parent)
        self.title('Face Recognition System - Developer Info')
        self.configure(fg_color=DARK_BG)
        self.build_ui()
        self.state('zoomed')
        self.focus_force()
        self.lift()

    def build_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        header = ctk.CTkFrame(self, fg_color='#090B10', height=70)
        header.grid(row=0, column=0, sticky='nsew')
        header.grid_propagate(False)

        ctk.CTkLabel(header, text='FACE RECOGNITION SYSTEM', text_color=ACCENT,
                     font=('Helvetica', 18, 'bold')).place(relx=0.03, rely=0.5, anchor='w')
        ctk.CTkLabel(header, text='SYSTEM ONLINE', text_color=ACCENT2,
                     font=('Helvetica', 11, 'bold')).place(relx=0.97, rely=0.5, anchor='e')

        main = ctk.CTkFrame(self, fg_color=DARK_BG)
        main.grid(row=1, column=0, sticky='nsew', padx=18, pady=18)
        main.grid_columnconfigure(0, weight=1)
        main.grid_columnconfigure(1, weight=1)
        main.grid_rowconfigure(0, weight=1)
        main.grid_rowconfigure(1, weight=1)

        summary = ctk.CTkFrame(main, fg_color=PANEL_BG, corner_radius=22,
                                border_width=1, border_color=BORDER)
        summary.grid(row=0, column=0, sticky='nsew', padx=(0, 12), pady=0)
        summary.grid_columnconfigure(0, weight=1)

        cards = ctk.CTkFrame(main, fg_color=PANEL_BG, corner_radius=22,
                              border_width=1, border_color=BORDER)
        cards.grid(row=0, column=1, sticky='nsew', padx=(12, 0), pady=0)
        cards.grid_columnconfigure((0, 1, 2), weight=1)
        cards.grid_rowconfigure((0, 1), weight=1)

        self.summary = summary
        self.cards = cards
        self.main = main
        self.card_frames = []

        section_title = ctk.CTkLabel(summary, text='Project Overview', text_color=TEXT_PRI,
                                     font=('Helvetica', 22, 'bold'))
        section_title.grid(row=0, column=0, sticky='w', padx=24, pady=(24, 8))

        section_subtitle = ctk.CTkLabel(summary, text='Final year attendance solution built with face recognition.',
                                        text_color=TEXT_SEC, font=('Helvetica', 12))
        section_subtitle.grid(row=1, column=0, sticky='w', padx=24)

        summary_text = (
            'A smart attendance system using webcam-based face recognition. '
            'It captures student attendance with OpenCV, verifies identities, '
            'and stores records securely in MySQL. '
            'This dashboard highlights the team, their roles, and the core technologies.'
        )
        tk.Label(summary, text=summary_text, justify='left', bg=PANEL_BG,
                 fg=TEXT_SEC, font=('Helvetica', 11), wraplength=400).grid(row=2, column=0, sticky='w', padx=24, pady=(10, 0))

        quote_label = ctk.CTkLabel(summary, text='Team Quote', text_color=TEXT_PRI,
                                   font=('Helvetica', 18, 'bold'))
        quote_label.grid(row=3, column=0, sticky='w', padx=24, pady=(24, 8))

        tk.Label(summary, text='"' + QUOTE + '"', justify='left', bg=PANEL_BG,
                 fg=ACCENT2, font=('Helvetica', 12, 'italic'), wraplength=400).grid(row=4, column=0, sticky='w', padx=24)

        tech_frame = ctk.CTkFrame(summary, fg_color=DARK_BG, corner_radius=16)
        tech_frame.grid(row=5, column=0, sticky='ew', padx=24, pady=(24, 24))
        tech_frame.grid_columnconfigure((0, 1), weight=1)

        title_badges = ctk.CTkLabel(tech_frame, text='Key Technologies', text_color=TEXT_PRI,
                                     font=('Helvetica', 14, 'bold'))
        title_badges.grid(row=0, column=0, columnspan=2, sticky='w', padx=18, pady=(16, 10))

        for idx, (tech, color) in enumerate(TECHS):
            badge = ctk.CTkLabel(tech_frame, text=tech, fg_color=color,
                                  text_color='white', font=('Helvetica', 11, 'bold'), corner_radius=12)
            badge.grid(row=1 + idx // 2, column=idx % 2, sticky='ew', padx=14, pady=8)

        for idx, dev in enumerate(DEVELOPERS):
            card = DeveloperCard(cards, dev, idx)
            card.grid(row=0, column=idx, padx=10, pady=24, sticky='nsew')
            cards.grid_columnconfigure(idx, weight=1)
            self.card_frames.append(card)

        self.bind('<Configure>', self.on_resize)
        self.after(100, self.adjust_layout)

        footer = ctk.CTkFrame(self, fg_color='#090B10', height=44)
        footer.grid(row=2, column=0, sticky='nsew')
        footer.grid_propagate(False)
        ctk.CTkLabel(footer, text='Face Recognition System - Final Year Project 2025-26 - Developed by Shivam Kumar, Abhishek Kumar & Aatish Raj',
                     text_color=TEXT_SEC, font=('Helvetica', 10)).place(relx=0.5, rely=0.5, anchor='center')

    def on_resize(self, event):
        if event.widget == self:
            self.adjust_layout()

    def adjust_layout(self):
        width = self.winfo_width()
        if width <= 0:
            return

        if width < 1080:
            self.main.grid_rowconfigure(0, weight=0)
            self.main.grid_rowconfigure(1, weight=1)
            self.summary.grid(row=0, column=0, sticky='nsew', padx=(0, 0), pady=(0, 12))
            self.cards.grid(row=1, column=0, sticky='nsew', padx=(0, 0), pady=(0, 0))
        else:
            self.main.grid_rowconfigure(0, weight=1)
            self.main.grid_rowconfigure(1, weight=0)
            self.summary.grid(row=0, column=0, sticky='nsew', padx=(0, 12), pady=0)
            self.cards.grid(row=0, column=1, sticky='nsew', padx=(12, 0), pady=0)

        if width < 900:
            cols = 1
        elif width < 1240:
            cols = 2
        else:
            cols = 3

        for col in range(3):
            self.cards.grid_columnconfigure(col, weight=1 if col < cols else 0)

        for idx, card in enumerate(self.card_frames):
            card.grid_forget()
            row = idx // cols
            col = idx % cols
            card.grid(row=row, column=col, padx=10, pady=12, sticky='nsew')
            self.cards.grid_rowconfigure(row, weight=0)


if __name__ == '__main__':
    app = DeveloperDashboard()
    app.mainloop()
