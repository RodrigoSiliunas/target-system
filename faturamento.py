sao_paulo = 67836.43
rio_de_janeiro = 36678.66
minas_gerais = 29229.88
espirito_santo = 27165.48
outros = 19849.53

total = sao_paulo + rio_de_janeiro + minas_gerais + espirito_santo + outros

print(
    f'São Paulo representa um total de {(sao_paulo / total) * 100:.2f}% do lucro total.\n'
    f'Rio de Janeiro representa um total de {(rio_de_janeiro / total) * 100:.2f}% do lucro total.\n'
    f'Minas Gerais representa um total de {(minas_gerais / total) * 100:.2f}% do lucro total.\n'
    f'Espirito Santo representa um total de {(espirito_santo / total) * 100:.2f}% do lucro total.\n'
    f'Outros representam um total de {(outros / total) * 100:.2f}% do lucro total.'
)