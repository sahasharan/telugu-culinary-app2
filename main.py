import streamlit as st
import pandas as pd
import json
from datetime import datetime
from typing import Dict, List, Optional
import os
from dify_client import ask_dify
from pathlib import Path

# Configure page settings
st.set_page_config(
    page_title="తెలుగు వంటకాలు - Telugu Culinary",
    page_icon="🍛",
    layout="wide",
    initial_sidebar_state="expanded"
)

class TeluguCulinaryApp:
    """Optimized Telugu Culinary Application with chatbot integration ready"""
    
    def __init__(self):
        self.data_dir = Path("data")
        self.data_dir.mkdir(exist_ok=True)
        self.recipes_file = self.data_dir / "recipes.json"
        self.favorites_file = self.data_dir / "favorites.json"
        self.load_data()
    
    def load_data(self):
        """Load recipes and favorites data with error handling"""
        try:
            with open(self.recipes_file, 'r', encoding='utf-8') as f:
                self.recipes = json.load(f)
        except FileNotFoundError:
            self.recipes = self.get_default_recipes()
            self.save_recipes()
        
        try:
            with open(self.favorites_file, 'r', encoding='utf-8') as f:
                self.favorites = json.load(f)
        except FileNotFoundError:
            self.favorites = []
    
    def save_recipes(self):
        """Save recipes to JSON file"""
        with open(self.recipes_file, 'w', encoding='utf-8') as f:
            json.dump(self.recipes, f, ensure_ascii=False, indent=2)
    
    def save_favorites(self):
        """Save favorites to JSON file"""
        with open(self.favorites_file, 'w', encoding='utf-8') as f:
            json.dump(self.favorites, f, ensure_ascii=False, indent=2)
    
    def get_default_recipes(self) -> Dict:
        """Return default Telugu recipes data"""
        return {
            "biryanis": [
                {
                    "id": "hyderabadi_biryani",
                    "name": "హైదరాబాదీ బిర్యానీ",
                    "english_name": "Hyderabadi Biryani",
                    "ingredients": ["బాస్మతి అన్నం", "మటన్", "యోగర్ట్", "ఉల్లిపాయలు", "మసాలా పౌడర్"],
                    "cooking_time": "2 గంటలు",
                    "difficulty": "కష్టం",
                    "servings": "4-6 మంది",
                    "description": "హైదరాబాద్ యొక్క ప్రసిద్ధ బిర్యానీ",
                    "instructions": [
                        "బాస్మతి అన్నాన్ని నానబెట్టండి",
                        "మటన్‌ను మసాలాలతో మెరినేట్ చేయండి",
                        "అన్నం వేయించండి",
                        "లేయర్లుగా అమర్చండి"
                    ]
                }
            ],
            "curries": [
                {
                    "id": "gongura_mutton",
                    "name": "గోంగూర మటన్",
                    "english_name": "Gongura Mutton",
                    "ingredients": ["మటన్", "గోంగూర ఆకులు", "ఉల్లిపాయలు", "వెల్లుల్లి"],
                    "cooking_time": "45 నిమిషాలు",
                    "difficulty": "మధ్యమం",
                    "servings": "4 మంది",
                    "description": "ఆంధ్రప్రదేశ్ యొక్క ప్రత్యేక వంటకం",
                    "instructions": [
                        "మటన్‌ను కట్ చేయండి",
                        "గోంగూర ఆకులను వేయించండి",
                        "మసాలాలు కలపండి",
                        "ఉడికించండి"
                    ]
                }
            ],
            "sweets": [
                {
                    "id": "ariselu",
                    "name": "అరిసెలు",
                    "english_name": "Ariselu",
                    "ingredients": ["బియ్యం పిండి", "గుడ్డు", "నువ్వులు", "నూనె"],
                    "cooking_time": "1 గంట",
                    "difficulty": "మధ్యమం",
                    "servings": "20 ముక్కలు",
                    "description": "పండుగల ప్రత్యేక తీపి వంటకం",
                    "instructions": [
                        "బియ్యం పిండిని కలపండి",
                        "గుడ్డుతో కలపండి",
                        "నువ్వులు వేయండి",
                        "నూనెలో వేయించండి"
                    ]
                }
            ]
        }
    
    def get_all_recipes(self) -> List[Dict]:
        """Get all recipes as a flat list"""
        all_recipes = []
        for category, recipes in self.recipes.items():
            for recipe in recipes:
                recipe['category'] = category
                all_recipes.append(recipe)
        return all_recipes
    
    def search_recipes(self, query: str) -> List[Dict]:
        """Search recipes by name or ingredients"""
        if not query:
            return self.get_all_recipes()
        
        query_lower = query.lower()
        matching_recipes = []
        
        for recipe in self.get_all_recipes():
            # Search in name, english name, ingredients, and description
            searchable_text = (
                recipe['name'] + ' ' + 
                recipe['english_name'] + ' ' +
                ' '.join(recipe['ingredients']) + ' ' +
                recipe['description']
            ).lower()
            
            if query_lower in searchable_text:
                matching_recipes.append(recipe)
        
        return matching_recipes
    
    def add_to_favorites(self, recipe_id: str):
        """Add recipe to favorites"""
        if recipe_id not in self.favorites:
            self.favorites.append(recipe_id)
            self.save_favorites()
            return True
        return False
    
    def remove_from_favorites(self, recipe_id: str):
        """Remove recipe from favorites"""
        if recipe_id in self.favorites:
            self.favorites.remove(recipe_id)
            self.save_favorites()
            return True
        return False
    
    def is_favorite(self, recipe_id: str) -> bool:
        """Check if recipe is in favorites"""
        return recipe_id in self.favorites

