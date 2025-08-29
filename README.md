# 🍛 Telugu Culinary Application

**తెలుగు వంటకాలు** - A comprehensive Streamlit application for traditional Telugu recipes with AI chatbot integration capabilities.

## 🌟 Features

### Core Functionality
- **🏠 Home Page**: Browse recipe categories and overview
- **🔍 Advanced Search**: Search by name, ingredients, or description
- **❤️ Favorites System**: Save and manage favorite recipes
- **➕ Recipe Management**: Add new traditional recipes
- **🤖 Chatbot Ready**: Pre-built integration points for AI assistant

### Technical Excellence
- **🚀 Optimized Performance**: List comprehensions and efficient data structures
- **📱 Responsive Design**: Works on desktop, tablet, and mobile
- **💾 Data Persistence**: JSON-based storage with automatic backups
- **🎨 Beautiful UI**: Custom CSS with Telugu font support
- **🔧 Modular Architecture**: Clean, maintainable code structure

## 📋 Quick Start

### Option 1: Automatic Setup (Recommended)
```bash
# Clone or download the project files
# Run the automatic setup
python setup.py

# Start the application
./run_app.sh        # Linux/Mac
# OR
run_app.bat         # Windows
```

### Option 2: Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run main.py
```

## 🛠️ Installation Guide

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (for initial setup)

### Step-by-Step Installation

1. **Download the Project**
   ```bash
   # Create project directory
   mkdir telugu-culinary-app
   cd telugu-culinary-app
   
   # Copy all provided files to this directory
   ```

2. **Run Automatic Setup**
   ```bash
   python setup.py
   ```
   This will:
   - Check Python compatibility
   - Install all required packages
   - Create necessary directories
   - Set up run scripts
   - Configure deployment files

3. **Start the Application**
   ```bash
   # Linux/Mac
   ./run_app.sh
   
   # Windows
   run_app.bat
   
   # Or manually
   streamlit run main.py
   ```

4. **Access the Application**
   - Open your browser
   - Go to: `http://localhost:8501`
   - Enjoy cooking! 🍛

## 📁 Project Structure

```
telugu-culinary-app/
├── main.py                 # Main application file
├── requirements.txt        # Python dependencies
├── setup.py               # Automatic setup script
├── README.md              # This file
├── run_app.sh             # Linux/Mac run script
├── run_app.bat            # Windows run script
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose setup
├── Procfile               # Railway deployment
├── render.yaml            # Render deployment
├── .streamlit/
│   └── config.toml        # Streamlit configuration
└── data/
    ├── recipes.json       # Recipe database
    └── favorites.json     # User favorites
```

## 🚀 Deployment Options

### 1. Local Development
```bash
streamlit run main.py
```

### 2. Docker Deployment
```bash
# Build and run with Docker Compose
docker-compose up -d

# Or build manually
docker build -t telugu-culinary .
docker run -p 8501:8501 telugu-culinary
```

### 3. Cloud Deployment (Free Options)

#### Streamlit Community Cloud
1. Push code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Deploy directly from GitHub
4. **Cost**: Free

#### Railway
1. Push code to GitHub
2. Connect Railway to your repository
3. Deploy with zero configuration
4. **Cost**: Free tier available

#### Render
1. Push code to GitHub
2. Create new Web Service on Render
3. Uses `render.yaml` configuration
4. **Cost**: Free tier available

#### Heroku Alternative - Railway Setup
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway init
railway up
```

## 🔧 Configuration

### Environment Variables
```bash
# Optional: Set custom port
PORT=8501

# Optional: Set data directory
DATA_DIR=./data
```

### Streamlit Configuration
The `.streamlit/config.toml` file contains optimized settings:
- Custom theme colors
- Performance optimizations
- CORS settings for deployment

## 🤖 Chatbot Integration Guide

The application is pre-built with chatbot integration points. To add AI functionality:

### 1. API Integration Points
```python
# In main.py, the chatbot placeholder shows integration structure
def integrate_chatbot_api(user_message):
    """
    Replace this function with your AI API call
    Examples: OpenAI GPT, Google PaLM, Anthropic Claude
    """
    # Your API integration here
    response = call_your_ai_api(user_message)
    return response
```

### 2. Suggested AI APIs
- **OpenAI GPT-4**: Best for conversational responses
- **Google PaLM**: Good for recipe understanding
- **Anthropic Claude**: Excellent for cooking assistance
- **Local Models**: Use Ollama for privacy

### 3. Integration Example
```python
import openai

def chatbot_response(message, recipes_context):
    """Enhanced chatbot with recipe context"""
    context = f"Telugu recipes database: {recipes_context}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a Telugu cooking expert."},
            {"role": "user", "content": f"{context}\n\nUser: {message}"}
        ]
    )
    
    return response.choices[0].message.content
