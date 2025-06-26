"""
Simplified CSS Loading Utilities for Strada Chiusa 2025
======================================================

Streamlined version that maintains all functionality while reducing complexity.
Keeps file separation but simplifies the loading logic.
"""

import os
from typing import Dict, List, Optional


class SimplifiedCSSLoader:
    """
    Simplified CSS loader that maintains file separation.
    """

    def __init__(self, base_path: str = None):
        """
        Initialize the CSS loader.

        Args:
            base_path (str): Base path for CSS files. If None, uses current directory.
        """
        self.base_path = base_path or os.path.dirname(__file__)
        self.loaded_styles = {}

    def load_css_file(self, filename: str) -> str:
        """
        Load a CSS file and return its content.

        Args:
            filename (str): Name of the CSS file to load

        Returns:
            str: CSS content

        Raises:
            FileNotFoundError: If the CSS file doesn't exist
        """
        if filename in self.loaded_styles:
            return self.loaded_styles[filename]

        file_path = os.path.join(self.base_path, filename)

        if not os.path.exists(file_path):
            print(f"Warning: CSS file not found: {file_path}")
            return ""

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            self.loaded_styles[filename] = content
            return content
        except Exception as e:
            print(f"Error reading CSS file {filename}: {str(e)}")
            return ""

    def load_all_css_files(self) -> str:
        """
        Load all CSS files in the correct order.

        Returns:
            str: Concatenated CSS content
        """
        css_files = [
            "0_0_default_style.css",      # Base styles and variables
            "additional_css_main.css",    # Main content styling
            "additional_css_topbar.css",  # Header/topbar styling
            "additional_css_sidebar_v2.css"  # Sidebar styling
        ]

        css_parts = []

        for filename in css_files:
            content = self.load_css_file(filename)
            if content:
                css_parts.append(f"\n/* ========== {filename} ========== */\n")
                css_parts.append(content)
            else:
                print(f"Skipping missing file: {filename}")

        return "\n".join(css_parts)


def load_strada_chiusa_css(selected_art_project: str = "sc25") -> str:
    """
    Load all CSS files for Strada Chiusa 2025 project.

    Args:
        selected_art_project (str): Project identifier for path construction

    Returns:
        str: Complete concatenated CSS
    """
    # Construct the path to the CSS files
    current_dir = os.path.dirname(__file__)
    css_path = os.path.join(current_dir, "pages", selected_art_project)

    # If the pages directory doesn't exist, try the current directory
    if not os.path.exists(css_path):
        css_path = current_dir

    # Initialize CSS loader
    css_loader = SimplifiedCSSLoader(css_path)

    try:
        # Load all CSS files
        complete_css = css_loader.load_all_css_files()

        if not complete_css.strip():
            print("No CSS content loaded, using fallback")
            return get_fallback_css()

        return complete_css

    except Exception as e:
        print(f"Error loading CSS: {str(e)}")
        return get_fallback_css()


def get_fallback_css() -> str:
    """
    Return minimal fallback CSS if files can't be loaded.

    Returns:
        str: Fallback CSS content
    """
    return """
/* Fallback CSS */
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue:wght@400&display=swap');

:root {
  --font-primary: "Bebas Neue", Impact, sans-serif;
  --color-primary: #dc2626;
  --color-text: #ffffff;
  --background-image: url('https://storage.googleapis.com/public-static-contents-test-0/photo-sc-folla-0.jpg');
}

.stApp {
  background: var(--background-image) center/cover fixed no-repeat !important;
  font-family: var(--font-primary);
  color: var(--color-text);
}

* {
  color: #ffffff !important;
  text-shadow: 1px 1px 2px rgba(0,0,0,0.8) !important;
}

.stMainBlockContainer {
  background: rgba(0,0,0,0.1) !important;
  backdrop-filter: blur(3px) !important;
  border: 1px solid rgba(255,255,255,0.1) !important;
  border-radius: 16px !important;
}

.stButton button {
  background: linear-gradient(90deg, #dc2626, #ef4444, #f87171) !important;
  color: white !important;
  border: none !important;
  padding: 1rem 2rem !important;
  border-radius: 16px !important;
  font-family: var(--font-primary) !important;
  text-transform: uppercase !important;
  font-weight: bold !important;
}
"""


