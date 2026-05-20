import math

# 1. 建立計算圓周長的函式 (注意：這裡保留了題目圖片中的拼字 calcCircumfrence)
def calcCircumfrence(radius):
    circumference = 2 * math.pi * radius
    print(f"The circumference is {circumference}")

# 2. 建立計算圓面積的函式
def calcArea(radius):
    area = math.pi * (radius ** 2)
    print(f"The area is {area}")

# --- 測試區塊 ---
# 假設半徑為 5 來測試這兩個函式
calcCircumfrence(5)
calcArea(5)
