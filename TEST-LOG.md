# Rogue AI Test Log

## Team Information

- Team name:
- Team members: Samantha and Nicole
- Driver:
- Logic Checker:
- Test Engineer:
- Reporter:

## Required Boundary Predictions

Complete these predictions before running the program.

| Test | Temperature | Battery | Security | Predicted messages | Actual messages | Match? |
|---|---:|---:|---|---|---|---|
| A | 99 | 19 | safe |  |  |  |
| B | 100 | 20 | danger |  |  |  |
| C | 101 | 21 | DANGER |  |  |  |

## AI-Assisted Tests

Ask the course AI assistant for one test at a time. Predict before running.

| Test | Temperature | Battery | Security | Team prediction | Actual result | What we learned |
|---|---:|---:|---|---|---|---|
| 1 | 100 | 19 | danger | WARNING:SYSTEM OVERHEAT, LOW POWER, SHUTDOWN REQUIRED | same as predicted  |  |
| 2 |  99| 20  | safe | Temperature Normal, Power Normal, System Safe | same as predicted  |  |
| 3 |  101| 21  | DANGER | WARNING: SYSTEM OVERHEATING, Power Normal, SHUTDOWN REQUIRED | WARNING: SYSTEM OVERHEATING, Power Normal, System Secure  | we learned that you should include variations of spelling in the requirements with alphabetical options|

## Random AI Safety Scenario

- Random temperature: 100
- Random battery: 19
- Random security status: danger
- Copilot's simulated program results:  WARNING:SYSTEM OVERHEAT, LOW POWER, SHUTDOWN REQUIRED
- Did the logic pass this scenario? Yes
- Temperature safety advice: N/A
- Power safety advice: N/A
- Privacy/security advice: N/A
- Funny scenario message:
- What we learned:

## Instructor Mystery Test

- Temperature:
- Battery:
- Security:
- Our prediction:
- Actual result:
- Did it match? Explain:

## Debugging Record

- What did not work or almost caused a problem? Most of our program worked except for variations in the spelling for 'danger' in the level 3 Program. 
- What hint did the instructor or AI assistant provide? The hint given to us was that 'danger' and 'DANGER' are not equal.
- What change did the team make? we wrote in two versions fo the word 'danger' so that the result would work in both scenarios 
- Why did that change work? It included both versions of the word 'danger' that might pop up 
