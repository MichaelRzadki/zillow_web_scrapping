from platform import architecture
import pandas as pd

df = pd.read_csv ('for_sale_data.csv',  encoding='utf-8')

#Clean Home Type
df['Home Type'] = df['Home Type'].str.strip('(')
df['Home Type'] = df['Home Type'].str.strip(')')
df['Home Type'] = df['Home Type'].str.strip("'")
df['Home Type'] = df['Home Type'].str.strip(',')
df['Home Type'] = df['Home Type'].str.strip("'")
df['Home Type'] = df['Home Type'].str.replace(" for sale",'')
df['Home Type'] = df['Home Type'].str.strip()



# Get Bedroom and bathroom stats
bedrooms = df['Rooms'].str.split(' ', expand= True)[0]
bathrooms = df['Rooms'].str[5]

df['Bedrooms'] = bedrooms
df['Bathrooms'] = bathrooms

# Clean Name Column to only get the Street Address
df['Name'] = df['Name'].str.split(',', expand= True)[0]

# Clean Floorsize to only contain integers
df['Floorsize'] = df['Floorsize'].str.replace(',','')

##### Split up Website Traffic Data into multiple Columns #####
# User Views
user_views = df['Website Traffic'].str.split('|', expand= True)[1]
user_views = user_views.str.strip('views')
user_views = user_views.str.replace(',', '')
df['User Views'] = user_views

#User Saves
user_saves = df['Website Traffic'].str.split('|', expand= True)[2]
user_saves = user_saves.str.strip('saves')
user_saves = user_saves.str.replace(',', '')
df['User Saves'] = user_saves
##### End of Split up Website Traffic Data into multiple Columns #####

#Clean the Price Column
df['Price'] = df['Price'].str.replace(',','')
df['Price'] = df['Price'].str.replace('$','')

