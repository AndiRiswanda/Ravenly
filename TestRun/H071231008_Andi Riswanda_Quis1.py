intel = []
i = 0
while i < 100:
    intel.append(f"H071231{i:03}")
    i += 1
intel = tuple(intel)
print(intel)