from decimal import *  #@UnusedWildImport
#^ MUST be included in py2exe!
import linecache  # Named "readline" in .exe source as py2exe failed to recognize module "linecache"
import sys
import time

from prettytable import PrettyTable #@UnresolvedImport


getcontext().prec = 50

print("PyMUN - Turn-based National Finance Simulator/Calculator - Version 2.35" '\n' "+- written by MusicTheorist" '\n')

day = 1440 #in minutes
week = day * 7
fortnight = week * 2
month = day * 30
halfYear = month * 6
year = halfYear * 2
biennium = year * 2
triennium = year * 3
olympiad = year * 4 + day
lustrum = olympiad + year
decade = lustrum * 2
score = decade * 2
halfCentury = decade * 5
century = halfCentury * 2
halfMillennium = century * 5
millennium = halfMillennium * 2

def initVar(x):
    try:
        x = Decimal(x)
    except InvalidOperation:
        try:
            x = Decimal(''.join(s for s in x if s.isdigit()))
            print('\n' "Oops! Looks like you entered in something other than a number. Don't worry, any number you typed in was accepted..." '\n' '\n' "Your value will be: %d" % x)
        except InvalidOperation:
            x = initVar(input('\n' "Couldn't understand what you typed in, try again? "))
    return x

def ifCategory(category, categorySelection, setTime):
    if categorySelection == 0.0:
        print('\n' "We haven't figured out the cost of your nation's %s." % category)
    else:
        timeString(setTime)
        print('\n' "The current cost of your nation's %s is $%s per %s." % (category, "{:,.2f}".format(categorySelection), timeDisplay))
        return
        
def setCost(categorySelection, category):
    ifSubchoice = True

    ifCategory(category, categorySelection, setTime)
    
    while True:
        if ifSubchoice == True:
            setCost = input("How much would %s cost in your nation every period? " % category)
        else:
            pass
        if not setCost:
            ifSubchoice = switch(ifSubchoice)
            setCost = input('\n' "Nothing was inputted. ")
        else:
            setCost = initVar(setCost)
            ifSubchoice = True
            break
        
    timeString(setTime)
    print('\n' "The nation's %s now cost $%s per %s." % (category, "{:,.2f}".format(setCost), timeDisplay))
    return setCost

def passTime(category, categorySelection):
    ifSubchoice = True
    
    ifCategory(category, categorySelection, setTime)

    while True:
        if ifSubchoice == True:
            timeOrPeriods = input("Would you like to calculate (T) in terms of a specific amount of time" '\n' "(in minute(s)) or (P) in terms of the amount of periods that have passed? Choose T or P: ").lower()
        else:
            pass

        if timeOrPeriods == "t":
            print('\n')
            timeTable()
            setPassedTime = initVar((input('\n' "Enter the desired amount of time in minute(s) that has gone by: ")))
            currentCost = Decimal((float(setPassedTime) / float(setTime)) * float(categorySelection))

            if currentCost < 0.005:
                print('\n' "The calculated cost is little to none.")
            else:
                timeString(setPassedTime)
                print('\n' "After %s, the cost of the nation's %s would add up to $%s at the current rate." % (otherTimeDisplay.lower(), category, "{:,.2f}".format(currentCost)))
            break
        
        elif timeOrPeriods == "p":
            timeString(setTime)
            setPassedPeriod = initVar((input('\n' "Enter the amount of intervals of time (1 interval = %s)" '\n' "that have gone by: " % timeDisplay)))
            currentCost = Decimal(float(setPassedPeriod) * float(categorySelection))

            if currentCost < 0.005:
                print('\n' "The calculated cost is little to none.")
            else:
                timeString(setTime * setPassedPeriod)
                print('\n' "After %s period(s) have passed, the cost of the nation's %s would add up to $%s at the current rate." % (format(setPassedPeriod, ","), category, "{:,.2f}".format(currentCost)))
            break
        
        elif not timeOrPeriods:
            ifSubchoice = switch(ifSubchoice)
            timeOrPeriods = input('\n' "Nothing was inputted. ")
        else:
            ifSubchoice = switch(ifSubchoice)
            timeOrPeriods = input('\n' "Not a valid choice! ")