```

## 📊 Features Deep Dive

### Recipe Management System
- **Smart Search**: Multi-field search with Telugu and English support
- **Category Organization**: Biryanis, Curries, Sweets, Snacks
- **Difficulty Levels**: సులభం, మధ్యమం, కష్టం
- **Favorites System**: Persistent user preferences

### Data Storage Strategy
- **JSON-based**: Human-readable and easily editable
- **Automatic Backups**: Prevents data loss
- **Unicode Support**: Full Telugu character compatibility
- **Scalable**: Easy migration to databases later

### Performance Optimizations
- **Lazy Loading**: Recipes loaded on demand
- **Efficient Search**: Optimized string matching
- **Memory Management**: Minimal resource usage
- **Fast Startup**: Sub-second application launch

## 🎨 Customization

### Adding New Recipe Categories
```python
# In main.py, modify get_default_recipes()
def get_default_recipes(self):
    return {
        "biryanis": [...],
        "curries": [...],
        "sweets": [...],
        "snacks": [],      # New category
        "breakfast": [],   # New category
        "drinks": []       # New category
    }
```

### Customizing UI Theme
Edit `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#FF6B35"        # Orange accent
backgroundColor = "#FFFFFF"      # White background
secondaryBackgroundColor = "#F0F2F6"  # Light gray
textColor = "#262730"           # Dark text
```

### Adding New Languages
```python
# Add language support in main.py
LANGUAGES = {
    "telugu": "తెలుగు",
    "english": "English",
    "hindi": "हिंदी"  # Add new language
}
```

## 🔍 Troubleshooting

### Common Issues and Solutions

#### Port Already in Use
```bash
# Kill existing Streamlit processes
pkill -f streamlit

# Or use different port
streamlit run main.py --server.port 8502
```

#### Package Installation Errors
```bash
# Upgrade pip first
pip install --upgrade pip

# Install with verbose output
pip install -r requirements.txt -v

# Alternative: Use conda
conda install streamlit pandas
```

#### Telugu Font Issues
```bash
# Install Telugu fonts on system
# Ubuntu/Debian:
sudo apt-get install fonts-noto-sans-telugu

# Windows: Install from Google Fonts
# Mac: Download from Apple Font Book
```

#### Memory Issues with Large Recipe Database
```python
# In main.py, implement pagination
def get_paginated_recipes(self, page=1, per_page=10):
    start = (page - 1) * per_page
    end = start + per_page
    return self.get_all_recipes()[start:end]
```

### Performance Optimization Tips

1. **Large Recipe Collections**: Use database instead of JSON
2. **Image Support**: Implement lazy loading for recipe images
3. **Search Speed**: Add search indexing for large datasets
4. **Mobile Performance**: Optimize CSS for mobile devices

## 🧪 Testing

### Running Tests
```bash
# Install testing dependencies
pip install pytest streamlit-testing

# Run tests (when test files are added)
pytest tests/
```

### Manual Testing Checklist
- [ ] Home page loads correctly
- [ ] Search functionality works with Telugu and English
- [ ] Favorites can be added and removed
- [ ] New recipes can be added
- [ ] Data persists between sessions
- [ ] Mobile responsiveness works
- [ ] Telugu characters display correctly

## 🤝 Contributing

### Adding New Recipes
1. Use the "Add Recipe" page in the application
2. Or directly edit `data/recipes.json`
3. Follow the existing JSON structure
4. Include both Telugu and English names

### Code Contributions
1. Follow PEP 8 style guidelines
2. Add comments for Telugu-specific functionality
3. Test on multiple platforms
4. Update documentation

### Recipe Categories to Add
- **Pickles** (అచ్చార్లు)
- **Chutneys** (చట్నీలు)
- **Festival Specials** (పండుగ వంటకాలు)
- **Regional Varieties** (ప్రాంతీయ వంటకాలు)

## 📈 Roadmap

### Version 2.0 Features
- [ ] AI Chatbot Integration
- [ ] Voice Recipe Reading
- [ ] Shopping List Generator
- [ ] Nutritional Information
- [ ] Recipe Video Support
- [ ] Social Sharing
- [ ] Multi-user Support
- [ ] Recipe Rating System

### Version 3.0 Features
- [ ] Mobile App (React Native)
- [ ] Offline Mode
- [ ] Recipe Recommendation Engine
- [ ] Cooking Timer Integration
- [ ] Smart Kitchen Device Integration
- [ ] Community Recipe Sharing
- [ ] Professional Chef Mode

## 📞 Support

### Getting Help
1. **Documentation**: Read this README thoroughly
2. **Issues**: Check troubleshooting section
3. **Community**: Join Telugu cooking communities
4. **Code Issues**: Check the code comments

### Contact Information
- **Project**: Telugu Culinary Application
- **Purpose**: Preserve and share Telugu culinary traditions
- **License**: Open source for educational use

## ⚖️ License

This project is created for educational and cultural preservation purposes. Feel free to use, modify, and distribute while maintaining attribution to Telugu culinary traditions.

## 🙏 Acknowledgments

- Traditional Telugu recipes from various regions
- Andhra Pradesh and Telangana culinary heritage
- Community contributions and feedback
- Open source libraries and frameworks

## 📝 Changelog

### v1.0.0 (Current)
- ✅ Complete Streamlit application
- ✅ Recipe management system
- ✅ Search and favorites functionality
- ✅ Deployment-ready configuration
- ✅ Docker support
- ✅ Multi-platform compatibility
- ✅ Chatbot integration foundation

---

**🍛 Happy Cooking! తిండి బాగుండాలి!**
