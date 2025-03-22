from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

# Conversion constant
MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """MilesConverterApp is a Kivy app for converting miles to kilometres."""

    # StringProperty to automatically update the output label
    output_text = StringProperty("0.0")

    def build(self):
        """Build the Kivy app from the KV file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Handle the calculation and update the output label."""
        miles = self.get_validated_miles()
        kilometres = miles * MILES_TO_KM
        self.output_text = str(kilometres)

    def handle_increment(self, change):
        """
        Handle the Up/Down button press and update the miles input.
        :param change: The amount to change the miles by (1 or -1).
        """
        miles = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(miles)
        self.handle_calculate()

    def get_validated_miles(self):
        """
        Validate the miles input and return a float.
        :return: 0 if invalid, otherwise the float value of the input.
        """
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0


# Run the app
MilesConverterApp().run()