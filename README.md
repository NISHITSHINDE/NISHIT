Last login: Wed Aug 19 22:09:12 on ttys000
nishitshinde@NISHIT ~ % mkdir smart_cache_prototype
cd smart_cache_prototype
nishithinde@NISHIT smart_cache_prototype % cat << 'EOF' > prototype.py
import time

# 1. The Big Toy Closet (Main Database)
database = {
    "toy_car": "Red Race Car Data",
    "blocks": "Lego Set Data",
    "puzzle": "100-piece Puzzle Data"
}

# 2. The Quick Toy Desk (Redis Cache)
cache = {}
toy_popularity = {}
database_cost_saved = 0.0

def get_toy(toy_name):
    global database_cost_saved

def clean_desk():
    # Dynamic TTL Engine: Throw away cold toys nobody asks for
    for toy, count in list(toy_popularity.items()):
        if count < 2:
            print(f"--> EVICTING: Throwing '{toy}' off the desk because it's cold.")
            cache.pop(toy, None)

# --- SIMULATION --- #
print("\n=== REQUEST 1: Asking for toy_car ===")
get_toy("toy_car")

print("\n=== REQUEST 2: Asking for toy_car again! ===")
get_toy("toy_car")

print("\n=== CLEANING DESK ===")
clean_desk()

print(f"\n=== LIVE SCOREBOARD ===")
print(f"Database Cost Savings ($): ${database_cost_saved:.2f}")
print(f"Toys remaining on Quick Desk: {list(cache.keys())}")
EOF
nishitshinde@NISHIT smart_cache_prototype % 
nishitshinde@NISHIT smart_cache_prototype % python3 prototype.py

THE SOLUTION STARTS FROM HERE:-

=== REQUEST 1: Asking for toy_car ===
--> MISS! Running to basement closet for 'toy_car'...

=== REQUEST 2: Asking for toy_car again! ===
--> QUICK DESK HIT! Handed over 'toy_car' instantly.

=== CLEANING DESK ===

=== LIVE SCOREBOARD ===
Database Cost Savings ($): $0.05
Toys remaining on Quick Desk: ['toy_car']
                  
