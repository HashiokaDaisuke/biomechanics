import co

people = [0,0]
people[0] = co.Class1("Daisuke Hashioka", "1999/2/12", 90, 50)
people[1] = co.Class1("Rihito", "1999/3/26", 95, 94)
#後で配列？化したいね！

n = 2

print(people[0].getName(),"の平均点は", people[0].getAverage(), "です．")
print(people[1].getName(),"の平均点は", people[1].getAverage(), "です．")
print(co.averageAdd(n - 1,people)/n)
