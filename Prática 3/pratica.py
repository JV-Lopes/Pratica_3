import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("londonweather.csv")

print("Prévia dos dados:")
print(df.head())

ultimo_ano = df["Year"].max()
primeiro_ano = ultimo_ano - 9
df_ultimos10 = df[df["Year"].between(primeiro_ano, ultimo_ano)]

print(f"\nÚltimo ano do dataset: {ultimo_ano}")
print(f"Selecionados os anos de {primeiro_ano} até {ultimo_ano}")

plt.figure(figsize=(12,6))
cores = plt.cm.tab10.colors
marcadores = ["o", "s", "D", "^", "v", ">", "<", "p", "*", "h"]

for i, ano in enumerate(range(primeiro_ano, ultimo_ano+1)):
    dados_ano = df_ultimos10[df_ultimos10["Year"] == ano]
    plt.plot(dados_ano["Month"], dados_ano["Tmax"], label=str(ano),
             color=cores[i % 10], marker=marcadores[i % 10])

plt.title("Temperaturas Máximas — Últimos 10 anos")
plt.xlabel("Mês")
plt.ylabel("Tmax (°C)")
plt.legend()
plt.grid(True)
plt.show()

linha_max = df_ultimos10.loc[df_ultimos10["Tmax"].idxmax()]
mes_max, ano_max, temp_max = linha_max["Month"], linha_max["Year"], linha_max["Tmax"]

print(f"\nMaior temperatura dos últimos 10 anos: {temp_max}°C ({mes_max}/{ano_max})")

plt.figure(figsize=(12,6))

for i, ano in enumerate(range(primeiro_ano, ultimo_ano+1)):
    dados_ano = df_ultimos10[df_ultimos10["Year"] == ano]
    plt.plot(dados_ano["Month"], dados_ano["Tmax"], label=str(ano),
             color=cores[i % 10], marker=marcadores[i % 10])

plt.annotate(
    f"{temp_max}°C é a maior temperatura registrada nos últimos 10 anos",
    xy=(mes_max, temp_max),
    xytext=(mes_max + 0.3, temp_max + 1),
    arrowprops=dict(arrowstyle="->", lw=2)
)

plt.title("Temperaturas Máximas — Últimos 10 anos (com anotação)")
plt.xlabel("Mês")
plt.ylabel("Tmax (°C)")
plt.legend()
plt.grid(True)
plt.show()

primeiro_ano_dataset = df["Year"].min()
primeiros10 = primeiro_ano_dataset + 9
df_primeiros10 = df[df["Year"].between(primeiro_ano_dataset, primeiros10)]

plt.figure(figsize=(12,6))

for i, ano in enumerate(range(primeiro_ano_dataset, primeiros10+1)):
    dados_ano = df_primeiros10[df_primeiros10["Year"] == ano]
    plt.plot(dados_ano["Month"], dados_ano["Tmax"], label=str(ano),
             color=cores[i % 10], marker=marcadores[i % 10])

plt.title("Temperaturas Máximas — Primeiros 10 anos")
plt.xlabel("Mês")
plt.ylabel("Tmax (°C)")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(12,7))
plt.scatter(df["Month"], df["Tmax"], s=df["Tmax"] * 4, alpha=0.5)

plt.title("Gráfico de Bolhas — Tmax por Mês (1957–2019)")
plt.xlabel("Mês")
plt.ylabel("Tmax (°C)")
plt.grid(True)
plt.show()
