URL = "http://99.153.249.66/admin/"
f_name = "//input[contains(@name,'first_name')]"
l_name = "//input[contains(@name,'last_name')]"
mid_name = "//input[contains(@name,'middle_name')]"
birthday = "//input[@type='text'][contains(@id,'birthday')]"
street = "//input[@type='text'][contains(@id,'address')]"
unit = "//input[@type='text'][contains(@id,'unit')]"
city = "//input[@type='text'][contains(@id,'city')]"
zipcode = "//input[@type='text'][contains(@id,'code')]"
idNumber = "//input[@type='text'][contains(@id,'number')]"
idIssued = "//input[contains(@name,'ID_issued_date')]"
idExp = "//input[contains(@name,'ID_expiration_date')]"
emergContact = "//input[@type='text'][contains(@id,'relationship')]"
postal = "//input[@id='id_postal_name']"
state = "//input[@id='id_name']"

states_info = {
            "AL": ("Alabama", "Central (CT)"),
            # "AK": ("Alaska", "Alaska (AKT)"),
            "AZ": ("Arizona", "Mountain (MT)"),
            "AR": ("Arkansas", "Central (CT)"),
            "CA": ("California", "Pacific (PT)"),
            "CO": ("Colorado", "Mountain (MT)"),
            "CT": ("Connecticut", "Eastern (ET)"),
            "DE": ("Delaware", "Eastern (ET)"),
            "FL": ("Florida", "Eastern (ET)"),
            "GA": ("Georgia", "Eastern (ET)"),
            "HI": ("Hawaii", "Hawaii (HT)"),
            "ID": ("Idaho", "Mountain (MT)"),
            "IL": ("Illinois", "Central (CT)"),
            "IN": ("Indiana", "Eastern (ET)"),
            "IA": ("Iowa", "Central (CT)"),
            "KS": ("Kansas", "Central (CT)"),
            "KY": ("Kentucky", "Eastern (ET)"),
            "LA": ("Louisiana", "Central (CT)"),
            "ME": ("Maine", "Eastern (ET)"),
            "MD": ("Maryland", "Eastern (ET)"),
            "MA": ("Massachusetts", "Eastern (ET)"),
            "MI": ("Michigan", "Eastern (ET)"),
            "MN": ("Minnesota", "Central (CT)"),
            "MS": ("Mississippi", "Central (CT)"),
            "MO": ("Missouri", "Central (CT)"),
            "MT": ("Montana", "Mountain (MT)"),
            "NE": ("Nebraska", "Central (CT)"),
            "NV": ("Nevada", "Pacific (PT)"),
            "NH": ("New Hampshire", "Eastern (ET)"),
            "NJ": ("New Jersey", "Eastern (ET)"),
            "NM": ("New Mexico", "Mountain (MT)"),
            "NY": ("New York", "Eastern (ET)"),
            "NC": ("North Carolina", "Eastern (ET)"),
            "ND": ("North Dakota", "Central (CT)"),
            "OH": ("Ohio", "Eastern (ET)"),
            "OK": ("Oklahoma", "Central (CT)"),
            "OR": ("Oregon", "Pacific (PT)"),
            "PA": ("Pennsylvania", "Eastern (ET)"),
            "RI": ("Rhode Island", "Eastern (ET)"),
            "SC": ("South Carolina", "Eastern (ET)"),
            "SD": ("South Dakota", "Central (CT)"),
            "TN": ("Tennessee", "Central (CT)"),
            "TX": ("Texas", "Central (CT)"),
            "UT": ("Utah", "Mountain (MT)"),
            "VT": ("Vermont", "Eastern (ET)"),
            "VA": ("Virginia", "Eastern (ET)"),
            "WA": ("Washington", "Pacific (PT)"),
            "WV": ("West Virginia", "Eastern (ET)"),
            "WI": ("Wisconsin", "Central (CT)"),
            "WY": ("Wyoming", "Mountain (MT)")
        }


