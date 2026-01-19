"""
EX06 (Compendio: listas + tuplas + diccionarios)
Ticket de compra: calcula coste por producto y total general.
"""

PRICES: dict[str, float] = {"Pan": 1.40, "Huevos": 2.30, "Cebolla": 0.85, "Aceite": 4.35}

def checkout(cart: list[tuple[str, int]]) -> tuple[dict[str, float], float]:
    """
    Recibe un carrito como lista de tuplas (producto, unidades).

    Devuelve:
    - Un diccionario con el coste por producto (producto -> coste)
    - Un float con el total general

    Reglas:
    - Si units < 0 -> ValueError
    - Si un producto no existe en PRICES -> ValueError
    - Si un producto aparece varias veces, se acumulan unidades

    Ejemplo:
    [("Pan", 2), ("Huevos", 1), ("Pan", 1)] ->
      ({"Pan": 4.2, "Huevos": 2.3}, 6.5)
    """
    unidades_acumuladas = {}
    
    for producto, unidades in cart:
        if unidades < 0:
            raise ValueError(f"Unidades negativas para {producto}: {unidades}")
        
        if producto not in PRICES:
            raise ValueError(f"Producto desconocido: {producto}")
        
        unidades_acumuladas[producto] = unidades_acumuladas.get(producto, 0) + unidades
    
    costes_por_producto = {}
    total = 0.0
    
    for producto, unidades in unidades_acumuladas.items():
        precio_unitario = PRICES[producto]
        coste = precio_unitario * unidades
        costes_por_producto[producto] = round(coste, 2)
        total += coste
    
    return costes_por_producto, round(total, 2)