def basicMath(costAccumulation, category):
    print('\n' "The total cost accumulated for the nation's %s is %s." % (category, "{:,.2f}".format(costAccumulation)))

    while True:
        mathInput = initVar(input('\n' "To add, enter in a positive number. To subtract, enter in a negative number: "))

        if costAccumulation + mathInput < 0:
            costAccumulation = 0
            break
        else:
            costAccumulation = costAccumulation + mathInput
            break

    print('\n' "The total cost accumulated for the nation's %s is now %s." % (category, "{:,.2f}".format(costAccumulation)))
    return costAccumulation

def calculatePeriods(time, category, redo):
    if redo == False:
        return Decimal((time / float(setTime)) * float(category))
    else:
        return Decimal((float(setTime) / float(time)) * float(category))

def timeString(timeInput): #Could've been a dictionary...
    global timeDisplay, otherTimeDisplay
    
    if timeInput == millennium:
            timeDisplay = "millennium"
            otherTimeDisplay = "A MILLENNIUM"
    elif timeInput == halfMillennium:
            timeDisplay = "500 years"
            otherTimeDisplay = "500 YEARS"
    elif timeInput == century:
            timeDisplay = "century"
            otherTimeDisplay = "A CENTURY"
    elif timeInput == halfCentury:
            timeDisplay = "50 years"
            otherTimeDisplay = "50 YEARS"
    elif timeInput == score:
            timeDisplay = "20 years"
            otherTimeDisplay = "20 YEARS"
    elif timeInput == decade:
            timeDisplay = "10 years"
            otherTimeDisplay = "10 YEARS"
    elif timeInput == lustrum:
            timeDisplay = "5 years"
            otherTimeDisplay = "5 YEARS"
    elif timeInput == olympiad:
            timeDisplay = "4 years"
            otherTimeDisplay = "4 YEARS"
    elif timeInput == triennium:
            timeDisplay = "3 years"
            otherTimeDisplay = "3 YEARS"
    elif timeInput == biennium:
            timeDisplay = "2 years"
            otherTimeDisplay = "2 YEARS"
    elif timeInput == year:
            timeDisplay = "year"
            otherTimeDisplay = "A YEAR"
    elif timeInput == halfYear:
            timeDisplay = "6 months"
            otherTimeDisplay = "6 MONTHS"
    elif timeInput == month:
            timeDisplay = "month"
            otherTimeDisplay = "A MONTH"
    elif timeInput == fortnight:
            timeDisplay = "2 weeks"
            otherTimeDisplay = "2 WEEKS"
    elif timeInput == week:
            timeDisplay = "week"
            otherTimeDisplay = "A WEEK"
    elif timeInput == day:
            timeDisplay = "day"
            otherTimeDisplay = "A DAY"
    else:
            timeDisplay = format(timeInput, ",") + " minute(s)"
            otherTimeDisplay = format(timeInput, ",") + " MINUTE(S)"

