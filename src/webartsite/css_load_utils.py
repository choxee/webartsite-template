"""
CSS Loading Utilities for Strada Chiusa 2025
============================================

This module provides utilities for loading and managing CSS files for the
Strada Chiusa 2025 Streamlit application with session state sidebar management.
"""

import os
from typing import Dict, List, Optional, Union


class CSSLoader:
    """
    A utility class for loading and managing CSS files.
    """

    def __init__(self, base_path: str = None):
        """
        Initialize the CSS loader.

        Args:
            base_path (str): Base path for CSS files. If None, uses current directory.
        """
        self.base_path = base_path or os.path.dirname(__file__)
        self.loaded_styles = {}

    def load_css_file(self, filename: str, cache: bool = True) -> str:
        """
        Load a CSS file and return its content.

        Args:
            filename (str): Name of the CSS file to load
            cache (bool): Whether to cache the loaded content

        Returns:
            str: CSS content

        Raises:
            FileNotFoundError: If the CSS file doesn't exist
        """
        if cache and filename in self.loaded_styles:
            return self.loaded_styles[filename]

        file_path = os.path.join(self.base_path, filename)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"CSS file not found: {file_path}")

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            if cache:
                self.loaded_styles[filename] = content

            return content
        except Exception as e:
            raise RuntimeError(f"Error reading CSS file {filename}: {str(e)}")

    def load_multiple_css_files(self, filenames: List[str], cache: bool = True) -> str:
        """
        Load multiple CSS files and concatenate their content.

        Args:
            filenames (List[str]): List of CSS filenames to load
            cache (bool): Whether to cache the loaded content

        Returns:
            str: Concatenated CSS content
        """
        css_parts = []

        for filename in filenames:
            try:
                content = self.load_css_file(filename, cache)
                css_parts.append(f"\n/* ========== {filename} ========== */\n")
                css_parts.append(content)
            except Exception as e:
                print(f"Warning: Could not load {filename}: {str(e)}")
                continue

        return "\n".join(css_parts)

    def get_cached_files(self) -> List[str]:
        """
        Get list of cached CSS files.

        Returns:
            List[str]: List of cached filenames
        """
        return list(self.loaded_styles.keys())

    def clear_cache(self, filename: str = None):
        """
        Clear cache for a specific file or all files.

        Args:
            filename (str, optional): Specific filename to clear. If None, clears all.
        """
        if filename:
            self.loaded_styles.pop(filename, None)
        else:
            self.loaded_styles.clear()


def generate_custom_css_with_template(template_config: Dict, base_css_content: str) -> str:
    """
    Generate CSS with custom font imports and root variables while keeping the rest intact.

    Args:
        template_config (Dict): Configuration dictionary with font_imports and root_variables
        base_css_content (str): Base CSS content to modify

    Returns:
        str: Modified CSS content
    """
    # Extract everything after the root variables section
    # Find the end of the :root section
    root_start = base_css_content.find(":root {")
    if root_start == -1:
        return base_css_content  # Fallback if no :root found

    root_end = base_css_content.find("}", root_start)
    if root_end == -1:
        return base_css_content  # Fallback if malformed CSS

    # Get the parts before and after the root variables
    before_root = base_css_content[:root_start]
    after_root = base_css_content[root_end + 1:]

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

    return final_css


def load_strada_chiusa_css(selected_art_project: str = "sc25") -> str:
    """
    Load all CSS files for Strada Chiusa 2025 project with session state sidebar support.

    Args:
        selected_art_project (str): Project identifier for path construction

    Returns:
        str: Complete concatenated CSS
    """
    # CSS Templates Configuration
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

    # Initialize CSS loader
    base_path = os.path.join(os.path.dirname(__file__), f"pages/{selected_art_project}")
    css_loader = CSSLoader(base_path)

    try:
        # Load base CSS
        base_css = css_loader.load_css_file("0_0_default_style.css")

        # Generate CSS with template modifications
        selected_template = "Strada Chiusa 2025"
        selected_config = CSS_TEMPLATES[selected_template]
        base_css_modified = generate_custom_css_with_template(selected_config, base_css)

        # Load additional CSS files
        additional_css_files = [
            "additional_css_main.css",
            "additional_css_topbar.css",
            "additional_css_sidebar.css"
        ]

        additional_css = css_loader.load_multiple_css_files(additional_css_files)

        # Combine all CSS
        complete_css = base_css_modified + "\n\n" + additional_css

        return complete_css

    except Exception as e:
        print(f"Error loading CSS: {str(e)}")
        # Fallback: try to load at least the base CSS
        try:
            return css_loader.load_css_file("0_0_default_style.css")
        except:
            return ""


