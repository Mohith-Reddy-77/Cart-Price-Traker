import tkinter as tk
from tkinter import messagebox

products = {
    "Food": {
        "Rice": {"price": 40, "stock": 50},
        "Wheat Flour": {"price": 35, "stock": 100},
        "Instant Noodles": {"price": 10, "stock": 200},
        "Moong Dal": {"price": 80, "stock": 30},
        "Cooking Oil": {"price": 100, "stock": 70},
        "Sugar": {"price": 40, "stock": 150},
        "Tea": {"price": 200, "stock": 60},
        "Salt": {"price": 20, "stock": 300},
        "Pickles": {"price": 50, "stock": 80},
        "Sweets": {"price": 200, "stock": 40}
    },
    "Clothes": {
        "T-shirts": {"price": 550, "stock": 100},
        "Salwar Kameez Sets": {"price": 800, "stock": 60},
        "Sarees": {"price": 1200, "stock": 40},
        "Jeans Pants": {"price": 800, "stock": 90},
        "Kurtis": {"price": 500, "stock": 80},
        "Flip-flops": {"price": 650, "stock": 100},
        "Night wear": {"price": 600, "stock": 50},
        "Cotton Shirts": {"price": 1000, "stock": 70},
        "Cotton Socks": {"price": 100, "stock": 150},
        "Jackets": {"price": 1000, "stock": 60}
    },
    "Electronics": {
        "Feature Phones": {"price": 1500, "stock": 30},
        "Earphones": {"price": 400, "stock": 120},
        "LED TV": {"price": 15000, "stock": 15},
        "Electric Fans": {"price": 2000, "stock": 50},
        "Power Banks": {"price": 1000, "stock": 80},
        "LED Bulbs": {"price": 100, "stock": 200},
        "Charger": {"price": 900, "stock": 150},
        "Mixers": {"price": 1500, "stock": 60},
        "Bluetooth Speakers": {"price": 1000, "stock": 100},
        "Smart Phone": {"price": 15000, "stock": 30}
    },
    "Toiletries": {
        "Toothpaste": {"price": 50, "stock": 200},
        "Bath Soap": {"price": 30, "stock": 300},
        "Shaving Cream": {"price": 50, "stock": 100},
        "Shampoo": {"price": 100, "stock": 150},
        "Hair Oil": {"price": 100, "stock": 120},
        "Deodorant": {"price": 150, "stock": 180},
        "Handwash": {"price": 75, "stock": 250},
        "Sanitary Napkins": {"price": 150, "stock": 100}
    },
    "Beauty Products": {
        "Aloe Vera Gel": {"price": 100, "stock": 120},
        "Face Wash": {"price": 150, "stock": 80},
        "Lip Balm": {"price": 50, "stock": 200},
        "Kajal": {"price": 40, "stock": 180},
        "Compact Powder": {"price": 150, "stock": 90},
        "Hair Serum": {"price": 200, "stock": 60},
        "Nail Polish": {"price": 50, "stock": 200},
        "Sunscreen": {"price": 200, "stock": 100},
        "Fairness Cream": {"price": 150, "stock": 150},
        "Body Scrubs": {"price": 300, "stock": 70}
    },
    "Home Decor": {
        "Wall Clocks": {"price": 500, "stock": 80},
        "Printed Curtains": {"price": 700, "stock": 50},
        "Cushion Covers": {"price": 200, "stock": 100},
        "Bamboo Plant Pots": {"price": 250, "stock": 90},
        "Bed Covers": {"price": 700, "stock": 60},
        "Fridge Magnets": {"price": 100, "stock": 150},
        "Wall Stickers": {"price": 200, "stock": 120},
        "Photo Frames": {"price": 250, "stock": 100},
        "Table Lamps": {"price": 600, "stock": 50},
        "Decorative Trays": {"price": 400, "stock": 70}
    },
    "Stationary": {
        "Long size ruled Book": {"price": 60, "stock": 150},
        "Short size ruled Book": {"price": 40, "stock": 200},
        "Ball pens(5)": {"price": 50, "stock": 300},
        "Geometry Box": {"price": 100, "stock": 80},
        "Colour pencils": {"price": 75, "stock": 120},
        "Pencil Box(10)": {"price": 100, "stock": 100},
        "A4 sheets(100)": {"price": 100, "stock": 250}
    },
    "Cleaning": {
        "Brooms": {"price": 50, "stock": 100},
        "Mops": {"price": 200, "stock": 50},
        "Dishwashing Liquid": {"price": 50, "stock": 200},
        "Dustpans": {"price": 50, "stock": 150},
        "Microfiber Cloths": {"price": 100, "stock": 180},
        "Scrub Pads": {"price": 30, "stock": 300},
        "Floor Cleaning Brushes": {"price": 100, "stock": 70},
        "Vacuum Cleaners": {"price": 2500, "stock": 20},
        "Liquid Soap for Cleaning": {"price": 100, "stock": 250},
        "Window Cleaners": {"price": 150, "stock": 100}
    }
}

class ShoppingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping System")
        self.root.geometry("1000x1000")
        self.root.config(bg="#f1f1f1")

        self.budget = 0
        self.cart = {}
        self.total = 0

        self.main_canvas = tk.Canvas(self.root, bg="#ffffff")
        self.main_scrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.main_canvas.yview)
        self.scrollable_frame = tk.Frame(self.main_canvas, bg="#ffffff")

        self.scrollable_frame.bind(
            "<Configure>", lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all"))
        )

        self.main_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.main_canvas.configure(yscrollcommand=self.main_scrollbar.set)

        self.main_canvas.pack(side="left", fill="both", expand=True)
        self.main_scrollbar.pack(side="right", fill="y")

        self.setup_main_ui()

    def setup_main_ui(self):
        tk.Label(self.scrollable_frame, text="Enter Budget:", font=("Arial", 16, "bold"), bg="#f1f1f1").pack(pady=10)
        self.budget_entry = tk.Entry(self.scrollable_frame, font=("Arial", 14), relief="solid", bd=2, width=20)
        self.budget_entry.pack(pady=10)
        tk.Button(self.scrollable_frame, text="Set Budget", command=self.set_budget, font=("Arial", 14), bg="#4CAF50", fg="white", relief="raised", bd=3).pack(pady=10)

        self.category_frame = tk.Frame(self.scrollable_frame, bg="#f1f1f1")
        self.items_frame = tk.Frame(self.scrollable_frame, bg="#f1f1f1")
        self.cart_frame = tk.Frame(self.scrollable_frame, bg="#f1f1f1")

        self.remaining_label = tk.Label(self.scrollable_frame, text="", font=("Arial", 14), bg="#f1f1f1")
        self.remaining_label.pack(pady=10)

    def set_budget(self):
        try:
            self.budget = int(self.budget_entry.get())
            if self.budget <= 0:
                raise ValueError
            self.remaining_label.config(text=f"Budget Set: ₹{self.budget}")
            self.show_categories()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid budget.")

    def show_categories(self):
        self.category_frame.destroy()
        self.search_entry = tk.Entry(self.scrollable_frame, font=("Arial", 12), relief="solid", bd=2, width=20)
        self.search_entry.pack(pady=10)
        tk.Button(self.scrollable_frame, text="Search Items", command=self.search_items, font=("Arial", 14), bg="black", fg="white", relief="raised", bd=3).pack(pady=10)

        self.category_frame = tk.Frame(self.scrollable_frame, bg="#f1f1f1")
        self.category_frame.pack(pady=10)

        tk.Label(self.category_frame, text="Select a Category:", font=("Arial", 16, "bold"), bg="#f1f1f1").pack(pady=10)

        category_inner_frame = tk.Frame(self.category_frame, bg="#f1f1f1")
        category_inner_frame.pack(fill=tk.X)

        for category in products.keys():
            tk.Button(category_inner_frame, text=category, font=("Arial", 12), bg="#03A9F4", fg="white", relief="raised", bd=3,
                      command=lambda c=category: self.show_items(c)).pack(side=tk.LEFT, padx=10, pady=5)

    def show_items(self, category):
        self.items_frame.destroy()
        self.items_frame = tk.Frame(self.scrollable_frame, bg="#f1f1f1", width=600)
        self.items_frame.pack(side="left", padx=10, fill=tk.Y)

        tk.Label(self.items_frame, text=f"{category} Items:", font=("Arial", 16, "bold"), bg="#f1f1f1").pack(pady=10)

        item_grid_frame = tk.Frame(self.items_frame, bg="#f1f1f1")
        item_grid_frame.pack(pady=10)

        tk.Label(item_grid_frame, text="Item", font=("Arial", 12, "bold"), width=20, anchor="w", bg="#f1f1f1").grid(row=0, column=0, padx=10)
        tk.Label(item_grid_frame, text="Price", font=("Arial", 12, "bold"), width=10, anchor="w", bg="#f1f1f1").grid(row=0, column=1, padx=10)
        tk.Label(item_grid_frame, text="Stock", font=("Arial", 12, "bold"), width=10, anchor="w", bg="#f1f1f1").grid(row=0, column=2, padx=10)
        tk.Label(item_grid_frame, text="Add", font=("Arial", 12, "bold"), width=10, anchor="w", bg="#f1f1f1").grid(row=0, column=3, padx=10)

        row = 1
        for item, details in products[category].items():
            tk.Label(item_grid_frame, text=item, font=("Arial", 12), width=20, anchor="w", bg="#f1f1f1").grid(row=row, column=0, padx=10)
            tk.Label(item_grid_frame, text=f"₹{details['price']}", font=("Arial", 12), width=10, anchor="w", bg="#f1f1f1").grid(row=row, column=1, padx=10)
            tk.Label(item_grid_frame, text=f"{details['stock']} left", font=("Arial", 12), width=10, anchor="w", bg="#f1f1f1").grid(row=row, column=2, padx=10)
            qty_entry = tk.Entry(item_grid_frame, width=5, font=("Arial", 12), relief="solid", bd=2)
            qty_entry.grid(row=row, column=3, padx=10)
            add_button = tk.Button(item_grid_frame, text="Add", font=("Arial", 12), bg="#4CAF50", fg="white", relief="raised", bd=2,
                                    command=lambda i=item, p=details['price'], q=qty_entry: self.add_to_cart(i, p, q, category))
            add_button.grid(row=row, column=4, padx=10)
            row += 1

        self.cart_frame.destroy()
        self.cart_frame = tk.Frame(self.scrollable_frame, bg="#f1f1f1", width=200)
        self.cart_frame.pack(side="right", padx=10, fill=tk.Y)
        self.update_cart()

    def add_to_cart(self, item, price, qty_entry, category):
        try:
            qty = int(qty_entry.get())
            if qty <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid quantity.")
            return

        new_total = self.total + (price * qty)

        if new_total > self.budget:
            messagebox.showerror("Budget Exceeded", f"Adding this item exceeds your budget by ₹{new_total-self.budget}")
            return
        if products[category][item]['stock'] < qty:
            messagebox.showerror("Invalid Input", "Invalid Quantity")
            return

        if item in self.cart:
            self.cart[item]["quantity"] += qty
            self.cart[item]["cost"] += price * qty
        else:
            self.cart[item] = {"category": category, "quantity": qty, "cost": price * qty}
        products[category][item]['stock'] = products[category][item]['stock'] - qty
        self.total = new_total
        self.update_cart()
        self.show_items(category)

    def update_cart(self):
        self.cart_frame.destroy()
        self.cart_frame = tk.Frame(self.scrollable_frame, bg="#f1f1f1", width=200)
        self.cart_frame.pack(side="right", padx=10, fill=tk.Y)

        tk.Label(self.cart_frame, text="Cart:", font=("Arial", 16, "bold"), bg="#f1f1f1").pack(pady=10)

        for item, details in self.cart.items():
            item_frame = tk.Frame(self.cart_frame, bg="#f1f1f1")
            item_frame.pack(pady=5)

            tk.Label(item_frame, text=f"{item} (x{details['quantity']}): ₹{details['cost']}", font=("Arial", 12), bg="#f1f1f1").pack(side=tk.LEFT)
            tk.Button(item_frame, text="Remove", font=("Arial", 10), bg="#FF5722", fg="white", relief="raised", bd=2, command=lambda i=item: self.remove_item(i)).pack(side=tk.LEFT, padx=10)

        tk.Label(self.cart_frame, text=f"Total: ₹{self.total}", font=("Arial", 14), bg="#f1f1f1").pack(pady=10)
        tk.Label(self.cart_frame, text=f"Budget Left: ₹{self.budget  - self.total}", font=("Arial", 14), bg="#f1f1f1").pack(pady=10)
        tk.Button(self.cart_frame, text="Checkout", font=("Arial", 14), bg="#4CAF50", fg="white", relief="raised", bd=2, command=self.checkout).pack(pady=10)
        tk.Button(self.cart_frame, text="Clear Cart", font=("Arial", 14), bg="#F44336", fg="white", relief="raised", bd=2, command=self.clear_cart).pack(pady=5)

    def checkout(self):
        if not self.cart:
            messagebox.showwarning("Empty Cart", "Your cart is empty. Add some items before checkout.")
            return
        if self.total > self.budget:
            messagebox.showerror("Budget Exceeded", "You cannot checkout as your total exceeds the available budget.")
            return
        messagebox.showinfo("Checkout Successful", f"Your total amount is ₹{self.total}. Thank you for shopping!")
        self.clear_cart()

    def remove_item(self, item):
        products[self.cart[item]['category']][item]['stock'] = products[self.cart[item]['category']][item]['stock'] + self.cart[item]['quantity']
        self.show_items(self.cart[item]['category'])
        self.total -= self.cart[item]['cost']
        del self.cart[item]
        self.update_cart()

    def clear_cart(self):
        self.cart.clear()
        self.total = 0
        self.update_cart()

    def search_items(self):
        query = self.search_entry.get().lower()
        found_items = {}
        for category, items in products.items():
            for item, details in items.items():
                if query in item.lower():
                    if category not in found_items:
                        found_items[category] = {}
                    found_items[category][item] = details
        if found_items:
            self.show_search_results(found_items)
        else:
            messagebox.showinfo("No Results", "No items found matching your search.")
    
    def show_search_results(self, found_items):
        self.items_frame.destroy()
        self.items_frame = tk.Frame(self.scrollable_frame, bg="#f1f1f1")
        self.items_frame.pack(pady=10)

        tk.Label(self.items_frame, text="Search Results:", font=("Arial", 16, "bold"), bg="#f1f1f1").grid(row=0, column=0, columnspan=5, pady=10)
        row_index = 1 
        for category, items in found_items.items():
            tk.Label(self.items_frame, text=f"{category}:", font=("Arial", 14, "bold"), bg="#f1f1f1").grid(row=row_index, column=0, columnspan=5, pady=5)
            row_index += 1
            tk.Label(self.items_frame, text="Item", font=("Arial", 12, "bold"), bg="#f1f1f1", width=25, anchor='w').grid(row=row_index, column=0)
            tk.Label(self.items_frame, text="Price", font=("Arial", 12, "bold"), bg="#f1f1f1", width=10).grid(row=row_index, column=1)
            tk.Label(self.items_frame, text="Stock", font=("Arial", 12, "bold"), bg="#f1f1f1", width=10).grid(row=row_index, column=2)
            tk.Label(self.items_frame, text="Qty", font=("Arial", 12, "bold"), bg="#f1f1f1", width=10).grid(row=row_index, column=3)
            tk.Label(self.items_frame, text="Add to Cart", font=("Arial", 12, "bold"), bg="#f1f1f1", width=12).grid(row=row_index, column=4)
            row_index += 1
            for item, details in items.items():
                tk.Label(self.items_frame, text=item, font=("Arial", 12), bg="#f1f1f1", width=25, anchor='w').grid(row=row_index, column=0)
                tk.Label(self.items_frame, text=f"₹{details['price']}", font=("Arial", 12), bg="#f1f1f1", width=10).grid(row=row_index, column=1)
                tk.Label(self.items_frame, text=f"{details['stock']} left", font=("Arial", 12), bg="#f1f1f1", width=10).grid(row=row_index, column=2)

                qty_entry = tk.Entry(self.items_frame, width=5, font=("Arial", 12), relief="solid", bd=2)
                qty_entry.grid(row=row_index, column=3, padx=10)

                add_button = tk.Button(self.items_frame, text="Add", font=("Arial", 12), bg="#4CAF50", fg="white", relief="raised", bd=2,
                                    command=lambda i=item, p=details['price'], q=qty_entry: self.add_to_cart(i, p, q, category))
                add_button.grid(row=row_index, column=4)
                row_index += 1

root = tk.Tk()
shopping_system = ShoppingSystem(root)
root.mainloop()
