# Week 1.6, Session 1: Task 5

from dataset import QuakeDataset
from feed import QuakeFeed


pink = "\033[95m"
reset = "\033[0m"

print(f"{pink}Significance levels: all, 1.0, 2.5, 4.5, significant")
level = input("Choose a significance level: ").strip().lower()
print("Time periods: hour, day, week, month")
period = input("Choose a time period: ").strip().lower()

try:
	feed = QuakeFeed(level, period)
except ValueError as error:
	print(f"{pink}{error}{reset}")
	raise SystemExit(1)

dataset = QuakeDataset(feed)
dataset.read_feed()

print(f"\n{pink}{dataset}")
if len(dataset) == 0:
	print(f"No earthquake data was found.{reset}")
	raise SystemExit

strongest = dataset.strongest_quake()
print(f"Mean depth = {dataset.mean_depth():.2f} km")
print(f"Mean magnitude = {dataset.mean_magnitude():.1f}")
print(f"\nStrongest quake occurred at {strongest.when:%H:%M:%S} on {strongest.when:%Y-%m-%d}")
print(f"at {strongest.longitude:.1f}° longitude, {strongest.latitude:.1f}° latitude")
print(f"The depth was {strongest.depth:.1f} km")
print(f"The magnitude was {strongest.magnitude:.1f}{reset}")
