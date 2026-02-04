student = {
    "name": "Jeevan",
    "age": 20,
    "course": "Python"
}
print(student["name"])
student["age"] = 22
student["city"]="vittal"
print(student)

#dictionary methods

marks={"Maths":90, "Science":85, "English":88}
print(marks.get("Maths"))
print(marks.get("history",0))
for subject, score in marks.items():
    print(subject, score)
marks.update({"Maths": 95})
print(marks)

marks.pop("Science")
print(marks)


#items

purchases={
    "Alice":250,
    "Bob":100,
    "Charlie":150
}
for name,amount in purchases.items():
    print(f"{name} spent ₹{amount}")

print("Total customers",len(purchases))

print("Customers List",list(purchases.keys()))

#dynamic data collection
n=int(input("Enter number of customers: "))
user_purchases={}

for i in range(n):
    name=input("Enter customer name: ")
    amount=int(input("Enter purchase amount: "))
    user_purchases[name]=amount

print("customer purchase data", user_purchases)

top_customer=max(user_purchases,key=user_purchases.get)
print("Top spending customer:",top_customer)

min_customer=min(user_purchases,key=user_purchases.get)
print("min spending customer:",min_customer)