#!/usr/bin/env python3
"""
Automatic Setup Script for Telugu Culinary Application
This script sets up everything needed to run the application
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in {description}: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor} is compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor} is not compatible. Need Python 3.8+")
        return False

def create_project_structure():
    """Create necessary directories"""
    print("🔄 Creating project structure...")
    
    directories = ['data', 'static', 'logs']
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Created directory: {directory}")
    
    return True

def install_requirements():
    """Install required packages"""
    if not run_command("pip install -r requirements.txt", "Installing requirements"):
        # Fallback installation
        packages = ["streamlit>=1.28.0", "pandas>=1.5.0"]
        for package in packages:
            if not run_command(f"pip install {package}", f"Installing {package}"):
                return False
    return True

def create_run_script():
    """Create a script to run the application"""
    run_script_content = """#!/bin/bash
# Telugu Culinary App Runner Script

echo "🍛 Starting Telugu Culinary Application..."
echo "📍 Open your browser to: http://localhost:8501"
echo "🛑 Press Ctrl+C to stop the application"

streamlit run main.py --server.port 8501 --server.address 0.0.0.0
"""
    
    with open("run_app.sh", "w") as f:
        f.write(run_script_content)
    
    # Make it executable on Unix systems
    if os.name != 'nt':
        os.chmod("run_app.sh", 0o755)
    
    # Create Windows batch file
    windows_script = """@echo off
echo 🍛 Starting Telugu Culinary Application...
echo 📍 Open your browser to: http://localhost:8501
echo 🛑 Press Ctrl+C to stop the application

streamlit run main.py --server.port 8501 --server.address 0.0.0.0
"""
    
    with open("run_app.bat", "w") as f:
        f.write(windows_script)
    
    print("✅ Created run scripts (run_app.sh for Linux/Mac, run_app.bat for Windows)")
    return True

def create_docker_files():
    """Create Docker configuration for easy deployment"""
    dockerfile_content = """FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
"""
    
    docker_compose_content = """version: '3.8'

services:
  telugu-culinary:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - ./data:/app/data
    environment:
      - STREAMLIT_SERVER_HEADLESS=true
      - STREAMLIT_SERVER_ENABLE_CORS=false
    restart: unless-stopped
"""
    
    with open("Dockerfile", "w") as f:
        f.write(dockerfile_content)
    
    with open("docker-compose.yml", "w") as f:
        f.write(docker_compose_content)
    
    print("✅ Created Docker configuration files")
    return True

def create_deployment_configs():
    """Create deployment configuration for various platforms"""
    
    # Streamlit Cloud config
    streamlit_config = """[general]
email = "your-email@example.com"

[server]
headless = true
enableCORS = false
port = $PORT

[theme]
primaryColor = "#FF6B35"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
"""
    
    config_dir = Path(".streamlit")
    config_dir.mkdir(exist_ok=True)
    
    with open(config_dir / "config.toml", "w") as f:
        f.write(streamlit_config)
    
    # Railway deployment config
    railway_config = """web: streamlit run main.py --server.port $PORT --server.address 0.0.0.0
"""
    
    with open("Procfile", "w") as f:
        f.write(railway_config)
    
    # Render deployment config
    render_config = """build:
  commands:
    - pip install -r requirements.txt
start:
  command: streamlit run main.py --server.port $PORT --server.address 0.0.0.0
"""
    
    with open("render.yaml", "w") as f:
        f.write(render_config)
    
    print("✅ Created deployment configurations for Streamlit Cloud, Railway, and Render")
    return True

def main():
    """Main setup function"""
    print("🚀 Telugu Culinary Application Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        print("Please install Python 3.8 or higher")
        sys.exit(1)
    
    # Create project structure
    if not create_project_structure():
        print("Failed to create project structure")
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        print("Failed to install requirements")
        sys.exit(1)
    
    # Create run scripts
    if not create_run_script():
        print("Failed to create run scripts")
        sys.exit(1)
    
    # Create Docker files
    if not create_docker_files():
        print("Failed to create Docker files")
        sys.exit(1)
    
    # Create deployment configs
    if not create_deployment_configs():
        print("Failed to create deployment configs")
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next Steps:")
    print("1. Run the application:")
    print("   - Linux/Mac: ./run_app.sh")
    print("   - Windows: run_app.bat")
    print("   - Manual: streamlit run main.py")
    print("\n2. Open your browser to: http://localhost:8501")
    print("\n3. For deployment:")
    print("   - Docker: docker-compose up")
    print("   - Cloud platforms: Use the created config files")
    print("\n🍛 Enjoy your Telugu Culinary Application!")

if __name__ == "__main__":
    main()