def set_background_image(image_url: str, css_templates: Dict = None) -> Dict:
    """
    Update the background image URL in the CSS template.

    Args:
        image_url (str): URL of the background image
        css_templates (Dict, optional): CSS templates dictionary to modify

    Returns:
        Dict: Updated CSS templates dictionary
    """
    if css_templates is None:
        css_templates = {
            "Strada Chiusa 2025": {
                "font_imports": [
                    "@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');"
                ],
                "root_variables": {
                    "--font-primary": '"Bebas Neue", sans-serif',
                    "--background-image": f"url('{image_url}')"
                }
            }
        }
    else:
        if "Strada Chiusa 2025" in css_templates:
            css_templates["Strada Chiusa 2025"]["root_variables"]["--background-image"] = f"url('{image_url}')"

    return css_templates


def get_css_file_info(selected_art_project: str = "sc25") -> Dict[str, Dict]:
    """
    Get information about available CSS files.

    Args:
        selected_art_project (str): Project identifier

    Returns:
        Dict: Information about CSS files
    """
    base_path = os.path.join(os.path.dirname(__file__), f"pages/{selected_art_project}")

    css_files = {
        "base": "0_0_default_style.css",
        "main": "additional_css_main.css",
        "topbar": "additional_css_topbar.css",
        "sidebar": "additional_css_sidebar.css"
    }

    file_info = {}

    for key, filename in css_files.items():
        file_path = os.path.join(base_path, filename)
        file_info[key] = {
            "filename": filename,
            "path": file_path,
            "exists": os.path.exists(file_path),
            "size": os.path.getsize(file_path) if os.path.exists(file_path) else 0
        }

    return file_info


# Convenience functions for backward compatibility
def generate_custom_css(template_config: Dict) -> str:
    """
    Legacy function for generating custom CSS.

    Args:
        template_config (Dict): Template configuration

    Returns:
        str: Generated CSS
    """
    return load_strada_chiusa_css()


def load_css_files(filenames: List[str], base_path: str = None) -> str:
    """
    Load multiple CSS files from a directory.

    Args:
        filenames (List[str]): List of CSS filenames
        base_path (str, optional): Base path for files

    Returns:
        str: Concatenated CSS content
    """
    loader = CSSLoader(base_path)
    return loader.load_multiple_css_files(filenames)

import os
from typing import Dict, List, Optional, Union


class CSSLoader:
    """
    A utility class for loading and managing CSS files.
    """

    def __init__(self, base_path: str = None):
        """
        Initialize the CSS loader.

        Args:
            base_path (str): Base path for CSS files. If None, uses current directory.
        """
        self.base_path = base_path or os.path.dirname(__file__)
        self.loaded_styles = {}

    def load_css_file(self, filename: str, cache: bool = True) -> str:
        """
        Load a CSS file and return its content.

        Args:
            filename (str): Name of the CSS file to load
            cache (bool): Whether to cache the loaded content

        Returns:
            str: CSS content

        Raises:
            FileNotFoundError: If the CSS file doesn't exist
        """
        if cache and filename in self.loaded_styles:
            return self.loaded_styles[filename]

        file_path = os.path.join(self.base_path, filename)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"CSS file not found: {file_path}")

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            if cache:
                self.loaded_styles[filename] = content

            return content
        except Exception as e:
            raise RuntimeError(f"Error reading CSS file {filename}: {str(e)}")

    def load_multiple_css_files(self, filenames: List[str], cache: bool = True) -> str:
        """
        Load multiple CSS files and concatenate their content.

        Args:
            filenames (List[str]): List of CSS filenames to load
            cache (bool): Whether to cache the loaded content

        Returns:
            str: Concatenated CSS content
        """
        css_parts = []

        for filename in filenames:
            try:
                content = self.load_css_file(filename, cache)
                css_parts.append(f"\n/* ========== {filename} ========== */\n")
                css_parts.append(content)
            except Exception as e:
                print(f"Warning: Could not load {filename}: {str(e)}")
                continue

        return "\n".join(css_parts)

    def get_cached_files(self) -> List[str]:
        """
        Get list of cached CSS files.

        Returns:
            List[str]: List of cached filenames
        """
        return list(self.loaded_styles.keys())

    def clear_cache(self, filename: str = None):
        """
        Clear cache for a specific file or all files.

        Args:
            filename (str, optional): Specific filename to clear. If None, clears all.
        """
        if filename:
            self.loaded_styles.pop(filename, None)
        else:
            self.loaded_styles.clear()


