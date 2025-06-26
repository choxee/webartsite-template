import os
import streamlit as st

from webartsite.path_config import contents_path

st.set_page_config(layout="wide")

selected_art_project = "sc25"

# CSS Style Templates Configuration
CSS_TEMPLATES = {
    "Strada Chiusa 2025": {
        "font_imports": [
            "@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');"
        ],
        "root_variables": {
            "--font-primary": '"Bebas Neue", sans-serif',
            "--bg-gradient-primary": "linear-gradient(135deg, rgba(0,0,0,0.85), rgba(20,20,20,0.9), rgba(40,40,40,0.85))",
            "--bg-gradient-secondary": "linear-gradient(135deg, rgba(0,0,0,0.9), rgba(15,15,15,0.95))",
            "--gradient-indigo": "linear-gradient(90deg, #dc2626, #ef4444, #f87171)",
            "--gradient-light-blue": "linear-gradient(135deg, #444444, #666666)",
            "--color-text": "#ffffff",
            "--color-text-dark": "#ffffff",
            "--color-text-muted": "#cccccc",
            "--color-bg": "rgba(0,0,0,0.9)",
            "--color-border": "#444444",
            "--color-input-border": "#666666",
            "--color-input-focus": "#dc2626",
            "--color-alert-border": "#dc2626",
            "--color-alert-text": "#ef4444",
            "--background-image": "url('https://storage.googleapis.com/public-static-contents-test-0/photo-sc-folla-0.jpg')"
        }
    }
}


