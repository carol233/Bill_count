from datetime import date

FEE = 188.31
all_day = 0.0

START_DATE = [2020, 1, 15]
END_DATE = [2020, 4, 14]

Hao_in = START_DATE
Carol_in = [2020, 1, 18]
Kiki_in = [2020, 2, 19]
Maggie_in = [2020, 3, 15]

Hao_out = [2020, 2, 22]
Carol_out = END_DATE
Kiki_out = END_DATE
Maggie_out = END_DATE

def daysBetween(END, START):
    d = date(END[0], END[1], END[2]) - date(START[0], START[1], START[2])
    return d.days + 1

def money(NAME):
    return FEE * NAME / all_day

days_count = []

Hao_day = daysBetween(Hao_out, Hao_in)
days_count.append(Hao_day)

Carol_day = daysBetween(Carol_out, Carol_in)
days_count.append(Carol_day)

Kiki_day = daysBetween(Kiki_out, Kiki_in)
days_count.append(Kiki_day)

Maggie_day = daysBetween(Maggie_out, Maggie_in)
days_count.append(Maggie_day)

for item in days_count:
    all_day += item

print("Electric：Start from " + str(START_DATE) + " to " +
      str(END_DATE) + " totally " +
      str(daysBetween(END_DATE, START_DATE)) + " days")
avg = FEE * 1.0 / all_day
print("Avg per person per day", avg)
print("Hao days: ", Hao_day, str(Hao_in), "to", str(Hao_out), format(money(Hao_day), '.2f'))
print("Carol days: ", Carol_day, str(Carol_in), "to", str(Carol_out), format(money(Carol_day), '.2f'))
print("Kiki days: ", Kiki_day, str(Kiki_in), "to", str(Kiki_out), format(money(Kiki_day), '.2f'))
print("Maggie days: ", Maggie_day, str(Maggie_in), "to", str(Maggie_out), format(money(Maggie_day), '.2f'))
