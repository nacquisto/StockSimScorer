class AnalysisTypeSelection:
    def __init__(self):
        self.analysis_types = {
            1: "Technical Analysis",
            2: "Fundamental Analysis"
        }

    def show_options(self):
        print("\nAvailable Analysis Types:")
        for key, value in self.analysis_types.items():
            print(f"{key}. {value}")

    def select_analysis_type(self):
        user_choice = int(input("Enter the number corresponding to the analysis type you want to perform: "))
        selected_analysis_type = self.analysis_types[user_choice]
        return selected_analysis_type