from manim import *

class Logo(Scene):
    def construct(self):
        # Define texts
        title = Text('EnigmaText', weight='LIGHT', font_size=125)
        subtitle = Text('Natural language processing, simplified.', font_size=25).shift(DOWN)

        # Write channel logo to screen
        self.wait(0.25)
        self.play(Write(title, run_time=1.25)) 
        self.play(Write(subtitle, run_time=1)) 
        self.wait()
        
        # Wipe the screen
        self.play(Unwrite(subtitle, run_time=0.75))
        self.play(Unwrite(title, run_time=0.75))
        self.wait(0.10)
