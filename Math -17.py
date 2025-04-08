dic = {}

print(dic)

dic[55] = "Nrasoç"
dic[1] = "iuas"

print(dic)

dici = {
    "SP" : "São paulo",
    "USA" : "Estados unidos",
    "FER" : "DFFFFFFFFFFFF",
}

print(dici["SP"])

print(dici.get("ES"))
print(dici.get("ES", "Não existe"))

print(dici.pop("USA"))

for i in dici:
    print(i)

for i in dici.keys():
    print(i)

for i in dici.values():
    print(i)

for i, x in dici.items():
    print(i, x)

for i in dici.items():
    print(i)

for i in enumerate(dici):
    print(i)

