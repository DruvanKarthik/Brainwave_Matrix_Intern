class Product:
    def __init__(self, p_id, name, size, quantity=0, price=0.0):
        self.id = p_id
        self.name = name
        self.size = size
        self.quantity = quantity
        self.price = price  

class InventoryManagement:
    def __init__(self):
        self.products = []

    def add(self, p_id, name, size, quantity, price):
        if self._product_exists(p_id):
            print(f"Product with ID {p_id} already exists.")
            return
        new_product = Product(p_id, name, size, quantity, price)
        self.products.append(new_product)
        print(f"Product {name} added successfully!")

    def edit(self, p_id):
        product = self._find_product_by_id(p_id)
        if product:
            choice = self.choice()
            if choice == 1:
                new_id = int(input("Enter new ID: "))
                if not self._product_exists(new_id):
                    product.id = new_id
                else:
                    print("ID already exists.")
            elif choice == 2:
                product.name = input("Enter new name of the product: ")
            elif choice == 3:
                product.size = input("Enter new size of the product: ")
            elif choice == 4:
                product.quantity = int(input("Enter new quantity of the product: "))
            elif choice == 5:
                product.price = float(input("Enter new price of the product: ")) 
        else:
            print(f"Product with ID {p_id} not found.")

    def delete(self, p_id):
        product = self._find_product_by_id(p_id)
        if product:
            self.products.remove(product)
            print(f"Product with ID {p_id} deleted successfully.")
        else:
            print(f"Product with ID {p_id} not found.")

    def track_inventory_levels(self):
        low_stock_threshold = 10
        for product in self.products:
            if product.quantity < low_stock_threshold:
                print(f"Low stock alert: Product {product.name} (ID: {product.id}) has low stock ({product.quantity}).")

    def generate_reports(self):
        print("Product Inventory Report:")
        total_value = 0
        for product in self.products:
            print(f"ID: {product.id}, Name: {product.name}, Size: {product.size}, Quantity: {product.quantity}, Price: {product.price}")
            total_value += product.quantity * product.price  # Calculate total value of stock
        print(f"Total inventory value: {total_value}")

    def sale_summaries(self):
        total_sales = 0
        for product in self.products:
            sales = int(input(f"Enter sales for {product.name} (ID: {product.id}): "))
            total_sales += sales * product.price  # Multiply by price for total sales value
            product.quantity -= sales  # Decrease stock quantity after sale
        print(f"Total Sales: {total_sales}")

    def choice(self):
        print("Choose a change to make:")
        print("1. Edit Product ID")
        print("2. Edit Product Name")
        print("3. Edit Product Size")
        print("4. Edit Product Quantity")
        print("5. Edit Product Price")
        return int(input("Enter your choice: "))

    def _find_product_by_id(self, p_id):
        for product in self.products:
            if product.id == p_id:
                return product
        return None

    def _product_exists(self, p_id):
        return any(product.id == p_id for product in self.products)

def main():
    inventory = InventoryManagement()
    
    # Adding sample products
    inventory.add(1, 'Product A', 'Small', 50, 10.0)
    inventory.add(2, 'Product B', 'Medium', 5, 15.0)
    
    # Performing operations
    inventory.track_inventory_levels()
    inventory.generate_reports()
    inventory.sale_summaries()
    
    # Editing and deleting product
    inventory.edit(1)
    inventory.delete(2)

if __name__ == "__main__":
    main()
