import tkinter as tk
from tkinter import ttk, messagebox

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("1200x800")
        self.root.resizable(True, True)
        self.root.configure(bg="#2d2d2d")

        # Contact list (in-memory)
        self.contacts = {}

        # Set up custom styles
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 14), background="#2d2d2d", foreground="white")
        style.configure("TEntry", font=("Helvetica", 14))
        style.configure("TButton", font=("Helvetica", 12), background="#5cb85c", foreground="white")
        style.configure("TMenubutton", font=("Helvetica", 14))
        style.configure("TTreeview", background="#333333", foreground="white", rowheight=25, fieldbackground="#333333")
        style.configure("TTreeview.Heading", font=("Helvetica", 14), background="#333333", foreground="white")
        style.map("TButton", background=[("active", "#4cae4c")])

        # UI Components
        header = ttk.Label(root, text="Contact Manager", font=("Helvetica", 18, "bold"))
        header.pack(pady=10)

        # Add Contact Frame
        frame_add = ttk.LabelFrame(root, text="Add / Update Contact", style="TLabel", padding=(10, 10))
        frame_add.pack(fill="x", padx=20, pady=10)

        ttk.Label(frame_add, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_name = ttk.Entry(frame_add)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_add, text="Phone:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_phone = ttk.Entry(frame_add)
        self.entry_phone.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_add, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_email = ttk.Entry(frame_add)
        self.entry_email.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame_add, text="Address:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.entry_address = ttk.Entry(frame_add)
        self.entry_address.grid(row=3, column=1, padx=5, pady=5)

        button_add_update = ttk.Button(frame_add, text="Add / Update", command=self.add_update_contact)
        button_add_update.grid(row=4, columnspan=2, pady=10)

        # Search Frame
        frame_search = ttk.LabelFrame(root, text="Search Contact", style="TLabel", padding=(10, 10))
        frame_search.pack(fill="x", padx=20, pady=10)

        ttk.Label(frame_search, text="Search by Name or Phone:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_search = ttk.Entry(frame_search)
        self.entry_search.grid(row=0, column=1, padx=5, pady=5)

        button_search = ttk.Button(frame_search, text="Search", command=self.search_contact)
        button_search.grid(row=0, column=2, padx=5, pady=5)

        # Contact List Frame
        frame_list = ttk.LabelFrame(root, text="Contact List", style="TLabel", padding=(10, 10))
        frame_list.pack(fill="both", expand=True, padx=20, pady=10)

        self.tree = ttk.Treeview(frame_list, columns=("Phone", "Email", "Address"), show="headings")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Address", text="Address")
        self.tree.pack(fill="both", expand=True)

        # Delete Button
        button_delete = ttk.Button(root, text="Delete Contact", command=self.delete_contact)
        button_delete.pack(pady=10)

    def add_update_contact(self):
        name = self.entry_name.get().strip()
        phone = self.entry_phone.get().strip()
        email = self.entry_email.get().strip()
        address = self.entry_address.get().strip()

        if name and phone:
            self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            self.refresh_contact_list()
            messagebox.showinfo("Success", f"Contact '{name}' has been added/updated.")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Name and Phone are required fields.")

    def refresh_contact_list(self):
        self.tree.delete(*self.tree.get_children())
        for name, details in self.contacts.items():
            self.tree.insert("", "end", values=(name, details["Phone"], details["Email"], details["Address"]))

    def search_contact(self):
        search_term = self.entry_search.get().strip()
        found = False
        for name, details in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in details["Phone"]:
                self.tree.delete(*self.tree.get_children())
                self.tree.insert("", "end", values=(name, details["Phone"], details["Email"], details["Address"]))
                found = True
                break
        if not found:
            messagebox.showinfo("Search Result", "No contact found.")
            self.refresh_contact_list()

    def delete_contact(self):
        selected_item = self.tree.selection()
        if selected_item:
            contact_name = self.tree.item(selected_item)["values"][0]
            del self.contacts[contact_name]
            self.tree.delete(selected_item)
            messagebox.showinfo("Deleted", f"Contact '{contact_name}' has been deleted.")
        else:
            messagebox.showwarning("Delete Error", "Please select a contact to delete.")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

# Initialize the main application
root = tk.Tk()
app = ContactManager(root)
root.mainloop()