def accumulationTable(category, categorySelection):
    timeString(setTime)
    print('\n' "At the current cost of $%s per %s for the nation's %s," '\n' "it will cost approximately:" % ("{:,.2f}".format(categorySelection), timeDisplay, category))
    
    p = PrettyTable(["Common Intervals of Time", "Cost per Interval (in Dollars)"])
    p.align["Common Intervals of Time"] = "l"
    p.padding_width = 2
    p.add_row(["Day", "{:,.2f}".format(calculatePeriods(day, categorySelection, False))])
    p.add_row(["Week", "{:,.2f}".format(calculatePeriods(week, categorySelection, False))])
    p.add_row(["2 Weeks", "{:,.2f}".format(calculatePeriods(fortnight, categorySelection, False))])
    p.add_row(["Month", "{:,.2f}".format(calculatePeriods(month, categorySelection, False))])
    p.add_row(["6 Months", "{:,.2f}".format(calculatePeriods(halfYear, categorySelection, False))])
    p.add_row(["Year", "{:,.2f}".format(calculatePeriods(year, categorySelection, False))])
    p.add_row(["2 Years", "{:,.2f}".format(calculatePeriods(biennium, categorySelection, False))])
    p.add_row(["3 Years", "{:,.2f}".format(calculatePeriods(triennium, categorySelection, False))])
    p.add_row(["4 Years", "{:,.2f}".format(calculatePeriods(olympiad, categorySelection, False))])
    p.add_row(["5 Years", "{:,.2f}".format(calculatePeriods(lustrum, categorySelection, False))])
    p.add_row(["Decade", "{:,.2f}".format(calculatePeriods(decade, categorySelection, False))])
    p.add_row(["20 Years", "{:,.2f}".format(calculatePeriods(score, categorySelection, False))])
    p.add_row(["50 Years", "{:,.2f}".format(calculatePeriods(halfCentury, categorySelection, False))])
    p.add_row(["Century", "{:,.2f}".format(calculatePeriods(century, categorySelection, False))])
    p.add_row(["500 Years", "{:,.2f}".format(calculatePeriods(halfMillennium, categorySelection, False))])
    p.add_row(["Millennium", "{:,.2f}".format(calculatePeriods(millennium, categorySelection, False))])
    print(p)

def lineCache(i):
    return Decimal(linecache.getline("variables_save.pmt", int(i)))

def timeSetting():
    goAhead = False
    
    timeTable()

    while goAhead == False:
            while True:
                timeEntry = (input('\n' "Either type in a period of time from the table or enter in a specific number of minute(s): ").lower()).replace(" ", "")

                if timeEntry.isalnum():
                    break
                else:
                    print('\n' "Only letters and numbers are accepted!")
                    pass

            while True:
                if not timeEntry:
                    print('\n' "Nothing was inputted.")
                elif not timeEntry.isdigit():
                    if timeEntry == "day":
                        setTime = day
                        goAhead = True
                        break
                    elif timeEntry == "week":
                        setTime = week
                        goAhead = True
                        break
                    elif timeEntry == "month":
                        setTime = month
                        goAhead = True
                        break
                    elif timeEntry == "year":
                        setTime = year
                        goAhead = True
                        break
                    elif timeEntry == "decade":
                        setTime = decade
                        goAhead = True
                        break
                    elif timeEntry == "century":
                        setTime = century
                        goAhead = True
                        break
                    elif timeEntry == "2weeks":
                        setTime = fortnight
                        goAhead = True
                        break
                    elif timeEntry == "6months":
                        setTime = halfYear
                        goAhead = True
                        break
                    elif timeEntry == "5years":
                        setTime = lustrum
                        goAhead = True
                        break
                    elif timeEntry == "millennium":
                        setTime = millennium
                        goAhead = True
                        break
                    elif timeEntry == "2years":
                        setTime = biennium
                        goAhead = True
                        break
                    elif timeEntry == "3years":
                        setTime = triennium
                        goAhead = True
                        break
                    elif timeEntry == "4years":
                        setTime = olympiad
                        goAhead = True
                        break
                    elif timeEntry == "20years":
                        setTime = score
                        goAhead = True
                        break
                    elif timeEntry == "50years":
                        setTime = halfCentury
                        goAhead = True
                        break
                    elif timeEntry == "500years":
                        setTime = halfMillennium
                        goAhead = True
                        break
                    else:
                        print('\n' "Couldn't understand what you typed in.")
                        break
                else:
                    setTime = initVar(timeEntry)
                    goAhead = True
                    break
    return setTime

def writeContents():
    print('\n' "Saving...")
    file = open("variables_save.pmt", 'w')
    file.write("%f" '\n' "%f" '\n' "%f" '\n' "%f" '\n' "%f" '\n' "%f" '\n' "%f" '\n' "%f" '\n' "%f" '\n' "%d" '\n'  % (military, economy, education, religion, militaryTotal, economyTotal, educationTotal, religionTotal, setTime, intervalAccumulation));
    file.close()
    print('\n' "Saved!")

