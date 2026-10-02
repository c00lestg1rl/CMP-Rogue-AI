# ============================================================
# CMP 131 - ROGUE AI EMERGENCY DIAGNOSTIC SYSTEM
# Team members: Samantha and Nicole 
# ============================================================

print("========================================")
print("     ROGUE AI DIAGNOSTIC SYSTEM")
print("========================================")

# LEVEL 1 - TEMPERATURE DIAGNOSTIC
# Ask for the system temperature and make the required decision.
temp= float(input("enter temperature: "))
if(temp >= 100):
    print("WARNING: SYSTEM OVERHEATING")
else:
    print("Temperature Normal")


# LEVEL 2 - POWER DIAGNOSTIC
# Ask for the battery percentage and make the required decision.
battery= int(input(" enter battery percentage: "))
if(battery < 20):
    print("LOW POWER")
else: 
    print("Power Normal")

# LEVEL 3 - SECURITY DIAGNOSTIC
# Ask for the security status and make the required decision.
security= str(input("enter security status: "))
if(security == 'danger', 'DANGER', 'Danger'):
    print("SHUTDOWN REQUIRED")
else: 
    print("System Secure")


print("========================================")
print("Diagnostic complete.")
print("========================================")