def generate_custom_css(template_config):
    """Generate CSS with custom font imports and root variables while keeping the rest intact"""

    # Read the base CSS file
    style_path = os.path.join(os.path.dirname(__file__), "pages/{}/0_0_default_style.css".format(selected_art_project))
    with open(style_path, "r") as f:
        base_style = f.read()

    # Extract everything after the root variables section
    # Find the end of the :root section
    root_start = base_style.find(":root {")
    if root_start == -1:
        return base_style  # Fallback if no :root found

    root_end = base_style.find("}", root_start)
    if root_end == -1:
        return base_style  # Fallback if malformed CSS

    # Get the parts before and after the root variables
    before_root = base_style[:root_start]
    after_root = base_style[root_end + 1:]

    # Find and replace font imports section
    import_end = before_root.rfind("*/")
    if import_end != -1:
        # Find the start of font imports section
        import_start = before_root.rfind("/* ==============================================\n   FONT IMPORTS")
        if import_start != -1:
            before_imports = before_root[:import_start]
            after_imports = before_root[import_end + 2:]
        else:
            before_imports = ""
            after_imports = before_root
    else:
        before_imports = ""
        after_imports = before_root

    # Build new font imports section
    font_imports_section = "/* ==============================================\n   FONT IMPORTS\n   ============================================== */\n"
    font_imports_section += "\n".join(template_config["font_imports"])
    font_imports_section += "\n/* ==============================================\n   FONT IMPORTS\n   ============================================== */\n"

    # Build new root variables section with enhanced typography
    root_variables_section = ":root {\n\n  /* Font System */\n"

    # Add font variables first
    if "--font-primary" in template_config["root_variables"]:
        root_variables_section += f"  --font-primary: {template_config['root_variables']['--font-primary']};\n\n"

    # Enhanced font weights, sizes, and spacing
    root_variables_section += """  /* Font Weights */
  --font-weight-light: 400;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  --font-weight-extrabold: 800;

  /* Enhanced Font Sizes (increased) */
  --font-size-xs: 1rem;       /* 16px - increased from 0.85rem */
  --font-size-sm: 1.125rem;   /* 18px - increased from 0.975rem */
  --font-size-base: 1.3rem; /* 22px - increased from 1.25rem */
  --font-size-lg: 1.5rem;     /* 24px - increased from 1.125rem */
  --font-size-xl: 1.625rem;   /* 26px - increased from 1.25rem */
  --font-size-2xl: 1.875rem;  /* 30px - increased from 1.5rem */
  --font-size-3xl: 2.25rem;   /* 36px - increased from 1.875rem */
  --font-size-4xl: 2.75rem;   /* 44px - increased from 2.25rem */
  --font-size-5xl: 3.5rem;    /* 56px - increased from 3rem */
  --font-size-6xl: 4.25rem;   /* 68px - increased from 3.75rem */

  /* Line Heights */
  --line-height-tight: 1.25;
  --line-height-snug: 1.375;
  --line-height-normal: 1.5;
  --line-height-relaxed: 1.625;
  --line-height-loose: 2;

  /* Enhanced Letter Spacing (increased) */
  --letter-spacing-tight: 0.025em;   /* increased from -0.025em */
  --letter-spacing-normal: 0.05em;   /* increased from 0 */
  --letter-spacing-wide: 0.075em;    /* increased from 0.025em */
  --letter-spacing-wider: 0.1em;     /* increased from 0.05em */
  --letter-spacing-widest: 0.15em;   /* increased from 0.1em */

  /* COLOR SCHEME */
"""

    # Add custom color variables
    for var_name, var_value in template_config["root_variables"].items():
        if var_name != "--font-primary":  # Already added above
            root_variables_section += f"  {var_name}: {var_value};\n"

    # Add remaining standard variables
    root_variables_section += """  --transition-fast: 0.2s ease;
  --transition-med: 0.3s ease;
  --radius-sm: 4px;
  --radius: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --shadow-sm: 0 4px 15px rgba(220, 38, 38, 0.1);
  --shadow-md: 0 8px 25px rgba(220, 38, 38, 0.15);
  --shadow-indigo: 0 4px 15px rgba(220, 38, 38, 0.3);
}"""

    # Combine everything
    final_css = before_imports + font_imports_section + after_imports + root_variables_section + after_root

    # Additional CSS modifications for black shaded theme with background image
    additional_css = """

/* ==============================================
   BLACK SHADED THEME WITH BACKGROUND IMAGE
   ============================================== */

/* Background Image Setup */
body, .stApp {
  background-image: var(--background-image) !important;
  background-size: cover !important;
  background-position: center !important;
  background-attachment: fixed !important;
  background-repeat: no-repeat !important;
}

/* Main content overlay */
.stApp {
  background: var(--background-image), var(--bg-gradient-primary) !important;
  background-size: cover, auto !important;
  background-position: center, center !important;
  background-attachment: fixed, scroll !important;
  background-repeat: no-repeat, no-repeat !important;
  backdrop-filter: blur(1px) !important;
}

/* Enhanced Typography with larger fonts and more letter spacing */
html {
  font-size: var(--font-size-base) !important;
  letter-spacing: var(--letter-spacing-normal) !important;
}

body, p, div, span, label {
  font-size: var(--font-size-base) !important;
  letter-spacing: var(--letter-spacing-normal) !important;
}

h1, h2, h3, h4, h5, h6 {
  letter-spacing: var(--letter-spacing-wide) !important;
}

/* ==============================================
   SIDEBAR - DESKTOP AND MOBILE OPTIMIZED
   ============================================== */

/* Desktop sidebar styling */
.stSidebar {
  background: linear-gradient(180deg, rgba(0,0,0,0.85), rgba(20,20,20,0.8)) !important;
  backdrop-filter: blur(10px) !important;
  border-right: 1px solid rgba(255,255,255,0.1) !important;
  box-shadow: 4px 0 20px rgba(0,0,0,0.5) !important;
  position: fixed !important;
  height: 100vh !important;
  overflow-y: auto !important;
  overflow-x: hidden !important;
  z-index: 999999 !important;
}

/* Add title at top of sidebar - above all navigation content */
.stSidebar > div:first-child::before {
  content: "STRADA CHIUSA 2025" !important;
  display: block !important;
  padding: 1.5rem 1.5rem 1rem !important;
  font-family: var(--font-primary) !important;
  font-size: var(--font-size-2xl) !important;
  font-weight: var(--font-weight-bold) !important;
  color: var(--color-text) !important;
  text-transform: uppercase !important;
  letter-spacing: var(--letter-spacing-wide) !important;
  text-align: center !important;
  background: linear-gradient(90deg, #dc2626, #ef4444, #f87171) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  background-clip: text !important;
  filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.9)) !important;
  border-bottom: 2px solid rgba(220, 38, 38, 0.3) !important;
  margin-bottom: 1rem !important;
  position: sticky !important;
  top: 0 !important;
  background-color: rgba(0,0,0,0.9) !important;
  backdrop-filter: blur(10px) !important;
  z-index: 10 !important;
  cursor: pointer !important;
  transition: all 0.2s ease !important;
}

.stSidebar > div:first-child::before:hover {
  filter: drop-shadow(3px 3px 6px rgba(220, 38, 38, 0.8)) !important;
  transform: scale(1.02) !important;
}

/* Alternative approach - target the sidebar header area for close button row */
.stSidebar [data-testid="stSidebarHeader"]::after {
  content: "NASCONDI" !important;
  display: block !important;
  padding: 1rem 1.5rem 0.75rem !important;
  font-family: var(--font-primary) !important;
  font-size: var(--font-size-lg) !important;
  font-weight: var(--font-weight-bold) !important;
  color: var(--color-text) !important;
  text-transform: uppercase !important;
  letter-spacing: var(--letter-spacing-wide) !important;
  text-align: center !important;
  background: linear-gradient(90deg, #666666, #888888, #aaaaaa) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  background-clip: text !important;
  filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.9)) !important;
  border-bottom: 1px solid rgba(170, 170, 170, 0.2) !important;
  margin-bottom: 0.5rem !important;
  cursor: pointer !important;
  transition: all 0.2s ease !important;
}

.stSidebar [data-testid="stSidebarHeader"]::after:hover {
  background: linear-gradient(90deg, #dc2626, #ef4444, #f87171) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  filter: drop-shadow(3px 3px 6px rgba(220, 38, 38, 0.8)) !important;
  transform: scale(1.02) !important;
}

/* Show sidebar title on mobile/tablet when hamburger menu appears */
@media (max-width: 768px) {
  .stSidebar > div:first-child::before,
  .stSidebar [data-testid="stSidebarHeader"]::after {
    display: block !important;
  }
}

/* Hide sidebar title on desktop when sidebar is always visible */
@media (min-width: 769px) {
  .stSidebar > div:first-child::before,
  .stSidebar [data-testid="stSidebarHeader"]::after {
    display: none !important;
  }
}

/* Sidebar content wrapper - ensure proper scrolling */
.stSidebar > div {
  height: 100% !important;
  overflow-y: auto !important;
  overflow-x: hidden !important;
  -webkit-overflow-scrolling: touch !important; /* iOS smooth scrolling */
}

/* Sidebar navigation container */
.stSidebar [data-testid="stSidebarUserContent"] {
  height: 100% !important;
  overflow-y: auto !important;
  overflow-x: hidden !important;
  padding-bottom: 2rem !important; /* Extra space at bottom */
}

.stSidebar [data-testid$="Header"],
.stSidebar [data-testid$="UserContent"] {
  background: rgba(0,0,0,0.6) !important;
  backdrop-filter: blur(5px) !important;
}

.stSidebar [data-testid="stNavSectionHeader"] {
  font-size: var(--font-size-sm) !important;
  letter-spacing: var(--letter-spacing-wider) !important;
}

.stSidebar [data-testid="stNavSectionHeader"]::after {
  background: linear-gradient(90deg, #dc2626, #ef4444, #f87171) !important;
}

.stSidebar [data-testid="stSidebarNavLink"] {
  font-size: var(--font-size-base) !important;
  letter-spacing: var(--letter-spacing-normal) !important;
  background: rgba(0,0,0,0.3) !important;
  margin: 0.5rem 0.5rem !important;
  border-radius: var(--radius) !important;
}

.stSidebar [data-testid="stSidebarNavLink"]:hover {
  background: rgba(220, 38, 38, 0.2) !important;
  backdrop-filter: blur(5px) !important;
}

.stSidebar [data-testid="stSidebarNavLink"]:hover::before,
.stSidebar [aria-current="page"]::before {
  background: linear-gradient(90deg, #dc2626, #ef4444, #f87171) !important;
}

.stSidebar [aria-current="page"] {
  background: rgba(220, 38, 38, 0.3) !important;
  border: 1px solid rgba(220, 38, 38, 0.5) !important;
  box-shadow: 0 4px 15px rgba(220, 38, 38, 0.3) !important;
}

/* Custom scrollbar for sidebar */
.stSidebar::-webkit-scrollbar {
  width: 6px !important;
}

.stSidebar::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.3) !important;
}

.stSidebar::-webkit-scrollbar-thumb {
  background: rgba(220, 38, 38, 0.5) !important;
  border-radius: var(--radius-sm) !important;
}

.stSidebar::-webkit-scrollbar-thumb:hover {
  background: rgba(220, 38, 38, 0.7) !important;
}

/* Black shaded header with glass effect */
.stAppHeader {
  background: linear-gradient(90deg, rgba(0,0,0,0.85), rgba(20,20,20,0.8)) !important;
  backdrop-filter: blur(10px) !important;
  box-shadow: 0 4px 15px rgba(0,0,0,0.5) !important;
  border-bottom: 1px solid rgba(220, 38, 38, 0.3) !important;
}

/* Navigation items in header */
.rc-overflow > * {
  background: rgba(0,0,0,0.6) !important;
  border: 1px solid rgba(220, 38, 38, 0.3) !important;
  font-size: var(--font-size-sm) !important;
  letter-spacing: var(--letter-spacing-normal) !important;
  backdrop-filter: blur(5px) !important;
}

.rc-overflow > *:hover {
  background: rgba(220, 38, 38, 0.2) !important;
  border: 1px solid rgba(220, 38, 38, 0.5) !important;
}

/* Main content area with glass effect */
.stMainBlockContainer {
  background: rgba(0,0,0,0.7) !important;
  backdrop-filter: blur(3px) !important;
  border: 1px solid rgba(255,255,255,0.1) !important;
}

.stMain {
  background: rgba(0,0,0,0.5) !important;
  backdrop-filter: blur(2px) !important;
}

/* Form elements with enhanced typography */
.stForm {
  background: rgba(0,0,0,0.8) !important;
  backdrop-filter: blur(5px) !important;
  border: 1px solid rgba(220, 38, 38, 0.2) !important;
}

.stTextInput label {
  font-size: var(--font-size-lg) !important;
  letter-spacing: var(--letter-spacing-normal) !important;
}

.stTextInput input {
  font-size: var(--font-size-base) !important;
  letter-spacing: var(--letter-spacing-normal) !important;
  background: rgba(0,0,0,0.6) !important;
  backdrop-filter: blur(3px) !important;
  color: var(--color-text) !important;
}

.stFormSubmitButton button {
  background: linear-gradient(90deg, #dc2626, #ef4444, #f87171) !important;
  box-shadow: 0 4px 15px rgba(220, 38, 38, 0.3) !important;
  font-size: var(--font-size-lg) !important;
  letter-spacing: var(--letter-spacing-wide) !important;
}

.stFormSubmitButton button:hover {
  box-shadow: 0 8px 25px rgba(220, 38, 38, 0.4) !important;
  background: linear-gradient(135deg, #b91c1c, #dc2626) !important;
}

/* Alert containers */
.stAlertContainer {
  background: rgba(0,0,0,0.8) !important;
  backdrop-filter: blur(5px) !important;
  border: 1px solid rgba(220, 38, 38, 0.3) !important;
}

.stAlertContainer p {
  font-size: var(--font-size-base) !important;
  letter-spacing: var(--letter-spacing-normal) !important;
}

/* Headings with enhanced spacing */
.stHeading h1 {
  font-size: var(--font-size-5xl) !important;
  letter-spacing: var(--letter-spacing-wide) !important;
}

/* Enhanced shadows to match black theme */
.shadow-sm { box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important; }
.shadow-md { box-shadow: 0 8px 25px rgba(0,0,0,0.4) !important; }
.shadow-indigo { box-shadow: 0 4px 15px rgba(220, 38, 38, 0.3) !important; }

/* AGGRESSIVE FULL-WIDTH - NO MARGINS */
.stApp,
.stMain,
.stMainBlockContainer,
.stVerticalBlock,
.stForm,
.stAlertContainer,
.stAppEmbeddingId-sydrjgxn657a,
.st-ae {
  margin: 10 !important;
  padding: 0.5rem 0.25rem !important;  /* Minimal padding for readability */
  width: 100% !important;
  max-width: 100% !important;
}

/* Only keep minimal padding for text readability */
.stMainBlockContainer {
  padding: 1rem 0.5rem !important;
}

/* ==============================================
   HIDE STREAMLIT ELEMENT TOOLBAR
   ============================================== */

/* Hide the element toolbar completely */
.stElementToolbar {
  display: none !important;
  visibility: hidden !important;
}

/* Alternative selector if the above doesn't work */
[data-testid="stElementToolbar"] {
  display: none !important;
  visibility: hidden !important;
}

/* Hide toolbar buttons specifically */
.stElementToolbarButton {
  display: none !important;
}

/* Hide any floating action buttons */
.element-container .stElementToolbar,
.stPlotlyChart .stElementToolbar,
.stDataFrame .stElementToolbar {
  display: none !important;
}

/* ==============================================
   INCREASED TRANSPARENCY FOR BACKGROUND VISIBILITY
   ============================================== */

/* Main App Container - More Transparent */
.stApp {
  background: rgba(15, 23, 42, 0.3) !important; /* Very transparent */
}

/* Main Content Areas - Highly Transparent */
.stMain {
  background: rgba(17, 24, 39, 0.2) !important; /* Very transparent */
  backdrop-filter: blur(2px) !important; /* Light blur for readability */
}

.stMainBlockContainer {
  background: rgba(15, 23, 42, 0.25) !important; /* Very transparent */
  backdrop-filter: blur(3px) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important; /* Subtle border */
}

/* Container Elements - More Transparent */
.stAppEmbeddingId-sydrjgxn657a,
.st-ae {
  background: rgba(15, 23, 42, 0.3) !important;
  backdrop-filter: blur(3px) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
}

.stVerticalBlock {
  background: rgba(0, 0, 0, 0.1) !important; /* Very light overlay */
}

/* Form Elements - Transparent but Readable */
.stForm {
  background: rgba(15, 23, 42, 0.4) !important; /* Slightly more opaque for readability */
  backdrop-filter: blur(5px) !important;
  border: 1px solid rgba(255, 255, 255, 0.15) !important;
}

/* Alert Containers - Transparent */
.stAlertContainer {
  background: rgba(17, 24, 39, 0.4) !important;
  backdrop-filter: blur(5px) !important;
  border: 1px solid rgba(236, 72, 153, 0.3) !important;
}

/* Text Input Backgrounds - Semi-transparent */
.stTextInput input {
  background: rgba(15, 23, 42, 0.6) !important;
  backdrop-filter: blur(3px) !important;
  color: #f8fafc !important;
}

/* Ensure text remains readable with semi-transparent backgrounds */
.stTextInput label {
  color: #f8fafc !important;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7) !important;
}

/* Add text shadow to improve readability on transparent backgrounds */
p, h1, h2, h3, h4, h5, h6 {
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5) !important;
}

/* Ultra Transparent Version - Use with Caution */
/* This makes containers almost invisible - only use if background image is not too busy */

.stMainBlockContainer,
.stMain,
.stVerticalBlock {
  background: rgba(0, 0, 0, 0.05) !important;
  backdrop-filter: blur(1px) !important;
}

/* Make topbar slightly higher */
.stAppHeader {
 min-height: 120px !important;
}

.stAppToolbar {
 padding: 2rem 2rem !important;
}

/* Move topbar buttons and logo slightly below */
.rc-overflow {
 margin-top: 0.5rem !important;
}

.stAppToolbar::before {
 top: calc(50% + 0.25rem) !important;
}

/* Remove external hover containers of topbar buttons */
.rc-overflow-item {
 background: none !important;
 border: none !important;
 box-shadow: none !important;
 padding: 0 !important;
}

.rc-overflow-item:hover {
 background: none !important;
 border: none !important;
 box-shadow: none !important;
 transform: none !important;
}

/* Style stTopNavSection like stBaseButton */
div[data-testid="stTopNavSection"] {
 background: linear-gradient(90deg, #dc2626, #ef4444, #f87171) !important;
 color: #ffffff !important;
 border: none !important;
 border-radius: var(--radius-lg) !important;
 padding: 0.875rem 2rem !important;
 font-family: var(--font-primary) !important;
 font-size: var(--font-size-base) !important;
 font-weight: var(--font-weight-bold) !important;
 text-transform: uppercase !important;
 letter-spacing: var(--letter-spacing-wide) !important;
 cursor: pointer !important;
 transition: var(--transition-med) !important;
 box-shadow: var(--shadow-sm) !important;
 text-shadow: 1px 1px 2px rgba(0,0,0,0.5) !important;
}

div[data-testid="stTopNavSection"]:hover {
 transform: translateY(-2px) !important;
 box-shadow: var(--shadow-md) !important;
 background: linear-gradient(135deg, #b91c1c, #dc2626) !important;
}

/* Allow more buttons in topbar before collapsing */
.rc-overflow {
 min-width: 800px !important;
 max-width: none !important;
 flex-wrap: nowrap !important;
}

.rc-overflow-item {
 flex-shrink: 0 !important;
 white-space: nowrap !important;
}

/* Allow more buttons without cutting left and right */
.rc-overflow {
 margin: 0.5rem 1rem !important;
 width: calc(100% - 120px) !important;
 max-width: none !important;
 flex-wrap: nowrap !important;
 overflow: visible !important;
}

.rc-overflow-item {
 flex-shrink: 1 !important;
 min-width: fit-content !important;
 white-space: nowrap !important;
}

.stAppToolbar {
 overflow: visible !important;
 width: 100% !important;
}

/* Move topbar buttons a bit right */
.rc-overflow {
 margin-left: 15rem !important;
}

/* Force topbar buttons centered from the start */
.rc-overflow {
 position: absolute !important;
 left: 50.5% !important;
 transform: translateX(-50%) !important;
 margin: 0.5rem 0 !important;
 width: auto !important;
 flex: none !important;
 justify-content: center !important;
}

/* Ensure parent container allows absolute positioning */
.stAppToolbar {
 position: relative !important;
}

/* ==============================================
   TITLE IN TOPBAR AND SIDEBAR
   ============================================== */

/* Add title to topbar - always centered */
.stAppToolbar::after {
  content: "STRADA CHIUSA 2025" !important;
  position: absolute !important;
  left: 50% !important;
  top: 50% !important;
  transform: translate(-50%, -50%) !important;
  font-family: var(--font-primary) !important;
  font-size: var(--font-size-xl) !important;
  font-weight: var(--font-weight-bold) !important;
  color: var(--color-text) !important;
  text-transform: uppercase !important;
  letter-spacing: var(--letter-spacing-wide) !important;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.8) !important;
  z-index: 1 !important;
  background: linear-gradient(90deg, #dc2626, #ef4444, #f87171) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  background-clip: text !important;
  filter: drop-shadow(1px 1px 2px rgba(0,0,0,0.9)) !important;
  white-space: nowrap !important;
  pointer-events: none !important; /* Ensures it doesn't interfere with buttons */
}

/* Hide title when sidebar is visible (desktop) - show only when hamburger menu appears */
@media (max-width: 768px) {
  .stAppToolbar::after {
    display: block !important;
  }
}

@media (min-width: 769px) {
  .stAppToolbar::after {
    display: none !important;
  }
}

/* Hide topbar navigation buttons when title is shown to avoid overlap */
@media (max-width: 768px) {
  .rc-overflow {
    display: none !important;
  }

  /* Ensure hamburger/sidebar button remains visible and accessible */
  .stAppHeader .stMainMenu,
  .stAppHeader [data-testid="stMainMenu"],
  .stAppHeader button[kind="header"] {
    display: block !important;
    z-index: 10 !important;
    position: relative !important;
  }
}

/* Add JavaScript-like click functionality through CSS */
.stAppToolbar::after {
  cursor: pointer !important;
  pointer-events: auto !important; /* Enable clicking */
}

.stAppToolbar::after:hover {
  filter: drop-shadow(2px 2px 4px rgba(220, 38, 38, 0.8)) !important;
  transform: translate(-50%, -50%) scale(1.02) !important;
  transition: all 0.2s ease !important;
}

h1, h2, h3, h4, h5, h6 {
margin-left: 3rem;
margin-right: 3rem;
 text-align: center;
}

/* ==============================================
   MOBILE RESPONSIVE DESIGN - ENHANCED SIDEBAR
   ============================================== */

/* Tablet and mobile breakpoints */
@media (max-width: 1024px) {
  .rc-overflow {
    margin: 0 40px 0 200px !important;
    gap: 0.5rem !important;
  }

  .stSidebar {
    width: 280px !important;
  }
}

@media (max-width: 768px) {
  :root {
    --font-size-5xl: 2.75rem !important;
    --font-size-4xl: 2.25rem !important;
    --font-size-3xl: 1.875rem !important;
    --font-size-base: 1.25rem !important;
  }

  /* Reduce topbar height on mobile */
  .stAppHeader {
    min-height: 60px !important; /* Reduced from 120px */
  }

  .stAppToolbar {
    padding: 0.75rem 1rem !important; /* Reduced from 2rem 2rem */
  }

  /* Mobile topbar title adjustments */
  .stAppToolbar::after {
    font-size: var(--font-size-lg) !important; /* Smaller on mobile */
    letter-spacing: var(--letter-spacing-normal) !important;
  }

  /* Mobile button positioning - buttons hidden, only hamburger visible */

  .stAppToolbar::before {
    top: calc(50% + 0.125rem) !important; /* Adjusted for smaller height */
    width: 35px !important; /* Slightly smaller logo */
    height: 35px !important;
  }

  /* Mobile sidebar optimizations */
  .stSidebar {
    width: 100vw !important;
    height: 100vh !important;
    height: 100dvh !important; /* Dynamic viewport height for mobile */
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    z-index: 999999 !important;
    overflow-y: auto !important;
    overflow-x: hidden !important;
    -webkit-overflow-scrolling: touch !important;
    transform: translateX(-100%) !important;
    transition: transform 0.3s ease-in-out !important;
    padding-top: 80px !important; /* Extra vertical space at top for mobile */
  }

  /* When sidebar is open on mobile */
  .stSidebar[data-testid="stSidebar"][aria-expanded="true"],
  .stSidebar.sidebar-expanded {
    transform: translateX(0) !important;
  }

  /* Sidebar content on mobile */
  .stSidebar > div {
    height: 100% !important;
    overflow-y: auto !important;
    overflow-x: hidden !important;
    -webkit-overflow-scrolling: touch !important;
    padding-bottom: 3rem !important;
    padding-top: 2rem !important; /* Additional top padding for mobile content */
  }

  /* First navigation section gets extra top margin on mobile */
  .stSidebar [data-testid="stSidebarUserContent"] > div:first-child {
    margin-top: 1.5rem !important;
  }

  /* Mobile navigation links - larger touch targets */
  .stSidebar [data-testid="stSidebarNavLink"] {
    padding: 1.25rem 1.5rem !important;
    margin: 0.75rem 1rem !important;
    font-size: var(--font-size-lg) !important;
    min-height: 50px !important;
    display: flex !important;
    align-items: center !important;
  }

  /* Mobile section headers */
  .stSidebar [data-testid="stNavSectionHeader"] {
    padding: 1.5rem 1.5rem 1rem !important;
    font-size: var(--font-size-base) !important;
  }

  /* Background overlay when sidebar is open */
  .stSidebar::before {
    content: "" !important;
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    width: 100vw !important;
    height: 100vh !important;
    background: rgba(0, 0, 0, 0.5) !important;
    z-index: -1 !important;
    opacity: 0 !important;
    transition: opacity 0.3s ease-in-out !important;
  }

  .stSidebar[aria-expanded="true"]::before,
  .stSidebar.sidebar-expanded::before {
    opacity: 1 !important;
  }

  /* Main content adjustments for mobile */
  .stApp {
    background-attachment: scroll !important;
  }

  .stMainBlockContainer {
    margin: 0.25rem !important;
    padding: 1rem !important;
  }

  .rc-overflow {
    margin: 0 20px 0 80px !important;
    flex-wrap: wrap !important;
    gap: 0.25rem !important;
  }

  .stAppToolbar::before {
    left: auto !important;
    right: 1rem !important;
    width: 30px !important; /* Further reduced for small screens */
    height: 30px !important;
  }

  /* Mobile hamburger menu visibility */
  .stAppHeader .stMainMenu {
    display: block !important;
  }

  /* Ensure smooth scrolling on iOS */
  body {
    -webkit-overflow-scrolling: touch !important;
  }
}

@media (max-width: 576px) {
  :root {
    --font-size-5xl: 2.5rem !important;
    --font-size-4xl: 2rem !important;
    --font-size-3xl: 1.75rem !important;
    --font-size-base: 1rem !important;
  }

  .stMainBlockContainer {
    margin: 0.125rem !important;
    padding: 0.75rem !important;
  }

  .stForm {
    padding: 1.5rem !important;
  }

  /* Mobile topbar title - even smaller on very small screens */
  .stAppToolbar::after {
    font-size: var(--font-size-base) !important;
  }

  /* Extra small screens - full width sidebar with more top space */
  .stSidebar {
    width: 100vw !important;
    padding-top: 100px !important; /* Even more top space for very small screens */
  }

  /* Sidebar title smaller on very small screens */
  .stSidebar::before {
    font-size: var(--font-size-xl) !important;
    padding: 1rem 1rem 0.75rem !important;
  }

  /* First content section gets extra spacing */
  .stSidebar [data-testid="stSidebarUserContent"] > div:first-child {
    margin-top: 2rem !important;
  }

  /* Larger touch targets for very small screens */
  .stSidebar [data-testid="stSidebarNavLink"] {
    padding: 1.5rem 1.5rem !important;
    margin: 1rem 1rem !important;
    font-size: var(--font-size-lg) !important;
    min-height: 60px !important;
  }
}

/* ==============================================
   SIDEBAR SCROLL ENHANCEMENTS FOR ALL DEVICES
   ============================================== */

/* Enhanced scrollbar for better mobile experience */
.stSidebar {
  scrollbar-width: thin !important;
  scrollbar-color: rgba(220, 38, 38, 0.5) rgba(0, 0, 0, 0.3) !important;
}

/* Webkit scrollbar for mobile browsers */
.stSidebar::-webkit-scrollbar {
  width: 8px !important;
  background: rgba(0, 0, 0, 0.2) !important;
}

.stSidebar::-webkit-scrollbar-thumb {
  background: rgba(220, 38, 38, 0.6) !important;
  border-radius: 4px !important;
  border: 1px solid rgba(0, 0, 0, 0.1) !important;
}

.stSidebar::-webkit-scrollbar-thumb:hover {
  background: rgba(220, 38, 38, 0.8) !important;
}

.stSidebar::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.1) !important;
  border-radius: 4px !important;
}

/* Ensure sidebar content doesn't get cut off */
.stSidebar [data-testid="stSidebarUserContent"] {
  min-height: 100vh !important;
  padding-bottom: 4rem !important;
}

/* Force scroll behavior */
.stSidebar,
.stSidebar > div,
.stSidebar [data-testid="stSidebarUserContent"] {
  scroll-behavior: smooth !important;
  overflow-y: auto !important;
  overflow-x: hidden !important;
}

/* iOS specific fixes */
@supports (-webkit-touch-callout: none) {
  .stSidebar {
    -webkit-overflow-scrolling: touch !important;
    transform: translate3d(0, 0, 0) !important; /* Hardware acceleration */
  }

  .stSidebar > div {
    -webkit-overflow-scrolling: touch !important;
    transform: translate3d(0, 0, 0) !important;
  }
}


"""

    final_css += additional_css

    return final_css