def main():
    """Main application function"""
    app = TeluguCulinaryApp()
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #FF6B35;
        font-size: 3rem;
        margin-bottom: 2rem;
    }
    .recipe-card {
        border: 2px solid #e0e0e0;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        background-color: #f9f9f9;
    }
    .favorite-btn {
        background-color: #FF69B4;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        cursor: pointer;
    }
    .category-header {
        color: #2E8B57;
        font-size: 1.5rem;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown('<h1 class="main-header">🍛 తెలుగు వంటకాలు</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem;">Telugu Culinary - Traditional Recipes & Modern Cooking</p>', unsafe_allow_html=True)
    
    # Sidebar navigation
    st.sidebar.title("🧭 Navigation")
    page = st.sidebar.selectbox(
        "Choose a page:",
        ["🏠 Home", "🔍 Search Recipes", "❤️ Favorites", "➕ Add Recipe", "🤖 Chatbot"]
    )
    
    if page == "🏠 Home":
        show_home_page(app)
    elif page == "🔍 Search Recipes":
        show_search_page(app)
    elif page == "❤️ Favorites":
        show_favorites_page(app)
    elif page == "➕ Add Recipe":
        show_add_recipe_page(app)
    elif page == "🤖 Chatbot":
        show_chatbot_page()

def show_home_page(app: TeluguCulinaryApp):
    """Display home page with recipe categories"""
    st.header("Welcome to Telugu Culinary App! 🙏")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Recipes", len(app.get_all_recipes()))
    with col2:
        st.metric("Categories", len(app.recipes.keys()))
    with col3:
        st.metric("Favorites", len(app.favorites))
    
    st.subheader("Recipe Categories")
    
    for category, recipes in app.recipes.items():
        with st.expander(f"🍽️ {category.title()} ({len(recipes)} recipes)"):
            for recipe in recipes[:3]:  # Show first 3 recipes
                display_recipe_card(app, recipe)
            
            if len(recipes) > 3:
                st.info(f"... and {len(recipes) - 3} more recipes in this category!")

def show_search_page(app: TeluguCulinaryApp):
    """Display search page"""
    st.header("🔍 Search Telugu Recipes")
    
    # Search filters
    col1, col2 = st.columns([3, 1])
    
    with col1:
        search_query = st.text_input(
            "Search recipes by name, ingredients, or description:",
            placeholder="E.g., బిర్యానీ, mutton, sweet"
        )
    
    with col2:
        difficulty_filter = st.selectbox(
            "Difficulty Level:",
            ["All", "సులభం", "మధ్యమం", "కష్టం"]
        )
    
    # Search results
    recipes = app.search_recipes(search_query)
    
    # Apply difficulty filter
    if difficulty_filter != "All":
        recipes = [r for r in recipes if r.get('difficulty') == difficulty_filter]
    
    st.subheader(f"Found {len(recipes)} recipes")
    
    if recipes:
        for recipe in recipes:
            display_recipe_card(app, recipe)
    else:
        st.info("No recipes found. Try different search terms!")

def show_favorites_page(app: TeluguCulinaryApp):
    """Display favorites page"""
    st.header("❤️ Your Favorite Recipes")
    
    if not app.favorites:
        st.info("No favorite recipes yet! Start adding some from the search page.")
        return
    
    favorite_recipes = [
        recipe for recipe in app.get_all_recipes() 
        if recipe['id'] in app.favorites
    ]
    
    for recipe in favorite_recipes:
        display_recipe_card(app, recipe, show_remove_favorite=True)

def show_add_recipe_page(app: TeluguCulinaryApp):
    """Display add recipe page"""
    st.header("➕ Add New Telugu Recipe")
    
    with st.form("add_recipe_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            telugu_name = st.text_input("Telugu Name *", placeholder="e.g., పులిహోర")
            english_name = st.text_input("English Name *", placeholder="e.g., Tamarind Rice")
            category = st.selectbox("Category *", ["biryanis", "curries", "sweets", "snacks", "breakfast"])
            difficulty = st.selectbox("Difficulty Level *", ["సులభం", "మధ్యమం", "కష్టం"])
        
        with col2:
            cooking_time = st.text_input("Cooking Time *", placeholder="e.g., 30 నిమిషాలు")
            servings = st.text_input("Servings *", placeholder="e.g., 4 మంది")
            description = st.text_area("Description", placeholder="Brief description of the dish")
        
        st.subheader("Ingredients")
        ingredients = st.text_area(
            "Enter ingredients (one per line) *",
            placeholder="బియ్యం\nనూనె\nఉప్పు"
        )
        
        st.subheader("Instructions")
        instructions = st.text_area(
            "Enter cooking instructions (one step per line) *",
            placeholder="బియ్యాన్ని కడిగి నానబెట్టండి\nనూనె వేడిచేసి మసాలాలు వేయండి"
        )
        
        submitted = st.form_submit_button("Add Recipe")
        
        if submitted:
            if all([telugu_name, english_name, cooking_time, servings, ingredients, instructions]):
                new_recipe = {
                    "id": f"{telugu_name.replace(' ', '_').lower()}_{len(app.get_all_recipes())}",
                    "name": telugu_name,
                    "english_name": english_name,
                    "ingredients": [ing.strip() for ing in ingredients.split('\n') if ing.strip()],
                    "cooking_time": cooking_time,
                    "difficulty": difficulty,
                    "servings": servings,
                    "description": description,
                    "instructions": [inst.strip() for inst in instructions.split('\n') if inst.strip()]
                }
                
                # Add to appropriate category
                if category not in app.recipes:
                    app.recipes[category] = []
                app.recipes[category].append(new_recipe)
                app.save_recipes()
                
                st.success("Recipe added successfully! 🎉")
            else:
                st.error("Please fill all required fields marked with *")

def show_chatbot_page():
    """Display the Annapurna chatbot page"""
    st.header("🤖 Annapurna - Telugu Culinary Chatbot")

    # Initialize session messages
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "నమస్కారం! I'm Annapurna, your Telugu cooking assistant. Ask me anything about recipes 🍲"}
        ]

    # Display previous chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask about Telugu recipes..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get response from Dify chatbot
        from dify_client import ask_dify
        response = ask_dify(prompt)

        # Display chatbot response
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})


