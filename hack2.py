class CropAndSoilManagementSystem:
    def __init__(self):
        self.crops = {
            "Wheat": {"soil_type": "Loamy", "climate": "Temperate"},
            "Rice": {"soil_type": "Clayey", "climate": "Tropical"},
            "Corn": {"soil_type": "Sandy", "climate": "Temperate"},
        }
        self.soil_health = {}
        self.diseases = {
            "Wheat": ["Rust", "Blight"],
            "Rice": ["Blast", "Brown Spot"],
            "Corn": ["Corn Smut", "Gray Leaf Spot"],
        }

    def crop_selection(self):
        soil_type = input("Enter your soil type (Loamy, Clayey, Sandy): ")
        climate = input("Enter your climate (Temperate, Tropical): ")

        suitable_crops = [
            crop for crop, attributes in self.crops.items()
            if attributes["soil_type"] == soil_type and attributes["climate"] == climate
        ]

        if suitable_crops:
            print("Suitable crops for your conditions:")
            for crop in suitable_crops:
                print(f"- {crop}")
        else:
            print("No suitable crops found for the given conditions.")

    def soil_management(self):
        soil_ph = float(input("Enter soil pH level: "))
        if soil_ph < 6.0:
            print("Consider adding lime to raise the pH.")
        elif soil_ph > 7.5:
            print("Consider adding sulfur to lower the pH.")
        else:
            print("Soil pH is optimal for most crops.")

    def disease_identification(self):
        crop = input("Enter the crop name (Wheat, Rice, Corn): ")
        if crop in self.diseases:
            print(f"Common diseases for {crop}:")
            for disease in self.diseases[crop]:
                print(f"- {disease}")
        else:
            print("No disease information available for this crop.")

    def main_menu(self):
        while True:
            print("\nCrop and Soil Management System")
            print("1. Crop Selection")
            print("2. Soil Management")
            print("3. Disease Identification")
            print("4. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                self.crop_selection()
            elif choice == '2':
                self.soil_management()
            elif choice == '3':
                self.disease_identification()
            elif choice == '4':
                print("Exiting the application.")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    system = CropAndSoilManagementSystem()
    system.main_menu()