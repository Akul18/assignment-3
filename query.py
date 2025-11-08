import sqlite3

with sqlite3.connect('concrete.db') as conn:
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # 1. SHOW ALL TESTS
    print("ALL TESTS")
    cursor.execute("SELECT * FROM concrete_tests")
    while row := cursor.fetchone():
          row_dict = dict(row)
          pass_fail = "PASS" if row_dict['passed'] else "FAIL"
          print(f"{row_dict['project_name']}: {row_dict['actual_strength']} - {pass_fail}")

    # 2. Show ONLY failed tests
    print("\nFAILED TESTS")

    cursor.execute("SELECT * FROM concrete_tests WHERE passed = 0")
    while row := cursor.fetchone():
          row_dict = dict(row)
          print(f"{row_dict['project_name']} on {row_dict['test_date']} \n  Required: {row_dict['required_strength']} PSI\n  Actual: {row_dict['actual_strength']} PSI\n")


    # 3. Count tests by project
    print("\nTESTS PER PROJECT")
    cursor.execute("SELECT * FROM concrete_tests")
    output_passed = dict()
    output_total = dict()
    while row := cursor.fetchone():
          row_dict = dict(row)
          name = row_dict['project_name']
          if name not in output_total:
                output_passed[name] = 0
                output_total[name] = 0
          output_passed[name] += row_dict['passed']
          output_total[name] += 1

    for project in sorted(output_total.keys()):
          print(f"{project}: {output_passed[project]}/{output_total[project]} passed")
          