#Get Additional Column Headers using Data from Bulding Stats Column
for index, row in df.iterrows():

    if row['Building Stats'] == '[]':
        continue
    building_stats = row['Building Stats'].split("\',")

    #Get Number of Days on Website
    if "dayson" in df.at[index,"Website Traffic"]:
        df.at[index,"Days on Website"] = df.at[index,"Website Traffic"].split('dayson')[0]
    #Else means it's been on the Website for one day
    else:
        df.at[index,"Days on Website"] = 1

    if 'sqft' in  df.at[index,"Home Type"]:
        df.at[index,"Home Type"] = 'Multi-family home'

    for item in building_stats:
        if  item == ', ' or "[" in item or item == ']':
            continue

        header = item.split(':', 1)[0]
        contents = item.split(':', 1)[1]
        contents = contents.strip()

        header = header.replace("'","")
        header = header.replace('"',"")
        header = header.strip()

        ##### Specific data process for columns ##### 
        # Header: Level Dimensions
        if header == 'Level' and "First" in contents:
            if contents == "First":
                df.at[index,"First Floor Dimensions"] = ""
            else: 
                df.at[index,"First Floor Dimensions"] = contents.split(":")[1]
        elif header == "Level" and "Second" in contents:
            if contents == "Second":
                df.at[index,"Second Floor Dimensions"] = ""
            else:
                df.at[index,"Second Floor Dimensions"] = contents.split(":")[1]
        elif header == "Level" and "Third" in contents:
            if contents == "Third":
                df.at[index,"Third Floor Dimensions"] = ""
            else:
                df.at[index,"Third Floor Dimensions"] = contents.split(":")[1]
        elif header == "Level" and "Fourth" in contents:
            df.at[index,"Fourth Floor Dimensions"] = contents.split(":")[1]
        elif header == "Level" and "Basement" in contents:
            df.at[index,"Basement Dimensions"] = contents.split(":")[1]
        #Appliances included Laundry Features
        elif  header == "Appliances included" and "Laundry features:" in contents:
            df.at[index,'Laundry features'] = contents.split("Laundry features:")[1]
            df.at[index,header] = contents.split("Laundry features:")[0]
        
        ########## Skip Colummns that do not have sufficent data ##########
        #Skip Total interior livable area
        elif header == "Total interior livable area":
            continue
        #Skip Construction materials
        elif header == "Construction materials":
            continue
                #Skip Features
        elif header == 'Features':
            continue
        #Skip Roof (Almost zero entries)
        elif header == "Roof":
            continue
        #Skip Foundation (Almost zero entries)
        elif header == "Foundation":
            continue
        #Skip Dimensions (Almost zero entries)
        elif header == "Dimensions":
            continue
        #Skip Road surface type
        elif header == "Road surface type":
            continue
        #Skip Energy efficient items
        elif header == "Energy efficient items":
            continue
        #Skip Accessibility features
        elif header == "Accessibility features":
            continue
        #Skip New construction
        elif header == "New construction":
            continue
        #Skip Senior community
        elif header == "Senior community":
            continue
        #Skip Senior community
        elif header == "Utilities for property":
            continue
        #Skip Total structure area
        elif header == "Total structure area":
            continue
        #Skip Fencing
        elif header == "Fencing":
            continue
        #Skip Acres allowed for irrigation
        elif header == "Acres allowed for irrigation":
            continue
        #Skip Water information
        elif header == "Water information":
            continue
        ########## End of Skipping Colummns that do not have sufficent data ##########
        
        # Header: Number of Stories
        elif header == "Levels":
            if "OneStories" in contents:
                df.at[index,"Number of Stories"] = '1'
            elif "TwoStories" in contents:
                df.at[index,"Number of Stories"] = '2'
            elif "Three Or" in contents:
                df.at[index,"Number of Stories"] = '3'
            else:
                df.at[index,"Number of Stories"] = ""
        # Header: Lot Size
        elif header == "Lot size":
            if "Acres" in contents:
               df.at[index,"Lot Size (sqft)"] = int(float(contents.split("Acres")[0]) * 43560)
            else:
                contents = contents.split("sqft")[0]
                contents = contents.replace(',','')
                df.at[index,"Lot Size (sqft)"] = contents
        # Header: Parcel Number
        elif header == 'Parcel number':
            if 'Attached' in contents:
                df.at[index,'Parcel Number'] = contents.split("Attached")[0] 
            elif 'Special' in contents:
                df.at[index,'Parcel Number'] = contents.split("Special")[0] 
    
            else:
                df.at[index,'Parcel Number'] = ""
        # Header: Architectural Style
        elif header == "Home type":
            if "Architectural style" in contents:
                architecture_style = contents.split("Architectural style:")[1] 
                architecture_style = architecture_style.split('subType:')[0]
                architecture_style = architecture_style.replace(','," , ")
                df.at[index,'Architectural Style'] = architecture_style

        # Header: Sewer Information
        elif header == "Sewer information":
            df.at[index,'Sewer Information'] = contents.split("Utilities for property:")[1] 
        # Header: Sub Region
        elif header == "Region":
            if 'Subdivision' in contents:
                df.at[index,'Sub Division'] = contents.split("Subdivision: ")[1]
        # Header: Parking Inforation
        elif header == "Total spaces":
            df.at[index,'Total Parking Spaces'] = contents.split("Parking features:")[0] 
            if 'Garage spaces' in contents:
                df.at[index,'Garage Parking Spaces'] = contents.split("Garage spaces: ")[1][0]
            if 'Covered spaces' in contents:
                df.at[index,'Covered Parking Spaces'] = contents.split("Covered spaces: ")[1][0]
            if 'Carport spaces' in contents:
                df.at[index,'Carport Parking Spaces'] = contents.split("Carport spaces: ")[1][0]
        # Header: Windows and Interior Features
        elif header == "Window features":
            df.at[index,'Window Features'] = contents.split("Interior features:")[0]
            df.at[index,'Interior Features'] = contents.split("Interior features:")[1]
        # Header: HOA Status
        elif header == 'Has HOA':
            df.at[index,'HOA Status'] = 'Yes'
            if 'HOA fee' in contents: 
                fee = contents.split("HOA fee: ")[1]
                fee = fee.split(' ')[0]
                fee = fee.replace('$', '')
                fee = fee.replace(',','')
                if "annual" in contents:
                    fee = int(fee) / 12
                df.at[index,'HOA Fee (monthly)'] = int(fee)
        # Header: Additional Structures
        elif header == 'Additional structures included':
            df.at[index,'Additional Structures'] = contents.split("Parcel number:")[0]
            parcel_info = contents.split("Parcel number:")[1]
            if 'Attached' in contents:
                df.at[index,'Parcel Number'] = parcel_info.split("Attached")[0] 
            elif 'Special' in contents:
                df.at[index,'Parcel Number'] = parcel_info.split("Special")[0] 
    
            else:
                df.at[index,'Parcel Number'] = ""
        # Header: Buyer Agency Comp
        elif header == 'Buyer agency compensation':
            percentage = contents.replace("'", '')
            percentage = percentage.replace(']','')
            percentage = percentage.replace("%%",'%')
            #percentage = re.sub('\D', '', percentage)
            df.at[index,'Buyer Agency Compensation'] = percentage
        # Header: Pull additional sewer info
        elif header == 'Electric information':
            df.at[index,'Sewer Information'] = contents.split("PublicUtilities for property: ")[1] 
        else:
            df.at[index,header] = contents

#Drop any unnecessary columns 
df = df.drop(columns=['Building Stats', 'Website Traffic', 'Rooms'])

#Output to CSV
df.to_csv('Sales_Data_Cleaned.csv', index=False, encoding='utf-8')