def display_recipe_card(app: TeluguCulinaryApp, recipe: Dict, show_remove_favorite: bool = False):
    """Display a recipe card with all details"""
    with st.container():
        st.markdown('<div class="recipe-card">', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            st.subheader(f"{recipe['name']} ({recipe['english_name']})")
            st.write(f"**Description:** {recipe['description']}")
        
        with col2:
            if show_remove_favorite:
                if st.button("❌ Remove", key=f"remove_{recipe['id']}"):
                    app.remove_from_favorites(recipe['id'])
                    st.rerun()
            else:
                if app.is_favorite(recipe['id']):
                    st.write("❤️ Favorite")
                else:
                    if st.button("❤️ Add to Favorites", key=f"fav_{recipe['id']}"):
                        app.add_to_favorites(recipe['id'])
                        st.rerun()
        
        with col3:
            st.write(f"⏰ {recipe['cooking_time']}")
            st.write(f"👥 {recipe['servings']}")
            st.write(f"📊 {recipe['difficulty']}")
        
        # Expandable details
        with st.expander("View Recipe Details"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Ingredients:**")
                for ingredient in recipe['ingredients']:
                    st.write(f"• {ingredient}")
            
            with col2:
                st.write("**Instructions:**")
                for i, instruction in enumerate(recipe['instructions'], 1):
                    st.write(f"{i}. {instruction}")
        
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()