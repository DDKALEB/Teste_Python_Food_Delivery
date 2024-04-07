class FoodDeliverySystem:
    def __init__(self):
        self.orders = {}  # Dicionário para armazenar os detalhes do pedido

    def place_order(self, order_id, order_details, pickup_date):
        if order_id not in self.orders:
            self.orders[order_id] = {"order_details": order_details, "pickup_date": pickup_date, "status": "pending"}
            return "Order placed successfully."
        else:
            return "Order with this ID already exists."

    def modify_order(self, order_id, new_order_details):
        if order_id in self.orders and self.orders[order_id]["status"] == "pending":
            self.orders[order_id]["order_details"] = new_order_details
            return "Order modified successfully."
        else:
            return "Order not found or already picked up. Cannot modify."

    def cancel_order(self, order_id):
        if order_id in self.orders and self.orders[order_id]["status"] == "pending":
            del self.orders[order_id]
            return "Order cancelled successfully."
        else:
            return "Order not found or already picked up. Cannot cancel."

    def generate_invoice(self, order_id):
        if order_id in self.orders:
            order_details = self.orders[order_id]["order_details"]
            total_bill = sum(item["price"] for item in order_details)
            if total_bill > 1000:
                total_bill += total_bill * 0.1  # Adiciona 10% de taxa
            else:
                total_bill += total_bill * 0.05  # Adiciona 5% de taxa
            return f"Total invoice amount: {total_bill}"
        else:
            return "Order not found."