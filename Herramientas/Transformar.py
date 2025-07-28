'''
Vamos a crear una calculadora sobre los precios de mercado y el valor de las transformaciones permitidas
por el juego, vamos a definir primero las posibles transformaciones unidireccionales:

25 tender timber => 50 timber
5 sturdy timber => 50 timber

100 timber => 80 powder
50 tender timber => 80 powder

100 powder => 10 abidos timber
100 powder => 10 sturdy timber
100 powder => 50 tender timber

Simplificando caminos tendriamos 


1 timber => 0.4 tender timber (8/10 * 5/10)
1 timber => 0.08 sturdy timber (8/10 * 1/10)
1 timber => 0.08 abidos timber (8/10 * 1/10)

1 tender timber => 2 timber 
1 tender timber => 0.16 sturdy timber (8/5 * 1/10)
1 tender timber => 0.16 abidos timber (8/5 * 1/10)

1 Sturdy timber => 10 timber
1 Sturdy timber => 4 tender timber   (x10 * 8/10 * 5/10)
1 Sturdy timber => 0.8 abidos timber (x10 * 8/10 * 1/10)

'''
def aplicar_taxes(valor, porcentaje=0.05):
    """
    Aplica un impuesto/tasa al valor de venta.
    Por defecto aplica un 5%.
    """
    return valor * (1 - porcentaje)

def mejores_transformaciones_con_taxes(precios, porcentaje_taxes=0.05):
    """
    Igual que mejores_transformaciones, pero aplica taxes al valor de venta
    y solo muestra las transformaciones con ganancia positiva tras impuestos.
    """
    transformaciones = [
        ("tender_timber", 25, "timber", 50),
        ("sturdy_timber", 5, "timber", 50),
        ("timber", 1, "tender_timber", 0.4),
        ("timber", 1, "sturdy_timber", 0.08),
        ("timber", 1, "abidos_timber", 0.08),
        ("tender_timber", 1, "sturdy_timber", 0.16),
        ("tender_timber", 1, "abidos_timber", 0.16),
        ("sturdy_timber", 1, "tender_timber", 4),
        ("sturdy_timber", 1, "timber", 10),
        ("sturdy_timber", 1, "abidos_timber", 0.8),
    ]
    resultados = []
    for entrada, cant_entrada, salida, cant_salida in transformaciones:
        if entrada in precios and salida in precios:
            coste = precios[entrada] * cant_entrada
            valor_bruto = precios[salida] * cant_salida
            valor_neto = aplicar_taxes(valor_bruto, porcentaje_taxes)
            ganancia = valor_neto - coste
            if ganancia > 0:
                resultados.append({
                    "transformacion": f"{cant_entrada} {entrada} => {cant_salida} {salida}",
                    "coste": coste,
                    "valor_bruto": valor_bruto,
                    "valor_neto": valor_neto,
                    "ganancia": ganancia
                })
    return resultados


#Ejemplo de uso:
# precios = {
#     "timber": 1.16,
#     "tender_timber": 2.45,
#     "sturdy_timber": 12.1,
#     "abidos_timber": 16.02
# }
# for r in mejores_transformaciones_con_taxes(precios):
#     print(r)