# Function to set background image
def set_background_image(image_url):
    """Update the background image URL in the CSS template"""
    CSS_TEMPLATES["Strada Chiusa 2025"]["root_variables"]["--background-image"] = f"url('{image_url}')"


# Example usage: uncomment and modify the URL to set your background image
# set_background_image("https://your-domain.com/path-to-your-background-image.jpg")

selected_template = "Strada Chiusa 2025"
selected_config = CSS_TEMPLATES[selected_template]
custom_css = generate_custom_css(selected_config)
st.markdown("<style>" + custom_css + "</style>", unsafe_allow_html=True)

pages = {
    "SC25": [
        st.Page("pages/{}/0_1_home.py".format(selected_art_project), title="SC25"),
        st.Page("pages/{}/0_2_lineup.py".format(selected_art_project), title="Lineup"),
        st.Page("pages/{}/0_3_full_schedule.py".format(selected_art_project), title="Programma completo"),

    ],
    "Chi siamo": [
        st.Page("pages/{}/1_2_stradachiusa.py".format(selected_art_project), title="Strada Chiusa"),
        st.Page("pages/{}/1_2_onda.py".format(selected_art_project), title="L'Onda"),
        st.Page("pages/{}/1_3_network.py".format(selected_art_project), title="Rete"),
        st.Page("pages/{}/4_1_history.py".format(selected_art_project), title="Edizioni passate"),

    ],
    "Partners": [
        st.Page("pages/{}/4_1_partners.py".format(selected_art_project), title="Partners"),
        st.Page("pages/{}/4_1_donations.py".format(selected_art_project), title="Donazioni"),
    ],
    "Contatti": [
        st.Page("pages/{}/4_1_collaborate.py".format(selected_art_project), title="Collabora"),
        st.Page("pages/{}/4_1_contacts_social.py".format(selected_art_project), title="Social"),
    ],
}

