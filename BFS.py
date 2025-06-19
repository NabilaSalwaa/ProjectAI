from collections import deque

romania_map = {
    'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
    'Zerind': ['Oradea', 'Arad'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

def bfs(start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in romania_map.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None

print("Daftar kota yang tersedia:")
print(", ".join(sorted(romania_map.keys())))
print()

start_city = input("Masukkan kota awal: ").strip().title()
goal_city = input("Masukkan kota tujuan: ").strip().title()

if start_city not in romania_map:
    print(f"Kota '{start_city}' tidak ditemukan dalam peta.")
elif goal_city not in romania_map:
    print(f"Kota '{goal_city}' tidak ditemukan dalam peta.")
else:
    result_path = bfs(start_city, goal_city)

    if result_path:
        print(f"\nJalur ditemukan dari {start_city} ke {goal_city}:")
        print(" -> ".join(result_path))
    else:
        print("Tidak ditemukan jalur dari {start_city} ke {goal_city}.")
