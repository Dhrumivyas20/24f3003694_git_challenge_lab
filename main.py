from sum_module import add, add_list
from difference_module import subtract
from product_module import multiply

def demo():
    print("Arithmetic demo:")
    print("2 + 3 =", add(2, 3))
    print("sum([1,2,3,4]) =", add_list([1,2,3,4]))
    print("5 - 2 =", subtract(5, 2))
    print("3 * 4 =", multiply(3, 4))

if __name__ == "__main__":
    demo()
