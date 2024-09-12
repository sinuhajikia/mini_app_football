class SoccerLeague:
    def __init__(self):
        # Dictionary to store club data and match results
        self.clubs = {}
        self.matches = []

    # Menu 1: Input Data Klub
    def add_club(self, name, city):
        if name in self.clubs:
            return "Error: Klub sudah ada."
        if not name or not city:
            return "Error: Nama klub dan kota tidak boleh kosong."
        
        self.clubs[name] = {
            'name': name,
            'city': city,
            'played': 0,
            'win': 0,
            'draw': 0,
            'lose': 0,
            'goals_for': 0,
            'goals_against': 0,
            'points': 0
        }
        return f"Klub {name} dari {city} berhasil ditambahkan."

    # Menu 2: Input Skor Pertandingan
    def add_match(self, club1, score1, club2, score2):
        if club1 == club2:
            return "Error: Klub tidak boleh bertanding melawan diri sendiri."
        if club1 not in self.clubs or club2 not in self.clubs:
            return "Error: Salah satu atau kedua klub tidak terdaftar."
        if (club1, club2) in self.matches or (club2, club1) in self.matches:
            return "Error: Pertandingan sudah pernah diinput."
        
        self.matches.append((club1, club2))
        
        # Update game data for both clubs
        self.clubs[club1]['played'] += 1
        self.clubs[club2]['played'] += 1
        self.clubs[club1]['goals_for'] += score1
        self.clubs[club2]['goals_for'] += score2
        self.clubs[club1]['goals_against'] += score2
        self.clubs[club2]['goals_against'] += score1

        # Determine match outcome
        if score1 > score2:  # Club 1 wins
            self.clubs[club1]['win'] += 1
            self.clubs[club1]['points'] += 3
            self.clubs[club2]['lose'] += 1
        elif score1 < score2:  # Club 2 wins
            self.clubs[club2]['win'] += 1
            self.clubs[club2]['points'] += 3
            self.clubs[club1]['lose'] += 1
        else:  # Draw
            self.clubs[club1]['draw'] += 1
            self.clubs[club2]['draw'] += 1
            self.clubs[club1]['points'] += 1
            self.clubs[club2]['points'] += 1
        
        return f"Skor pertandingan antara {club1} dan {club2} berhasil ditambahkan."

    # Menu 3: Tampilan Klasemen
    def view_standings(self):
        # Sort clubs by points, goals difference, and goals for
        standings = sorted(self.clubs.values(), key=lambda x: (x['points'], x['goals_for'] - x['goals_against'], x['goals_for']), reverse=True)
        
        # Display standings
        print("No  Klub     Ma  Me  S  K  GM  GK  Point")
        for i, club in enumerate(standings, start=1):
            print(f"{i:<4}{club['name']:<10}{club['played']:<4}{club['win']:<4}{club['draw']:<4}{club['lose']:<4}{club['goals_for']:<4}{club['goals_against']:<4}{club['points']:<5}")

# Create a new league
league = SoccerLeague()

# Menu interaction example
while True:
    print("\nMenu:")
    print("1. Input Data Klub")
    print("2. Input Skor Pertandingan")
    print("3. Lihat Klasemen")
    print("4. Keluar")
    
    choice = input("Pilih menu: ")
    
    if choice == '1':
        name = input("Nama Klub: ")
        city = input("Kota Klub: ")
        print(league.add_club(name, city))
        
    elif choice == '2':
        club1 = input("Nama Klub 1: ")
        score1 = int(input("Skor Klub 1: "))
        club2 = input("Nama Klub 2: ")
        score2 = int(input("Skor Klub 2: "))
        print(league.add_match(club1, score1, club2, score2))
    
    elif choice == '3':
        league.view_standings()
    
    elif choice == '4':
        print("Keluar aplikasi.")
        break
    
    else:
        print("Pilihan tidak valid.")