def sumTable():
    c = PrettyTable(["Institution", "Periodic Cost (Dollars)", "Total Cost Accumulated (Dollars)"])
    c.align["Institution"] = "l"
    c.padding_width = 1
    c.add_row(["Military", "{:,.2f}".format(military), "{:,.2f}".format(militaryTotal)])
    c.add_row(["Economy", "{:,.2f}".format(economy), "{:,.2f}".format(economyTotal)])
    c.add_row(["Education", "{:,.2f}".format(education), "{:,.2f}".format(educationTotal)])
    c.add_row(["Religion", "{:,.2f}".format(religion), "{:,.2f}".format(religionTotal)])
    print(c)

def timeTable():
    d = PrettyTable(["Common Intervals of Time", "Minutes"])
    d.align["Common Intervals of Time"] = "l"
    d.padding_width = 2
    d.add_row(["Day", "{:,}".format(day)])
    d.add_row(["Week", "{:,}".format(week)])
    d.add_row(["2 Weeks", "{:,}".format(fortnight)])
    d.add_row(["Month", "{:,}".format(month)])
    d.add_row(["6 Months", "{:,}".format(halfYear)])
    d.add_row(["Year", "{:,}".format(year)])
    d.add_row(["2 Years", "{:,}".format(biennium)])
    d.add_row(["3 Years", "{:,}".format(triennium)])
    d.add_row(["4 Years", "{:,}".format(olympiad)])
    d.add_row(["5 Years", "{:,}".format(lustrum)])
    d.add_row(["Decade", "{:,}".format(decade)])
    d.add_row(["20 Years", "{:,}".format(score)])
    d.add_row(["50 Years", "{:,}".format(halfCentury)])
    d.add_row(["Century", "{:,}".format(century)])
    d.add_row(["500 Years", "{:,}".format(halfMillennium)])
    d.add_row(["Millennium", "{:,}".format(millennium)])
    print(d)

def switch(Bool):
    if Bool == True:
        return False
    else:
        pass

def defineVariables(): #Probable dictionary?
    global military, economy, education, religion, militaryTotal, economyTotal, educationTotal, religionTotal, setTime, categorySelection, intervalAccumulation, nextPeriodBoolean, ifChoice
    
    military = 0.0
    economy = 0.0
    education = 0.0
    religion = 0.0

    militaryTotal = 0
    economyTotal = 0
    educationTotal = 0
    religionTotal = 0

    setTime = 0.0
    intervalAccumulation = 0
    nextPeriodBoolean = True
    ifChoice = True
    
def endOfTurn(turnTable, turnsLeft, howMany):
    global militaryTotal, economyTotal, educationTotal, religionTotal, intervalAccumulation, ifChoice

    intervalAccumulation = intervalAccumulation + 1
    militaryTotal = Decimal(militaryTotal) + Decimal(military)
    economyTotal = Decimal(economyTotal) + Decimal(economy)
    religionTotal = Decimal(religionTotal) + Decimal(religion)
    educationTotal = Decimal(educationTotal) + Decimal(education)

    ifChoice = True
    
    if turnTable == False:
        timeString(setTime)
        print('\n' "+- AFTER %s... -+" '\n' % otherTimeDisplay)
        sumTable()
        time.sleep(10)
    elif turnTable == True:
        if turnsLeft == False:
            print('\n' "+- AFTER %s TURNS... -+" '\n' % howMany)
            sumTable()
            time.sleep(10)
        else:
            pass

defineVariables()

print("You will able to use this program to simulate the finances of a nation." '\n' '\n' "How frequently would you like to calculate how much your country's resources" '\n' "would cost?" '\n' '\n' "Monetary values will be rounded down to 2 decimal places." '\n')

setTime = timeSetting()

