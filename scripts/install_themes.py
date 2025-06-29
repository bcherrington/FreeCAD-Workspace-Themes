#!/usr/bin/env python3
"""
FreeCAD Workspace Themes Installation Script

This script helps install FreeCAD Workspace Themes to the correct user directory.
It can be used as an alternative to the FreeCAD Add-on Manager.

Usage:
    python install_themes.py [--dry-run] [--theme THEME_NAME]

Options:
    --dry-run       Show what would be installed without actually copying files
    --theme         Install only a specific theme (Carbon Designer, Slate Professional, Graphite Professional)
    --help          Show this help message
"""

import os
import sys
import shutil
import argparse
from pathlib import Path

def get_freecad_user_dir():
    """Get the FreeCAD user data directory for the current platform."""
    if sys.platform.startswith('win'):
        # Windows
        appdata = os.environ.get('APPDATA')
        if appdata:
            return Path(appdata) / 'FreeCAD'
    else:
        # Linux/macOS
        home = Path.home()
        if sys.platform == 'darwin':
            # macOS
            return home / 'Library' / 'Application Support' / 'FreeCAD'
        else:
            # Linux
            return home / '.local' / 'share' / 'FreeCAD'
    
    return None

def get_script_dir():
    """Get the directory containing this script."""
    return Path(__file__).parent.parent

def install_theme(theme_name, source_dir, target_dir, dry_run=False):
    """Install a single theme to the target directory."""
    theme_source = source_dir / theme_name

    if not theme_source.exists():
        print(f"❌ Theme '{theme_name}' not found in source directory")
        return False

    # Create target directory
    target_theme_dir = target_dir / theme_name

    # Define all theme files that should be copied
    theme_files = [
        f'{theme_name}.cfg',
        f'{theme_name}.qss',
        f'{theme_name} Overlay.qss'
    ]

    if dry_run:
        print(f"📁 Would create directory: {target_theme_dir}")
        for file_name in theme_files:
            source_file = theme_source / file_name
            if source_file.exists():
                print(f"📄 Would copy: {source_file} → {target_theme_dir}")
        return True

    try:
        # Create target directory
        target_theme_dir.mkdir(parents=True, exist_ok=True)

        # Copy all theme files
        for file_name in theme_files:
            source_file = theme_source / file_name
            if source_file.exists():
                shutil.copy2(source_file, target_theme_dir)
                print(f"✅ Copied: {file_name}")
            else:
                print(f"⚠️  Warning: {file_name} not found")

        return True

    except Exception as e:
        print(f"❌ Error installing {theme_name}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Install FreeCAD Workspace Themes')
    parser.add_argument('--dry-run', action='store_true', 
                       help='Show what would be installed without actually copying files')
    parser.add_argument('--theme', choices=['Carbon Designer', 'Slate Professional', 'Graphite Professional'],
                       help='Install only a specific theme')
    
    args = parser.parse_args()
    
    print("🎨 FreeCAD Workspace Themes Installer")
    print("=" * 40)
    
    # Get directories
    source_dir = get_script_dir()
    freecad_dir = get_freecad_user_dir()
    
    if not freecad_dir:
        print("❌ Could not determine FreeCAD user directory")
        return 1
    
    target_dir = freecad_dir / 'Preference Packs' / 'FreeCAD Workspace Themes'
    
    print(f"📂 Source: {source_dir}")
    print(f"📂 Target: {target_dir}")
    print()
    
    if args.dry_run:
        print("🔍 DRY RUN MODE - No files will be copied")
        print()
    
    # Determine which themes to install
    if args.theme:
        themes = [args.theme]
    else:
        themes = ['Carbon Designer', 'Slate Professional', 'Graphite Professional']
    
    # Install themes
    success_count = 0
    for theme in themes:
        print(f"Installing {theme}...")
        if install_theme(theme, source_dir, target_dir, args.dry_run):
            success_count += 1
        print()
    
    # Summary
    if args.dry_run:
        print(f"📋 Would install {success_count}/{len(themes)} themes")
    else:
        print(f"🎉 Successfully installed {success_count}/{len(themes)} themes")
        
        if success_count > 0:
            print()
            print("📝 Next steps:")
            print("1. Open FreeCAD")
            print("2. Go to Tools → Preferences → General → Preference packs")
            print("3. Select your desired theme and click Apply")
            print("4. Restart FreeCAD for full effect")
    
    return 0 if success_count == len(themes) else 1

if __name__ == '__main__':
    sys.exit(main())
