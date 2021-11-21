import joblib as jb
import sys

model = jb.load("salary_model.pk1")

z = model.predict([[sys.argv[1]]])

print("\n\n\nPredicted Salary for '"+sys.argv[1]+"' years' of experience --> ", end="")

print(z)

print("\n\n")