print('\n' "Now let's set up the cost of your nation's institutions.")

military = setCost(military, "armed forces")
economy = setCost(economy, "finances")
education = setCost(education, "schools")
religion = setCost(religion, "religions")

print('\n' "---" '\n' '\n' "Welcome to the simulation!" '\n' '\n' "After a single action, a period of time will have passed, however you can change" '\n' "that in the simulation's settings.")

while True:
    isTimeSkip = True
    ifSubchoice = True
    
    if ifChoice == True:
        choice = input('\n' "What would you like to do? You can:" '\n' '\n' "1.) Set the cost of a nation's institution" '\n' "2.) Calculate the cost of an institution over a specified amount of time" '\n' "3.) Manually add or subtract money from an institution" '\n' "4.) View table of nation's costs" '\n' "5.) Observe costs at common periods of time" '\n'  "6.) Save prices to use later" '\n' "7.) Load prices from previous save" '\n' "8.) Edit the simulation's settings" '\n' "9.) Manually skip forward to the next cost report (Do nothing)" '\n' "0.) Exit the program"  '\n' '\n' "Which action would you like to do? ").lower()
    else:
        pass
    
    if choice == "1":
        while True:
            if ifSubchoice == True:
                secondChoiceOne = input('\n' "Which category would you like to modify?" '\n' '\n' "1.) Military" '\n' "2.) Economy" '\n' "3.) Education" '\n' "4.) Religion" '\n' '\n' "Category: ")
            else:
                pass
            
            if secondChoiceOne == "1":
                military = setCost(military, "armed forces")
                ifSubchoice = True
                break
            elif secondChoiceOne == "2":
                economy = setCost(economy, "finances")
                ifSubchoice = True
                break
            elif secondChoiceOne == "3":
                education = setCost(education, "schools")
                ifSubchoice = True
                break
            elif secondChoiceOne == "4":
                religion = setCost(religion, "religions")
                ifSubchoice = True
                break
            else:
                ifSubchoice = switch(ifSubchoice)
                secondChoiceOne = input('\n' "Invalid choice! ")

    elif choice == "2":
        while True:
            if ifSubchoice == True:
                secondChoiceTwo = input('\n' "Which category would you like to use?" '\n' '\n' "1.) Military" '\n' "2.) Economy" '\n' "3.) Education" '\n' "4.) Religion" '\n' '\n' "Category: ")
            else:
                pass
            
            if secondChoiceTwo == "1":
                passTime("armed forces", military)
                ifSubchoice = True
                break
            elif secondChoiceTwo == "2":
                passTime("finances", economy)
                ifSubchoice = True
                break
            elif secondChoiceTwo == "3":
                passTime("schools", education)
                ifSubchoice = True
                break
            elif secondChoiceTwo == "4":
                passTime("religions", religion)
                ifSubchoice = True
                break
            else:
                ifSubchoice = switch(ifSubchoice)
                secondChoiceTwo = input('\n' "Invalid choice! ")

    elif choice == "3":
        while True:
            if ifSubchoice == True:
                secondChoiceThree = input('\n' "Which category would you like to modify?" '\n' '\n' "1.) Military" '\n' "2.) Economy" '\n' "3.) Education" '\n' "4.) Religion" '\n' '\n' "Category: ")
            else:
                pass
            
            if secondChoiceThree == "1":
                militaryTotal = basicMath(militaryTotal, "armed forces")
                ifSubchoice = True
                break
            elif secondChoiceThree == "2":
                economyTotal = basicMath(economyTotal, "finances")
                ifSubchoice = True
                break
            elif secondChoiceThree == "3":
                educationTotal = basicMath(educationTotal, "schools")
                ifSubchoice = True
                break
            elif secondChoiceThree == "4":
                religionTotal = basicMath(religionTotal, "religions")
                ifSubchoice = True
                break
            else:
                ifSubchoice = switch(ifSubchoice)
                secondChoiceThree = input('\n' "Invalid choice! ")

    elif choice == "4":
        print('\n' "After %s period(s) (each being %s minute(s))..." '\n' % (format(intervalAccumulation, ","), format(setTime, ","))) 
        sumTable()
        time.sleep(10)
        
    elif choice == "5":
        while True:
            if ifSubchoice == True:
                secondChoiceFour = input('\n' "Which category would you like to use?" '\n' '\n' "1.) Military" '\n' "2.) Economy" '\n' "3.) Education" '\n' "4.) Religion" '\n' '\n' "Category: ")
            else:
                pass

            if secondChoiceFour == "1":
                accumulationTable("armed forces", military)
                ifSubchoice = True
                break
            elif secondChoiceFour == "2":
                accumulationTable("finances", economy)
                ifSubchoice = True
                break
            elif secondChoiceFour == "3":
                accumulationTable("schools", education)
                ifSubchoice = True
                break
            elif secondChoiceFour == "4":
                accumulationTable("religions", religion)
                ifSubchoice = True
                break
            else:
                ifSubchoice = switch(ifSubchoice)
                secondChoiceFour = input('\n' "Invalid choice! ")

    elif choice == "6":
        while True:
            if ifSubchoice == True:
                secondChoiceFive = input('\n' "WARNING: This will overwrite your nation's previous statistics. Are you sure you want to continue (Y/N)? ").lower()
            else:
                pass
            
            if secondChoiceFive == "y":
                writeContents()
                ifSubchoice = True
                break
            elif secondChoiceFive == "n":
                isTimeSkip = False
                ifSubchoice = True
                break
            else:
                ifSubchoice = switch(ifSubchoice)
                secondChoiceFive = input('\n' "Invalid choice! ")
            
    elif choice == "7":
        while True:
            if ifSubchoice == True:
                secondChoiceSix = input('\n' "WARNING: This will overwrite your nation's current statistics. Are you sure you want to continue (Y/N)? ").lower()
            else:
                pass

            if secondChoiceSix == "y":
                print('\n' "Loading...")

                military = Decimal(lineCache(1))
                economy = Decimal(lineCache(2))
                education = Decimal(lineCache(3))
                religion = Decimal(lineCache(4))

                militaryTotal = Decimal(lineCache(5))
                economyTotal = Decimal(lineCache(6))
                educationTotal = Decimal(lineCache(7))
                religionTotal = Decimal(lineCache(8))

                setTime = lineCache(9)
                intervalAccumulation = int(lineCache(10))

                print('\n' "Loaded!")
                ifSubchoice = True
                break
            elif secondChoiceSix == "n":
                isTimeSkip = False
                ifSubchoice = True
                break
            else:
                ifSubchoice = switch(ifSubchoice)
                secondChoiceSix = input('\n' "Invalid choice! ")

    elif choice == "8":
        while True:
            if ifSubchoice == True:
                secondChoiceSeven = input('\n' "Select which setting to modify:" '\n' "1.) Modify rate of calculating costs" '\n' "2.) Automatically skip to next period of time after action (Only way to" '\n' "accumulate costs is manually choose Do Nothing)" '\n' "3.) Reset simulation" '\n' "Or 4.) Exit settings" '\n').lower()
            else:
                pass
            
            if secondChoiceSeven == "1":
                print('\n')
                previousTime = setTime
                setTime = timeSetting()

                military = calculatePeriods(previousTime, military, True)
                economy = calculatePeriods(previousTime, economy, True)
                education = calculatePeriods(previousTime, education, True)
                religion = calculatePeriods(previousTime, religion, True)
                
                ifSubchoice = True
            elif secondChoiceSeven == "2":
                ifSubchoice = True
                
                while True:
                    if ifSubchoice == True:
                        thirdChoiceOne = input('\n' "Currently, the simulation automatically adding costs after each action is %s (The default setting is True)." '\n' "Would you like to change that (Y/N)? " % nextPeriodBoolean).lower()
                    else:
                        pass

                    if thirdChoiceOne == "y":
                        nextPeriodBoolean = not nextPeriodBoolean
                        ifSubchoice = True
                        break
                    elif thirdChoiceOne == "n":
                        ifSubchoice = True
                        break
                    else:
                        ifSubchoice = switch(ifSubchoice)
                        thirdChoiceOne = input('\n' "Not a valid choice! ")
            elif secondChoiceSeven == "3":
                ifSubchoice = True

                while True:
                    thirdChoiceTwo = input('\n' "ARE YOU SURE (Y/N)? ").lower()
                    if thirdChoiceTwo == "y":
                        print('\n' "Simulation RESET" '\n')

                        defineVariables()
                        setTime = timeSetting()

                        military = setCost(military, "armed forces")
                        economy = setCost(economy, "finances")
                        education = setCost(education, "schools")
                        religion = setCost(religion, "religions")
                        
                        ifSubchoice = True
                        break
                    elif thirdChoiceTwo == "n":
                        ifSubchoice = True
                        break
                    else:
                        ifSubchoice = switch(ifSubchoice)
                        thirdChoiceTwo = input('\n' "Not a valid choice! ")
            elif secondChoiceSeven == "4":
                ifSubchoice = True
                break
            else:
                ifSubchoice = switch(ifSubchoice)
                secondChoiceSeven = input('\n' "Not a valid choice! ")

    elif choice == "9":
        continuation = False
        
        while continuation == False:
            if ifSubchoice == True:
                secondChoiceEight = input('\n' "Would you like to skip multiple turns (Y/N)? ").lower()
            else:
                pass
            
            if secondChoiceEight == "y":
                while True:
                    thirdChoiceThree = int(initVar(input(('\n' "How many turns would you like to skip? You can skip up to 100 at a time. "))))

                    if thirdChoiceThree > 100:
                        thirdChoiceThree = 100
                    else:
                        pass
                    
                    for i in range(thirdChoiceThree):
                        endOfTurn(True, True, 0)

                    endOfTurn(True, False, thirdChoiceThree)
                    
                    isTimeSkip = False
                    continuation = True
                    break
            elif secondChoiceEight == "n":        
                isTimeSkip = False
                continuation = True
                endOfTurn(False, True, 0)
                break
            else:
                ifSubchoice = switch(ifSubchoice)
                secondChoiceEight = input('\n' "Invalid choice! ")

    elif choice == "0":
        while True:
            if ifSubchoice == True:
                secondChoiceNine = input('\n' "ARE YOU SURE (Y/N)? ").lower()
            else:
                pass

            if secondChoiceNine == "y":
                ifSubchoice = True
                
                while True:
                    if ifSubchoice == True:
                        thirdChoiceFour = input('\n' "Would you like to save your progress (Y/N)? WARNING: This will overwrite your" '\n' "nation's previous statistics. ").lower()
                    else:
                        pass
                    
                    if thirdChoiceFour == "y":
                        writeContents()
                        time.sleep(3)
                        
                        print('\n' "End of simulation!")

                        time.sleep(5)
                        sys.exit()
                    elif thirdChoiceFour == "n":
                        print('\n' "End of simulation!")
                        time.sleep(5)
                        sys.exit()
                    else:
                        ifSubchoice = switch(ifSubchoice)
                        thirdChoiceFour = input('\n' "Invalid choice! ") 
            elif secondChoiceNine == "n":
                isTimeSkip = False
                ifSubchoice = True
                break
            else:
                ifSubchoice = switch(ifSubchoice)
                secondChoiceNine = input('\n' "Invalid choice! ")
                
    elif not choice:
        choice = input('\n' "Nothing was inputted. ")
        isTimeSkip = False
        ifChoice = switch(ifChoice)
        
    else:
        choice = input('\n' "Please choose a number 0-9. ")
        isTimeSkip = False
        ifChoice = switch(ifChoice)
        
    if isTimeSkip == True and nextPeriodBoolean == True:
        endOfTurn(False, True, 0)
    else:
        pass
