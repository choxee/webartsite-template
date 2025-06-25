import os
import streamlit as st

from webartsite.path_config import contents_path

st.set_page_config(layout="wide")

selected_art_project = "pezze"

# CSS Style Templates Configuration
CSS_TEMPLATES = {
    "Neon Cyber (Default)": {
        "font_imports": [
            "@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&display=swap');"
        ],
        "root_variables": {
            "--font-primary": '"Orbitron", monospace',
            "--bg-gradient-primary": "linear-gradient(135deg, #0f0f23, #1e1b4b, #312e81)",
            "--bg-gradient-secondary": "linear-gradient(135deg, #111827, #1f2937)",
            "--gradient-indigo": "linear-gradient(90deg, #ec4899, #f97316, #eab308)",
            "--gradient-light-blue": "linear-gradient(135deg, #1e1b4b, #312e81)",
            "--color-text": "#f8fafc",
            "--color-text-dark": "#ffffff",
            "--color-text-muted": "#94a3b8",
            "--color-bg": "#0f172a",
            "--color-border": "#334155",
            "--color-input-border": "#475569",
            "--color-input-focus": "#ec4899",
            "--color-alert-border": "#ec4899",
            "--color-alert-text": "#f97316"
        }
    },
    "Elegant Modern": {
        "font_imports": [
            "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');",
            "@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700;800;900&display=swap');"
        ],
        "root_variables": {
            "--font-primary": '"Inter", sans-serif',
            "--bg-gradient-primary": "linear-gradient(135deg, #1e293b, #334155, #475569)",
            "--bg-gradient-secondary": "linear-gradient(135deg, #f8fafc, #e2e8f0)",
            "--gradient-indigo": "linear-gradient(90deg, #6366f1, #8b5cf6, #a855f7)",
            "--gradient-light-blue": "linear-gradient(135deg, #0ea5e9, #06b6d4)",
            "--color-text": "#1e293b",
            "--color-text-dark": "#0f172a",
            "--color-text-muted": "#64748b",
            "--color-bg": "#ffffff",
            "--color-border": "#e2e8f0",
            "--color-input-border": "#cbd5e1",
            "--color-input-focus": "#6366f1",
            "--color-alert-border": "#6366f1",
            "--color-alert-text": "#4338ca"
        }
    },
    "Retro Wave": {
        "font_imports": [
            "@import url('https://fonts.googleapis.com/css2?family=Audiowide&display=swap');",
            "@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@300;400;500;600;700&display=swap');"
        ],
        "root_variables": {
            "--font-primary": '"Audiowide", sans-serif',
            "--bg-gradient-primary": "linear-gradient(135deg, #0a0a23, #1a1a2e, #16213e)",
            "--bg-gradient-secondary": "linear-gradient(135deg, #0f3460, #533a7b)",
            "--gradient-indigo": "linear-gradient(90deg, #ff006e, #fb5607, #ffbe0b)",
            "--gradient-light-blue": "linear-gradient(135deg, #8338ec, #3a86ff)",
            "--color-text": "#ffffff",
            "--color-text-dark": "#ffffff",
            "--color-text-muted": "#c7d2fe",
            "--color-bg": "#0a0a23",
            "--color-border": "#533a7b",
            "--color-input-border": "#8338ec",
            "--color-input-focus": "#ff006e",
            "--color-alert-border": "#ff006e",
            "--color-alert-text": "#ffbe0b"
        }
    },
    "Nature Organic": {
        "font_imports": [
            "@import url('https://fonts.googleapis.com/css2?family=Comfortaa:wght@300;400;500;600;700&display=swap');",
            "@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;500;600;700;800&display=swap');"
        ],
        "root_variables": {
            "--font-primary": '"Comfortaa", sans-serif',
            "--bg-gradient-primary": "linear-gradient(135deg, #1a3b2e, #2d5a4a, #3e7b65)",
            "--bg-gradient-secondary": "linear-gradient(135deg, #f0f9f4, #e8f5e8)",
            "--gradient-indigo": "linear-gradient(90deg, #10b981, #34d399, #6ee7b7)",
            "--gradient-light-blue": "linear-gradient(135deg, #059669, #0d9488)",
            "--color-text": "#064e3b",
            "--color-text-dark": "#022c22",
            "--color-text-muted": "#6b7280",
            "--color-bg": "#f9fdf9",
            "--color-border": "#d1fae5",
            "--color-input-border": "#a7f3d0",
            "--color-input-focus": "#10b981",
            "--color-alert-border": "#10b981",
            "--color-alert-text": "#059669"
        }
    },
    "Minimalist Mono": {
        "font_imports": [
            "@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700;800&display=swap');"
        ],
        "root_variables": {
            "--font-primary": '"JetBrains Mono", monospace',
            "--bg-gradient-primary": "linear-gradient(135deg, #ffffff, #f8fafc, #f1f5f9)",
            "--bg-gradient-secondary": "linear-gradient(135deg, #ffffff, #f8fafc)",
            "--gradient-indigo": "linear-gradient(90deg, #000000, #374151, #6b7280)",
            "--gradient-light-blue": "linear-gradient(135deg, #374151, #4b5563)",
            "--color-text": "#111827",
            "--color-text-dark": "#000000",
            "--color-text-muted": "#6b7280",
            "--color-bg": "#ffffff",
            "--color-border": "#e5e7eb",
            "--color-input-border": "#d1d5db",
            "--color-input-focus": "#374151",
            "--color-alert-border": "#374151",
            "--color-alert-text": "#111827"
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

    # Build new root variables section
    root_variables_section = ":root {\n\n  /* Font System */\n"

    # Add font variables first
    if "--font-primary" in template_config["root_variables"]:
        root_variables_section += f"  --font-primary: {template_config['root_variables']['--font-primary']};\n\n"

    # Add standard font weights, sizes, etc. (keep original structure)
    root_variables_section += """  /* Font Weights */
  --font-weight-light: 400;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  --font-weight-extrabold: 800;

  /* Font Sizes */
  --font-size-xs: 0.85rem;    /* 12px */
  --font-size-sm: 0.975rem;   /* 14px */
  --font-size-base: 1.25rem;     /* 16px */
  --font-size-lg: 1.125rem;   /* 18px */
  --font-size-xl: 1.25rem;    /* 20px */
  --font-size-2xl: 1.5rem;    /* 24px */
  --font-size-3xl: 1.875rem;  /* 30px */
  --font-size-4xl: 2.25rem;   /* 36px */
  --font-size-5xl: 3rem;      /* 48px */
  --font-size-6xl: 3.75rem;   /* 60px */

  /* Line Heights */
  --line-height-tight: 1.25;
  --line-height-snug: 1.375;
  --line-height-normal: 1.5;
  --line-height-relaxed: 1.625;
  --line-height-loose: 2;

  /* Letter Spacing */
  --letter-spacing-tight: -0.025em;
  --letter-spacing-normal: 0;
  --letter-spacing-wide: 0.025em;
  --letter-spacing-wider: 0.05em;
  --letter-spacing-widest: 0.1em;

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
  --shadow-sm: 0 4px 15px rgba(236, 72, 153, 0.1);
  --shadow-md: 0 8px 25px rgba(236, 72, 153, 0.15);
  --shadow-indigo: 0 4px 15px rgba(236, 72, 153, 0.3);
}"""

    # Combine everything
    final_css = before_imports + font_imports_section + after_imports + root_variables_section + after_root

    return final_css



with st.expander(" 🎨 Change style"):
    st.markdown("### 🎨 Style Template")
    selected_template = st.selectbox(
        "Choose a style template:",
        options=list(CSS_TEMPLATES.keys()),
        index=0,
        help="Select a visual theme for the website"
    )
    template_info = {
        "Neon Cyber (Default)": "Futuristic cyberpunk aesthetic with neon gradients",
        "Elegant Modern": "Clean, professional design with subtle colors",
        "Retro Wave": "80s-inspired synthwave style with bold colors",
        "Nature Organic": "Earth-toned, organic design with green accents",
        "Minimalist Mono": "Clean monospace design with minimal styling"
    }
    st.write(template_info[selected_template])

# Generate and apply the selected CSS template
selected_config = CSS_TEMPLATES[selected_template]
custom_css = generate_custom_css(selected_config)
st.markdown("<style>" + custom_css + "</style>", unsafe_allow_html=True)

pages = {
    "Home": [
        st.Page("pages/{}/0_1_home.py".format(selected_art_project), title="Home"),
        st.Page("pages/{}/0_2_booking.py".format(selected_art_project), title="Bookings"),
    ],
    "About": [
        st.Page("pages/{}/1_1_band.py".format(selected_art_project), title="Band"),
        st.Page("pages/{}/1_2_people.py".format(selected_art_project), title="People"),
        st.Page("pages/{}/1_3_network.py".format(selected_art_project), title="Network"),

    ],
    "Songs": [
        st.Page("pages/{}/2_songs.py".format(selected_art_project), title="Songs"),
    ],
    "Live coding": [
        st.Page("pages/{}/3_1_live_coding_music.py".format(selected_art_project), title="Music"),
        st.Page("pages/{}/3_2_live_coding_visuals.py".format(selected_art_project), title="Visuals"),
        st.Page("pages/{}/3_3_live_coding_choreography.py".format(selected_art_project), title="Choreography"),
    ],
    "Contacts": [
        st.Page("pages/{}/4_1_contacts_social.py".format(selected_art_project), title="Social"),
        st.Page("pages/{}/4_2_contacts_booking.py".format(selected_art_project), title="Booking"),
    ],
}

pg = st.navigation(pages, position="top")
pg.run()