def set_background_image(image_url: str) -> str:
    """
    Update the background image URL and return modified CSS.

    Args:
        image_url (str): URL of the background image

    Returns:
        str: CSS with updated background image
    """
    css = load_strada_chiusa_css()

    # Replace the background image URL
    old_url = "url('https://storage.googleapis.com/public-static-contents-test-0/photo-sc-folla-0.jpg')"
    new_url = f"url('{image_url}')"

    return css.replace(old_url, new_url)


def get_css_file_info(selected_art_project: str = "sc25") -> Dict[str, Dict]:
    """
    Get information about available CSS files.

    Args:
        selected_art_project (str): Project identifier

    Returns:
        Dict: Information about CSS files
    """
    current_dir = os.path.dirname(__file__)
    base_path = os.path.join(current_dir, "pages", selected_art_project)

    # If the pages directory doesn't exist, try the current directory
    if not os.path.exists(base_path):
        base_path = current_dir

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
def load_css_files(filenames: List[str] = None, base_path: str = None) -> str:
    """
    Load multiple CSS files from a directory.

    Args:
        filenames (List[str]): List of CSS filenames (ignored in simplified version)
        base_path (str, optional): Base path for files

    Returns:
        str: Concatenated CSS content
    """
    if base_path:
        loader = SimplifiedCSSLoader(base_path)
        return loader.load_all_css_files()
    else:
        return load_strada_chiusa_css()


def generate_custom_css(template_config: Dict = None) -> str:
    """
    Legacy function for generating custom CSS.

    Args:
        template_config (Dict): Template configuration (ignored in simplified version)

    Returns:
        str: Generated CSS
    """
    return load_strada_chiusa_css()


# Main function to get complete CSS
def get_complete_css(selected_art_project: str = "sc25") -> str:
    """
    Get the complete CSS for the application.

    Args:
        selected_art_project (str): Project identifier

    Returns:
        str: Complete CSS content
    """
    return load_strada_chiusa_css(selected_art_project)


def get_enhanced_button_fix_css():
    """Enhanced CSS for fixing sidebar buttons and hiding main menu"""
    return """
    /* ==============================================
       HIDE MAIN MENU BUTTON COMPLETELY
       ============================================== */

    /* Hide the main menu (three dots) button */
    .stMainMenu,
    [data-testid="stMainMenu"],
    span[id="MainMenu"],
    .stAppHeader .stMainMenu,
    button[aria-haspopup="true"][aria-expanded="false"] {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
    }

    /* Hide deploy button as well */
    .stAppDeployButton,
    [data-testid="stAppDeployButton"] {
        display: none !important;
        visibility: hidden !important;
    }

    /* ==============================================
       SIDEBAR BUTTON FIXES
       ============================================== */

    /* Target ALL sidebar control buttons */
    button[data-testid="baseButton-header"],
    button[data-testid="stBaseButton-headerNoPadding"],
    button[data-testid="stSidebarCollapseButton"],
    button[data-testid="stExpandSidebarButton"],
    [data-testid="collapsedControl"] button,
    [data-testid="stSidebarCollapseButton"] button,
    .stSidebar button[kind="headerNoPadding"],
    .stAppHeader button[kind="headerNoPadding"] {
        font-size: 0 !important;
        color: transparent !important;
        background: rgba(0,0,0,0.7) !important;
        border: 2px solid rgba(220,38,38,0.4) !important;
        border-radius: 12px !important;
        width: 44px !important;
        height: 44px !important;
        position: relative !important;
        text-indent: -9999px !important;
        overflow: hidden !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3) !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        cursor: pointer !important;
    }

    /* Hide all content inside buttons */
    button[data-testid="baseButton-header"] *,
    button[data-testid="stBaseButton-headerNoPadding"] *,
    button[data-testid="stSidebarCollapseButton"] *,
    button[data-testid="stExpandSidebarButton"] *,
    [data-testid="collapsedControl"] *,
    [data-testid="stSidebarCollapseButton"] *,
    .stSidebar button[kind="headerNoPadding"] *,
    .stAppHeader button[kind="headerNoPadding"] * {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
    }

    /* Add arrows using CSS content */
    button[data-testid="baseButton-header"]::after,
    button[data-testid="stBaseButton-headerNoPadding"]::after,
    button[data-testid="stSidebarCollapseButton"]::after,
    button[data-testid="stExpandSidebarButton"]::after,
    [data-testid="collapsedControl"] button::after,
    [data-testid="stSidebarCollapseButton"] button::after,
    .stSidebar button[kind="headerNoPadding"]::after,
    .stAppHeader button[kind="headerNoPadding"]::after {
        content: "◀◀" !important;
        position: absolute !important;
        top: 50% !important;
        left: 50% !important;
        transform: translate(-50%, -50%) !important;
        font-size: 16px !important;
        color: white !important;
        font-weight: bold !important;
        text-indent: 0 !important;
        display: block !important;
        font-family: Arial, sans-serif !important;
        z-index: 10 !important;
        line-height: 1 !important;
    }

    /* When sidebar is collapsed, show open arrow */
    .stSidebar[aria-expanded="false"] button::after,
    button[data-testid="stExpandSidebarButton"]::after {
        content: "▶▶" !important;
    }

    /* When sidebar is open, show close arrow */
    .stSidebar[aria-expanded="true"] button::after,
    button[data-testid="stSidebarCollapseButton"]::after {
        content: "◀◀" !important;
    }

    /* Hover effects */
    button[data-testid="baseButton-header"]:hover,
    button[data-testid="stBaseButton-headerNoPadding"]:hover,
    button[data-testid="stSidebarCollapseButton"]:hover,
    button[data-testid="stExpandSidebarButton"]:hover,
    [data-testid="collapsedControl"] button:hover,
    [data-testid="stSidebarCollapseButton"] button:hover,
    .stSidebar button[kind="headerNoPadding"]:hover,
    .stAppHeader button[kind="headerNoPadding"]:hover {
        background: rgba(220,38,38,0.3) !important;
        border-color: rgba(220,38,38,0.6) !important;
        transform: scale(1.05) !important;
    }

    /* ==============================================
       ADDITIONAL STREAMLIT ELEMENT HIDING
       ============================================== */

    /* Hide any element containing problematic text */
    *[class*="keyboard_double_arrow"],
    *[data-testid*="keyboard_double_arrow"],
    span:contains("keyboard_double_arrow_left"),
    span:contains("keyboard_double_arrow_right") {
        display: none !important;
    }

    /* Clean up toolbar area */
    .stToolbarActions {
        display: none !important;
    }

    /* ==============================================
       RESPONSIVE ADJUSTMENTS
       ============================================== */

    @media (max-width: 768px) {
        /* Ensure buttons work on mobile */
        button[data-testid="baseButton-header"],
        button[data-testid="stBaseButton-headerNoPadding"],
        button[data-testid="stSidebarCollapseButton"],
        button[data-testid="stExpandSidebarButton"] {
            width: 48px !important;
            height: 48px !important;
            min-width: 48px !important;
            min-height: 48px !important;
        }
    }
    """


