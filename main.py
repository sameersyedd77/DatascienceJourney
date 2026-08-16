import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

print("Missing Values:")
print(df.isnull().sum())

df["average"] = df[["math", "science", "english"]].mean(axis=1)

df["performance"] = df["average"].apply(
    lambda x: "Excellent" if x >= 85
    else "Good" if x >= 70
    else "Needs Improvement"
)

print(df["performance"].value_counts())

subject_averages = df[["math", "science", "english"]].mean()

print(subject_averages)

print("Highest Performing Subject:", subject_averages.idxmax())

plt.bar(subject_averages.index, subject_averages.values)
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.title("Average Marks by Subject")
plt.savefig("charts/subject_average.png")
plt.show()

top_student = df.loc[df["average"].idxmax()]

print("Top Performing student:")
print("Name:", top_student["name"])
print("Average:", round(top_student["average"],2))

performance_counts = df["performance"].value_counts()

print("performance summary:")
print(performance_counts)

df.plot(x="name", y="average", kind="bar")

plt.title("Average score by Student")
plt.xlabel("Student")
plt.ylabel("Average Score")
plt.xticks(rotation=0)
plt.savefig("charts/students_average.png")
plt.show()

df["performance"].value_counts().plot(kind="bar")

plt.title("Students by Performance Category")
plt.xlabel("Performance")
plt.ylabel("Number of Students")
plt.xticks(rotation=0)
plt.savefig("charts/performance_category.png")
plt.show()

print("\nStudent Performance:")
print(df[["name", "average", "performance"]].round({"average": 2}))
print("\nAverage Score by Performance:")
print(df.groupby("performance")["average"].mean().round(2))
print("\nTop 3 Students:")
print(df[["name", "average"]].sort_values("average", ascending=False).head(3))

print("\nSubject Correlation:")
print(df[["math", "science", "english"]].corr().round(2))

df["Strongest_subject"] = df[["math", "science", "english"]].idxmax(axis=1)

print("\nStrongest Subject for Each Student:")
print(df[["name", "Strongest_subject"]])
print("\nStrongest Subject Summary:")
print(df["Strongest_subject"].value_counts())
print("\nClass Average:")
print(round(df["average"].mean(), 2))

print("\nHighest Average:")
print(round(df["average"].max(), 2))

print("\nLowest Average:")
print(round(df["average"].min(), 2))

print("\nStudents Above Class Average:")
print(df[df["average"] > df["average"].mean()][["name", "average"]].round({"average": 2}))
print("\nOverall Class Statistics:")
print("Class Average:", round(df["average"].mean(), 2))
print("Highest Average:", round(df["average"].max(), 2))
print("Lowest Average:", round(df["average"].min(), 2))
print("Median Average:", round(df["average"].median(), 2))
print("Standard Deviation:", round(df["average"].std(), 2))

df["rank"] = df["average"].rank(ascending=False, method="min").astype(int)

print("\nStudent Ranking:")
print(df[["rank", "name", "average"]].sort_values("rank").round({"average": 2}))

performance_percentage = df["performance"].value_counts(normalize=True) * 100

print("\nPerformance Percentage:")
print(performance_percentage.round(2))

print("\n" + "=" * 40)
print("FINAL PROJECT INSIGHTS")
print("=" * 40)

print("Top Student:", top_student["name"])
print("Top Student Average:", round(top_student["average"], 2))
print("Highest Performing Subject:", subject_averages.idxmax())
print("Class Average:", round(df["average"].mean(), 2))
print("Number of Students:", len(df))

df.to_csv("student_analysis_results.csv", index=False)

print("\nAnalysis results saved to student_analysis_results.csv")
df[["name", "average", "performance",]].to_csv(
    "students_performance_report.csv",
    index=False
)