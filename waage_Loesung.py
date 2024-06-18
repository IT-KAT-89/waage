
                             
def find_weight_combination(target_mass):
    """
    Findet die Kombination der Gewichte 1 kg, 3 kg, 9 kg und 27 kg,
    die die angegebene Masse ergibt.
    
    Args:
        target_mass (int): Die gewünschte Masse in kg.
        
    Returns:
        list: Eine Liste mit den Gewichten, die addiert die Zielmasse ergeben.
    """
    weights = [1, 3, 9, 27]
    combination = []
    
    # Für Massen von 27 kg bis 40 kg
    if target_mass >= 27:
        combination.append(27)
        target_mass -= 27
    
    # Für Massen von 14 kg bis 26 kg
    if 14 <= target_mass <= 26:
        combination.append(-27)
        target_mass = 27 - target_mass
    
    # Addiere die restlichen Gewichte
    for weight in [9, 3, 1]:
        while target_mass >= weight:
            combination.append(weight)
            target_mass -= weight
    
    return combination

print(find_weight_combination(19))
    
