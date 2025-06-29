# FreeCAD Workspace Themes

Professional theme collection for FreeCAD featuring expertly designed color palettes and modern styling optimized for CAD workflows.

## 🎨 Available Themes

### Carbon Designer ⭐ (Featured)
Professional dark theme with carbon-inspired color palette. Features balanced contrast, modern styling, and optimized colors for technical CAD work.

**Key Features:**
- Carbon-inspired color palette with professional appearance
- Balanced contrast for extended CAD sessions
- Modern interface styling with clean lines
- Optimized for technical precision work

### Slate Professional
Expert-designed slate-based color palette with cool undertones. Professional appearance with sophisticated hierarchy and enhanced accessibility.

**Key Features:**
- Slate-based color palette with cool undertones
- Sophisticated visual hierarchy
- Enhanced accessibility with WCAG AA compliant contrast
- Modern scrollbars and refined interface elements

### Graphite Professional 🏆 (Recommended)
Pure gray color palette without blue undertones. Neutral color temperature for technical precision with clean, professional appearance ideal for CAD work.

**Key Features:**
- Pure gray palette without color temperature bias
- Neutral colors for technical precision
- Clean, professional appearance
- Optimized Sketcher colors for white backgrounds
- Context-aware styling for different interface areas

## 📦 Installation

### Via FreeCAD Add-on Manager (Recommended)

1. Open FreeCAD
2. Go to **Tools → Addon Manager**
3. Search for "FreeCAD Workspace Themes"
4. Click **Install**
5. Restart FreeCAD

### Manual Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/bcherrington/FreeCAD-Workspace-Themes.git
   ```

2. Copy to your FreeCAD user directory:
   ```bash
   # Linux/macOS
   cp -r FreeCAD-Workspace-Themes ~/.local/share/FreeCAD/Preference\ Packs/
   
   # Windows
   copy FreeCAD-Workspace-Themes %APPDATA%\FreeCAD\Preference\ Packs\
   ```

## 🚀 Usage

### Method 1: Preference Packs (Recommended)

1. Go to **Tools → Preferences → General → Preference packs**
2. Select your desired theme from the list:
   - Carbon Designer
   - Slate Professional  
   - Graphite Professional
3. Click **Apply**
4. Restart FreeCAD for full effect

### Method 2: Manual Configuration

1. Go to **Tools → Preferences → Display → UI**
2. Set **StyleSheet** to your chosen theme `.qss` file
3. Set **OverlayActiveStyleSheet** to the corresponding `Overlay.qss` file
4. Click **Apply** and **OK**

## 🎯 Theme Comparison

| Feature | Carbon Designer | Slate Professional | Graphite Professional |
|---------|----------------|-------------------|----------------------|
| **Color Temperature** | Neutral-warm | Cool | Neutral |
| **Primary Use** | General CAD | Professional design | Technical precision |
| **Contrast Level** | Balanced | High | Moderate-high |
| **Accessibility** | WCAG AA | WCAG AA+ | WCAG AA+ |
| **Sketcher Colors** | Optimized | Enhanced | Premium |
| **Best For** | Daily CAD work | Design presentations | Technical drawings |

## 🛠️ Customization

Each theme includes:
- **Main stylesheet** (`.qss`) - Core interface styling
- **Overlay stylesheet** (`.qss`) - Context-specific overrides
- **Preference configuration** (`.cfg`) - Color settings and preferences

To customize a theme:
1. Copy the theme files to a new name
2. Edit the `.qss` and `.cfg` files as needed
3. Apply using the manual configuration method

## 📋 Requirements

- **FreeCAD Version:** 0.20.0 or later
- **Operating Systems:** Linux, Windows, macOS
- **Python:** 3.8+ (included with FreeCAD)

## 🔧 Technical Details

### File Structure
```
FreeCAD-Workspace-Themes/
├── package.xml                           # Add-on metadata
├── Carbon Designer/
│   ├── Carbon Designer.cfg               # Theme preferences
│   ├── Carbon Designer.qss               # Main stylesheet
│   └── overlay/
│       └── Carbon Designer Overlay.qss   # Overlay stylesheet
├── Slate Professional/
│   ├── Slate Professional.cfg
│   ├── Slate Professional.qss
│   └── overlay/
│       └── Slate Professional Overlay.qss
├── Graphite Professional/
│   ├── Graphite Professional.cfg
│   ├── Graphite Professional.qss
│   └── overlay/
│       └── Graphite Professional Overlay.qss
└── scripts/
    └── install_themes.py                 # Manual installation script
```

### Color Philosophy

**Carbon Designer:** Inspired by carbon fiber materials, featuring deep grays with subtle warm undertones for a professional yet approachable interface.

**Slate Professional:** Based on natural slate colors with cool undertones, designed for sophisticated professional environments requiring visual hierarchy.

**Graphite Professional:** Pure grayscale palette eliminating color temperature bias, ideal for technical work requiring color-neutral precision.

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with multiple FreeCAD versions
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- FreeCAD development team for the excellent CAD platform
- Color theory experts who influenced the palette designs
- FreeCAD community for feedback and testing

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/bcherrington/FreeCAD-Workspace-Themes/issues)
- **Forum:** [FreeCAD Forum](https://forum.freecadweb.org/)
- **Documentation:** [FreeCAD Wiki](https://wiki.freecad.org/)

---

**Made with ❤️ for the FreeCAD community**