def generate_custom_css_with_template(template_config: Dict, base_css_content: str) -> str:
    """
    Generate CSS with custom font imports and root variables while keeping the rest intact.

    Args:
        template_config (Dict): Configuration dictionary with font_imports and root_variables
        base_css_content (str): Base CSS content to modify

    Returns:
        str: Modified CSS content
    """
    # Extract everything after the root variables section
    # Find the end of the :root section
    root_start = base_css_content.find(":root {")
    if root_start == -1:
        return base_css_content  # Fallback if no :root found

    root_end = base_css_content.find("}", root_start)
    if root_end == -1:
        return base_css_content  # Fallback if malformed CSS

    # Get the parts before and after the root variables
    before_root = base_css_content[:root_start]
    after_root = base_css_content[root_end + 1:]

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

    return final_css


def load_strada_chiusa_css(selected_art_project: str = "sc25") -> str:
    """
    Load all CSS files for Strada Chiusa 2025 project.

    Args:
        selected_art_project (str): Project identifier for path construction

    Returns:
        str: Complete concatenated CSS
    """
    # CSS Templates Configuration
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

    # Initialize CSS loader
    base_path = os.path.join(os.path.dirname(__file__), f"pages/{selected_art_project}")
    css_loader = CSSLoader(base_path)

    try:
        # Load base CSS
        base_css = css_loader.load_css_file("0_0_default_style.css")

        # Generate CSS with template modifications
        selected_template = "Strada Chiusa 2025"
        selected_config = CSS_TEMPLATES[selected_template]
        base_css_modified = generate_custom_css_with_template(selected_config, base_css)

        # Load additional CSS files
        additional_css_files = [
            "additional_css_main.css",
            "additional_css_topbar.css",
            "additional_css_sidebar_v2.css"
        ]

        additional_css = css_loader.load_multiple_css_files(additional_css_files)

        # Combine all CSS
        complete_css = base_css_modified + "\n\n" + additional_css

        return complete_css

    except Exception as e:
        print(f"Error loading CSS: {str(e)}")
        # Fallback: try to load at least the base CSS
        try:
            return css_loader.load_css_file("0_0_default_style.css")
        except:
            return ""


def set_background_image(image_url: str, css_templates: Dict = None) -> Dict:
    """
    Update the background image URL in the CSS template.

    Args:
        image_url (str): URL of the background image
        css_templates (Dict, optional): CSS templates dictionary to modify

    Returns:
        Dict: Updated CSS templates dictionary
    """
    if css_templates is None:
        css_templates = {
            "Strada Chiusa 2025": {
                "font_imports": [
                    "@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');"
                ],
                "root_variables": {
                    "--font-primary": '"Bebas Neue", sans-serif',
                    "--background-image": f"url('{image_url}')"
                }
            }
        }
    else:
        if "Strada Chiusa 2025" in css_templates:
            css_templates["Strada Chiusa 2025"]["root_variables"]["--background-image"] = f"url('{image_url}')"

    return css_templates


def get_css_file_info(selected_art_project: str = "sc25") -> Dict[str, Dict]:
    """
    Get information about available CSS files.

    Args:
        selected_art_project (str): Project identifier

    Returns:
        Dict: Information about CSS files
    """
    base_path = os.path.join(os.path.dirname(__file__), f"pages/{selected_art_project}")

    css_files = {
        "base": "0_0_default_style.css",
        "main": "additional_css_main.css",
        "topbar": "additional_css_topbar.css",
        "sidebar": "additional_css_sidebar.css"
    }

    file_info = {}

    for key, filename in css_files.items():
        file_path = os.path.join(base_path, filename)
        file_info[key] = {
            "filename": filename,
            "path": file_path,
            "exists": os.path.exists(file_path),
            "size": os.path.getsize(file_path) if os.path.exists(file_path) else 0
        }

    return file_info


# Convenience functions for backward compatibility
def generate_custom_css(template_config: Dict) -> str:
    """
    Legacy function for generating custom CSS.

    Args:
        template_config (Dict): Template configuration

    Returns:
        str: Generated CSS
    """
    return load_strada_chiusa_css()


def load_css_files(filenames: List[str], base_path: str = None) -> str:
    """
    Load multiple CSS files from a directory.

    Args:
        filenames (List[str]): List of CSS filenames
        base_path (str, optional): Base path for files

    Returns:
        str: Concatenated CSS content
    """
    loader = CSSLoader(base_path)
    return loader.load_multiple_css_files(filenames)