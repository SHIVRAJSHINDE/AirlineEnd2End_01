from src.Components.Step_01_Cleaning import cleaning

if __name__ == "__main___":
    cleaningObj = cleaning()
    df = cleaningObj.readData()
    print(df)