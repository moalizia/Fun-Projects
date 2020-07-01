def wave(x, y):
        if (y == 0) and (x == 0):
            print("    --    ")
            print("  --  --  ")
            print("00      --      --")
            print("          --  --")
            print("            --")
        elif (y == 0) and (x == 1):
            print("    --    ")
            print("  --  --  ")
            print("--      00      --")
            print("          --  --")
            print("            --")
        elif (y == 0) and (x == 2):
            print("    --    ")
            print("  --  --  ")
            print("--      --      00")
            print("          --  --")
            print("            --")
        elif (y > 0) and (x > 0) and (y < 1) and (x < 0.5):
            print("    --    ")
            print("  00  --  ")
            print("--      --      --")
            print("          --  --")
            print("            --")
        elif y == 1:
            print("    00    ")
            print("  --  --  ")
            print("--      --      --")
            print("          --  --")
            print("            --")
        elif y == -1:
            print("    --    ")
            print("  --  --  ")
            print("--      --      --")
            print("          --  --")
            print("            00")
        elif (y < 1) and (x > 0.5) and (y > 0) and (x < 1):
            print("    --    ")
            print("  --  00  ")
            print("--      --      --")
            print("          --  --")
            print("            --")
        elif (y > -1) and (x > 1) and (y < 0) and (x < 1.5):
            print("    --    ")
            print("  --  --  ")
            print("--      --      --")
            print("          00  --")
            print("            --")
        elif (y > -1) and (x < 2) and (y > -1) and (x > 1.5):
            print("    --    ")
            print("  --  --  ")
            print("--      --      --")
            print("          --  00")
            print("            --")

l = 5
inc = 0.5
while l == 5:
    y = 0
    x = 0
    while (y < 1) and (x < 0.5):
        wave(x, y)
        x = x + inc
        y = y + inc
    while (y == 0) and (x == 0.5):
        wave(x, y)
        x = x + inc
        y = y - inc
    while (y > -1) and (x < 1.5):
        wave(x, y)
        x = x + inc
        y = y - inc
    while (y < 0) and  (x < 2):
        wave(x, y)
        x = x + inc
        y = y + inc
    while (y == 1) and (x == 2):
        wave(x, y)
        x = x + inc
        y = y + inc
