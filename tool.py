tools = [

    ["Hammer"            ,"Hand Tools", 20, 10],
    ["Screwdriver Set"   , "Hand Tools", 15, 8],
    ["Adjustable Wrench" , "Hand Tools", 12, 5],
    ["Combination Pliers", "Hand Tools", 10, 5],
    ["Pipe Wrench"       , "Hand Tools", 4, 6],
    ["Allen Key Set"     , "Hand Tools", 18, 10],

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

while True:

    print("\n===================================")
    print(" TOOL MANAGEMENT ")
    print("===================================")

    print("1. Display Inventory")
    print("2. Add Tool")
    print("3. Update Quantity")
    print("4. Low Stock Report")
    print("5. Tool Search")
    print("6. Category Search")
    print("7. Delete Tool")
    print("8. Statistics Report")
    print("9. Exit")

    choice = input("Enter Choice: ")

    # DISPLAY INVENTORY

    if choice == "1":

        print("\n========== INVENTORY ==========")

        for tool in tools:

            if tool[2] >= tool[3]:

                status = "SUFFICIENT STOCK"

            else:

                status = "REORDER REQUIRED"

            print("\nTool Name :", tool[0])
            print("Category  :", tool[1])
            print("Available :", tool[2])
            print("Minimum   :", tool[3])
            print("Status    :", status)

    # ADD TOOL

    elif choice == "2":

        name = input("Enter Tool Name: ")

        category = input("Enter Category: ")

        quantity = int(input("Enter Quantity: "))

        minimum = int(input("Enter Minimum Quantity: "))

        tools.append([name, category, quantity, minimum])

        print("Tool Added Successfully!")

    # UPDATE QUANTITY

    elif choice == "3":

        search = input("Enter Tool Name: ")

        found = False

        for tool in tools:

            if tool[0].lower() == search.lower():

                found = True

                amount = int(input("Enter Quantity to Add: "))

                tool[2] = tool[2] + amount

                print("Quantity Updated")

        if found == False:

            print("Tool Not Found")

    # LOW STOCK REPORT

    elif choice == "4":

        print("\n========== LOW STOCK ==========")

        found = False

        for tool in tools:

            if tool[2] < tool[3]:

                found = True

                print("\nTool Name :", tool[0])
                print("Available :", tool[2])
                print("Minimum   :", tool[3])
                print("STATUS    : REORDER REQUIRED")

        if found == False:

            print("No Low Stock Items")

    # TOOL SEARCH

    elif choice == "5":

        search = input("Enter Tool Name: ")

        found = False

        for tool in tools:

            if tool[0].lower() == search.lower():

                found = True

                print("\nTool Name :", tool[0])
                print("Category  :", tool[1])
                print("Available :", tool[2])
                print("Minimum   :", tool[3])

        if found == False:

            print("Tool Not Found")

    # CATEGORY SEARCH

    elif choice == "6":

        category_search = input("Enter Category Name: ")

        found = False

        print("\n========== CATEGORY TOOLS ==========")

        for tool in tools:

            if tool[1].lower() == category_search.lower():

                found = True

                if tool[2] >= tool[3]:

                    status = "SUFFICIENT"

                else:

                    status = "LOW STOCK"

                print("\nTool Name :", tool[0])
                print("Available :", tool[2])
                print("Minimum   :", tool[3])
                print("Status    :", status)

        if found == False:

            print("No Tools Found In This Category")
    
    # DELETE TOOL

    elif choice == "7":
        delete_name = input("Enter Tool Name To Delete: ")

        found = False

        for tool in tools:

            if tool[0].lower() == delete_name.lower():

                tools.remove(tool)

                found = True

                print("Tool Deleted Successfully")

                break

        if found == False:

            print("Tool Not Found")
        
        break

    # STATISTICS DASHBOARD

    elif choice == "8":

        total_tools = len(tools)

        low_stock = 0
        sufficient = 0
        

        for tool in tools:

            # STOCK STATUS

            if tool[2] >= tool[3]:

                sufficient += 1

            else:

                low_stock += 1

            

        print("\n===================================")
        print(" INVENTORY STATISTICS DASHBOARD ")
        print("===================================")

        print("Total Tools          :", total_tools)
        print("Sufficient Stock     :", sufficient)
        print("Low Stock Items      :", low_stock)
        

    # EXIT
    elif choice == "9":

        print("Exiting Tool Management")

        break

    else:

        print("Invalid Choice")