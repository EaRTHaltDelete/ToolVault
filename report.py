tools = [

    ["Hammer", "Hand Tools", 20, 10],
    ["Screwdriver Set", "Hand Tools", 15, 8],
    ["Adjustable Wrench", "Hand Tools", 12, 5],
    ["Combination Pliers", "Hand Tools", 10, 5],
    ["Pipe Wrench", "Hand Tools", 4, 6],
    ["Allen Key Set", "Hand Tools", 18, 10],

    ["Drill Machine", "Power Tools", 3, 5],
    ["Angle Grinder", "Power Tools", 6, 4],
    ["Circular Saw", "Power Tools", 2, 3],
    ["Impact Wrench", "Power Tools", 7, 5],
    ["Electric Screw Gun", "Power Tools", 5, 4],
    ["Heat Gun", "Power Tools", 8, 5],

    ["Nuts", "Fasteners", 40, 60],
    ["Bolts", "Fasteners", 120, 100],
    ["Washers", "Fasteners", 200, 150],
    ["Anchor Bolts", "Fasteners", 25, 40],
    ["Machine Screws", "Fasteners", 90, 80],

    ["Safety Gloves", "Safety Equipment", 14, 10],
    ["Safety Helmet", "Safety Equipment", 5, 8],
    ["Safety Goggles", "Safety Equipment", 9, 10],
    ["Ear Protection", "Safety Equipment", 6, 5],
    ["Reflective Jacket", "Safety Equipment", 3, 6],

    ["Digital Multimeter", "Electrical Tools", 4, 3],
    ["Wire Stripper", "Electrical Tools", 11, 5],
    ["Soldering Iron", "Electrical Tools", 7, 4],
    ["Insulation Tape", "Electrical Tools", 30, 20],
    ["Voltage Tester", "Electrical Tools", 2, 4],

    ["Vernier Caliper", "Measuring Tools", 5, 3],
    ["Micrometer", "Measuring Tools", 4, 2],
    ["Steel Scale", "Measuring Tools", 20, 10],
    ["Measuring Tape", "Measuring Tools", 13, 8],
    ["Dial Gauge", "Measuring Tools", 2, 3],

    ["Hydraulic Jack", "Lifting Equipment", 2, 2],
    ["Chain Pulley", "Lifting Equipment", 1, 2],
    ["Forklift Battery", "Lifting Equipment", 3, 2],

    ["Lubricating Oil", "Maintenance Supplies", 25, 15],
    ["Grease Gun", "Maintenance Supplies", 5, 3],
    ["Cleaning Brush", "Maintenance Supplies", 16, 10],
    ["Coolant Can", "Maintenance Supplies", 7, 5]

]

total_tools = len(tools)

sufficient = 0
low_stock = 0

for tool in tools:

    if tool[2] >= tool[3]:

        sufficient = sufficient + 1

    else:

        low_stock = low_stock + 1

print("\n===================================")
print(" INVENTORY REPORT ")
print("===================================")

print("Total Tools      :", total_tools)
print("Sufficient Stock :", sufficient)
print("Low Stock Items  :", low_stock)

print("\n========== CATEGORY LIST ==========")

for tool in tools:

    print(tool[0], "-", tool[1])