rounds = [
    {'theme': 'Entrada', 'scores': {'Valentina': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9}, 'Mateo': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7}, 'Camila': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8}, 'Santiago': {'judge_1': 6, 'judge_2': 7, 'judge_3': 6}, 'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 8}}},
    {'theme': 'Plato principal', 'scores': {'Valentina': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8}, 'Mateo': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9}, 'Camila': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7}, 'Santiago': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8}, 'Lucía': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7}}},
    {'theme': 'Postre', 'scores': {'Valentina': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7}, 'Mateo': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8}, 'Camila': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9}, 'Santiago': {'judge_1': 7, 'judge_2': 7, 'judge_3': 6}, 'Lucía': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9}}},
    {'theme': 'Cocina internacional', 'scores': {'Valentina': {'judge_1': 8, 'judge_2': 9, 'judge_3': 9}, 'Mateo': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7}, 'Camila': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8}, 'Santiago': {'judge_1': 8, 'judge_2': 9, 'judge_3': 7}, 'Lucía': {'judge_1': 7, 'judge_2': 7, 'judge_3': 8}}},
    {'theme': 'Final libre', 'scores': {'Valentina': {'judge_1': 9, 'judge_2': 8, 'judge_3': 9}, 'Mateo': {'judge_1': 8, 'judge_2': 9, 'judge_3': 8}, 'Camila': {'judge_1': 7, 'judge_2': 7, 'judge_3': 7}, 'Santiago': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9}, 'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 7}}}
]

stats = {}

for i, round_data in enumerate(rounds, 1):
    theme = round_data['theme']
    scores = round_data['scores']
    
    round_results = []
    
    for name, judges in scores.items():
        # Suma los puntos de los 3 jueces para cada cocinero
        total_round_score = sum(judges.values())
        round_results.append((name, total_round_score))
        
        # Actualiza estadísticas globales
        if name not in stats:
            stats[name] = {'total': 0, 'wins': 0, 'best': 0}
        
        stats[name]['total'] += total_round_score
        if total_round_score > stats[name]['best']:
            stats[name]['best'] = total_round_score

    # Ordena los resultados de la ronda para la tabla de posiciones y determina al ganador
    round_results.sort(key=lambda x: x[1], reverse=True)
    winner_name, winner_score = round_results[0]
    stats[winner_name]['wins'] += 1

    # Imprimir resumen de ronda
    print(f"\nRonda {i} - {theme}:")
    print(f"Ganador: {winner_name} ({winner_score} pts)")
    print(f"{'Cocinero':<12} {'Puntaje'}")
    print("-" * 25)
    for name, score in round_results:
        print(f"{name:<12} {score}")

# --- Tabla Final ---
print("\n")
print(f"{'Tabla de posiciones final:'}")
print(f"{'Cocinero':<12} {'Puntaje':<12} {'Ganas':<12} {'Mejor':<12} {'Promedio':<12}")
print("-" * 65)

# Convertir stats a lista para ordenar por puntaje total descendente
final_ranking = sorted(stats.items(), key=lambda x: x[1]['total'], reverse=True)

num_rounds = len(rounds)
for name, data in final_ranking:
    promedio = data['total'] / num_rounds
    print(f"{name:<12} {data['total']:<12} {data['wins']:<12} {data['best']:<12} {promedio:<12.1f}")

print("-" * 65)
