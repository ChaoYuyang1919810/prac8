from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

# Define colors for buttons
NEW_COLOUR = (1, 0, 0, 1)  # RGBA for red
ALTERNATIVE_COLOUR = (1, 0, 1, 1)  # RGBA for magenta


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty("")  # StringProperty to display status text

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # Dictionary of names and phone numbers (data model)
        self.name_to_phone = {
            "Bob Brown": "0414144411",
            "Cat Cyan": "0441411211",
            "Oren Ochre": "0432123456"
        }

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_widgets()  # Create buttons when the app starts
        return self.root

    def create_widgets(self):
        """Create buttons from data and add them to the GUI."""
        for name in self.name_to_phone:
            # Create a button for each data entry
            temp_button = Button(text=name)
            temp_button.bind(on_press=self.press_entry)  # Bind button press event
            temp_button.background_color = NEW_COLOUR  # Set button color
            # Add the button to the "entries_box" layout widget
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        """Handle pressing entry buttons."""
        # Get name (dictionary key) from the text of the clicked button
        name = instance.text
        # Change the button's background color
        instance.background_color = ALTERNATIVE_COLOUR
        # Update status text with the corresponding phone number
        self.status_text = f"{name}'s number is {self.name_to_phone[name]}"

    def clear_all(self):
        """Clear all widgets that are children of the "entries_box" layout widget."""
        self.root.ids.entries_box.clear_widgets()
        self.status_text = ""  # Clear status text when widgets are cleared


# Run the app
DynamicWidgetsApp().run()