import pandas as pd
import random

def get_food_name(category, sub_category, flavour):
    food_mappings = {
        'main course': {
            'indian': {
                'spicy': ['Butter Chicken', 'Chicken Tikka Masala', 'Paneer Kadai', 'Chole Bhature'],
                'sweet': ['Shahi Paneer', 'Navratan Korma', 'Malai Kofta', 'Paneer Makhanwala'],
                'tangy': ['Kadai Chicken', 'Achari Paneer', 'Dhaba Dal', 'Amritsari Fish'],
                'sour': ['Kadhi Pakora', 'Dahi Bhalla', 'Dal Bukhara', 'Bharwa Baigan'],
                'exotic': ['Rogan Josh', 'Kashmiri Pulao', 'Mughlai Biryani', 'Nargisi Kofta'],
                'healthy': ['Quinoa Biryani', 'Grilled Fish Curry', 'Sprouts Curry', 'Baked Tandoori Roti']
            },
            'south': {
                'spicy': ['Chettinad Chicken', 'Andhra Fish Curry', 'Guntur Chicken', 'Pepper Chicken'],
                'sweet': ['Coconut Rice', 'Sweet Pongal', 'Kesari Bath', 'Kabali Rice'],
                'tangy': ['Rasam Rice', 'Puliyogare', 'Lemon Rice', 'Tomato Rice'],
                'sour': ['Tamarind Rice', 'Pulihora', 'Mango Rice', 'Lime Rice'],
                'exotic': ['Allepy Fish Curry', 'Kerala Stew', 'Malabar Biryani', 'Appam Stew'],
                'healthy': ['Millet Bisibelebath', 'Ragi Mudde', 'Vegetable Stew', 'Quinoa Upma']
            }
        },
        'dessert': {
            'indian': {
                'spicy': ['Masala Kheer', 'Ginger Halwa', 'Cardamom Ladoo'],
                'sweet': ['Gulab Jamun', 'Rasgulla', 'Kaju Katli', 'Jalebi'],
                'tangy': ['Imli Kulfi', 'Tamarind Ladoo', 'Mango Barfi', 'Orange Kalakand'],
                'sour': ['Lime Soufflé', 'Orange Barfi', 'Citrus Halwa', 'Lemon Sandesh'],
                'exotic': ['Paan Ice Cream', 'Rose Kheer', 'Thandai Mousse', 'Gulkand Burfi'],
                'healthy': ['Date Barfi', 'Ragi Halwa', 'Quinoa Kheer', 'Oats Ladoo']
            },
            'south': {
                'spicy': ['Ginger Payasam', 'Pepper Halwa', 'Cardamom Sweet'],
                'sweet': ['Mysore Pak', 'Rava Kesari', 'Palkova', 'Basundi'],
                'tangy': ['Mango Payasam', 'Pineapple Kesari', 'Citrus Halwa'],
                'sour': ['Lime Kesari', 'Orange Payasam', 'Tamarind Sweet'],
                'exotic': ['Tender Coconut Pudding', 'Palm Jaggery Payasam', 'Jackfruit Halwa'],
                'healthy': ['Ragi Halwa', 'Millet Payasam', 'Nuts Kesari']
            }
        },
        'soup': {
            'indian': {
                'spicy': ['Mulligatawny Soup', 'Rasam', 'Pepper Soup', 'Masala Soup'],
                'sweet': ['Sweet Corn Soup', 'Carrot Ginger Soup', 'Pumpkin Soup'],
                'tangy': ['Tomato Soup', 'Lemon Coriander Soup', 'Tamarind Rasam'],
                'sour': ['Amchur Soup', 'Kokum Soup', 'Lime Soup', 'Tamarind Soup'],
                'exotic': ['Mushroom Soup', 'Asparagus Soup', 'Broccoli Soup'],
                'healthy': ['Mixed Vegetable Soup', 'Spinach Soup', 'Lentil Soup']
            }
        },
        'breakfast': {
            'indian': {
                'spicy': ['Masala Dosa', 'Sambar Vada', 'Spicy Upma', 'Misal Pav'],
                'sweet': ['Meethi Poori', 'Sweet Semiya', 'Sheera', 'Chenna Toast'],
                'tangy': ['Poha', 'Lemon Upma', 'Tomato Uttapam', 'Masala Idli'],
                'sour': ['Lemon Sevai', 'Tamarind Poha', 'Amchur Paratha'],
                'exotic': ['Stuffed Kulcha', 'Paneer Paratha', 'Mushroom Dosa'],
                'healthy': ['Ragi Dosa', 'Oats Idli', 'Quinoa Upma', 'Sprouts Poha']
            }
        },
        'chapati': {
            'indian': {
                'spicy': ['Masala Roti', 'Chilli Paratha', 'Mirchi Paratha'],
                'sweet': ['Puran Poli', 'Meethi Roti', 'Sweet Paratha'],
                'tangy': ['Masala Paratha', 'Achari Paratha', 'Pudina Roti'],
                'sour': ['Amchur Paratha', 'Khatta Paratha', 'Dahi Roti'],
                'exotic': ['Mughlai Paratha', 'Stuffed Naan', 'Kashmiri Naan'],
                'healthy': ['Multigrain Roti', 'Methi Paratha', 'Palak Roti']
            }
        },
        'beverage': {
            'indian': {
                'spicy': ['Masala Chai', 'Kadak Chai', 'Ginger Tea'],
                'sweet': ['Badam Milk', 'Rose Milk', 'Kesar Milk'],
                'tangy': ['Jal Jeera', 'Aam Panna', 'Nimbu Pani'],
                'sour': ['Kokum Sherbet', 'Tamarind Juice', 'Lime Soda'],
                'exotic': ['Thandai', 'Kesaria Milk', 'Gulkand Lassi'],
                'healthy': ['Buttermilk', 'Sattu Drink', 'Coconut Water']
            }
        }
    }
    
    try:
        options = food_mappings[category][sub_category][flavour]
        return random.choice(options)
    except:
        # Create meaningful names for combinations not in the mapping
        if category == 'fast-food':
            return f"{flavour.title()} {sub_category.title()} Burger"
        elif category == 'drinks':
            return f"{flavour.title()} {sub_category.title()} Smoothie"
        elif category == 'rice':
            return f"{flavour.title()} {sub_category.title()} Rice"
        elif category == 'cakes':
            return f"{flavour.title()} {sub_category.title()} Cake"
        elif category == 'appetizers':
            return f"{flavour.title()} {sub_category.title()} Starter"
        else:
            return f"{flavour.title()} {sub_category.title()} {category.title()}"

# Read the original dataset
df = pd.read_csv('Food Dataset.csv')

# Only replace the food names where they contain "Sample food"
df['food_name'] = df.apply(lambda row: 
    get_food_name(row['food_category'], row['sub_category'], row['flavour']) 
    if 'Sample food' in str(row['food_name']) 
    else row['food_name'], 
    axis=1
)

# Save the updated dataset with exactly the same format
df.to_csv('Food Dataset Updated.csv', index=False)

# Print a few examples of the changes made
print("\nExample of updated food names:")
sample = df[df['food_name'] != 'Sample food'].head(10)
for _, row in sample.iterrows():
    print(f"Category: {row['food_category']}, Sub-category: {row['sub_category']}, Flavour: {row['flavour']}")
    print(f"New name: {row['food_name']}\n")