def get_enhanced_button_fix_js():
    """Enhanced JavaScript for sidebar button management"""
    return """
    <script>
    (function() {
        'use strict';

        let observer;
        let fixCounter = 0;
        const MAX_FIXES = 50;

        function logDebug(message) {
            if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
                console.log(`[SC25 Button Fix ${fixCounter}]:`, message);
            }
        }

        function hideMainMenu() {
            // Hide main menu button (three dots)
            const mainMenuSelectors = [
                '.stMainMenu',
                '[data-testid="stMainMenu"]',
                'span[id="MainMenu"]',
                '.stAppHeader .stMainMenu',
                'button[aria-haspopup="true"]',
                '.stAppDeployButton',
                '[data-testid="stAppDeployButton"]'
            ];

            mainMenuSelectors.forEach(selector => {
                const elements = document.querySelectorAll(selector);
                elements.forEach(element => {
                    element.style.display = 'none';
                    element.style.visibility = 'hidden';
                    element.style.opacity = '0';
                    element.style.pointerEvents = 'none';
                });
            });
        }

        function fixSidebarButtons() {
            if (fixCounter >= MAX_FIXES) {
                logDebug('Maximum fixes reached, stopping');
                return;
            }

            fixCounter++;
            let buttonsFixed = 0;

            // Hide main menu first
            hideMainMenu();

            // Get sidebar state
            const sidebar = document.querySelector('[data-testid="stSidebar"]');
            const isExpanded = sidebar && sidebar.getAttribute('aria-expanded') === 'true';

            logDebug(`Sidebar expanded: ${isExpanded}`);

            // All possible sidebar button selectors
            const buttonSelectors = [
                'button[data-testid="baseButton-header"]',
                'button[data-testid="stBaseButton-headerNoPadding"]',
                'button[data-testid="stSidebarCollapseButton"]',
                'button[data-testid="stExpandSidebarButton"]',
                '[data-testid="collapsedControl"] button',
                '[data-testid="stSidebarCollapseButton"] button',
                '.stSidebar button[kind="headerNoPadding"]',
                '.stAppHeader button[kind="headerNoPadding"]'
            ];

            buttonSelectors.forEach(selector => {
                const buttons = document.querySelectorAll(selector);
                buttons.forEach(button => {
                    const buttonText = button.textContent || button.innerText || '';
                    const hasProblematicContent = buttonText.includes('keyboard_double_arrow') || 
                                                buttonText.includes('KEYBOARD_DOUBLE_ARROW') ||
                                                button.querySelector('[data-testid*="stIcon"]');

                    if (hasProblematicContent || selector.includes('Sidebar') || selector.includes('Button')) {
                        // Determine correct arrow based on sidebar state and button type
                        let arrowText = '▶▶'; // default to open arrow

                        if (selector.includes('Collapse') || (isExpanded && !selector.includes('Expand'))) {
                            arrowText = '◀◀'; // close arrow
                        }

                        // Apply comprehensive styling
                        button.innerHTML = arrowText;
                        button.style.cssText = `
                            background: rgba(0,0,0,0.7) !important;
                            border: 2px solid rgba(220,38,38,0.4) !important;
                            border-radius: 12px !important;
                            color: white !important;
                            font-size: 16px !important;
                            font-weight: bold !important;
                            width: 44px !important;
                            height: 44px !important;
                            display: flex !important;
                            align-items: center !important;
                            justify-content: center !important;
                            font-family: Arial, sans-serif !important;
                            transition: all 0.3s ease !important;
                            cursor: pointer !important;
                            box-shadow: 0 2px 8px rgba(0,0,0,0.3) !important;
                            position: relative !important;
                            z-index: 100 !important;
                        `;

                        // Add hover effects
                        button.onmouseenter = function() {
                            this.style.background = 'rgba(220,38,38,0.3)';
                            this.style.borderColor = 'rgba(220,38,38,0.6)';
                            this.style.transform = 'scale(1.05)';
                        };

                        button.onmouseleave = function() {
                            this.style.background = 'rgba(0,0,0,0.7)';
                            this.style.borderColor = 'rgba(220,38,38,0.4)';
                            this.style.transform = 'scale(1)';
                        };

                        // Add click handler to update arrow after state change
                        button.onclick = function(e) {
                            // Don't prevent the original click
                            setTimeout(() => {
                                const newSidebar = document.querySelector('[data-testid="stSidebar"]');
                                const newIsExpanded = newSidebar && newSidebar.getAttribute('aria-expanded') === 'true';

                                if (selector.includes('Collapse') || (newIsExpanded && !selector.includes('Expand'))) {
                                    this.innerHTML = '◀◀';
                                } else {
                                    this.innerHTML = '▶▶';
                                }
                            }, 150);
                        };

                        buttonsFixed++;
                        logDebug(`Fixed button: ${selector} with arrow: ${arrowText}`);
                    }
                });
            });

            logDebug(`Fixed ${buttonsFixed} buttons`);
        }

        function startObserver() {
            if (observer) observer.disconnect();

            observer = new MutationObserver(function(mutations) {
                let shouldFix = false;

                mutations.forEach(mutation => {
                    if (mutation.type === 'childList' || 
                        (mutation.type === 'attributes' && 
                         (mutation.attributeName === 'aria-expanded' || 
                          mutation.attributeName === 'class'))) {
                        shouldFix = true;
                    }
                });

                if (shouldFix) {
                    setTimeout(fixSidebarButtons, 100);
                }
            });

            observer.observe(document.body, {
                childList: true,
                subtree: true,
                attributes: true,
                attributeFilter: ['aria-expanded', 'class', 'data-testid']
            });
        }

        // Initial fixes
        setTimeout(fixSidebarButtons, 100);
        setTimeout(fixSidebarButtons, 500);
        setTimeout(fixSidebarButtons, 1000);

        // Start observing changes
        startObserver();

        // Window load event
        window.addEventListener('load', () => {
            setTimeout(fixSidebarButtons, 200);
        });

        // Periodic check every 3 seconds (reduced frequency)
        setInterval(() => {
            if (fixCounter < MAX_FIXES) {
                fixSidebarButtons();
            }
        }, 3000);

        logDebug('Enhanced button fix system initialized');
    })();
    </script>
    """
