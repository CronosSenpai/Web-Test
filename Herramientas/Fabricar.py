def analizar_receta(precio_abidos_stone, precio_timber, precio_tender_timber, precio_abidos_timber):
    """
    Analiza si merece la pena comprar materiales, venderlos o craftear según los precios dados.
    """
    # Coste total de materiales
    coste_materiales = (
        33 * precio_abidos_timber +
        45 * precio_tender_timber +
        86 * precio_timber
    )
    # Valor de la receta (con bonus de 348)
    valor_receta = coste_materiales + 348

    if valor_receta > precio_abidos_stone:
        return "No merece la pena comprar materiales"
    elif (coste_materiales * 0.95) > precio_abidos_stone:
        return "Merece la pena vender los materiales"
    else:
        return "Merece la pena craftear pero no comprar materiales"

# Ejemplo de uso:
# resultado = analizar_receta(
#     precio_abidos_stone=5000,
#     precio_timber=80,
#     precio_tender_timber=100,
#     precio_abidos_timber=1000
# )
#