pg = st.navigation(pages, position="top")

# Add JavaScript for sidebar auto-close targeting the double arrow button
st.markdown("""
<script>
// Function to navigate to home page when title is clicked
function navigateToHome() {
    if (window.parent && window.parent.location) {
        window.parent.location.href = window.parent.location.origin + window.parent.location.pathname;
    } else {
        window.location.href = window.location.origin + window.location.pathname;
    }
}

// Function to find and click the double arrow close button
function clickDoubleArrowButton() {
    console.log('Looking for double arrow close button...');

    // Look for buttons that might contain double arrows or collapse functionality
    const potentialButtons = document.querySelectorAll('button, [role="button"]');

    for (let button of potentialButtons) {
        // Check if button is in the sidebar area
        const isInSidebar = button.closest('[data-testid="stSidebar"]') || 
                           button.closest('.stSidebar') ||
                           button.closest('[data-testid="stSidebarHeader"]');

        if (!isInSidebar) continue;

        // Check button content for double arrows or collapse indicators
        const buttonText = button.textContent || '';
        const buttonHTML = button.innerHTML || '';
        const ariaLabel = button.getAttribute('aria-label') || '';
        const title = button.getAttribute('title') || '';

        // Look for double arrow patterns
        const hasDoubleArrow = 
            buttonText.includes('«') || buttonText.includes('»') ||
            buttonText.includes('<<') || buttonText.includes('>>') ||
            buttonText.includes('‹‹') || buttonText.includes('››') ||
            buttonHTML.includes('&#x') || // Unicode arrows
            buttonHTML.includes('&lt;&lt;') || buttonHTML.includes('&gt;&gt;') ||
            ariaLabel.toLowerCase().includes('collapse') ||
            ariaLabel.toLowerCase().includes('close') ||
            title.toLowerCase().includes('collapse') ||
            title.toLowerCase().includes('close');

        // Check for specific Streamlit close button classes or data attributes
        const hasCloseIndicators = 
            button.getAttribute('data-testid') === 'stSidebarCollapseButton' ||
            button.className.includes('collapse') ||
            button.className.includes('close') ||
            button.getAttribute('kind') === 'secondary';

        if (hasDoubleArrow || hasCloseIndicators) {
            console.log('Found potential double arrow button:', {
                element: button,
                text: buttonText,
                html: buttonHTML,
                ariaLabel: ariaLabel,
                title: title,
                classes: button.className,
                testId: button.getAttribute('data-testid')
            });

            try {
                // Try multiple ways to click the button
                button.click();
                console.log('Successfully clicked double arrow button!');
                return true;
            } catch (e) {
                console.log('Direct click failed, trying events:', e);

                // Try mouse events
                try {
                    button.dispatchEvent(new MouseEvent('mousedown', { bubbles: true }));
                    button.dispatchEvent(new MouseEvent('mouseup', { bubbles: true }));
                    button.dispatchEvent(new MouseEvent('click', { bubbles: true }));
                    console.log('Successfully triggered mouse events!');
                    return true;
                } catch (e2) {
                    console.log('Mouse events failed:', e2);
                }
            }
        }
    }

    console.log('Could not find double arrow close button');
    return false;
}

// Enhanced navigation click detection with auto-close
function setupNavigationAutoClose() {
    console.log('Setting up navigation auto-close...');

    // Use event delegation on document to catch all clicks
    document.addEventListener('click', function(e) {
        // Only process on mobile
        if (window.innerWidth > 768) return;

        // Check if click is in sidebar
        const sidebar = e.target.closest('[data-testid="stSidebar"], .stSidebar');
        if (!sidebar) return;

        // Ignore clicks on our custom titles
        if (e.target.closest('.custom-sidebar-title, .custom-sidebar-header-title')) return;

        // Ignore clicks on the close button itself
        const isCloseButton = e.target.closest('button, [role="button"]');
        if (isCloseButton) {
            const buttonText = isCloseButton.textContent || '';
            const buttonHTML = isCloseButton.innerHTML || '';
            const ariaLabel = isCloseButton.getAttribute('aria-label') || '';

            // If it's the close button, don't auto-close (let it work normally)
            if (buttonText.includes('«') || buttonText.includes('»') ||
                buttonHTML.includes('&#x') ||
                ariaLabel.toLowerCase().includes('collapse') ||
                ariaLabel.toLowerCase().includes('close')) {
                console.log('Close button clicked, not auto-closing');
                return;
            }
        }

        // Check if clicked element is a navigation link
        const navLink = e.target.closest('a[href], [role="button"], button');
        if (!navLink) return;

        // Make sure it's actually a navigation item, not other sidebar elements
        const isNavigation = 
            navLink.closest('[data-testid="stSidebarNavItems"]') ||
            navLink.closest('[data-testid="stSidebarUserContent"]') ||
            (navLink.tagName === 'A' && navLink.getAttribute('href'));

        if (isNavigation) {
            console.log('Navigation link clicked:', navLink);
            console.log('Will auto-close sidebar in 300ms...');

            // Delay to allow navigation to start, then close sidebar
            setTimeout(function() {
                console.log('Attempting to close sidebar...');
                clickDoubleArrowButton();
            }, 300);
        }
    }, true); // Use capture phase to catch events early
}

// Add titles and functionality
function addSidebarTitle() {
    const sidebar = document.querySelector('.stSidebar');
    const sidebarFirstChild = document.querySelector('.stSidebar > div:first-child');

    if (sidebar && sidebarFirstChild && !document.querySelector('.custom-sidebar-title')) {
        const titleElement = document.createElement('div');
        titleElement.className = 'custom-sidebar-title';
        titleElement.innerHTML = 'STRADA CHIUSA 2025';
        titleElement.style.cssText = `
            position: sticky !important;
            top: 0 !important;
            z-index: 100 !important;
            padding: 1.5rem 1.5rem 1rem !important;
            font-family: "Bebas Neue", sans-serif !important;
            font-size: 1.875rem !important;
            font-weight: 700 !important;
            color: #ffffff !important;
            text-transform: uppercase !important;
            letter-spacing: 0.075em !important;
            text-align: center !important;
            background: linear-gradient(90deg, #dc2626, #ef4444, #f87171) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            background-clip: text !important;
            filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.9)) !important;
            border-bottom: 2px solid rgba(220, 38, 38, 0.3) !important;
            margin-bottom: 1rem !important;
            cursor: pointer !important;
            transition: all 0.2s ease !important;
            background-color: rgba(0,0,0,0.9) !important;
            backdrop-filter: blur(10px) !important;
        `;

        titleElement.addEventListener('click', function() {
            navigateToHome();
            if (window.innerWidth <= 768) {
                setTimeout(clickDoubleArrowButton, 200);
            }
        });

        titleElement.addEventListener('mouseover', function() {
            this.style.filter = 'drop-shadow(3px 3px 6px rgba(220, 38, 38, 0.8))';
            this.style.transform = 'scale(1.02)';
        });
        titleElement.addEventListener('mouseout', function() {
            this.style.filter = 'drop-shadow(2px 2px 4px rgba(0,0,0,0.9))';
            this.style.transform = 'scale(1)';
        });

        sidebarFirstChild.insertBefore(titleElement, sidebarFirstChild.firstChild);
    }
}

function addSidebarHeaderTitle() {
    const sidebarHeader = document.querySelector('[data-testid="stSidebarHeader"]');

    if (sidebarHeader && !document.querySelector('.custom-sidebar-header-title')) {
        const titleElement = document.createElement('div');
        titleElement.className = 'custom-sidebar-header-title';
        titleElement.innerHTML = 'NASCONDI';
        titleElement.style.cssText = `
            padding: 0.5rem 1rem !important;
            font-family: "Bebas Neue", sans-serif !important;
            font-size: 1.2rem !important;
            font-weight: 700 !important;
            color: #ffffff !important;
            text-transform: uppercase !important;
            letter-spacing: 0.075em !important;
            text-align: center !important;
            background: linear-gradient(90deg, #666666, #888888, #aaaaaa) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            background-clip: text !important;
            filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.9)) !important;
            cursor: pointer !important;
            transition: all 0.2s ease !important;
            margin-left: 1rem !important;
            display: inline-block !important;
        `;

        titleElement.addEventListener('click', clickDoubleArrowButton);

        titleElement.addEventListener('mouseover', function() {
            this.style.background = 'linear-gradient(90deg, #dc2626, #ef4444, #f87171)';
            this.style.filter = 'drop-shadow(3px 3px 6px rgba(220, 38, 38, 0.8))';
            this.style.transform = 'scale(1.05)';
        });
        titleElement.addEventListener('mouseout', function() {
            this.style.background = 'linear-gradient(90deg, #666666, #888888, #aaaaaa)';
            this.style.filter = 'drop-shadow(2px 2px 4px rgba(0,0,0,0.9))';
            this.style.transform = 'scale(1)';
        });

        sidebarHeader.appendChild(titleElement);
    }
}

// Make close button row sticky and always visible
function makeCloseRowSticky() {
    const sidebarHeader = document.querySelector('[data-testid="stSidebarHeader"]');
    if (!sidebarHeader) return;

    sidebarHeader.style.cssText += `
        position: sticky !important;
        top: 0 !important;
        z-index: 1000 !important;
        background: rgba(0,0,0,0.9) !important;
        backdrop-filter: blur(10px) !important;
        border-bottom: 2px solid rgba(220, 38, 38, 0.3) !important;
        padding: 1rem !important;
        margin-bottom: 1rem !important;
    `;
}

// Enhanced topbar title click detection
document.addEventListener('click', function(e) {
    const toolbar = document.querySelector('.stAppToolbar');

    if (toolbar && e.target.closest('.stAppToolbar')) {
        const rect = toolbar.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2;
        const centerY = rect.top + rect.height / 2;

        if (Math.abs(e.clientX - centerX) < 120 && Math.abs(e.clientY - centerY) < 25) {
            navigateToHome();
        }
    }
});

// Debug function to examine all buttons in sidebar
function debugSidebarButtons() {
    console.log('=== SIDEBAR BUTTONS DEBUG ===');

    const allButtons = document.querySelectorAll('button, [role="button"]');
    const sidebarButtons = Array.from(allButtons).filter(btn => 
        btn.closest('[data-testid="stSidebar"]') || btn.closest('.stSidebar')
    );

    console.log(`Found ${sidebarButtons.length} buttons in sidebar:`);

    sidebarButtons.forEach((btn, index) => {
        console.log(`Button ${index + 1}:`, {
            element: btn,
            text: btn.textContent?.trim(),
            innerHTML: btn.innerHTML,
            ariaLabel: btn.getAttribute('aria-label'),
            title: btn.getAttribute('title'),
            className: btn.className,
            testId: btn.getAttribute('data-testid'),
            kind: btn.getAttribute('kind'),
            position: {
                top: btn.getBoundingClientRect().top,
                left: btn.getBoundingClientRect().left
            }
        });
    });

    console.log('==============================');
}

// Main initialization
function initializeSidebar() {
    console.log('Initializing sidebar functionality...');

    addSidebarTitle();
    addSidebarHeaderTitle();
    makeCloseRowSticky();
    setupNavigationAutoClose();

    // Run debug to see what buttons are available
    setTimeout(debugSidebarButtons, 1000);
}

// Initialize when ready
document.addEventListener('DOMContentLoaded', initializeSidebar);
setTimeout(initializeSidebar, 1000);

// Monitor for changes
setInterval(function() {
    if (window.innerWidth <= 768) {
        addSidebarTitle();
        addSidebarHeaderTitle();
        makeCloseRowSticky();
    }
}, 3000);

// MutationObserver for dynamic updates
const observer = new MutationObserver(function(mutations) {
    let shouldUpdate = false;

    mutations.forEach(function(mutation) {
        if (mutation.type === 'childList') {
            mutation.addedNodes.forEach(function(node) {
                if (node.nodeType === 1 && node.querySelector && (
                    node.querySelector('[data-testid="stSidebar"]') ||
                    node.getAttribute('data-testid') === 'stSidebar'
                )) {
                    shouldUpdate = true;
                }
            });
        }
    });

    if (shouldUpdate) {
        console.log('Detected sidebar changes, re-initializing...');
        setTimeout(initializeSidebar, 300);
    }
});

observer.observe(document.body, {
    childList: true,
    subtree: true
});
</script>
""", unsafe_allow_html=True)

pg.run()