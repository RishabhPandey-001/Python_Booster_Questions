# 21.	Menu-Driven Converter:
# •	cm to feet
# •	km to miles
# •	USD to INR
# •	Exit

def cm_to_feet(cm):
    return cm / 30.48
def km_to_miles(km):
    return km * 0.621371
def USD_to_INR(USD):
    return USD* 84.51
def meter_to_cm(meter):
    return meter * 100
def millimeter_to_meter(millimeter):
    return millimeter * 0.001
def inch_to_meter(inch):
    return inch * 2.54 * 0.01
def mile_to_km(mile):
    return mile * 1.609344
def km_to_meter(km):
    return km * 1000 
def main():
    while True:
        print("\n----- Menu-Driven Converter -----")
        print("1. Convert cm to feet")
        print("2. Convert km to miles")
        print("3. Convert USD to INR")
        print("4. convert meter to cm")
        print("5. convert milli meter to meter")
        print("6. convert inch to meter")
        print("7. convert mile to km")
        print("8. convert km to meter")
        print("9. Exit")

        choice = input("Enter your choice: ")   
        
        if choice == '1':
            cm = float(input("Enter length in cm: "))
            feet = cm_to_feet(cm)
            print(f"{cm} cm = {feet:.2f} feet")

        elif choice == '2':
            km = float(input("Enter distance in km: "))
            miles = km_to_miles(km)
            print(f"{km} km = {miles:.2f} miles")

        elif choice == '3':
            usd = float(input("Enter amount in USD: "))
            inr = USD_to_INR(usd)
            print(f"${usd} USD = ₹{inr:.2f} INR")
        
        elif choice == '4':
            meter = float(input("Enter distance in meter: "))
            Centimeter = meter_to_cm(meter)
            print(f"{meter} m = {Centimeter:.2f} cm")

            
        elif choice == '5':
            Millimeter = float(input("Enter distance in Millimeter: "))
            Mmeter = millimeter_to_meter(Millimeter)
            print(f"{Millimeter} mm = {Mmeter:.2f} m")

        elif choice == '6':
            inch = float(input("Enter distance in inch: "))
            Imeter = inch_to_meter(inch)
            print(f"{inch} inch = {Imeter:.2f} m")  

        elif choice == '7':
            miles = float(input("Enter distance in miles: "))
            M_Km = mile_to_km(miles)
            print(f"{miles} miles = {M_Km:.2f} km")

        elif choice == '8':
            KM = float(input("Enter distance in km: "))
            k_m = km_to_meter(KM)
            print(f"{KM} inch = {k_m:.2f} m") 
              

        elif choice == '9':
            print("Exiting the converter. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 10.")

if __name__ == "__main__":
    main()    
