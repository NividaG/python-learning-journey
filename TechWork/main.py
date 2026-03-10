# main.py
import core.math_utils as math_utils
from core.utils import apply_discount, clean_text



class Book:
    def __init__(self, title: str, author: str, price: float):
        self.title = clean_text(title)
        self.author = clean_text(author)
        self.price = price

    def get_final_price(self, discount: float) -> float:
        return apply_discount(self.price, discount)

    def display_info(self) -> None:
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: £{self.price}")

# ---- Program Execution ----

try:
    book1 = Book("  PYTHON 101  ", " John Smith ", 200)

    book1.display_info()

    final_price = book1.get_final_price(10)
    print(f"Price after discount: £{final_price:.2f}")
   

except Exception as e:
    print("An error occurred:", e)
    book1 = Book("  PYTHON 101  ", " John Smith ", 200)

    book1.display_info()

    final_price = book1.get_final_price(10)
    print("An error occurred:", e)



print(math_utils.square(5))
print(math_utils.square([1,2,3]))