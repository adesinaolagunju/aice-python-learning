scores = [85, 42, 90, 55, 72, 38, 68, 91, 47, 60]

passed = [score for score in scores if score >= 50]
print(f"Passed: {passed}")

failed = [score for score in scores if score < 50]
print(f"Failed: {failed}")

fruits = ["mango", "orange", "banana", "pineapple", "pawpaw", "apple"]
long_fruits = [fruit for fruit in fruits if len(fruit) > 5]
print(f"Fruits with more than 5 letters: {long_fruits}") 
